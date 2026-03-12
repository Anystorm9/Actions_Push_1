import random
from sikuli import *

zona = Location(125, 412)
zona1 = Location(1010, 679)
zona2 = Location(640, 725)
zona3 = Location(1108, 601)
zona4 = Location(635, 609)

imagen = "imagen.png"
patron = Pattern(imagen).similar(0.9)

imagen0 = "imagen0.png"
patron0 = Pattern(imagen0).similar(0.9)

def espera_aleatoria(min_seg=1, max_seg=10):
    wait(random.uniform(min_seg, max_seg))

# CLICK ALEATORIO EN UN RANGO DE ±10 PIXELES
def click_aleatorio(zona, rango=10):
    x = zona.getX() + random.randint(-rango, rango)
    y = zona.getY() + random.randint(-rango, rango)
    hover(Location(x, y))
    wait(random.uniform(0.1, 0.5))
    click(Location(x, y))

firefox = App("firefox")
firefox.focus()

espera_aleatoria(1,10)

click_aleatorio(zona)

type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)
type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)

click_aleatorio(zona1)

type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)

type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)
type(Key.DOWN)

espera_aleatoria(1,10)
type("1", Key.ALT)
type(Key.UP)
type("1", Key.ALT)

espera_aleatoria(1,10)
firefox.focus()
type("1", Key.ALT)
type(Key.UP)
type("1", Key.ALT)

espera_aleatoria(1,10)
firefox.focus()
type("1", Key.ALT)

type(Key.UP)
type("1", Key.ALT)

espera_aleatoria(1,10)

if exists(patron):
    print("Imagen encontrada")
    click(patron)
else:
    print("Imagen no encontrada")

click_aleatorio(zona3)
type("1", Key.ALT)
click_aleatorio(zona3)

type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)

espera_aleatoria(1,10)
type("1", Key.ALT)
type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)

espera_aleatoria(1,10)
type("1", Key.ALT)
type(Key.DOWN)
type("1", Key.ALT)
type("1", Key.ALT)
type("1", Key.ALT)

click_aleatorio(zona3)
type("1", Key.ALT)

espera_aleatoria(1,10)
type(Key.DOWN)
type("1", Key.ALT)

click_aleatorio(zona3)
type("1", Key.ALT)

espera_aleatoria(1,10)
type(Key.DOWN)
type("1", Key.ALT)

click_aleatorio(zona3)
type("1", Key.ALT)

click_aleatorio(zona4)

espera_aleatoria(1,10)
type("1", Key.ALT)
type("1", Key.ALT)

if exists(patron0):
    print("Imagen encontrada")
    click(patron0)
else:
    print("Imagen no encontrada")

#https://ouo.io/rG8i4g
#https://104.223.85.164/go/rG8i4g?__pot=aHR0cHM6Ly9vdW8uaW8 proxyorb
