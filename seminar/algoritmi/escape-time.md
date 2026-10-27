# Escape time algoritam
Krećemo sa najjednostavijim algoritmom za vizualizaciju Mandelbrotovog skupa tzv. *Escape time algoritam*. Prije samog algoritma ćemo izvesti jednostavan uvijet na modul broja $z$ koja garantira da će niz nakon tog člana divergirati u beskonačnost.


__Propozicija 1.1.__ Ako postoji $n \in \mathbb{N}$ takav da je $|z_n| > 2$, tada $|z_k| \xrightarrow{k \to \infty} \infty$.

*Dokaz:* Neka je $r = |z_n| > 2$ i $|c| \leq r$ (ako je $|c| > 2$, uzmemo $n = 1$ jer je $z_1 = c$). Tada je

$$
|z_{n+1}| = |z_n^2 +c| \geq |z_n|^2 - |c| \geq r^2 - r = (r - 1)\, r.
$$

Dakle, modul se u svakom koraku pomnoži barem s $r - 1 > 1$ (i dalje raste, pa isto vrijedi i u sljedećim koracima), stoga $|z_k| \to \infty$. Dobiveni rezultat nazivamo *uvijet bijega*.
$\square$

Uočimo da kada bismo za neku vrijednost $c$ niz $(z_n)_{n \in \mathbb{N}}$ promatrali kroz iteracije postajali bismo sve sigurniji da $c \in M$ ili   $c \notin M$ kako broj iteracija ide u beskonačnost. Naravno, računalo kao takvo ne može doći do beskonačnosti tj. ne može beskonačno iterirati i računati naš niz $(z_n)_{n \in \mathbb{N}}$ stoga možemo odabrati neki dovoljno veliki broj MAX_ITER $\in  \mathbb{N}$ koji će nam dati ograničenje koliko iteracija računamo prije nego proglasimo je li $c \in M$.

Ako imate minimalno predznanje iz programiranja već sada u glavi zasigurno imate neku vrstu (pseudo)koda koji bi koristio ove rezultate i opažanja za klasifikaciju točaka u kompleksnoj ravnini, klasifikacija naravno u smislu pripadosti Mandelbrotovom skupu.

Prije same implementacije moramo proći kroz određene tehnikalije koje će biti ključne u samom izvođenju algoritma.

Zapišimo $z_n = x_n + i y_n$ i $c = a + i b$. Tada je

$$
z_n^2 + c = (x_n + i y_n)^2 + a + i b = \left(x_n^2 - y_n^2 + a\right) + i\left(2 x_n y_n + b\right).
$$

Prema tome, kompleksna iteracija svodi se na dvije realne jednadžbe:

$$
\begin{aligned}
x_{n+1} &= x_n^2 - y_n^2 + a, \\
y_{n+1} &= 2 x_n y_n + b,
\end{aligned}
\qquad x_0 = y_0 = 0.
$$

Također uočimo da *uvjet bijega* možemo računati bez korijena:

$$
|z_n| > 2 \iff \sqrt{x_n^2 + y_n^2} > 2 \iff x_n^2 + y_n^2 > 4.
$$

Ovime smo se oslobodili kompleksnog računa, u svakom smislu, račun možemo obaviti samo s jednostavnom realnom aritmetikom.
 
Slike na računalu kao takve su diskretni objekti tj. sastoje se od konačno mnogo piksela. Novi problem je kako pretvoriti piksel u kompleksan broj. Prvo definiramo pravokutni dio kompleksne ravnine koji želimo prikazati tj. odabiremo brojeve $a_{min}, a_{max}$ i $b_{min}, b_{max}$ Nakon toga biramo rezoluciju tojest broj piksela koji želimo prikazati u tom pravokutniku. Svaka slika ima širinu $W$ i visinu $H$. Piksel ćemo prikazivati kao uređeni par $(p,q) \in W \times H$, $p \in [0, W-1], q \in [0, H-1]$. Središtu piksela pridružujemo kompleksni broj $c = a + ib$, gdje je


$$
\begin{aligned}
a &= a_{\min} + \frac{p + \frac{1}{2}}{W}\,(a_{\max} - a_{\min}) \\
b &= b_{\max} - \frac{q + \frac{1}{2}}{H}\,(b_{\max} - b_{\min})
\end{aligned}
$$


Ovime smo uspjeli konkretizirati dio kompleksne ravnine u nešto s čime računalo može raditi. Tako da smo spremni za samu implementaciju algoritma.


## Implementacija

```python title="src/mandelbrot/escape_time.py"
--8<-- "src/mandelbrot/escape_time.py"
```

```python title="src/mandelbrot/escape_time_plot.py"
--8<-- "src/mandelbrot/escape_time_plot.py"
```

<figure markdown="span">
  ![Mandelbrotov skup iscrtan escape time algoritmom](../assets/2400x1800.png)
  <figcaption>Rezolucija 2400 × 1800</figcaption>
</figure>

<div class="grid" markdown>

<figure markdown="span">
  ![Detalj ruba Mandelbrotova skupa u rezoluciji 2400 × 1800](../assets/2400x1800_detalj.png)
  <figcaption>Detalj, rezolucija 2400 × 1800</figcaption>
</figure>

<figure markdown="span">
  ![Isti detalj ruba Mandelbrotova skupa u rezoluciji 4800 × 3600](../assets/4800x3600_detalj.png)
  <figcaption>Detalj, rezolucija 4800 × 3600</figcaption>
</figure>

</div>
