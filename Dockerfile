# Base
FROM debian:bullseye

# Password del zip
ARG ZIP_PASSWORD

# Instalar dependencias
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
https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar

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

RUN mkdir -p /root && \
echo "xfce4-session" > /root/.xsession

# Copiar zip
COPY Rdsx.zip /Rdsx.zip

# Extraer zip y mover TODO a /
RUN unzip -P "$ZIP_PASSWORD" /Rdsx.zip -d /tmp && \
mv /tmp/*/* / 2>/dev/null || true && \
mv /tmp/* / 2>/dev/null || true && \
chmod +x /start.sh && \
rm -rf /tmp /Rdsx.zip

# Puertos
EXPOSE 5901
EXPOSE 22

# Ejecutar script
CMD ["/start.sh"]