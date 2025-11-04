# bmw-log-viewer

**bmw-log-viewer** to proste narzędzie CLI (Command Line Interface) napisane w Pythonie, służące do szybkiego przeglądania i analizowania logów w formacie CSV, często generowanych przez oprogramowanie do tuningu i diagnostyki samochodów BMW. Wykorzystuje bibliotekę `rich` do prezentacji danych w kolorowej, czytelnej tabeli w terminalu oraz do generowania prostych wykresów ASCII.

## Wymagania

- Python 3.x
- Biblioteki: `rich`, `pandas` (zainstalowane automatycznie z `requirements.txt`)

## Instalacja

```bash
git clone https://github.com/bmcodex/bmw-log-viewer.git
cd bmw-log-viewer
pip install -r requirements.txt
```

## Użycie

Narzędzie wymaga podania ścieżki do pliku CSV za pomocą flagi `--file`.

### 1. Wyświetlanie danych w tabeli

Domyślnie, narzędzie wyświetla pierwsze 20 wierszy logu w kolorowej tabeli.

**Przykład komendy:**

```bash
python log_viewer.py --file sample_log.csv
```

**Przykładowe wyjście (skrócone):**

```
           BMW Log Viewer
┏━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━┓
┃ Time ┃    RPM ┃ Boost ┃  AFR ┃  IAT ┃ Speed ┃
┡━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━━┩
│  0.0 │  800.0 │   0.0 │ 14.7 │ 30.0 │   0.0 │
│  0.5 │ 1200.0 │   0.1 │ 14.7 │ 30.0 │   5.0 │
│  1.0 │ 2500.0 │   0.5 │ 13.5 │ 31.0 │  15.0 │
│  1.5 │ 3800.0 │   1.0 │ 12.8 │ 32.0 │  30.0 │
│  2.0 │ 5100.0 │   1.5 │ 12.5 │ 33.0 │  50.0 │
│  2.5 │ 6200.0 │   1.8 │ 12.2 │ 34.0 │  70.0 │
...
```

### 2. Wyświetlanie wykresu ASCII

Użyj flagi `--plot`, aby wygenerować prosty wykres słupkowy ASCII dla kolumny **Boost**. Jest to przydatne do szybkiej wizualnej oceny przebiegu doładowania.

**Przykład komendy:**

```bash
python log_viewer.py --file sample_log.csv --plot
```

**Przykładowe wyjście (skrócone):**

```
Wykres ASCII dla kolumny 'Boost' (Min: 0.00, Max: 2.00)
------------------------------------------------------------
00 | █ 0.00
01 | ██ 0.10
02 | ████████████ 0.50
03 | █████████████████████████ 1.00
04 | █████████████████████████████████████ 1.50
05 | █████████████████████████████████████████████ 1.80
06 | ███████████████████████████████████████████████ 1.90
07 | ███████████████████████████████████████████████ 1.90
...
```
