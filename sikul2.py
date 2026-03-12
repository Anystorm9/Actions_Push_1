import random
from sikuli import *

# ---------- SETTINGS ----------
Settings.MoveMouseDelay = 0.25
Settings.Highlight = True

# ---------- IMAGENES ----------
patron = Pattern("imagen.png").similar(0.88)
patron0 = Pattern("imagen0.png").similar(0.88)
patronx = Pattern("tab.png").similar(0.85)
patron_tab0 = Pattern("tab0.png").similar(0.80)
patron1 = Pattern("pal.png").similar(0.80)

# ---------- SCROLL HUMANO ----------
def scroll_humano():

    pasos = random.randint(3,6)

    for i in range(pasos):
        type(Key.DOWN)
        wait(random.uniform(0.2,0.4))

# ---------- CLICK HUMANO ----------
def click_humano(loc):

    mouseMove(loc)
    wait(random.uniform(0.1,0.25))
    click(loc)

# ---------- CLICK EN IMAGEN ----------
def click_en_imagen(match):

    r = match

    x = random.randint(r.getX()+8, r.getX()+r.getW()-8)
    y = random.randint(r.getY()+8, r.getY()+r.getH()-8)

    click_humano(Location(x,y))

# ---------- BUSCAR IMAGENES ----------
def buscar_imagenes():

    m1 = SCREEN.exists(patron,0.3)

    if m1:
        print("Click imagen")
        wait(4)  # 4-second delay before clicking
        click_en_imagen(m1)
        return True

    m2 = SCREEN.exists(patron0,0.3)

    if m2:
        print("Click imagen0")
        wait(4)  # 4-second delay before clicking
        click_en_imagen(m2)
        return True

    return False

# ---------- BUSCAR TAB ----------
def buscar_tab():

    m = SCREEN.exists(patronx,2)

    if m:

        print("Click TAB")

        click_en_imagen(m)

        wait(2)

        return True

    else:

        print("Abriendo URL")

        type("t", Key.CTRL)

        wait(0.5)

        paste("https://ouo.io/rG8i4g")

        type(Key.ENTER)

        wait(8)

        return False

# ---------- VERsIFICACION INICIAL ----------
def verificacion_inicial():

    print("Buscando TAB0")

    mr = SCREEN.exists(patron_tab0,5)

    if mr:

        print("TAB0 encontrada")

        click_en_imagen(mr)

        wait(8)

        m2 = SCREEN.exists(patron1,5)

        if m2:

            print("Click imagen1")

            click_en_imagen(m2)

        wait(2)

        return True

    else:

        print("TAB0 no encontrada")

        return False

# ---------- BUSCAR CON SCROLL ----------
def buscar_con_scroll(intentos=25):

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

        wait(random.uniform(0.5,1))

# ---------- INICIO ----------
verificacion_inicial()

ciclo()
