import random
from sikuli import *

# ---------- AJUSTES DE MOUSE ----------
Settings.MoveMouseDelay = 0.3
Settings.DelayAfterDrag = 0.2
Settings.DelayBeforeMouseDown = 0.1
Settings.DelayAfterMouseDown = 0.1

# ---------- IMAGENES ----------
patron = Pattern("imagen.png").similar(0.88)
patron0 = Pattern("imagen0.png").similar(0.88)
patronx = "tab.png"  # pestaña prioritaria

# ---------- ESPERA HUMANA ----------
def espera(min=1,max=4):
    wait(random.uniform(min,max))

# ---------- MOVIMIENTO HUMANO ----------
def mover_mouse_humano(destino):
    try:
        actual = Env.getMouseLocation()
    except:
        actual = Location(500,500)
    pasos = random.randint(10,18)
    for i in range(pasos):
        curva = random.uniform(-3,3)
        x = actual.x + (destino.x - actual.x) * i / pasos + curva
        y = actual.y + (destino.y - actual.y) * i / pasos + curva
        try:
            mouseMove(Location(int(x),int(y)))
        except:
            wait(0.1)
        wait(random.uniform(0.01,0.03))

# ---------- CLICK HUMANO ----------
def click_humano(p):
    try:
        mover_mouse_humano(p)
        wait(random.uniform(0.08,0.25))
        click(p)
    except:
        print("Mouse bloqueado, reintentando...")
        wait(0.5)
        mouseMove(p)
        click(p)

# ---------- CLICK EN IMAGEN ----------
def click_en_imagen(match):
    r = match
    x = random.randint(r.getX()+3, r.getX()+r.getW()-3)
    y = random.randint(r.getY()+3, r.getY()+r.getH()-3)
    destino = Location(x,y)
    click_humano(destino)

# ---------- DETECTAR PESTAÑA PRIORITARIA ----------
def reaccion_pestana():
    m = SCREEN.exists(patronx,0.2)
    if m:
        print("Pestaña detectada")
        click_humano(m.getTarget())
        wait(random.uniform(0.6,1.2))
        return True
    return False

# ---------- FUNCION DE SCROLL CONTINUO HASTA ENCONTRAR IMAGEN ----------
def scroll_hasta_imagen(patron_buscar, max_scroll=1000):
    scrolls = 0
    while scrolls < max_scroll:
        # revisar si la imagen aparece
        m = SCREEN.exists(patron_buscar,0.2)
        if m:
            print(str(patron_buscar) + " encontrada")
            wait(random.uniform(0.5,1))
            click_en_imagen(m)
            return True

        # reaccion a pestaña si aparece
        reaccion_pestana()

        # scroll hacia abajo
        type(Key.DOWN)
        wait(random.uniform(0.08,0.25))
        scrolls += 1

    print(str(patron_buscar) + " NO se encontro")
    return False

# ---------- SCRIPT PRINCIPAL ----------

# 1️⃣ Buscar imagen y click
scroll_hasta_imagen(patron)

espera(1,3)

# 2️⃣ Click en pestaña prioritaria si aparece (ya estaba funcionando)
reaccion_pestana()

espera(1,3)

# 3️⃣ Continuar scroll hasta encontrar imagen0
scroll_hasta_imagen(patron0)