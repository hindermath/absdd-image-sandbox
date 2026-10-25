#!/usr/bin/env node
// Host-only document export. Never installs packages or invokes the sandbox.
import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {spawnSync} from 'node:child_process';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
function option(name) {
  const at = args.indexOf(name);
  return at < 0 ? undefined : args[at + 1];
}
const output = option('--out');
const renderRoot = option('--render-dir');
if (!output || args.some((arg, i) => i % 2 === 0 && !['--out', '--render-dir'].includes(arg))) {
  throw new Error('Usage: export-workshop-presentations.mjs --out NEW_DIRECTORY [--render-dir DIRECTORY]');
}
const modules = process.env.ARTIFACT_TOOL_MODULES;
const resolver = createRequire(modules ? path.join(path.resolve(modules), '__resolver__.cjs') : import.meta.url);
const entrypoint = resolver.resolve('@oai/artifact-tool');
const {Presentation, PresentationFile} = await import(pathToFileURL(entrypoint).href);
const native = createRequire(entrypoint);
const {Canvas, FontLibrary} = native('skia-canvas');
for (const name of ['Arial', 'Courier New']) {
  if (!FontLibrary.families.includes(name)) throw new Error(`Required authoring font unavailable: ${name}`);
}
const context = new Canvas(1, 1).getContext('2d');
const palette = {ink: '#182626', muted: '#4B5B5B', teal: '#006B65', amber: '#965300', light: '#F1F5F4'};

function pandoc(input, from, to) {
  const result = spawnSync('pandoc', ['--from', from, '--to', to], {input, encoding: 'utf8'});
  if (result.error || result.status !== 0) throw new Error(result.error?.message ?? result.stderr);
  return result.stdout;
}
function inline(nodes) {
  return nodes.map(node => {
    if (node.t === 'Str') return node.c;
    if (node.t === 'Space') return ' ';
    if (node.t === 'SoftBreak' || node.t === 'LineBreak') return '\n';
    if (node.t === 'Code') return node.c[1];
    if (node.t === 'Link') return inline(node.c[1]);
    if (['Emph', 'Strong', 'Span'].includes(node.t)) return inline(node.t === 'Span' ? node.c[1] : node.c);
    throw new Error(`Unsupported workshop inline: ${node.t}`);
  }).join('');
}
function parse(markdown) {
  const ast = JSON.parse(pandoc(markdown, 'markdown+fenced_divs-smart', 'json'));
  const slides = [];
  let current;
  let id;
  for (const block of ast.blocks) {
    if (block.t === 'RawBlock' && /slide: W\d+/.test(block.c[1])) {
      id = block.c[1].match(/slide: (W\d+)/)[1];
    } else if (block.t === 'Header' && block.c[0] === 1) {
      current = {id, title: inline(block.c[2]), bullets: [], paragraphs: [], code: [], notes: ''};
      slides.push(current);
    } else if (!current || block.t === 'HorizontalRule') {
      continue;
    } else if (block.t === 'BulletList') {
      current.bullets.push(...block.c.map(item => item.map(part => inline(part.c)).join('\n')));
    } else if (block.t === 'Para' || block.t === 'Plain') {
      current.paragraphs.push(inline(block.c));
    } else if (block.t === 'CodeBlock') {
      current.code.push(block.c[1]);
    } else if (block.t === 'Div' && block.c[0][1].includes('notes')) {
      current.notes += pandoc(JSON.stringify({...ast, blocks: block.c[1]}), 'json', 'plain');
    } else {
      throw new Error(`Unsupported workshop block: ${block.t}`);
    }
  }
  if (slides.length !== 39 || new Set(slides.map(s => s.id)).size !== 39) throw new Error('Expected 39 unique workshop slides');
  return slides;
}
function lines(text, font, width) {
  context.font = font;
  const result = [];
  for (const part of text.split('\n')) {
    let line = '';
    for (const word of part.split(/\s+/)) {
      const trial = line ? `${line} ${word}` : word;
      if (line && context.measureText(trial).width > width) { result.push(line); line = word; }
      else line = trial;
    }
    result.push(line);
  }
  return result;
}
function text(slide, name, value, box, size, extra = {}) {
  const shape = slide.shapes.add({geometry: 'textbox', name, position: box,
    ...(name === 'title' ? {placeholderType: 'title'} : {}),
    fill: extra.fill ?? 'none', line: {fill: 'none', width: 0}});
  shape.text = value;
  shape.text.style = {typeface: extra.font ?? 'Arial', fontSize: size, color: extra.color ?? palette.ink,
    bold: extra.bold ?? false, autoFit: 'none', wrap: extra.wrap ?? 'square', insets: extra.insets ?? 0};
  return shape;
}
function addDiagram(slide, lang) {
  const labels = lang === 'de'
    ? ['Host\nausgewählter Projektordner', 'Mount: echte Host-Dateien', 'Linux-Container\nBenutzer adedev', 'Agentenzustand: getrennte Volumes']
    : ['Host\nselected project folder', 'Mount: real host files', 'Linux container\nadedev user', 'Agent state: separate volumes'];
  text(slide, 'host', labels[0], {left: 790, top: 220, width: 420, height: 105}, 29,
    {fill: '#E8F3F1', insets: 15});
  slide.shapes.add({geometry: 'downArrow', name: 'mount-direction',
    position: {left: 978, top: 342, width: 34, height: 52}, fill: palette.teal, line: {fill: 'none'}});
  text(slide, 'mount-label', labels[1], {left: 795, top: 402, width: 410, height: 40}, 23, {color: palette.teal});
  text(slide, 'container', labels[2], {left: 790, top: 456, width: 420, height: 100}, 29,
    {fill: palette.light, insets: 15});
  text(slide, 'volumes', labels[3], {left: 790, top: 585, width: 420, height: 60}, 23);
}
function makeSlide(deck, data, lang, index) {
  const slide = deck.slides.add();
  slide.background.fill = '#FFFFFF';
  slide.speakerNotes.text = `${data.id}\n${data.notes}`;
  slide.speakerNotes.setVisible(true);
  if (index === 0) {
    slide.shapes.add({geometry: 'rect', position: {left: 64, top: 106, width: 100, height: 8}, fill: palette.teal, line: {fill: 'none'}});
    text(slide, 'title', data.title, {left: 64, top: 155, width: 1152, height: 108}, 76, {bold: true});
    text(slide, 'subtitle', data.paragraphs.join('\n'), {left: 68, top: 310, width: 1090, height: 245}, 34);
  } else {
    const titleLines = lines(data.title, 'bold 48px Arial', 1136);
    if (titleLines.length > 2) throw new Error(`Title too long: ${data.id}`);
    text(slide, 'title', titleLines.join('\n'), {left: 64, top: 48, width: 1152, height: 118}, 48, {bold: true});
    slide.shapes.add({geometry: 'rect', name: 'heading-rule',
      position: {left: 64, top: 172, width: 1152, height: 3}, fill: palette.teal, line: {fill: 'none'}});
    const diagram = data.id === 'W03';
    const hasCode = data.code.length > 0;
    const size = diagram ? 29 : hasCode ? 28 : 34;
    const width = diagram ? 660 : 1152;
    const height = data.bullets.reduce((sum, bullet) => sum + lines(bullet, `${size}px Arial`, width - 58).length * size * 1.24 + 12, 0) + 8;
    if (data.bullets.length) {
      const body = text(slide, 'body', '', {left: 64, top: 214, width, height}, size);
      body.text = data.bullets.map(value => ({runs: [value], bulletCharacter: '\u2022',
        marginLeft: 18 * 12700, indent: -9 * 12700, spaceAfter: 8 * 100}));
    }
    if (diagram) addDiagram(slide, lang);
    if (hasCode) {
      const code = data.code.join('\n\n');
      context.font = '22px "Courier New"';
      if (code.split('\n').some(line => context.measureText(line).width > 1116)) throw new Error(`Code too wide: ${data.id}`);
      const codeHeight = code.split('\n').length * 28 + 36;
      const y = 214 + height + 20;
      if (y + codeHeight > 658) throw new Error(`Content too high: ${data.id}`);
      text(slide, 'command', code, {left: 64, top: y, width: 1152, height: codeHeight}, 22,
        {font: 'Courier New', bold: true, fill: palette.light, insets: 18, wrap: 'none'});
    }
  }
  text(slide, 'page', `absdd-image-sandbox  |  ${lang.toUpperCase()}  |  ${String(index + 1).padStart(2, '0')} / 39`,
    {left: 64, top: 681, width: 1152, height: 24}, 16, {color: palette.muted});
  return slide;
}

await fs.mkdir(path.resolve(output), {recursive: true});
for (const lang of ['de', 'en']) {
  const source = path.join(repo, 'docs/praesentationen', `workshop-spec-kit.${lang}.md`);
  const data = parse(await fs.readFile(source, 'utf8'));
  const deck = Presentation.create({slideSize: {width: 1280, height: 720}});
  for (const [index, slide] of data.entries()) makeSlide(deck, slide, lang, index);
  const destination = path.join(path.resolve(output), `workshop-spec-kit.${lang}.pptx`);
  try { await fs.access(destination); throw new Error(`Refusing to overwrite ${destination}`); }
  catch (error) { if (error.code !== 'ENOENT') throw error; }
  await (await PresentationFile.exportPptx(deck)).save(destination);
  if (renderRoot) {
    const directory = path.join(path.resolve(renderRoot), lang);
    await fs.mkdir(directory, {recursive: true});
    for (const [i, slide] of deck.slides.items.entries()) {
      const png = await deck.export({slide, format: 'png', scale: 1});
      await fs.writeFile(path.join(directory, `slide-${String(i + 1).padStart(2, '0')}.png`), new Uint8Array(await png.arrayBuffer()));
    }
  }
  console.log(`${lang}: ${data.length} editable slides exported`);
}
