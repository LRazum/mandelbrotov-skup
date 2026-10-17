# Pravila projekta

Ova datoteka vrijedi za cijeli repozitorij i sve AI alate koji u njemu rade.
`CLAUDE.md` samo upućuje na nju. Prije izmjena pročitaj i
[protokol izmjena](docs/PROTOKOL_IZMJENA.md).

## Svrha i autorstvo

- Tema je vizualizacija Mandelbrotova skupa: razumljiva matematička podloga i
  usporedba dvaju do triju postupaka od jednostavnijih prema naprednijima.
- Ciljana je publika dobar student računarstva na PMF-MO. Svaki postupak mora
  biti dovoljno pristupačan da ga autor može samostalno objasniti i reproducirati.
- Jedini ljudski autor i doprinositelj jest vlasnik repozitorija. AI alat nije
  dodatni autor, recenzent čije se odobrenje zahtijeva ni zamjena za autorov rad.
- Seminar i izlaganje isključivo su na hrvatskom standardnom jeziku.

## Pravila kolegija imaju prednost

Zahtjevi i kriteriji iz korisnikove poruke preneseni su u
[pravila kolegija](docs/PRAVILA_KOLEGIJA.md). Ne ublažavaj ih radi lakše izvedbe.
Obvezni minimum čine 50 linija koda, 10 slajdova, jedan matematički rezultat
sa skicom ili idejom dokaza, jedan zadatak za slušatelje i dva primarna izvora.
Plan usporedbe dvaju do triju postupaka dodatni je cilj autora.

## Granica dopuštene uporabe AI-ja

AI smije pomagati pri:

- istraživanju teme i pronalaženju literature, uz provjeru primarnih izvora;
- planiranju strukture, naslova i redoslijeda rada te osmišljavanju ideja za zadatke;
- provjeri pravopisa autorova teksta i prijevodu stručnih termina;
- organizaciji repozitorija i pisanju njegovih radnih pravila;
- izradi tehničkog koda web-stranice: izgled, navigacija, pristupačnost, prikaz
  autorovih formula i povezivanje s već postojećim autorovim algoritmima;
- pregledu autorova rada, upozoravanju na pogreške, postavljanju pitanja za
  provjeru razumijevanja i pokretanju postojećih provjera.

AI ne piše predani tekst, matematičke iskaze, izvode, dokaze ni njihove skice,
tekst slajdova ili implementacije algoritama koji su sadržaj rada. To uključuje
i gotove zamjenske odlomke, gotov pseudokôd te sadržajni kôd u primjerima,
testovima ili bilježnicama. Autor ih izrađuje sam. Pravopisna korektura ne smije
prerasti u pisanje novih odlomaka ili promjenu matematičkog značenja.

Granica ovisi o svrsi sadržaja, a ne o putanji ili programskom jeziku.
Mandelbrotov izračun smješten u `web/` i dalje je algoritamski kôd rada.
AI smije prijaviti problem i uputiti na provjeren izvor, bez pisanja gotovog
popravka za zabranjeni dio. Ako zadatak prelazi tu granicu, objasni koji dio
pravila kolegija to ograničava i nastavi s dopuštenim dijelom posla.

Svaku uporabu evidentiraj u [evidenciji AI-ja](docs/AI_UPORABA.md): alat, datum,
svrha, zahvaćeni materijali i provjera. Svaka objavljena web-stranica seminara
mora imati jasan odjeljak o korištenim AI alatima i njihovoj svrsi. Autor sam
oblikuje završni tekst tog odjeljka. Interna evidencija nije zamjena za njega.

## Literatura i matematička točnost

- AI odgovor nije znanstveni izvor. Ne citiraj ga kao potvrdu tvrdnje.
- Tražilica i bibliografski zapis pomažu pronaći izvor; tvrdnju provjeri u samom
  izvorniku. Za svaku važnu tvrdnju zabilježi točno mjesto u izvoru.
- U [evidenciji izvora](docs/IZVORI.md) odvoji kandidate od pročitanih i
  provjerenih izvora. Ne izmišljaj autore, DOI-jeve, stranice ili rezultate.
- Najmanje dva primarna izvora moraju stvarno podupirati sadržaj rada.
  Sažetak, blog ili pregledni udžbenik nije automatski primarni izvor.
- Dosljedno navodi izvore tvrdnji, preuzetog koda, slika i drugih tuđih materijala.
  Podrijetlo i dopuštenje uporabe slike evidentiraj prije objave.
- Numeričku aproksimaciju ne predstavljaj kao egzaktan dokaz pripadnosti skupu.
  Za svaki postupak autor navodi pretpostavke i ograničenja.

## Opseg i kvaliteta izvedbe

- Koristi najmanje predznanja koje je dovoljno za cilj. Napredniju metodu dodaj
  tek kada autor razumije osnovnu i može obrazložiti prednost nad njom.
- Promjena palete, vektorizacija ili paralelizacija same po sebi nisu dokaz da
  su obrađeni različiti algoritmi. Inačice istog postupka označi kao inačice.
- Implementacija u `src/` odvojena je od prikaza, primjera i konkretnih parametara.
  Nazivi su smisleni, kôd idiomatski, a zajednička logika bez nepotrebnog ponavljanja.
- Identifikatori mogu biti na engleskom prema običajima odabranog jezika;
  dokumentacija, objašnjenja i korisniku vidljiv tekst pišu se hrvatski.
- Primjeri moraju biti ponovljivi. Uz mjerenja zabilježi parametre, verziju koda,
  okruženje i što se točno mjeri; usporedbe provodi pod usporedivim uvjetima.
- Slike koje predstavljaju rezultat algoritma nastaju iz autorova koda.
  Ilustracija generirana AI-jem ne može zamijeniti rezultat izračuna.
- Smislene provjere obuhvaćaju rubne slučajeve i očekivana svojstva. Ne dodaj
  testove za trivijalne organizacijske promjene ni okvir koji još nema primjenu.
- Web i slajdovi moraju biti čitljivi, s dosljednim nazivljem i notacijom;
  prije predaje provjeri stvarni prikaz formula, slika i isječaka koda.

## Samostalan rad u Gitu

- Jedan zadatak ima jasan cilj i kriterij gotovosti u planu.
- Za izdvojenu promjenu koristi kratku opisnu granu; AI grane imaju prefiks `codex/`.
  PR je po potrebi koristan za vlastiti pregled, bez obveznog drugog recenzenta.
- Ne uvodi podjele vlasništva, timska odobrenja, privatni repozitorij memorije,
  automatske nadzore ili produkcijsku infrastrukturu bez stvarne potrebe.
- Ne prepisuj autorove nepovezane izmjene. Commitovi su mali i opisni.
  Ne prepisuj Git povijest i ne objavljuj rad bez autorova zahtjeva.
- Nakon promjene uskladi pripadajuću dokumentaciju i provedi relevantne provjere.
  U završnom izvještaju razlikuj provjereno, nedovršeno i neprovjereno.
- Zahtjev je ispunjen tek kad postoji stvarni autorov materijal i provjera;
  plan, prazna mapa ili AI nacrt nisu ispunjen zahtjev seminara.
