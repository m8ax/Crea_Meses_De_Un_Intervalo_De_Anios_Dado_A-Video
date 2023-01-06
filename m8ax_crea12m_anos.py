# Programa Para Crear Calendarios De lOS 12 Meses, Del Año Que Le Digas... Hasta El Año Que Le Digas.
# Crea 12 Imágenes Por Año En El Intervalo Que Le Hemos Dicho, Una Con Cada Mes...
# Si En El Intervalo Le Decimos Que Haga Calendarios De 2020 A 2022, Hará 36 Calendarios Porque Son 3 Años...
# A Cada Calendario Se Le Añade El Fondo m8axfondo.png Con Mi Logo Difuminado... Se Pude Cambiar Por Lo Que Se Quiera, Editando La Imágen.
# Cuando Termine De Generar Los Calendarios, Hará Un Video Con Todos Ellos...

import calendar
import os
import time
import numpy as np
import errno
import glob
import cv2
from shutil import rmtree
from PIL import Image, ImageDraw, ImageFont

def Romano(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    miles = m[num // 1000]
    cientos = c[(num % 1000) // 100]
    decenas = x[(num % 100) // 10]
    unidad = i[num % 10]
    solucion = miles + cientos + decenas + unidad
    return solucion

def segahms(segundos):
    horas = int(segundos / 60 / 60)
    segundos -= horas * 60 * 60
    minutos = int(segundos / 60)
    segundos -= minutos * 60
    return f"{horas}h:{minutos}m:{int(segundos)}s"

def barra_progreso_vibrante(progreso, total, tiembarra):
    porcen = 100 * (progreso / float(total))
    segrestante = 0
    if porcen > 0:
        segrestante = (100 * (tiembarra - time.time()) / porcen) - (
            tiembarra - time.time()
        )
    barra = "█" * int(porcen) + "-" * (100 - int(porcen))
    print(
        (
            f"\r\033[38;2;{np.random.randint(0, 256)};{np.random.randint(0, 256)};{np.random.randint(0, 256)}m{porcen:.2f}% - |{barra}|"
            f" - ETA - {segahms(segrestante*-1)}      "
        ),
        end="\r\033[0m",
    )

month_names = {
    "January": "Enero",
    "February": "Febrero",
    "March": "Marzo",
    "April": "Abril",
    "May": "Mayo",
    "June": "Junio",
    "July": "Julio",
    "August": "Agosto",
    "September": "Septiembre",
    "October": "Octubre",
    "November": "Noviembre",
    "December": "Diciembre",
}

os.system("cls")

try:
    rmtree("M8AX-ResultadoS")
except:
    nn = 0

try:
    os.mkdir("M8AX-ResultadoS")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

yearr = int(
    input("\n¿ Desde Que Año, Quieres Que Hagamos Calendarios Con Sus 12 Meses ?\n\n")
)

hasta = int(input("\n¿ Hasta Que Año, Hacemos Calendarios Con Sus 12 Meses ?\n\n"))
hasta += 1
cuantosa = hasta - yearr
vamos = 0
tiembarra = time.time()
totaltiem = tiembarra
print("\nM8AX - ... Comienzo De La Creación De Calendarios ...\n")
nn = 0

for year in range(yearr, hasta):
    vamos += 1

    for k in range(1, 13):
        month = k
        image = Image.new("RGB", (1920, 1080), (255, 255, 255))
        imagen1 = Image.open("m8axfondo.png")
        image.paste(imagen1)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 17)
        draw.text(
            (1600, 1045),
            "MvIiIaX Corp. https://youtube.com/m8ax",
            font=font,
            fill="gray",
        )
        font = ImageFont.truetype("arial.ttf", 50)
        if month == 12 or month == 1 or month == 2:
            title = (
                month_names[calendar.month_name[month]]
                + " "
                + str(year)
                + " - "
                + Romano(year)
                + " - Invierno"
            )
        if month == 3 or month == 4 or month == 5:
            title = (
                month_names[calendar.month_name[month]]
                + " "
                + str(year)
                + " - "
                + Romano(year)
                + " - Primavera"
            )
        if month == 6 or month == 7 or month == 8:
            title = (
                month_names[calendar.month_name[month]]
                + " "
                + str(year)
                + " - "
                + Romano(year)
                + " - Verano"
            )
        if month == 9 or month == 10 or month == 11:
            title = (
                month_names[calendar.month_name[month]]
                + " "
                + str(year)
                + " - "
                + Romano(year)
                + " - Otoño"
            )
        l, t, r, b = font.getbbox(title)
        w, h = r - l, b - t
        draw.text(((1920 - w) / 2, 20), title, font=font, fill=(37, 90, 80))
        draw.line(((1920 - w) / 2, 80, (1920 + w) / 2, 80), fill=(0, 0, 0))
        font = ImageFont.truetype("arial.ttf", 39)
        days = [
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo",
        ]

        for i, day in enumerate(days):
            l, t, r, b = font.getbbox(day)
            w, h = r - l, b - t
            if days[i] == "Sábado" or days[i] == "Domingo":
                draw.text(
                    (i * (1920 / 7) + (1920 / 14) - w / 2, 80),
                    day,
                    font=font,
                    fill=(255, 0, 0),
                )
            else:
                draw.text(
                    (i * (1920 / 7) + (1920 / 14) - w / 2, 80),
                    day,
                    font=font,
                    fill=(0, 0, 0),
                )
        font = ImageFont.truetype("arial.ttf", 32)
        num_days = calendar.monthrange(year, month)[1]
        start_day = calendar.weekday(year, month, 1)
        day = 1
        loro = start_day - 1

        for i in range(start_day, start_day + num_days):
            loro += 1
            x = (i % 7) * (1920 / 7) + (1920 / 14)
            y = 120 + (i // 7) * (1080 / 6)
            if loro % 5 == 0 or loro % 6 == 0:
                draw.text((x, y), str(Romano(day)), font=font, fill=(255, 0, 0))
            else:
                draw.text((x, y), str(day), font=font, fill=(0, 0, 0))
            day += 1
            if loro == 7:
                loro = 0
        image.save("./M8AX-ResultadoS/" + str(year) + "-" + str(k) + ".png")
    barra_progreso_vibrante((vamos * 100) / cuantosa, 100, tiembarra)

barra_progreso_vibrante((vamos * 100) / cuantosa, 100, tiembarra)
print(
    "\n\nM8AX - ... Fin De Creacion De Calendarios ...\n\nM8AX - ... Comenzando Creación De Video ...\n"
)
framesize = ((1920), (1080))
outv = cv2.VideoWriter(
    "M8AX-Calendarios-" + str(yearr) + "_" + str(hasta) + "-Video.WebM",
    cv2.VideoWriter_fourcc(*"vp09"),
    1,
    framesize,
)
tiembarra = time.time()
print("")

for filename in sorted(glob.glob("./M8AX-ResultadoS/*.png"), key=os.path.getmtime):
    imgv = cv2.imread(filename)
    outv.write(imgv)
    nn = nn + 1
    barra_progreso_vibrante(
        (nn * 100) / (len(glob.glob("./M8AX-ResultadoS/*.png"))), 100, tiembarra
    )

barra_progreso_vibrante(
    (nn * 100) / (len(glob.glob("./M8AX-ResultadoS/*.png"))), 100, tiembarra
)
print("\n")
print(*sorted(glob.glob("./M8AX-ResultadoS/*.png"), key=os.path.getmtime), sep="\n")
outv.release()
calpors = round((cuantosa * 12) / (time.time() - totaltiem), 3)
print(
    f"\n... Video Realizado Correctamente ...\n\n----- M8AX INFORMACIÓN -----\n\nCalendarios Creados - {cuantosa*12}.\n\nTiempo De Proceso - {round(time.time()-totaltiem,3)} Segundos - {segahms(time.time()-totaltiem)}.\n\nCalendarios Por Segundo Procesados - {calpors} Cal/s.\n\nA Este Rítmo, En Un Minuto Se Realizan - {round(calpors*60,3)} Calendarios.\n\nA Este Rítmo, En Una Hora Se Realizan - {round(calpors*3600,3)} Calendarios."
)
print("\nSuscribete A Mi Canal De Youtube - https://youtube.com/m8ax")