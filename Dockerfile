FROM debian:trixie

RUN apt-get -y update && apt-get -y install nodejs npm
RUN npm i -g opencode-ai@latest

RUN useradd -m opencode
USER opencode
RUN mkdir -p /home/opencode/.local/share/opencode
COPY --chown=opencode:opencode ./opencode.json /home/opencode/.config/opencode/opencode.json

CMD ["/bin/bash", "-c", "while :; do sleep 1; done;"]
