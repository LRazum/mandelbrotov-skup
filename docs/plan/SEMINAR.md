# Plan seminara

Ovo je plan rada, a ne tekst, matematički izvod ili prezentacija za predaju.
Stanje na dan 17. listopada 2026.: postavljena je organizacija repozitorija;
sadržaj seminara još nije izrađen.

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
| Matematički rezultat | Odabrati rezultat povezan s vizualizacijom, primjerice temu kriterija bijega; autor sam piše iskaz i skicu dokaza. |
| Jezik implementacije | Otvoreno; prednost jeziku koji autor poznaje i koji ne skriva postupak iza gotove biblioteke. |
| Izrada weba i format slajdova | Otvoreno; odabrati jednostavan alat s dobrim prikazom matematike i koda. |
| Bibliografski stil | Otvoreno; jedan dosljedan stil za web, slajdove i tuđe materijale. |
| Trajanje i rok izlaganja | Nisu dostavljeni; opseg prilagoditi kada budu poznati. |

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
| Barem 50 linija koda | Popis autorovih izvornih datoteka i zabilježen način brojanja; organizacijska dokumentacija nije kôd seminara. | Nije potvrđeno. |
| Barem 10 slajdova | Datoteka prezentacije i provjeren broj slajdova. | Nije potvrđeno. |
| Matematički rezultat sa skicom ili idejom dokaza | Mjesto u autorovu tekstu i slajdovima te provjeren izvor. | Nije potvrđeno. |
| Zadatak za slušatelje | Mjesto zadatka i veza s izlaganjem. | Nije potvrđeno. |
| Barem dva primarna izvora | Potpune reference, provjerena mjesta i stvarna uporaba u radu. | Nije potvrđeno. |
| Odjeljak o AI-ju na svakoj web-stranici | Pregled svih objavljenih stranica i usklađenost s evidencijom. | Nije potvrđeno. |
| Hrvatski jezik i kvaliteta izvedbe | Pregled teksta, matematike, slajdova, weba i koda prema kriterijima kolegija. | Nije potvrđeno. |
