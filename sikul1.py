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
patronx = Pattern("tab.png").similar(0.85)

# ---------- ESPERA HUMANA ----------
def espera(a=1,b=3):
    wait(random.uniform(a,b))

# ---------- MICRO PAUSA HUMANA ----------
def micro_pausa():
    if random.random() < 0.15:
        wait(random.uniform(0.4,1.2))

# ---------- PAUSA LARGA OCASIONAL ----------
def pausa_larga():
    if random.random() < 0.05:
        t = random.uniform(4,9)
        print("Pausa humana:", t)
        wait(t)

# ---------- MOVIMIENTO HUMANO ----------
def mover_mouse_humano(destino):

    try:
        actual = Env.getMouseLocation()
    except:
        actual = Location(500,500)

    pasos = random.randint(15,25)

    for i in range(pasos):

        curvaX = random.uniform(-6,6)
        curvaY = random.uniform(-6,6)

        x = actual.x + (destino.x-actual.x)*i/pasos + curvaX
        y = actual.y + (destino.y-actual.y)*i/pasos + curvaY

        mouseMove(Location(int(x),int(y)))

        wait(random.uniform(0.01,0.04))

# ---------- CLICK HUMANO ----------
def click_humano(p):

    mover_mouse_humano(p)

    wait(random.uniform(0.15,0.35))

    click(p)

    micro_pausa()

# ---------- CLICK DENTRO DE IMAGEN ----------
def click_en_imagen(match):

    r = match

    margen = 8

    x = random.randint(r.getX()+margen, r.getX()+r.getW()-margen)
    y = random.randint(r.getY()+margen, r.getY()+r.getH()-margen)

    destino = Location(x,y)

    click_humano(destino)

# ---------- BUSCAR IMAGEN ----------
def buscar_imagen():

    m = SCREEN.exists(patron,0.5)

    if m:
        print("Click en imagen")
        click_en_imagen(m)
        return True

    return False

# ---------- BUSCAR IMAGEN0 ----------
def buscar_imagen0():

    m = SCREEN.exists(patron0,0.5)

    if m:
        print("Click en imagen0")
        click_en_imagen(m)
        return True

    return False

# ---------- ABRIR LINK EN NUEVA TAB ----------
def abrir_link():

    print("TAB no encontrada, abriendo link")

    type("t", Key.CTRL)

    wait(random.uniform(0.8,1.5))

    type("https://ouo.io/rG8i4g")

    wait(random.uniform(0.3,0.8))

    type(Key.ENTER)

    wait(random.uniform(3,5))

# ---------- BUSCAR TAB ----------
def buscar_tab():

    m = SCREEN.exists(patronx,1)

    if m:
        print("Click en TAB")

        click_humano(m.getTarget())

        wait(random.uniform(1,2))

        return True

    else:
        abrir_link()
        return False

# ---------- SCROLL HUMANO ----------
def scroll_humano():

    pasos = random.randint(3,8)

    for i in range(pasos):

        type(Key.DOWN)

        wait(random.uniform(0.05,0.25))

        if random.random() < 0.2:
            wait(random.uniform(0.2,0.5))

# ---------- BUSCAR IMAGENES CON SCROLL ----------
def buscar_con_scroll(funcion_busqueda, intentos=6):

    for i in range(intentos):

        encontrado = funcion_busqueda()

        if encontrado:
            return True

        scroll_humano()
        espera(0.5,1.2)

    return False

# ---------- CICLO PRINCIPAL ----------
def ciclo():

    while True:

        pausa_larga()

        # PASO 1: buscar imagen
        encontrado = buscar_con_scroll(buscar_imagen,5)

        if encontrado:

            espera(1,2)

            # PASO 2: buscar imagen0
            encontrado2 = buscar_con_scroll(buscar_imagen0,6)

            if encontrado2:

                espera(1,2)

                scroll_humano()

            else:

                print("imagen0 no encontrada")

        else:

            print("No hay imagen, buscando TAB")

            buscar_tab()

        micro_pausa()

# ---------- INICIO ----------
ciclo()