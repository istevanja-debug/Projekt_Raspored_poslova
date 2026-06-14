# Projekt_Raspored_poslova

## Opis funkcionalnosti aplikacije  

Aplikacija omogućuje praćenje rasporeda poslova za tvrtku koja se bavi instaliranjem klimatizacijskih uređaja.  
  
Funkcionalnosti:  
1. pregled svih poslova (Read)
2. dodavanje novog ugovorenog posla u tablicu s detaljima o adresi na koju se uređaj treba instalirati/servisirati, datumu i vremenu u koje se posao treba doći obaviti, tip uređaja koji se mora donijeti, koji radnik obavlja instalaciju, ukupna cijena za dogovorenu instalaciju, te oznaka je li posao obavljen ili nije. (create)
3. uređivanje postojećeg posla u slučaju da dođe do izmjene ugovorenih detalja s klijentima (update)
4. uklanjanje posla iz tablice - ako je dogovoreni posao otkazan, ovime se uklanja iz rasporeda (delete)
5. označavanje posla kao obavljenog
6. statistika - prikaz broja obavljenih/neobavljenih poslova, ukupne zarade, pretraga poslova po radniku ili po datumu (read)
  
  
Posao(id, adresa, datum, vrijeme, klima, radnik, cijena, obavljeno)

## UseCase dijagram
  
![LucidChart dijagram](LucidChart_IvonaPapa.png)
  

## Kako pokrenuti aplikaciju
  
1. Provjerite imate li instaliran Docker na svom računalu.
2. klonirajte repozitorij:  
```git clone https://github.com/istevanja-debug/Projekt_Raspored_poslova```
3. Uđite u direktorij projekta:  
```cd Projekt_Raspored_poslova```
4. Izradite Docker image:  
```docker build -t raspored_poslova .```
5. Pokrenite Docker kontejner:  
```docker run -p 5000:5000 raspored_poslova```
6. Otvorite preglednik na adresi  
http://localhost:5000/poslovi 
  
## Tehnologije korištene u izradi projekta
  
1. Backend (Python, Flask, PonyORM)
2. Baza podataka (SQLite)
3. Frontend (HTML, CSS, Bootstrap)
4. Docker
5. GitHub
6. PyCharm

## Autorica: Ivona Papa