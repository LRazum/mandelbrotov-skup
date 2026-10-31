# Plan seminara

Ovo je plan rada, a ne tekst, matematički izvod ili prezentacija za predaju.
Stanje na dan 25. listopada 2026.: postavljena je organizacija repozitorija i
poznati su rokovi; sadržaj seminara još nije izrađen.

## Cilj i granice opsega

Autor predstavlja osnovnu matematiku Mandelbrotova skupa i uspoređuje dva do
tri postupka vizualizacije. Prioritet su dvije dobro shvaćene metode; treća je
proširenje kada za nju postoje vrijeme i potrebno razumijevanje. Ovo je autorov
cilj, uz zasebne minimalne zahtjeve kolegija.

Svaka metoda treba imati obrazložen izbor, provjeren primarni izvor, autorovu
implementaciju, primjere, ograničenja i usporedbu pod usporedivim uvjetima.
Autor treba moći objasniti svaki korak bez oslanjanja na AI-generirani kôd.

## Otvorene odluke

| Odluka | Stanje i kriterij |
| --- | --- |
| Konačne dvije metode i moguća treća | Odabrati nakon čitanja literature; postupno povećanje težine i mogućnost samostalne reprodukcije. |
| Implementacija druge metode | Odlučeno 31. 10. 2026.: Mariani–Silver je samo opisan, a AI-generirani kôd uklonjen je iz rada. Za tu metodu zato otpadaju implementacija, primjeri i mjerenja iz kriterija metode i koraka „Druga metoda”. |
| Matematički rezultat | Odabrati rezultat povezan s vizualizacijom, primjerice temu kriterija bijega; autor sam piše iskaz i skicu dokaza. |
| Jezik implementacije | Odlučeno 25. 10. 2026.: Python 3.12 i `matplotlib` za prikaz. Autor je 27. 10. 2026. odustao od zasebnih testova; kriterij kolegija o odvojenim testovima ili primjerima ispunjava se primjerima u `examples/`. Prvu inačicu pisati bez vektorizacije kako bi svaki korak postupka bio vidljiv. |
| Izrada weba | Odlučeno 27. 10. 2026.: MkDocs s temom Material i KaTeX za formule; autor piše Markdown u `seminar/`, a stranica se automatski objavljuje na GitHub Pages iz grane `main`. Razlog: Markdown s LaTeX-ovim formulama, uključivanje autorova koda iz `src/` i alat u Pythonu. MkDocs je zaključan na 1.6.1 jer tema Material nije usklađena s MkDocsom 2.0. |
| Format slajdova | Otvoreno; odabrati jednostavan alat s dobrim prikazom matematike i koda. |
| Bibliografski stil | Otvoreno; jedan dosljedan stil za web, slajdove i tuđe materijale. |
| Trajanje i rok izlaganja | Odlučeno 25. 10. 2026. prema autorovoj informaciji: predaja rada u četvrtak 12. 11. 2026., izlaganje u petak 13. 11. 2026. u trajanju od 45 minuta, uključujući zadatke i pitanja studentima. |

## Kandidati za postupno učenje

Ovo je početni prijedlog za istraživanje, a ne konačan odabir ili objašnjenje metoda:

| Redoslijed | Kandidat | Predznanje i što provjeriti prije odabira |
| --- | --- | --- |
| 1 | Postupak vremena bijega (*escape-time*) | Osnovna iteracija i kompleksni brojevi; početna usporedna implementacija. Izvor K1. |
| 2 | Mariani–Silver, adaptivna podjela pravokutnika | Rekurzija i uzorkovanje; kandidat za smanjenje broja izračuna. Konačno uzorkovanje može propustiti detalje pa ga treba usporediti s prvom metodom, bez jamstva identičnog rezultata. Izvor K2. |
| 3, opcionalno | Procjena vanjske udaljenosti | Derivacije i numerička aproksimacija; prihvatiti samo ako autor razumije potrebnu matematiku. Numerička procjena nije automatski stroga granica udaljenosti. Izvori K3 i K4. |

Oznake izvora i izravne poveznice nalaze se u [evidenciji izvora](../IZVORI.md).
Optimizacije i promjene bojanja mogu biti dio usporedbe, uz jasno označavanje
da su inačice istog postupka.

Za svaku kandidatsku metodu prije prihvaćanja provjeriti:

- Koji problem rješava i razlikuje li se bitno od već odabrane metode?
- Može li autor pratiti izvornik i samostalno reproducirati postupak?
- Koliko dodatne matematike i programiranja zahtijeva?
- Može li se prikazati prednost i objasniti ograničenje na malom primjeru?

## Predložena struktura web-rada

1. Motivacija i cilj vizualizacije.
2. Potrebna matematička podloga i definicije.
3. Odabrani matematički rezultat i ideja dokaza.
4. Osnovni postupak vizualizacije.
5. Drugi postupak i usporedba s prvim.
6. Treći postupak, samo ako je prihvaćen u opseg.
7. Usporedni rezultati, ograničenja i osvrt.
8. Zadatak za slušatelje vezan uz prikazane pojmove ili demonstraciju.
9. Reference i autorov odjeljak o uporabi AI-ja.

Naslove autor može prilagoditi nakon istraživanja. Razina detaljnosti i duljine
cjelina trebaju biti uravnotežene, a svaka nova metoda oslonjena na prethodno objašnjeno.

## Raspored najmanje deset slajdova

Plan uloga, bez napisanog sadržaja: 1. naslov i cilj; 2. motivacija;
3. matematička podloga; 4. rezultat i ideja dokaza; 5. prva metoda;
6. njezin primjer; 7. druga metoda; 8. usporedba i ograničenja;
9. zadatak za slušatelje; 10. osvrt i reference.

To je početna raspodjela, a ne izrađena prezentacija. Ako sadržaj nije čitljiv,
podijeliti ga na dodatne slajdove; treća metoda traži prostor u rasporedu.

## Vremenski raspored

Okvirni raspored do predaje 12. 11. 2026. Svaka faza završava kriterijem iz
popisa koraka u nastavku; kašnjenje se nadoknađuje smanjenjem opsega, a ne
preskakanjem provjera.

| Razdoblje | Cilj faze |
| --- | --- |
| 25. – 28. 10. | Literatura i odabir opsega: primarni izvori, matematički rezultat, jezik i alati. |
| 29. 10. – 1. 11. | Matematička podloga i skica dokaza; prva metoda s provjerama. |
| 2. – 5. 11. | Druga metoda i usporedba s prvom. Do 5. 11. odluka o trećoj metodi. |
| 6. – 9. 11. | Tekst web-rada, slajdovi i zadatak za slušatelje. |
| 10. – 11. 11. | Pregled jezika, prikaza formula, referenci i odjeljka o AI-ju; proba izlaganja. |
| 12. 11. | Predaja rada. |
| 13. 11. | Izlaganje od 45 minuta. |

Izlaganje od 45 minuta s pitanjima i zadacima vjerojatno traži znatno više od
minimalnih deset slajdova. Raspodjelu vremena po cjelinama autor određuje nakon
odabira opsega i provjerava na probi. Treća metoda ulazi u opseg samo ako su prve
dvije dovršene i provjerene do 5. 11.

## Koraci i kriteriji gotovosti

- [x] **Postava repozitorija:** pravila, kazalo, protokol, plan i radne evidencije postoje.
- [ ] **Literatura:** autor je pročitao relevantne dijelove najmanje dvaju primarnih
  izvora i zabilježio mjesta na koja će se pozivati.
- [ ] **Odabir opsega:** zabilježene su dvije metode, odluka o trećoj, matematički
  rezultat i potrebna predznanja; odabrani su jezik i alati.
- [ ] **Matematika:** autor je napisao podlogu, rezultat i skicu dokaza te ih provjerio u izvorima.
- [ ] **Prva metoda:** autorova implementacija, odvojene provjere i primjeri; autor može objasniti svaki korak.
- [ ] **Druga metoda:** isti kriteriji i usporediva demonstracija razlike prema prvoj.
- [ ] **Moguća treća metoda:** prihvaćena i dovršena ili izričito izostavljena iz opsega.
- [ ] **Usporedba:** ponovljivi prikazi i mjerenja s navedenim parametrima i ograničenjima.
- [ ] **Web-rad:** autorov tekst ugrađen u tehničku stranicu; provjereni struktura,
  prikaz formula, čitljivost, reference, podrijetlo slika i odjeljak o AI-ju na svakoj stranici.
- [ ] **Prezentacija:** autor je izradio barem deset čitljivih slajdova i provjerio stvarni prikaz.
- [ ] **Zadatak:** autorov zadatak provjerava nešto objašnjeno tijekom prezentacije.
- [ ] **Proba izlaganja:** autor može objasniti metode i ideju dokaza te ponoviti demonstracije.

## Završna provjera zahtjeva kolegija

Sva polja zasad ostaju nepotvrđena. Uz potvrdu autor upisuje konkretnu putanju
ili drugi dokaz i datum provjere.

| Zahtjev | Dokaz ispunjenja | Stanje |
| --- | --- | --- |
| Barem 50 linija koda | Popis autorovih izvornih datoteka i zabilježen način brojanja; organizacijska dokumentacija nije kôd seminara. | Nije potvrđeno. Autorovi `escape_time.py`, `escape_time_plot.py` (s izmjenama koje još nisu u commitu) i `examples/escape_time_plot.py` imaju 2026-10-31 ukupno 81 redak, od toga 52 neprazna; bez primjera 76 redaka, od toga 49 nepraznih. Upute ne propisuju način brojanja. |
| Barem 10 slajdova | Datoteka prezentacije i provjeren broj slajdova. | Nije potvrđeno. |
| Matematički rezultat sa skicom ili idejom dokaza | Mjesto u autorovu tekstu i slajdovima te provjeren izvor. | Nije potvrđeno. |
| Zadatak za slušatelje | Mjesto zadatka i veza s izlaganjem. | Nije potvrđeno. |
| Barem dva primarna izvora | Potpune reference, provjerena mjesta i stvarna uporaba u radu. | Nije potvrđeno. |
| Odjeljak o AI-ju na svakoj web-stranici | Pregled svih objavljenih stranica i usklađenost s evidencijom. | Nije potvrđeno. |
| Hrvatski jezik i kvaliteta izvedbe | Pregled teksta, matematike, slajdova, weba i koda prema kriterijima kolegija. | Nije potvrđeno. |
