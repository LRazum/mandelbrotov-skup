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
slajdovi i web-stranica još nisu izrađeni. Jezik implementacije jest Python;
format slajdova i alat za izradu weba još nisu odabrani.

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
