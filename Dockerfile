# Tag latest observed on 2026-05-14, pinned here by digest for reproducible builds.
FROM docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox@sha256:a21e15872aed8b0e4b9e18e0ff1e678318968efb4b8367ddf9fa4a63fc1d294c

# renovate-dotnet: datasource=dotnet-version depName=dotnet-sdk versioning=semver extractVersion=^(?<version>\d+\.\d+) argName=DOTNET_SDK_PACKAGE
ARG DOTNET_SDK_PACKAGE=dotnet-sdk-10.0
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
# renovate: datasource=node-version depName=node versioning=node argName=NODE_MAJOR
ARG NODE_MAJOR=22
# renovate: datasource=github-releases depName=astral-sh/uv versioning=semver argName=UV_VERSION
ARG UV_VERSION=0.11.16
# renovate: datasource=npm depName=opencode-ai versioning=npm argName=OPENCODE_VERSION
ARG OPENCODE_VERSION=1.14.50
# renovate: datasource=npm depName=@openai/codex versioning=npm argName=CODEX_VERSION
ARG CODEX_VERSION=0.130.0

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
        jq \
        just \
        libssl-dev \
        maven \
        openjdk-21-jdk-headless \
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
    && wget https://packages.microsoft.com/config/debian/13/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
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
    && apt-get -y install --no-install-recommends "${DOTNET_SDK_PACKAGE}" nodejs \
    && ln -sf /usr/bin/fdfind /usr/local/bin/fd \
    && rm -rf /var/lib/apt/lists/*
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
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
RUN npm i -g "opencode-ai@${OPENCODE_VERSION}" "@openai/codex@${CODEX_VERSION}" \
    && ln -sf "$(npm root -g)/@openai/codex/bin/codex.js" /usr/local/bin/codex
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

RUN useradd -m adedev
RUN mkdir -p /dotnet-build && chown adedev:adedev /dotnet-build
USER adedev
ENV PATH="/usr/local/go/bin:/home/adedev/go/bin:/home/adedev/.cargo/bin:/home/adedev/.local/bin:${PATH}"
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
RUN mkdir -p /home/adedev/.local/share/opencode
RUN mkdir -p /home/adedev/.codex
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc
USER root
COPY ./scripts/audit-export.sh /usr/local/bin/audit-export
COPY ./scripts/container-entrypoint.sh /usr/local/bin/ade-entrypoint
RUN sed -i 's/\r$//' /usr/local/bin/audit-export /usr/local/bin/ade-entrypoint \
    && chmod 0755 /usr/local/bin/audit-export /usr/local/bin/ade-entrypoint
USER adedev

ENTRYPOINT ["/usr/local/bin/ade-entrypoint"]
CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
