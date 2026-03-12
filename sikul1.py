import random
from sikuli import *

Settings.MoveMouseDelay = 0.25

# ---------- IMAGENES ----------
patron = Pattern("imagen.png").similar(0.88)
patron0 = Pattern("imagen0.png").similar(0.88)
patronx = Pattern("tab.png").similar(0.85)
patron_tab0 = Pattern("tab0.png").similar(0.85)

# ---------- SCROLL ----------
def scroll_humano():

    pasos = random.randint(6,12)

    for i in range(pasos):
        type(Key.DOWN)
        wait(random.uniform(0.03,0.08))

# ---------- CLICK HUMANO ----------
def click_humano(loc):

    mouseMove(loc)
    wait(random.uniform(0.1,0.2))
    click(loc)

# ---------- CLICK EN IMAGEN ----------
def click_en_imagen(match):

    r = match

    x = random.randint(r.getX()+8, r.getX()+r.getW()-8)
    y = random.randint(r.getY()+8, r.getY()+r.getH()-8)

    click_humano(Location(x,y))

# ---------- BUSCAR CUALQUIER IMAGEN ----------
def buscar_imagenes():

    m1 = SCREEN.exists(patron,0.2)

    if m1:
        print("Click imagen")
        click_en_imagen(m1)
        return True

    m2 = SCREEN.exists(patron0,0.2)

    if m2:
        print("Click imagen0")
        click_en_imagen(m2)
        return True

    return False

# ---------- BUSCAR TAB ----------
def buscar_tab():

    m = SCREEN.exists(patronx,1)

    if m:

        print("Click TAB")

        click_humano(m.getTarget())

        wait(1)

        return True

    else:

        print("Abriendo URL")

        type("t", Key.CTRL)

        wait(0.5)

        paste("https://ouo.io/rG8i4g")

        type(Key.ENTER)

        wait(5)

        return False

# ---------- VERIFICACION INICIAL TAB0 ----------
def verificacion_inicial():

    print("Buscando TAB0")

    m = SCREEN.exists(patron_tab0,1)

    if m:

        print("TAB0 encontrada")

        # CAMBIA ESTAS COORDENADAS
        click_humano(Location(500,400))

        wait(1)

        return True

    else:

        print("TAB0 no encontrada")

        return False

# ---------- BUSCAR CON SCROLL ----------
def buscar_con_scroll(intentos=20):

    for i in range(intentos):

        if buscar_imagenes():
            return True

        scroll_humano()

    return False

# ---------- CICLO PRINCIPAL ----------
def ciclo():

    while True:

        print("Buscando imagen o imagen0")

        encontrado = buscar_con_scroll(25)

        if not encontrado:

            print("No se encontraron imagenes")

            buscar_tab()

        wait(0.5)

# ---------- INICIO ----------
verificacion_inicial()
ciclo()