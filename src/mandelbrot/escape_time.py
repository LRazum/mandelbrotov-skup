from numpy import zeros
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def escape_time(a, b, MAX_ITER):

    x = 0
    y = 0

    for n in range(0, MAX_ITER):

        x_novi = x*x - y*y + a
        y_novi = 2*x*y + b

        x = x_novi
        y = y_novi

        if x*x + y*y > 4:
            return (1, n)

    return (0, MAX_ITER)



def escape_time_plot(W, H, a_min, a_max, b_min, b_max, MAX_ITER):

    slika = zeros((H, W, 3))

    paleta = plt.get_cmap("inferno")


    for q in range(0, H-1):

        b = b_max - ((q + 0.5) / H) * (b_max - b_min)

        for p in range(0, W-1):

            a = a_min + ((p + 0.5) / W) * (a_max - a_min)

            escaped, n = escape_time(a,b,MAX_ITER)

            if escaped == 0:
                slika[q,p] = (0,0,0)

            else:
                slika[q,p] = paleta(n / MAX_ITER)[:3]


    plt.imshow(slika, extent=(a_min, a_max, b_min, b_max))
    plt.show()

    return slika
