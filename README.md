# Vizualizacija Mandelbrotova skupa

Repozitorij za samostalnu izradu seminarskog rada: matematika Mandelbrotova
skupa i usporedba dvaju do triju postupaka njegove vizualizacije, od osnovnih
prema naprednijima. Autor treba razumjeti svaki odabrani postupak i moći ga
samostalno ponovno implementirati i objasniti.

Seminar, web-stranica i izlaganje izrađuju se na hrvatskom jeziku. Jedini ljudski
autor i doprinositelj jest vlasnik repozitorija.

## Početak rada

1. Pročitaj [pravila projekta](AGENTS.md) i [pravila kolegija](docs/PRAVILA_KOLEGIJA.md).
2. U [planu seminara](docs/plan/SEMINAR.md) odaberi sljedeći nedovršeni korak.
3. Prati [protokol izmjena](docs/PROTOKOL_IZMJENA.md).

## Struktura

| Putanja | Namjena |
| --- | --- |
| `docs/` | Pravila, plan, evidencija izvora i uporabe AI-ja; nije tekst za predaju. |
| `seminar/` | Autorov tekst i matematika za web-stranicu rada. |
| `prezentacija/` | Autorovi izvori slajdova i materijali za izlaganje. |
| `src/` | Autorove implementacije algoritama. |
| `examples/` | Primjeri pokretanja i parametri demonstracija. |
| `web/` | Tehnička izvedba web-stranice, odvojena od sadržaja i algoritama. |
| `assets/` | Slike i drugi materijali s evidentiranim podrijetlom. |

## Trenutačno stanje

Postavljena je organizacija rada. Tekst, matematički rezultat, algoritmi,
slajdovi i sadržaj web-stranice još nisu izrađeni. Jezik implementacije jest
Python, a web se izrađuje alatom MkDocs s temom Material; format slajdova još
nije odabran. Postavljen je tehnički kostur weba s praznim stranicama.

AI smije pomagati u dopuštenim pripremnim i tehničkim poslovima. Prema pravilima
kolegija autor sam piše tekst, matematiku i algoritamski kôd rada. Pojedinosti
su u [AGENTS.md](AGENTS.md), a popis dokumentacije u [kazalu](docs/INDEX.md).

## Pokretanje

Potreban je Python 3.12 s modulom `venv` (na Ubuntuu paket `python3.12-venv`).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/mandelbrot/escape_time.py
```

Ovisnosti su u `requirements.txt`.

## Web-stranica

Tekst stranica piše se u Markdownu u mapi `seminar/`; formule se pišu kao u
LaTeX-u, `$…$` u retku i `$$…$$` izlučeno. Slike se spremaju u `assets/` i na
stranici navode kao `assets/slika.png` (iz `seminar/algoritmi/` kao
`../assets/slika.png`). Isječak autorova koda uključuje se retkom
`--8<-- "src/…"` unutar bloka koda, kao u `seminar/algoritmi/escape-time.md`.
Redoslijed i naslovi stranica u izborniku određuju se u `web/mkdocs.yml`.

Lokalni pregled s osvježavanjem pri svakoj izmjeni, na adresi
<http://127.0.0.1:8000/mandelbrotov-skup/>:

```bash
.venv/bin/pip install -r web/requirements.txt
.venv/bin/mkdocs serve -f web/mkdocs.yml
```

Svaki push na granu `main` pokreće `.github/workflows/web.yml`, koji gradi
stranicu i objavljuje je na <https://lrazum.github.io/mandelbrotov-skup/>.
Gradnja s `--strict` ne uspijeva ako postoji neispravna poveznica ili
nedostaje uključena datoteka koda.
