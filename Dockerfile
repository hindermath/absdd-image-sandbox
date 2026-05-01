FROM mcr.microsoft.com/dotnet/sdk:latest

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends ca-certificates curl git nodejs npm \
    && rm -rf /var/lib/apt/lists/*
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
RUN npm i -g opencode-ai@latest
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && install -m 0755 /root/.local/bin/uv /usr/local/bin/uv \
    && install -m 0755 /root/.local/bin/uvx /usr/local/bin/uvx
COPY ./dotnet/dotnet-wrapper.sh /usr/local/bin/dotnet
RUN chmod 0755 /usr/local/bin/dotnet

RUN useradd -m opencode
RUN mkdir -p /dotnet-build && chown opencode:opencode /dotnet-build
USER opencode
ENV PATH="/home/opencode/.local/bin:${PATH}"
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3
RUN mkdir -p /home/opencode/.local/share/opencode
COPY --chown=opencode:opencode ./opencode.json /home/opencode/.config/opencode/opencode.json

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
