# Što je Mandelbrotov skup?

Za svaki kompleksni broj $c \in  \mathbb{C}$ promatramo niz $z_0 = 0, z_{n+1} = z_n^2 + c.$ Dobivamo niz $(z_n)_{n \in \mathbb{N}}$. Uočimo da se broj $z_n$ mijenja pri svakoj iteraciji dok $c$ ostaje fiksan. Mandelbrotov skup je skup svih parametra $c$ za koje je niz $(z_n)_{n \in \mathbb{N}}$ ograničen. Formalno $M$ je Mandelbrotov skup ako:

$$
{
M=\left\{c\in\mathbb{C}:\sup_{n \in \mathbb{N_0}}|z_n|<\infty\right\}.
}
$$

Kada pogledamo ovu definiciju ne očekujemo da će skup biti kompliciran, a još manje da će imati fraktalnu strukturu. Sada kada smo postavili matematičku osnovu, ostatak seminara bavit ćemo se problemom kako na računalu vizualizirati ovaj skup.
