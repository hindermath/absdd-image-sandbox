FROM docker.gitlab-ce.gwdg.de/agentic-coding/agent-sandbox/agent-sandbox:latest

ARG DOTNET_SDK_PACKAGE=dotnet-sdk-10.0

USER root
RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
        bubblewrap \
        ca-certificates \
        curl \
        direnv \
        fd-find \
        git \
        git-delta \
        jq \
        just \
        maven \
        openjdk-21-jdk-headless \
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
ENV PATH="/home/adedev/.local/bin:${PATH}"
WORKDIR /home/adedev
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3 \
    && python3 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p /home/adedev/.local/share/opencode
RUN mkdir -p /home/adedev/.codex
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
