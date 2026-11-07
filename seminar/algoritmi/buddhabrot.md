# Buddhabrot

Treći algoritam koji obrađujemo u potpunosti je drugačiji od prijašnjih; ne samo po načinu koji funkcionira nego i samoj informaciji koju računa i prikazuje. Buddhabrot je algoritam koji vizualizira koliko su često članovi nizova $(z_n)_{n\in \mathbb{N}}$, kojima $|z_n| \xrightarrow{n \to \infty} \infty$, posjetili pojedine dijelove kompleksne ravnine.

Ukratko, Buddhabrot bilježi položaje članova $z_1, z_2,...$ i to samo za nizove kod kojih otkrijemo bijeg. Te položaje nazivamo orbitom ili trajektorijom promatranog niza. Boju piksela na vizualu određuje ukupan broj zabilježenih posjeta pikselu (područja s više posjeta prikazuju se svjetlije).

Za takvo crtanje uvodimo *matricu posjeta* dimenzija $H \times W$, čiji su svi elementi inicijalizirani na nulu. Svaki element predstavlja brojač jednog piksela. Kada član prihvaćene orbite padne u taj piksel, povećavamo njegov brojač. Ako više članova iste orbite padne u isti piksel, svaki se broji zasebno. Matrica tako predstavlja dvodimenzionalni histogram posjeta.

Ugrubo, postupak je sljedeći:

1. **Odabir broja $c$.** Odabiremo kompleksni broj $c$ iz predefiniranog područja.
2. **Provjera bijega za niz $(z_n)_{n \in \mathbb{N}}^c$.** Provjeravamo vrijedi li $|z_n| \xrightarrow{n \to \infty} \infty$ za naš novi niz.
    - Ako bijeg nije otkriven, taj niz ne pridonosi slici.
    - Ako je bijeg otkriven, povećamo brojače piksela u koje su padali članovi niza prije bijega.
3. **Ponavljanje.** Postupak ponavljamo za mnogo brojeva $c$.
4. **Bojanje.** Vrijednosti brojača pretvaramo u svjetlinu ili boju. Veći broj posjeta daje svjetliji piksel.
