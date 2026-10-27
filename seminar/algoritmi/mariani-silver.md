# Mariani Silver

Drugi algoritam koji ćemo obraditi je *Mariani-Silver algoritam*, on ubrzava crtanje tako da segmentira sliku u pravokutne dijelove i tako pokušava preskočiti izračun njihove unutrašnjosti. Za izračun i dalje koristimo *Escape time* no broj točaka za koji ga koristimo je znatno manji.

Glavna ideja kod Mariani Silvera je ta da ako rubovi nekog pravokutnika imaju isti rezultat (pripadnost ili ne pripadnost skupu) tada isto vrijedi i za sve točke u interioru pravokutnika. Ako rub nije jednolik pravokutnik se dijeli na manje dijelove. Zatim se postupak rekurzivno ponavlja na svakom manjem (novom) dijelu.

Ono što opravdava ovaj algoritam je činjenica da je Mandelbrotov skup povezan i jednostavno povezan, to jest da mu je komplement u $\mathbb{C}$ povezan skup. Zato ako je kontura sadržana u skupu onda je u skupu i njen interior. Ovu tvrdnju nećemo dokazivati jer izlazi iz opsega seminara. Naravno, to samo znači da je algoritam matematički točan no u praksi on je i dalje heuristika. Razlog tomu je to što sam rub ima beskonačno mnogo točaka, dok ga računalo prikazuje s ograničenim brojem piksela stoga ne možemo biti sigurni da sve točke (pikseli) na rubu imaju jednak rezultat.

  
Ugrubo, postupak je sljedeći:
1. **Rezultati na rubu.** Ispitujemo rubove pravokutnika.
2. **Provjera jednakosti.**
    - Ako su rezultati jednaki, popunimo pravokutnik zajedničkom vrijednošću i završavamo njegovu obradu.
    - Ako rezultati nisu svi jednaki, provjeravamo veličinu pravokutnika; ako je dovoljno malen, računamo svaki piksel posebno.
3. **Podjela pravokutnika.** Ako je pravokutnik prevelik, dijelimo ga na 4 manja pravokutnika i ponavljamo cijeli postupak za svaki od njih.

Mogli bi se pitati  "Što točno ovdje znači izraz *jednaki rezultati*?" ako ste pažljivo čitali prošlo poglavlje o *Escape time* algoritmu uočili ste da sama funkcija `escape_time` uz klasifikaciju vraća i broj iteracije u kojoj je točka klasificirana. Stoga jednakost određujemo uspomoć tih brojeva, tojest pikseli imaju jednak rezultat ako: su svi rubni pikseli pobjegli u istoj iteraciji ili ni za jedan rubni piksel nije otkriven bijeg u zadanom broju iteracija. 

Također je važno uočiti sljedeće, kada dijelimo pravokutnik na četiri manja pravokutnika svi novi pravokutnici dijele dva ruba sa starim pravokutnikom, tojest umjesto ponovnog računanja rezultata za rubove novih pravokutnika možemo iskoristiti rezultate prošlog pravokutnika. To nas motivira da uvedemo *matricu rezultata* u kojoj ćemo čuvati informaciju za svaki piksel na slici; matrica opisuje rezultat na sljedeća tri načina: 
1. *Neizračunat*: za njega još nema rezultata,
2. *Bijeg u iteraciji n*: bijeg je otkriven u iteraciji n,
3. *Neotkriven bijeg*: dosegnut je `MAX_ITER` te bijeg nije otkriven.

Uz sve ovo koristimo sljedeću sigurnosnu provjeru, za pravokutnik koji trenutno obrađujemo provjeravamo sadrži li 0. Ako sadrži dijelimo ga na manje bez obzira na jednakost rezultata, ako ne sadrži nastavljamo normalno izvođenje algoritma. Jasno je zašto koristimo ovu zaštitu, zamislimo da pravokutnik omeđuje cijeli skup, sve točke na rubu pravokutnika ne pripadaju skupu pa bi automatski rekli isto za sav interior pravokutnika. 

Nakon ovog kratkog opisa spremni smo za samu implementaciju algoritma.

## Implementacija

```python title="src/mandelbrot/mariani_silver.py"
--8<-- "src/mandelbrot/mariani_silver.py"
```