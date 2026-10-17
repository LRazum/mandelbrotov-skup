# Protokol izmjena

Repozitorij održava jedan ljudski autor. Organizacija slijedi osnovni obrazac
Ardyna i PelosiPlusa: središnja pravila, kazalo, plan i usklađivanje povezanih
materijala. Nisu potrebne timske uloge ni odobrenje drugog doprinositelja.

## Izvori pravila i odluka

1. [Pravila kolegija](PRAVILA_KOLEGIJA.md) određuju zahtjeve i dopuštenu uporabu AI-ja.
2. [AGENTS.md](../AGENTS.md) određuje način rada u repozitoriju.
3. [Plan seminara](plan/SEMINAR.md) prati prihvaćeni opseg, odluke i stanje zadataka.
4. README i kazalo služe orijentaciji i moraju pratiti prethodne dokumente.

Matematičke tvrdnje provjeravaju se u primarnim izvorima. Rezultat programa
ili očekivanje iz testa ne nadjačava matematički izvor; neslaganje treba istražiti.

## Jedan zadatak

1. Pročitaj pravila i trenutačno stanje plana. Pregledaj postojeće izmjene.
2. Odredi cilj, zahvaćene datoteke i provjeru koja će pokazati da je zadatak gotov.
3. Provjeri pripada li posao autoru ili dopuštenoj AI pomoći prema `AGENTS.md`.
4. Napravi najmanju potpunu izmjenu. Sačuvaj nepovezani autorov rad.
5. Provedi relevantne provjere i uskladi povezane materijale iz tablice u nastavku.
6. Ažuriraj stanje zadatka, izvore i evidenciju AI-ja kada su zahvaćeni.

Važnu odluku zapiši u plan s datumom, razlogom i posljedicama. Zasebne zapise
odluka uvedi tek ako za njih nastane potreba. PR je opcionalan; njegov predložak
služi i vlastitom pregledu, bez obveznog vanjskog odobrenja.

## Što izmjena povlači za sobom

| Mijenja se | Provjeri i uskladi |
| --- | --- |
| Zahtjev ili tumačenje pravila | Pravila kolegija, `AGENTS.md`, plan; sačuvaj izvor izmjene. |
| Izbor metode ili matematičkog rezultata | Plan, primarni izvori, preduvjeti i autorovo razumijevanje. |
| Autorov algoritam | Autorovi testovi i primjeri, opis metode, slike, mjerenja i pripadajući slajdovi. |
| Parametri ili okruženje mjerenja | Upute za ponavljanje, usporedni rezultati i zaključci koji ih koriste. |
| Izvor, tuđa slika ili isječak koda | Evidencija izvora, točne reference i podrijetlo na webu i slajdovima. |
| Autorov tekst ili notacija | Povezani slajdovi, formule, nazivlje, poveznice i pravopis. |
| Tehnički kôd weba | Prikaz na različitim zaslonima, pristupačnost, formule i integracija autorova koda. |
| Uporaba AI-ja | Interna evidencija i autorov odjeljak na svakoj objavljenoj web-stranici. |
| Putanja, alat ili naredba | README, kazalo, plan i sve poveznice ili upute koje se na to pozivaju. |

## Provjera i izvještaj

Za dokumentacijske promjene provjeri poveznice, dosljednost pravila i razliku
u Gitu. Za izvršivi kôd pokreni postojeće relevantne provjere. Za web i slajdove
provjeri njihov stvarni prikaz kada postoje; broj datoteka ili uspješan izvoz
ne potvrđuje čitljivost.

U izvještaju napiši što je promijenjeno, što je provjereno i što ostaje otvoreno.
Ne označavaj zahtjeve kolegija ispunjenima bez stvarnog materijala i provjere.
