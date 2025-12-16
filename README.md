# Prosjektoppgave-H-st
Terminoppgave_VG2_Høst

Sosiale medier chatting website. (Chit Chat)
Dette prosjektet skal være en enkel chatting nettside der brukere kan se lage en bruker, legge til venner å chatte/snakke med dem.

I dette prosjektet skal jeg jobbe med å lage en Christmas Nettbutikk der man kan kjøpe ting som:

- Julepynt
- Gaver
- Julemat og snacks
- Gavekort
- og mer

---





Prosjektet skal fungere som en prototype/MVP (Minimum Viable Product), hvor hovedfokuset er å vise struktur, funksjonalitet og kompetanse innen Utvikling, Drift og Brukerstøtte.

En mulig MVP kan inneholde:
- Produktside med liste over juleprodukter
- Handlekurv-funksjon
- Enkel “betalingsside” (uten ekte betaling)
- Admin-panel eller database for å legge til produkter

---


### Språk, Teknologier og Utstyr
| Teknologi / Utstyr               | Bruk                                                |
| -------------------------------- | --------------------------------------------------- |
| **Python + Flask**               | Backend / webserver på Raspberry Pi                 |
| **MariaDB**                      | Database for lagring og henting av produkter        |
| **HTML, CSS, JavaScript**        | Frontend – vise produkter, handlekurv og navigasjon |
| **Git + GitHub**                 | Versjonskontroll og dokumentasjon                   |
| **Raspberry Pi**                 | Infrastruktur, hosting av webserver og database     |
| **Figma**                        | Skisse/design av nettsiden                          |
| **Vercel / Netlify** (valgfritt) | Alternativ hosting for frontend-testing             |

---

### Kompetanse i fagene
#### Utvikling
- Lage frontend og backend som kommuniserer via API-er
- Strukturere koden med funksjoner, lister, løkker og if-tester
- Bruke database til å lagre og hente produkter
  
#### Drift
- Sette opp Raspberry Pi som webserver
- Installere og konfigurere MariaDB
- Holde tjenesten kjørende via systemd / Nginx
  
#### Brukerstøtte
- Lage brukerveiledning og FAQ
- Feilsøking av vanlige problemer
- Teste løsning og gi anbefalinger til forbedringer

---


#### Figma-skisse
- Forside med produkter og juletema
- Handlekurv-ikon og checkout-knapp
- Admin-side for å legge til produkter


#### Utkast til mappestruktur
```bash
christmas-nettbutikk/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── product.html
│   │   └── cart.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── db/
│   ├── schema.sql
│   └── seed.sql
├── docs/
│   ├── brukerveiledning.md
│   └── teknisk_dokumentasjon.md
├── .gitignore
├── README.md
└── requirements.txt





