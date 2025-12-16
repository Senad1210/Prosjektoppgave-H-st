# Prosjektoppgave-H-st
Terminoppgave_VG2_Høst

Sosiale medier chatting website (Chit Chat)

Dette prosjektet er en enkel chatting-nettside der brukere kan lage en konto, legge til venner og chatte med dem i sanntid.

I dette prosjektet skal jeg lage en sosial medieplattform som tilbyr:

### Sider:
- Hjemmeside / feed
- Kontakter / venneliste
- Innstillinger / profil
- Chat-vindu

### Funksjonalitet:
- Opprette en bruker
- Logge inn / autentisering
- Se om andre brukere er online
- Sende meldinger og bilder
- Legge til andre brukere som venn

---

Prosjektet skal fungere som en prototype/MVP (Minimum Viable Product), med fokus på å vise struktur, funksjonalitet og kompetanse innen Utvikling, Drift og Brukerstøtte.

En mulig MVP kan inneholde:
- Brukerregistrering og login
- Liste over venner og online-status
- Sanntidschat med tekstmeldinger og bilder
- Enkel innstillingsside for profil

---

### Språk, Teknologier og Utstyr
| Teknologi / Utstyr               | Bruk                                                   |
| -------------------------------- | ----------------------------------------------------- |
| **Python + Flask**               | Backend / webserver                                   |
| **MariaDB / SQL**             | Database for lagring av brukere, venner og meldinger |
| **HTML, CSS, JavaScript**        | Frontend – vise chat, kontakter og innstillinger     |
| **Git + GitHub**                 | Versjonskontroll og dokumentasjon                    |
| **Raspberry Pi / lokal server**  | Infrastruktur, hosting av webserver og database     |
| **Figma**                        | Skisse/design av nettsiden                            |
| **Vercel / Netlify** (valgfritt) | Alternativ hosting for frontend-testing              |

---

### Kompetanse i fagene
#### Utvikling
- Lage frontend og backend som kommuniserer via API-er
- Strukturere koden med funksjoner, klasser og logikk
- Bruke database til å lagre og hente brukere, venner og meldinger
- Implementere sanntidschat via WebSockets

#### Drift
- Sette opp server (Raspberry Pi eller alternativ hosting)
- Installere og konfigurere MariaDB / SQLite
- Holde tjenesten kjørende via systemd / Nginx
- Håndtere sikkerhet og tilgangskontroll

#### Brukerstøtte
- Lage brukerveiledning og FAQ

---

### Figma-skisse
- Hjemmeside med chat-feed
- Kontakter-side med online-status
- Chat-vindu med meldinger og bildeopplasting
- Innstillingsside med profil og preferanser

---

### Utkast til mappestruktur
```bash
chit-chat/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── contacts.html
│   │   └── chat.html
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
