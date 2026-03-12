# Instrucciones para el Entorno de Escritorio Remoto (VNC) y SSH

Este documento explica cómo construir y ejecutar un contenedor Docker que proporciona un entorno de escritorio completo (XFCE) accesible a través de VNC y una terminal a través de SSH. Ambos servicios se exponen a Internet de forma segura mediante túneles de Cloudflare.

## Paso 1: Construir la Imagen de Docker

Abre una terminal y ejecuta el siguiente comando en el directorio raíz del proyecto (la carpeta que contiene el directorio `ssh_connect`).

```bash
docker build -t rds .
```

- `-t mi-escritorio-vnc`: Nombra la imagen para identificarla fácilmente.
- `ssh_connect`: Indica a Docker que el `Dockerfile` y los archivos necesarios están dentro de este directorio.

## Paso 2: Ejecutar el Contenedor de Docker

Una vez construida la imagen, inicia el contenedor en segundo plano (detached mode):

```bash
docker run --name rds0 rds
```

## Paso 3: Obtener las URLs de Conexión (VNC y SSH)

El script de inicio del contenedor crea dos túneles de Cloudflare. Para obtener las URLs, necesitas ver los registros (logs) del contenedor. Espera unos 10-15 segundos para que los túneles se inicien.

Ejecuta este comando para ver los registros del último contenedor que iniciaste:

```bash
docker ps -q | xargs docker logs
```

La salida mostrará dos bloques de información importantes:

1.  **URL de SSH:**
    ```
    #####################################################################
    ## Your SSH connection URL is:
    https://ssh-url-aleatoria.trycloudflare.com
    #####################################################################
    ```

2.  **URL de VNC:**
    ```
    +--------------------------------------------------------------------------------------------+
    |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
    |  https://vnc-url-aleatoria.trycloudflare.com                                               |
    +--------------------------------------------------------------------------------------------+
    ```

**Copia ambas URLs.** Las necesitarás para conectarte.

---

## Paso 4: Conectarse al Contenedor

### **A) Conexión vía VNC (Escritorio Remoto)**

Necesitarás un cliente VNC. Recomendamos **RealVNC Viewer** o **TightVNC Viewer**.

1.  **Iniciar el Túnel Local:**
    En tu PC local, abre una terminal y ejecuta el siguiente comando, reemplazando `vnc-url-aleatoria.trycloudflare.com` con la URL de VNC que obtuviste.

    ```bash
    
    ```
    **Deja esta terminal abierta.** Está manteniendo el túnel activo.

2.  **Conectar con VNC Viewer:**
    - Abre tu cliente VNC.
    - Conéctate a la dirección: `localhost:5901`
    - Cuando te pida la contraseña, usa: `vncpass`

### **B) Conexión vía SSH (Terminal)**

Tienes dos métodos para conectarte por SSH.

#### **Método 1: Directo con Cloudflared (Recomendado)**

Este es el método más simple.

1.  Abre una nueva terminal en tu PC.
2.  Ejecuta el siguiente comando, reemplazando `ssh-url-aleatoria.trycloudflare.com` con tu URL de SSH.

    ```bash
    cloudflared access ssh --hostname ssh-url-aleatoria.trycloudflare.com
    ```
3.  Te pedirá el usuario y la contraseña:
    - **Usuario:** `root`
    - **Contraseña:** `yourpassword`

#### **Método 2: Túnel Manual (Alternativo)**

Este método requiere dos terminales.

1.  **Terminal 1: Iniciar el Túnel Local:**
    Ejecuta este comando para crear un túnel desde el puerto `2222` de tu PC al contenedor. Usa tu URL de SSH.

    ```bash
    cloudflared access tcp --hostname ssh-url-aleatoria.trycloudflare.com --url localhost:2222
    ```
    **Deja esta terminal abierta.**

2.  **Terminal 2: Conectar con SSH:**
    Abre una **segunda terminal** y conéctate a tu puerto local.

    ```bash
    ssh root@localhost -p 2222
    ```
    - **Contraseña:** `yourpassword`

---

## Solución de Problemas de SSH

### **Error: `WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!`**

Este error es normal si destruyes y recreas el contenedor. Significa que la "huella digital" del nuevo servidor SSH no coincide con la guardada anteriormente.

**Solución:**
Ejecuta este comando en tu terminal local para eliminar la huella antigua. Si usaste un puerto diferente, cámbialo.

- Para el método 2 (`-p 2222`):
  ```bash
  ssh-keygen -R "[localhost]:2222"
  ```

Después de ejecutarlo, intenta conectarte de nuevo. Te preguntará si confías en la nueva huella; escribe `yes` y presiona Enter.
