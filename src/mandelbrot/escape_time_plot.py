from numpy import zeros
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from mandelbrot.escape_time import escape_time


def piksel_u_a(p, W, a_min, a_max):

    sirina = a_max - a_min
    udio = (p + 0.5) / W
    a = a_min + udio * sirina
    return a


def piksel_u_b(q, H, b_min, b_max):

    visina = b_max - b_min
    udio = (q + 0.5) / H
    b = b_max - udio * visina
    return b


def boja_tocke(escaped, n, MAX_ITER, paleta):

    if escaped == 0:
        return (0, 0, 0)
    udio = n / MAX_ITER
    rgba = paleta(udio)
    rgb = rgba[:3]
    return rgb


def nacrtaj(slika, a_min, a_max, b_min, b_max):

    granice = (a_min, a_max, b_min, b_max)
    plt.imshow(slika, extent=granice)
    plt.show()


def escape_time_plot(W, H, a_min, a_max, b_min, b_max, MAX_ITER):

    slika = zeros((H, W, 3))
    paleta = plt.get_cmap("inferno")

    for q in range(0, H):
        b = piksel_u_b(q, H, b_min, b_max)
        for p in range(0, W):
            a = piksel_u_a(p, W, a_min, a_max)
            escaped, n = escape_time(a, b, MAX_ITER)
            slika[q, p] = boja_tocke(escaped, n, MAX_ITER, paleta)

    nacrtaj(slika, a_min, a_max, b_min, b_max)

    return slika



# 37 linija koda