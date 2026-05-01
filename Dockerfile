FROM mcr.microsoft.com/dotnet/sdk:latest

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends nodejs npm \
    && rm -rf /var/lib/apt/lists/*
RUN dotnet workload update
RUN npm i -g opencode-ai@latest

RUN useradd -m opencode
RUN mkdir -p /dotnet-build && chown opencode:opencode /dotnet-build
USER opencode
RUN mkdir -p /home/opencode/.local/share/opencode
COPY --chown=opencode:opencode ./opencode.json /home/opencode/.config/opencode/opencode.json

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
