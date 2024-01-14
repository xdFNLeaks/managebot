FROM python:3.11 as builder
RUN apt-get update -y && apt-get install -y ca-certificates curl gnupg
RUN install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN chmod a+r /etc/apt/keyrings/docker.gpg
RUN echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update
RUN apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

FROM builder as pythonsetup
WORKDIR /usr/src/app
RUN pip install -U py-cord --pre

FROM pythonsetup
WORKDIR /usr/src/app
COPY "bot.py" .
VOLUME [ "/var/run/docker.sock" ]
VOLUME [ "/usr/src/app/config" ]
CMD [ "python", "./bot.py" ]
