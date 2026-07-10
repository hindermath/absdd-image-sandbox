# Tag 10.0 observed on 2026-06-03, pinned here by digest for reproducible builds.
FROM mcr.microsoft.com/dotnet/sdk:10.0@sha256:1f48db91b4f27fdb4409b7b4253ce1fd4f78f69d34efd9edb788c03a337f5ab8

# renovate: datasource=java-version depName=java packageName=java-jdk versioning=semver-coerced argName=JAVA_VERSION
ARG JAVA_VERSION=21
# renovate: datasource=golang-version depName=go versioning=semver argName=GO_VERSION
ARG GO_VERSION=1.26.3
# renovate: datasource=go depName=golang.org/x/tools/gopls versioning=semver argName=GOPLS_VERSION
ARG GOPLS_VERSION=v0.21.1
# renovate: datasource=go depName=honnef.co/go/tools versioning=semver argName=STATICCHECK_VERSION
ARG STATICCHECK_VERSION=v0.7.0
# renovate: datasource=go depName=golang.org/x/vuln versioning=semver argName=GOVULNCHECK_VERSION
ARG GOVULNCHECK_VERSION=v1.3.0
# renovate: datasource=go depName=github.com/go-delve/delve versioning=semver argName=DELVE_VERSION
ARG DELVE_VERSION=v1.26.3
# renovate: datasource=rust-version depName=rust versioning=rust-release-channel argName=RUST_TOOLCHAIN
ARG RUST_TOOLCHAIN=1.95.0
# renovate: datasource=github-releases depName=rust-lang/rustup versioning=semver argName=RUSTUP_VERSION
ARG RUSTUP_VERSION=1.28.2
# renovate: datasource=docker depName=swift versioning=docker argName=SWIFT_DOCKER_TAG
ARG SWIFT_DOCKER_TAG=6.3.3-noble
# renovate: datasource=node-version depName=node versioning=node argName=NODE_MAJOR
ARG NODE_MAJOR=22
# renovate: datasource=github-releases depName=astral-sh/uv versioning=semver argName=UV_VERSION
ARG UV_VERSION=0.11.16
# renovate: datasource=npm depName=opencode-ai versioning=npm argName=OPENCODE_VERSION
ARG OPENCODE_VERSION=1.14.50
# renovate: datasource=npm depName=@openai/codex versioning=npm argName=CODEX_VERSION
ARG CODEX_VERSION=0.144.1
# renovate: datasource=npm depName=@anthropic-ai/claude-code versioning=npm argName=CLAUDE_CODE_VERSION
ARG CLAUDE_CODE_VERSION=2.1.206
# renovate: datasource=npm depName=@google/gemini-cli versioning=npm argName=GEMINI_CLI_VERSION
ARG GEMINI_CLI_VERSION=0.50.0
# renovate: datasource=npm depName=@github/copilot versioning=npm argName=COPILOT_CLI_VERSION
ARG COPILOT_CLI_VERSION=1.0.70
# renovate: datasource=github-releases depName=anchore/syft versioning=semver argName=SYFT_VERSION
ARG SYFT_VERSION=1.46.0

USER root
RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
        bubblewrap \
        build-essential \
        ca-certificates \
        curl \
        direnv \
        fd-find \
        git \
        git-delta \
        gnupg \
        gnupg2 \
        jq \
        just \
        libcurl4-openssl-dev \
        libedit2 \
        libgcc-13-dev \
        libncurses-dev \
        libpython3-dev \
        libsqlite3-0 \
        libssl-dev \
        libstdc++-13-dev \
        libxml2-dev \
        libz3-dev \
        maven \
        openjdk-${JAVA_VERSION}-jdk-headless \
        pandoc \
        pkg-config \
        python-is-python3 \
        python3 \
        python3-venv \
        ripgrep \
        shellcheck \
        shfmt \
        tree \
        wget \
        yq \
    && mkdir -p /usr/share/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key -o /tmp/nodesource-repo.gpg.key \
    && gpg --dearmor --yes -o /usr/share/keyrings/nodesource.gpg /tmp/nodesource-repo.gpg.key \
    && chmod 0644 /usr/share/keyrings/nodesource.gpg \
    && rm /tmp/nodesource-repo.gpg.key \
    && arch="$(dpkg --print-architecture)" \
    && case "${arch}" in \
        amd64|arm64) ;; \
        *) echo "Unsupported NodeSource architecture: ${arch}" >&2; exit 1 ;; \
    esac \
    && printf 'Types: deb\nURIs: https://deb.nodesource.com/node_%s.x\nSuites: nodistro\nComponents: main\nArchitectures: %s\nSigned-By: /usr/share/keyrings/nodesource.gpg\n' "${NODE_MAJOR}" "${arch}" > /etc/apt/sources.list.d/nodesource.sources \
    && printf 'Package: nodejs\nPin: origin deb.nodesource.com\nPin-Priority: 600\n' > /etc/apt/preferences.d/nodejs \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends nodejs \
    && ln -sf /usr/bin/fdfind /usr/local/bin/fd \
    && rm -rf /var/lib/apt/lists/*
RUN set -eux; \
    case "${SWIFT_DOCKER_TAG}" in \
        *-noble) ;; \
        *) echo "Unsupported Swift Docker tag for Ubuntu 24.04 base image: ${SWIFT_DOCKER_TAG}" >&2; exit 1 ;; \
    esac; \
    swift_base_version="${SWIFT_DOCKER_TAG%%-*}"; \
    case "${swift_base_version}" in \
        [0-9]*.[0-9]*.[0-9]*) ;; \
        *) echo "Unsupported Swift version in SWIFT_DOCKER_TAG: ${SWIFT_DOCKER_TAG}" >&2; exit 1 ;; \
    esac; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) os_arch_suffix="" ;; \
        arm64) os_arch_suffix="-aarch64" ;; \
        *) echo "Unsupported Swift architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    swift_signing_key="52BB7E3DE28A71BE22EC05FFEF80A866B47A981F"; \
    swift_platform="ubuntu24.04"; \
    swift_branch="swift-${swift_base_version}-release"; \
    swift_version="swift-${swift_base_version}-RELEASE"; \
    swift_webdir="https://download.swift.org/${swift_branch}/$(printf '%s' "${swift_platform}" | tr -d .)${os_arch_suffix}"; \
    swift_bin_url="${swift_webdir}/${swift_version}/${swift_version}-${swift_platform}${os_arch_suffix}.tar.gz"; \
    tmp_dir="$(mktemp -d)"; \
    export GNUPGHOME="${tmp_dir}/gnupg"; \
    mkdir -p "${GNUPGHOME}"; \
    curl -fsSL "${swift_bin_url}" -o "${tmp_dir}/swift.tar.gz"; \
    curl -fsSL "${swift_bin_url}.sig" -o "${tmp_dir}/swift.tar.gz.sig"; \
    gpg --batch --quiet --keyserver keyserver.ubuntu.com --recv-keys "${swift_signing_key}"; \
    gpg --batch --verify "${tmp_dir}/swift.tar.gz.sig" "${tmp_dir}/swift.tar.gz"; \
    tar -xzf "${tmp_dir}/swift.tar.gz" --directory / --strip-components=1; \
    chmod -R o+r /usr/lib/swift; \
    rm -rf "${tmp_dir}"
RUN swift --version \
    && swiftc --version \
    && command -v sourcekit-lsp
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) go_arch="amd64" ;; \
        arm64) go_arch="arm64" ;; \
        *) echo "Unsupported Go architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    wget "https://go.dev/dl/go${GO_VERSION}.linux-${go_arch}.tar.gz" -O /tmp/go.tgz; \
    rm -rf /usr/local/go; \
    tar -C /usr/local -xzf /tmp/go.tgz; \
    rm /tmp/go.tgz
RUN printf '%s\n' 'export PATH="/usr/local/go/bin:/home/adedev/go/bin:/home/adedev/.cargo/bin:${PATH}"' \
    > /etc/profile.d/ade-toolchains.sh
RUN npm i -g \
        "opencode-ai@${OPENCODE_VERSION}" \
        "@openai/codex@${CODEX_VERSION}" \
        "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}" \
        "@google/gemini-cli@${GEMINI_CLI_VERSION}" \
        "@github/copilot@${COPILOT_CLI_VERSION}" \
    && ln -sf "$(npm root -g)/@openai/codex/bin/codex.js" /usr/local/bin/codex
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) syft_arch="amd64" ;; \
        arm64) syft_arch="arm64" ;; \
        *) echo "Unsupported Syft architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    archive="syft_${SYFT_VERSION}_linux_${syft_arch}.tar.gz"; \
    base_url="https://github.com/anchore/syft/releases/download/v${SYFT_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${base_url}/${archive}" -o "${tmp_dir}/${archive}"; \
    curl -fsSL "${base_url}/syft_${SYFT_VERSION}_checksums.txt" -o "${tmp_dir}/checksums.txt"; \
    (cd "${tmp_dir}" && grep "  ${archive}$" checksums.txt | sha256sum -c -); \
    tar -xzf "${tmp_dir}/${archive}" -C /usr/local/bin syft; \
    chmod 0755 /usr/local/bin/syft; \
    rm -rf "${tmp_dir}"
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) uv_target="x86_64-unknown-linux-gnu" ;; \
        arm64) uv_target="aarch64-unknown-linux-gnu" ;; \
        *) echo "Unsupported uv architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    uv_archive="uv-${uv_target}.tar.gz"; \
    uv_base_url="https://github.com/astral-sh/uv/releases/download/${UV_VERSION}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${uv_base_url}/${uv_archive}" -o "${tmp_dir}/${uv_archive}"; \
    curl -fsSL "${uv_base_url}/${uv_archive}.sha256" -o "${tmp_dir}/${uv_archive}.sha256"; \
    (cd "${tmp_dir}" && sha256sum -c "${uv_archive}.sha256"); \
    tar -xzf "${tmp_dir}/${uv_archive}" -C "${tmp_dir}"; \
    install -m 0755 "${tmp_dir}/uv-${uv_target}/uv" /usr/local/bin/uv; \
    install -m 0755 "${tmp_dir}/uv-${uv_target}/uvx" /usr/local/bin/uvx; \
    rm -rf "${tmp_dir}"
COPY ./dotnet/dotnet-wrapper.sh /usr/local/bin/dotnet
RUN sed -i 's/\r$//' /usr/local/bin/dotnet \
    && chmod 0755 /usr/local/bin/dotnet
COPY ./spec-kit/patch-specify-cli.py /usr/local/bin/patch-specify-cli.py
RUN chmod 0644 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p /etc/codex
COPY ./codex/config.toml /etc/codex/config.toml
COPY ./codex/config.toml /etc/codex/managed_config.toml
COPY ./codex/requirements.toml /etc/codex/requirements.toml
RUN chmod 0644 /etc/codex/config.toml /etc/codex/managed_config.toml /etc/codex/requirements.toml

RUN useradd -m adedev
RUN mkdir -p /dotnet-build && chown adedev:adedev /dotnet-build
USER adedev
ENV PATH="/usr/local/go/bin:/home/adedev/go/bin:/home/adedev/.cargo/bin:/home/adedev/.local/bin:${PATH}"
ENV CODEX_HOME="/home/adedev/.codex" \
    CLAUDE_CONFIG_DIR="/home/adedev/.claude" \
    GEMINI_CLI_HOME="/home/adedev/.gemini-home" \
    COPILOT_HOME="/home/adedev/.copilot" \
    DISABLE_AUTOUPDATER="1"
WORKDIR /home/adedev
RUN go install "golang.org/x/tools/gopls@${GOPLS_VERSION}" \
    && go install "honnef.co/go/tools/cmd/staticcheck@${STATICCHECK_VERSION}" \
    && go install "golang.org/x/vuln/cmd/govulncheck@${GOVULNCHECK_VERSION}" \
    && go install "github.com/go-delve/delve/cmd/dlv@${DELVE_VERSION}"
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    case "${arch}" in \
        amd64) rust_host="x86_64-unknown-linux-gnu" ;; \
        arm64) rust_host="aarch64-unknown-linux-gnu" ;; \
        *) echo "Unsupported rustup architecture: ${arch}" >&2; exit 1 ;; \
    esac; \
    rustup_base_url="https://static.rust-lang.org/rustup/archive/${RUSTUP_VERSION}/${rust_host}"; \
    tmp_dir="$(mktemp -d)"; \
    curl -fsSL "${rustup_base_url}/rustup-init" -o "${tmp_dir}/rustup-init"; \
    curl -fsSL "${rustup_base_url}/rustup-init.sha256" -o "${tmp_dir}/rustup-init.sha256"; \
    (cd "${tmp_dir}" && sha256sum -c rustup-init.sha256); \
    chmod 0755 "${tmp_dir}/rustup-init"; \
    "${tmp_dir}/rustup-init" -y --no-modify-path --profile minimal --default-host "${rust_host}" --default-toolchain "${RUST_TOOLCHAIN}"; \
    rm -rf "${tmp_dir}"; \
    rustup component add rustfmt clippy rust-analyzer rust-src
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3 \
    && python3 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p \
      /home/adedev/.local/share/opencode \
      /home/adedev/.codex \
      /home/adedev/.claude \
      /home/adedev/.gemini-home \
      /home/adedev/.copilot
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc
USER root
COPY ./scripts/audit-export.sh /usr/local/bin/audit-export
COPY ./scripts/container-entrypoint.sh /usr/local/bin/ade-entrypoint
COPY ./scripts/install-home-baseline-reference.sh /usr/local/bin/install-home-baseline-reference
COPY ./home-baseline.lock.json /usr/local/share/absdd-image-sandbox/home-baseline.lock.json
RUN sed -i 's/\r$//' /usr/local/bin/audit-export /usr/local/bin/ade-entrypoint \
        /usr/local/bin/install-home-baseline-reference \
    && chmod 0755 /usr/local/bin/audit-export /usr/local/bin/ade-entrypoint \
        /usr/local/bin/install-home-baseline-reference \
    && install-home-baseline-reference \
        /usr/local/share/absdd-image-sandbox/home-baseline.lock.json \
        /opt/home-baseline \
    && ln -s /opt/home-baseline /home/adedev/home-baseline-tmp \
    && chown -h adedev:adedev /home/adedev/home-baseline-tmp
USER adedev

ENTRYPOINT ["/usr/local/bin/ade-entrypoint"]
CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
