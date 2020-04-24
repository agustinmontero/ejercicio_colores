from PIL import Image
import matplotlib.pyplot as plt
import glob

img_list = glob.glob('img/*.jpg')
img_rgb = []
IMG_COLOR = 'RGB'

for i in img_list:
    img_rgb.append(Image.open(i).convert(IMG_COLOR))

red_channel = []
green_channel = []
blue_channel = []

for i in img_rgb:
    r, g, b = i.split()
    red_channel.append(r)
    green_channel.append(g)
    blue_channel.append(b)


filtro_rojo = (1, 0, 0)
filtro_verde = (0, 1, 0)
filtro_blue = (0, 0, 1)
filtro_amarillo = (1, 1, 0)
filtro_fucsia = (1, 0, 0.8)
filtros_colores = [filtro_rojo, filtro_verde, filtro_blue, filtro_amarillo, filtro_fucsia]


def ponderar_color(filtro, r, g, b):
    """
    Pondera los colores rgb, según el filtro.
    :param filtro: filtro de un color
    :param r: canal red
    :param g: canal green
    :param b: canal blue
    :return: tupla (r, g, b) ponderada segun el filtro
    """
    r1 = r.point(lambda j: j * filtro[0])
    g1 = g.point(lambda j: j * filtro[1])
    b1 = b.point(lambda j: j * filtro[2])
    return r1, g1, b1


resultado_ponderado_lista = []
for i in range(len(img_rgb)):
    res_p_temp = []
    for f in filtros_colores:
        res_p_temp.append(ponderar_color(f, red_channel[i], green_channel[i], blue_channel[i]))
    resultado_ponderado_lista.append(res_p_temp)

resultado_merge = []
for r_ponderado in resultado_ponderado_lista:
    r_merge_temp = []
    for r in r_ponderado:
        pass

# resultado5 = Image.merge('RGB', (r5, g5, b5)

# %%


