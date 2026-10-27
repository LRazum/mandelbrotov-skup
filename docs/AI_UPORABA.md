# Evidencija uporabe umjetne inteligencije

Radna evidencija služi provjerljivosti dopuštene pomoći. Nije gotov odjeljak
za objavu: završnu izjavu za svaku web-stranicu seminara piše autor.

Za svaki novi posao dodaj stvarno korišteni alat i model ako je poznat, datum,
svrhu, zahvaćene materijale i način provjere. Ne navodi alat koji nije korišten
i ne prikazuj generirani sadržaj kao autorov samostalni rad.

| Datum | Alat | Svrha | Materijali | Provjera i stanje |
| --- | --- | --- | --- | --- |
| 2026-10-17 | OpenAI Codex; točna oznaka modela nije zabilježena | Organizacija repozitorija, prijenos dostavljenih pravila i planiranje rada; usporedba strukture Ardyna i PelosiPlusa. | `README.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, konfiguracija urednika i Git predložak. | Upute kolegija potječu iz autorove poruke. Organizacijske datoteke izrađene su uz AI pomoć; sadržaj seminara i algoritmi nisu napisani. |
| 2026-10-17 | OpenAI Codex s web-pretraživanjem | Pronalaženje autorskih opisa mogućih metoda i provjera njihove prikladnosti za plan. | `docs/IZVORI.md`, `docs/plan/SEMINAR.md`. | Otvoreni su autorski izvori navedeni u evidenciji izvora. To nije autorova provjera literature ni potvrda ispunjenja bibliografskog minimuma. |
| 2026-10-20 | Copilot SDK u VS Codeu; točna oznaka modela nije zabilježena | Orijentacija o prvom koraku rada, na temelju postojećeg plana; nisu generirani sadržaj seminara, matematika ni algoritamski kôd. | `README.md`, `docs/plan/SEMINAR.md`, `docs/IZVORI.md`. | Preporuka je usklađena s planom i statusima kandidata u evidenciji izvora; autor treba sam pročitati izvore i zabilježiti provjerene tvrdnje. |
| 2026-10-25 | Claude Code (Claude Opus 5.5) | Orijentacija o redoslijedu prvih koraka, prijedlog kandidata za primarne izvore i vremenski raspored do predaje prema autorovim rokovima; nisu generirani tekst seminara, matematika ni algoritamski kôd. | `docs/plan/SEMINAR.md` (rokovi, raspored, odluka o jeziku), `docs/IZVORI.md` (kandidati M1–M4), `pyproject.toml`, `requirements.txt` i upute za pokretanje u `README.md`; radna skripta za autorovo učenje `docs/skripta/`: objašnjenja, definicije podloge, primjeri, kontrolna pitanja i bibliografija. Nije tekst za predaju; iskaz i skica dokaza kriterija bijega ostavljeni su autoru. | Bibliografski podaci M1–M4 provjereni su preko Crossrefa, kataloga i izdavača, a M2 i u samom PDF-u; autor još nije pročitao izvore. Algoritam i testovi nisu napisani. Tvrdnje u skripti oslonjene su na M2 (pogl. 1 i 3, provjereno u PDF-u); ostala mjesta autor treba provjeriti. Skripta nije prevedena jer LaTeX nije instaliran. |

## Prije objave

- Autor provjerava odgovara li evidencija stvarnoj uporabi alata.
- Autor piše jasan odjeljak na svakoj objavljenoj web-stranici: koji alati i za što.
- Tvrdnje i reference provjerene su u primarnim izvorima, a ne u AI odgovorima.
- Izjava o uporabi AI-ja ne zamjenjuje poštovanje zabrane pisanja sadržaja rada.
