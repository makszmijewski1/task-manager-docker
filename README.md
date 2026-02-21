🐳 Task Manager – Projekt z konteneryzacji
📌 Opis projektu

Projekt przedstawia prosty system zarządzania zadaniami (Task Manager) uruchamiany w środowisku kontenerowym przy użyciu Docker Compose.

System składa się z czterech współpracujących kontenerów:

🐘 PostgreSQL – baza danych

🚀 FastAPI – backend API

🌐 Nginx – frontend (statyczna strona HTML)

🛠 Adminer – panel administracyjny do zarządzania bazą danych

Celem projektu jest pokazanie:

komunikacji między kontenerami

wykorzystania wolumenów

wystawienia usług na porty hosta

działania spójnej usługi wielokontenerowej

🧱 Architektura systemu

Użytkownik (przeglądarka)
↓
Frontend (Nginx) → Backend (FastAPI) → PostgreSQL
↓
Adminer

📦 Wykorzystane technologie

Docker

Docker Compose

Python 3.11

FastAPI

PostgreSQL 15

Nginx

Adminer

SQLAlchemy

📂 Struktura projektu
task-manager-docker/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
└── docker-compose.yml
🚀 Uruchomienie projektu
1️⃣ Wymagania

Zainstalowany Docker Desktop

Włączony Docker Engine

Sprawdzenie:

docker --version
docker compose version
2️⃣ Uruchomienie systemu

W katalogu głównym projektu:

docker compose up --build

Po pierwszym uruchomieniu obrazy zostaną zbudowane automatycznie.

🌍 Dostęp do usług
Usługa	Adres
Frontend	http://localhost:3000
Backend	http://localhost:8000
Adminer	http://localhost:8080
🗄 Dane logowania do bazy (Adminer)

System: PostgreSQL

Server: db

Username: user

Password: password

Database: tasks

🔌 Endpointy API
Sprawdzenie działania backendu
GET http://localhost:8000/

Odpowiedź:

{
  "message": "Task Manager API działa 🚀"
}
Dodanie zadania
POST http://localhost:8000/tasks/?title=Nowe_zadanie

Przykład curl:

curl -X POST "http://localhost:8000/tasks/?title=Test"
💾 Wolumeny

Projekt wykorzystuje wolumen:

postgres_data

Dzięki temu dane bazy nie znikają po usunięciu kontenera.

🔄 Sieć kontenerów

Kontenery komunikują się przez wewnętrzną sieć Docker Compose.

Backend łączy się z bazą przy użyciu nazwy serwisu:

postgresql://user:password@db:5432/tasks

db jest nazwą usługi w docker-compose.yml.

🛠 Zatrzymanie projektu
docker compose down

Usunięcie wraz z wolumenami:

docker compose down -v
🎯 Wymagania projektowe – spełnione

✔ Minimum 4 kontenery
✔ Baza danych
✔ Aplikacja korzystająca z bazy
✔ Co najmniej jedna usługa dostępna z zewnątrz
✔ Wspólna sieć kontenerów
✔ Wykorzystanie wolumenu
✔ Docker Compose

📷 Do prezentacji

Podczas prezentacji należy pokazać:

docker compose up

Działający frontend

Działające API

Adminer oraz tabelę tasks

Komunikację backend ↔ baza danych

👨‍💻 Maksymilian Zmijewski 7869

Projekt wykonany w ramach zajęć z konteneryzacji.