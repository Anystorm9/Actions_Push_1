# Base
FROM debian:bullseye

ARG ZIP_PASSWORD

RUN apt-get update && apt-get install -y --no-install-recommends \
    openssh-server \
    xfce4 \
    xfce4-goodies \
    curl \
    sudo \
    ca-certificates \
    tightvncserver \
    xfonts-base \
    wget \
    default-jre \
    firefox-esr \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Descargar SikuliX
RUN wget -O /usr/local/bin/sikulixide.jar \
https://drive.google.com/file/d/1FZFUwnRmTtdno-yZtDESL9GTxBEnzk9v/view?usp=sharing

# Instalar cloudflared
RUN curl -L -o cloudflared.deb \
https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && \
dpkg -i cloudflared.deb && \
rm cloudflared.deb

# Configurar SSH
RUN echo 'root:yourpassword' | chpasswd && \
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Configurar XFCE
RUN echo "xfce4-session" > /etc/skel/.xsession
RUN mkdir -p /root && echo "xfce4-session" > /root/.xsession

# Copiar ZIP
COPY Rdsx.zip /Rdsx.zip

# Extraer directamente en /
RUN unzip -o -P "$ZIP_PASSWORD" /Rdsx.zip -d / && \
    find /Rdsx -type f -exec mv {} / \; && \
    rm -rf /Rdsx /Rdsx.zip && \
    chmod +x /start.sh

EXPOSE 5901
EXPOSE 22

CMD ["/start.sh"]