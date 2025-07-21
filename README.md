# Konsolowy Menedżer Zadań (To-Do List Manager)
## Opis projektu

### Cel projektu: 
Stworzenie prostego, konsolowego narzędzia, które umożliwi użytkownikowi efektywne zarządzanie codziennymi zadaniami. Aplikacja ma pozwalać na dodawanie, przeglądanie, oznaczanie jako ukończone oraz usuwanie zadań.

### Oczekiwane rezultaty: 
Działające, intuicyjne w obsłudze narzędzie, które przechowuje dane między sesjami, zapewniając podstawową funkcjonalność zarządzania listą zadań.

## Opis funkcjonalności projektu
Projekt oferuje następujące funkcje dostępne z poziomu konsoli:

- Dodawanie zadań: Użytkownik może wprowadzić opis nowego zadania, które zostanie dodane do listy.

- Wyświetlanie zadań: Prezentacja wszystkich zadań wraz z ich statusami (ukończone/nieukończone) oraz unikalnymi identyfikatorami.

- Oznaczanie zadań jako ukończonych: Możliwość zmiany statusu zadania na "ukończone" poprzez podanie jego ID.

- Usuwanie zadań: Opcja usunięcia zadania z listy na podstawie jego ID.

- Trwałość danych: Wszystkie zmiany są automatycznie zapisywane, co zapewnia ich zachowanie po ponownym uruchomieniu aplikacji.

- "Cytat dnia": Przy starcie aplikacji wyświetlany jest losowy cytat pobrany z zewnętrznego API.

Jasne! Oto opis projektu po polsku, krótko i na temat, aby spełnić Twoje wymagania.

Opis projektu
Temat projektu
Konsolowy Menedżer Zadań (To-Do List Manager)

Określenie celu projektu i oczekiwanych rezultatów
Cel projektu: Stworzenie prostego, konsolowego narzędzia, które umożliwi użytkownikowi efektywne zarządzanie codziennymi zadaniami. Aplikacja ma pozwalać na dodawanie, przeglądanie, oznaczanie jako ukończone oraz usuwanie zadań.

Oczekiwane rezultaty: Działające, intuicyjne w obsłudze narzędzie, które przechowuje dane między sesjami, zapewniając podstawową funkcjonalność zarządzania listą zadań.

Opis funkcjonalności projektu
Projekt oferuje następujące funkcje dostępne z poziomu konsoli:

Dodawanie zadań: Użytkownik może wprowadzić opis nowego zadania, które zostanie dodane do listy.

Wyświetlanie zadań: Prezentacja wszystkich zadań wraz z ich statusami (ukończone/nieukończone) oraz unikalnymi identyfikatorami.

Oznaczanie zadań jako ukończonych: Możliwość zmiany statusu zadania na "ukończone" poprzez podanie jego ID.

Usuwanie zadań: Opcja usunięcia zadania z listy na podstawie jego ID.

Trwałość danych: Wszystkie zmiany są automatycznie zapisywane, co zapewnia ich zachowanie po ponownym uruchomieniu aplikacji.

"Cytat dnia": Przy starcie aplikacji wyświetlany jest losowy cytat pobrany z zewnętrznego API.

## Krótka instrukcja uruchomienia projektu
1. Sklonuj lub pobierz pliki projektu do wybranego katalogu.
2. Otwórz terminal (wiersz poleceń) i przejdź do katalogu projektu.
3. Zainstaluj wymagane biblioteki za pomocą pliku requirements.txt:
```bash
pip install -r requirements.txt
```
4. Uruchom aplikację:
```bash
python main.py
```

## Opis technologii użytych w projekcie
**python**: główny język programowania aplikacji.

**json**: używany do serializacji i deserializacji danych zadań do/z pliku tasks.json, zapewniając trwałość danych.

**datetime**: służy do oznaczania czasu utworzenia każdego zadania.

**numpy**: wykorzystany w projekcie do generowania unikalnych identyfikatorów (ID) dla zadań, co stanowi proste użycie frameworka AI/numerycznego zgodnie z wymaganiami.

**requests**: biblioteka do wykonywania żądań HTTP, używana do pobierania "cytatu dnia" z zewnętrznego API (np. zenquotes.io).

**unittest**: wykorzystany do implementacji testów jednostkowych, sprawdzających poprawność kluczowych funkcji menedżera zadań.


## Analiza Wymagań

### Wymagania Funkcjonalne (F) i Niefunkcjonalne (NF)
F1: Dodawanie zadań: Użytkownik dodaje nowe zadania.

F2: Wyświetlanie zadań: Widok wszystkich zadań (opis, ID, status).

F3: Oznaczanie ukończonych: Zmiana statusu zadania na ukończone (po ID).

F4: Usuwanie zadań: Usuwanie zadań (po ID).

F5: Nieukończone zadania: Wyświetlanie tylko nieukończonych zadań.

F6: Trwałość danych: Zadania zapisywane i ładowane z pliku.

F7: Cytat dnia: Pobieranie i wyświetlanie losowego cytatu z API przy starcie.

NF1: Prostota: Intuicyjny interfejs konsolowy.

NF2: Szybkość: Natychmiastowa reakcja na działania użytkownika.

NF3: Modularność: Kod podzielony na logiczne moduły.

NF4: Obsługa błędów: Radzenie sobie z błędami (np. błędne ID, problemy z plikiem).

## Interfejs Użytkownika i Funkcjonalność Systemu

**Interfejs użytkownika**: konsolowy (CLI) z menu tekstowym, gdzie użytkownik wprowadza dane i otrzymuje komunikaty tekstowe.

**Funkcjonalność systemu**: aplikacja działa w pętli: wyświetla menu, czeka na wybór, wykonuje odpowiednią akcję (dodaj, wyświetl, oznacz, usuń, wyjdź), obsługuje błędy i automatycznie zapisuje dane w pliku JSON.

## Opis wyników testów i ewentualne poprawki
Zaimplementowane testy jednostkowe dla TaskManager (dodawanie, oznaczanie, usuwanie zadań, filtry, obsługa błędów ID) przeszły pomyślnie.

Wszystkie podstawowe funkcje działają poprawnie, bez stwierdzonych krytycznych błędów. Poprawki nie są wymagane dla obecnej funkcjonalności. Dalsze działania to ewentualne rozszerzenie testów o walidację wejścia czy błędy pliku tasks.json

## Wnioski
Projekt to działający, konsolowy menedżer zadań z kluczowymi funkcjami (dodawanie, podgląd, oznaczanie, usuwanie) i trwałością danych. Wykorzystanie klas, modułów, generatorów, list składanych, obsługi wyjątków, integracja z API oraz użycie NumPy zapewniły zgodność z wymaganiami i dobrą strukturę kodu, co potwierdzają testy jednostkowe.

### Możliwe Usprawnienia
- Projekt można dalej rozwijać, dodając:

- Priorytety i terminy dla zadań.

- Funkcje filtrowania i sortowania.

- Kategorie zadań.

- Graficzny interfejs (GUI) zamiast konsoli.

- Integrację z bazą danych (np. SQLite) dla lepszej skalowalności.
