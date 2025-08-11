# Math Microservice - Flask OOP

## Descriere

Această aplicație este un microserviciu dezvoltat cu Flask, care expune un API REST pentru operații matematice de bază: pow, fibonacci și factorial. Toate cererile către API sunt persistate într-o bază de date SQLite. Structura proiectului respectă principiile MVC pentru claritate și extensibilitate, iar serializarea/deserializarea datelor se face cu Pydantic.

## Structură proiect

- **app/**: codul sursă principal, organizat modular (MVC)
  - `models.py`: modele SQLAlchemy și Pydantic
  - `controllers.py`: logica matematică
  - `routes.py`: rutele API
  - `__init__.py`: inițializare Flask și DB
- **main.py**: punctul de pornire al aplicației
- **requirements.txt**: dependențe
- **test_api.py**: teste automate cu unittest
- **test_requests.py**: teste API cu requests

## Funcționalități
- API REST pentru pow, fibonacci, factorial
- Persistență cereri în SQLite
- Serializare cu Pydantic
- Teste automate
- Ușor de extins cu noi operații matematice

## Cum rulezi aplicația

1. Instalează dependențele:
   ```bash
   pip install -r requirements.txt
   ```
2. Pornește serverul Flask:
   ```bash
   python main.py
   ```
3. Testează API-ul cu test_requests.py sau cu unelte ca Postman/curl.
   ```bash
   python test_requests.py
   ```
4. Rulează testele automate:
   ```bash
   python test_api.py
   ```

## Linting cu flake8

1. Instalează flake8:
   ```bash
   pip install flake8
   ```
2. Rulează flake8 în directorul proiectului:
   ```bash
   flake8 .
   ```

## Extensibilitate

Poți adăuga ușor noi operații matematice, adăugând funcția în `controllers.py` și o rută nouă în `routes.py`.
