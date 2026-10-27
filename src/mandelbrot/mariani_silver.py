import numpy as np
import matplotlib.pyplot as plt
from .escape_time import escape_time


def mariani_silver_plot(W, H, a_min, a_max, b_min, b_max, MAX_ITER):
    
    rezultati = np.full((H, W), -1)

    korak_a = (a_max - a_min) / W
    korak_b = (b_max - b_min) / H

    def izracunaj(p, q):
        if rezultati[q, p] == -1:
            a = a_min + (p + 0.5) * korak_a
            b = b_max - (q + 0.5) * korak_b

            escaped, n = escape_time(a, b, MAX_ITER)

            if escaped:
                rezultati[q, p] = n
            else:
                rezultati[q, p] = MAX_ITER + 1

        return rezultati[q, p]

    def obradi(p0, p1, q0, q1):

        if p1 - p0 < 4 or q1 - q0 < 4:
            for q in range(q0, q1 + 1):
                for p in range(p0, p1 + 1):
                    izracunaj(p, q)
            return

        rub = []

        for p in range(p0, p1 + 1):
            rub.append(izracunaj(p, q0))
            rub.append(izracunaj(p, q1))

        for q in range(q0, q1 + 1):
            rub.append(izracunaj(p0, q))
            rub.append(izracunaj(p1, q))

        isti = True
        broj = rub[0]

        for x in rub:
            if x != broj:
                isti = False
                break

        a0 = a_min + p0 * korak_a
        a1 = a_min + (p1 + 1) * korak_a
        b0 = b_max - (q1 + 1) * korak_b
        b1 = b_max - q0 * korak_b

        sadrzi_nulu = False

        if a0 <= 0 <= a1 and b0 <= 0 <= b1:
            sadrzi_nulu = True

        if isti and not sadrzi_nulu:
            for q in range(q0, q1 + 1):
                for p in range(p0, p1 + 1):
                    rezultati[q, p] = broj
            return

        pm = (p0 + p1) // 2
        qm = (q0 + q1) // 2

        obradi(p0,pm,q0,qm)
        obradi(pm + 1,p1,q0,qm)
        obradi(p0,pm, qm + 1,q1)
        obradi(pm + 1,p1, qm + 1,q1)

    obradi(0, W - 1, 0, H - 1)

    boje = plt.get_cmap("inferno").copy()
    boje.set_over("black")

    boje = plt.get_cmap("inferno")
    boje.set_over("black")

    plt.imshow(rezultati, cmap=boje, vmin=0, vmax=MAX_ITER,
               extent=(a_min, a_max, b_min, b_max))
    plt.show()

    return rezultati