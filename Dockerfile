FROM mcr.microsoft.com/dotnet/sdk:latest

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends ca-certificates curl git \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get -y install --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*
RUN dotnet workload config --update-mode manifests \
    && dotnet workload update
RUN npm i -g opencode-ai@latest
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && install -m 0755 /root/.local/bin/uv /usr/local/bin/uv \
    && install -m 0755 /root/.local/bin/uvx /usr/local/bin/uvx
COPY ./dotnet/dotnet-wrapper.sh /usr/local/bin/dotnet
RUN chmod 0755 /usr/local/bin/dotnet
COPY ./spec-kit/patch-specify-cli.py /usr/local/bin/patch-specify-cli.py

RUN useradd -m adedev
RUN mkdir -p /dotnet-build && chown adedev:adedev /dotnet-build
USER adedev
ENV PATH="/home/adedev/.local/bin:${PATH}"
RUN uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v0.8.3 \
    && python3 /usr/local/bin/patch-specify-cli.py
RUN mkdir -p /home/adedev/.local/share/opencode
COPY --chown=adedev:adedev ./opencode.jsonc /home/adedev/.config/opencode/opencode.jsonc

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
