# Projekt_Raspored_poslova

Aplikacija omogućuje praćenje rasporeda poslova za tvrtku koja se bavi instaliranjem klimatizacijskih uređaja. 

Funkcionalnosti: 
1. dodaj_posao - dodavanje novog ugovorenog posla u tablicu s detaljima o adresi na koju se uređaj treba instalirati/servisirati, datumu i vremenu u koje se posao treba doći obaviti, tip uređaja koji se mora donijeti, koji radnik obavlja instalaciju, ukupna cijena za dogovorenu instalaciju, te oznaka je li posao obavljen ili nije. 
2. uredi_posao - u slučaju da dođe do izmjene ugovorenih detalja s klijentima, uređivanje već dodanog posla
3. obrisi_posao - ako je dokazani posao otkazan, ovime se uklanja iz rasporeda
4. ne znam jos


Posao(id, adresa, datum, vrijeme, klima, radnik, cijena, obavljeno)

# UseCase dijagram

![LucidChart dijagram](LucidChart_IvonaPapa.png)


# Instalacija
---
Skidanje koda s GitHub-a:


Docker tutorial: 
docker build -t raspored_poslova .
docker ps
docker run -p 8080:8080 raspored_poslova