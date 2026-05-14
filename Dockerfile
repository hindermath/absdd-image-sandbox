FROM docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox:latest

ARG DOTNET_SDK_PACKAGE=dotnet-sdk-10.0
ARG GO_VERSION=1.26.3
ARG GOPLS_VERSION=v0.21.1
ARG STATICCHECK_VERSION=v0.7.0
ARG GOVULNCHECK_VERSION=v1.3.0
ARG DELVE_VERSION=v1.26.3
ARG RUST_TOOLCHAIN=1.95.0

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
    && apt-get -y update \
    && apt-get -y install --no-install-recommends "${DOTNET_SDK_PACKAGE}" \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get -y install --no-install-recommends nodejs \
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
RUN npm i -g opencode-ai@latest @openai/codex@latest \
    && ln -sf "$(npm root -g)/@openai/codex/bin/codex.js" /usr/local/bin/codex
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && install -m 0755 /root/.local/bin/uv /usr/local/bin/uv \
    && install -m 0755 /root/.local/bin/uvx /usr/local/bin/uvx
COPY ./dotnet/dotnet-wrapper.sh /usr/local/bin/dotnet
RUN sed -i 's/\r$//' /usr/local/bin/dotnet \
    && chmod 0755 /usr/local/bin/dotnet
COPY ./spec-kit/patch-specify-cli.py /usr/local/bin/patch-specify-cli.py
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
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
    | sh -s -- -y --no-modify-path --profile minimal --default-toolchain "${RUST_TOOLCHAIN}" \
    && rustup component add rustfmt clippy rust-analyzer rust-src
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3 \
    && python3 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p /home/adedev/.local/share/opencode
RUN mkdir -p /home/adedev/.codex
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
