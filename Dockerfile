# Base Image
FROM debian:bullseye

# Instalar paquetes necesarios
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
RUN wget -O /usr/local/bin/sikulixide.jar https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar && \
    chmod +x /usr/local/bin/sikulixide.jar

# Instalar Cloudflared
RUN curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && \
    dpkg -i cloudflared.deb && \
    rm cloudflared.deb

# Configurar SSH
RUN echo 'root:yourpassword' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# XFCE como sesión por defecto
RUN echo "xfce4-session" > /etc/skel/.xsession

# Configurar root
RUN mkdir -p /root && \
    echo "xfce4-session" > /root/.xsession && \
    chown root:root /root /root/.xsession

# Copiar ZIP
COPY Rdsx.zip /

# Extraer ZIP con contraseña
ARG ZIP_PASSWORD
RUN unzip -P "$ZIP_PASSWORD" -o /Rdsx.zip -d / && \
    rm /Rdsx.zip && \
    chmod +x /start.sh

# Exponer puertos
EXPOSE 5901
EXPOSE 22

# Ejecutar
CMD ["/start.sh"]