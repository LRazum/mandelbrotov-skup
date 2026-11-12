# Vizualizacija Mandelbrotova skupa

Seminarski rad o Mandelbrotovu skupu i postupcima njegove vizualizacije na
računalu, izrađen na PMF-MO. Rad polazi od definicije skupa i kriterija bijega,
a zatim obrađuje tri postupka, od jednostavnijega prema naprednijima.

**Web-stranica rada:** <https://lrazum.github.io/mandelbrotov-skup/>

- **Predaja rada:** 12. studenoga 2026.
- **Izlaganje:** 13. studenoga 2026., 45 minuta, sa zadatkom za slušatelje.
- **Autor:** vlasnik repozitorija ([LRazum](https://github.com/LRazum)).

## Sadržaj rada

| Cjelina | Stranica | Što sadrži |
| --- | --- | --- |
| Uvod | [`seminar/index.md`](seminar/index.md) | Motivacija i cilj seminara. |
| Matematička podloga | [`seminar/podloga.md`](seminar/podloga.md) | Definicija Mandelbrotova skupa. |
| Escape time algoritam | [`seminar/algoritmi/escape-time.md`](seminar/algoritmi/escape-time.md) | Kriterij bijega s dokazom, autorova implementacija u Pythonu i slike s parametrima. |
| Mariani–Silver algoritam | [`seminar/algoritmi/mariani-silver.md`](seminar/algoritmi/mariani-silver.md) | Opis postupka adaptivne podjele pravokutnika i slike. |
| Buddhabrot | [`seminar/algoritmi/buddhabrot.md`](seminar/algoritmi/buddhabrot.md) | Ideja algoritma i vizualizacije, bez vlastite implementacije. |
| Literatura | [`seminar/literatura.md`](seminar/literatura.md) | Primarni i dopunski izvori. |
| Uporaba umjetne inteligencije | [`seminar/uporaba-ai.md`](seminar/uporaba-ai.md) | Autorova izjava o korištenim AI alatima i njihovoj svrsi. |

Opseg je namjerno postupan: escape time je implementiran i služi kao osnova,
Mariani–Silver je obrađen opisno kao ubrzanje istoga pristupa, a Buddhabrot kao
drukčiji pogled na isti skup kroz ideju algoritma i vizualizacije. Zadatak za
slušatelje daje se samo na izlaganju i nije dio web-stranice.

## Struktura repozitorija

| Putanja | Namjena |
| --- | --- |
| `seminar/` | Tekst i matematika web-stranice rada (Markdown s LaTeX formulama). |
| `src/mandelbrot/` | Autorova implementacija escape time algoritma i iscrtavanja. |
| `examples/` | Primjer pokretanja s parametrima demonstracije. |
| `assets/` | Slike rezultata, razvrstane po algoritmima. |
| `web/` | Tehnička izvedba web-stranice (MkDocs, tema Material, KaTeX). |
| `docs/` | Radna dokumentacija: pravila, plan, evidencija izvora i uporabe AI-ja. Nije tekst za predaju. |

Autorstvo koda po datotekama navedeno je u
[evidenciji AI-ja](docs/AI_UPORABA.md#autorstvo-koda), a pregled radne
dokumentacije u [kazalu](docs/INDEX.md).

## Pokretanje primjera

Potreban je Python 3.12 s modulom `venv` (na Ubuntuu paket `python3.12-venv`).

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
PYTHONPATH=src .venv/bin/python examples/escape_time_plot.py
```

Primjer iscrtava cijeli skup u rezoluciji 1200 × 900 uz najviše 100 iteracija.
Parametri slika objavljenih na stranici navedeni su uz same slike.

## Lokalna izgradnja web-stranice

```bash
.venv/bin/pip install -r web/requirements.txt
.venv/bin/mkdocs serve -f web/mkdocs.yml
```

Stranica je tada dostupna na <http://127.0.0.1:8000/mandelbrotov-skup/> i
osvježava se pri svakoj izmjeni. Redoslijed stranica u izborniku određen je u
`web/mkdocs.yml`, a isječci koda uključuju se izravno iz `src/` pa prikazani kôd
uvijek odgovara stvarnoj implementaciji.

Svaki push na granu `main` pokreće `.github/workflows/web.yml`, koji gradi
stranicu s `--strict` i objavljuje je na GitHub Pages.

## Uporaba umjetne inteligencije

Tekst, matematika i algoritamski kôd rada autorov su samostalni rad. AI alati
korišteni su za organizaciju repozitorija, tehničku izradu web-stranice,
pravopisnu provjeru i pregled koda, u skladu s [pravilima projekta](AGENTS.md).
Svaka uporaba evidentirana je u [evidenciji AI-ja](docs/AI_UPORABA.md), a
autorova izjava objavljena je na stranici
[Uporaba umjetne inteligencije](https://lrazum.github.io/mandelbrotov-skup/uporaba-ai/).
