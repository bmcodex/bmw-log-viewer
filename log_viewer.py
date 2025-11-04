import argparse
import sys
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich.style import Style

# Inicjalizacja konsoli rich
console = Console()

# Funkcja do wyświetlania danych w tabeli
def display_table(file_path):
    try:
        # Wczytanie pliku CSV
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        console.print(f"[bold red]Błąd:[/bold red] Plik '{file_path}' nie został znaleziony.", file=sys.stderr)
        sys.exit(1)
    except pd.errors.EmptyDataError:
        console.print(f"[bold red]Błąd:[/bold red] Plik '{file_path}' jest pusty.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Wystąpił błąd podczas wczytywania pliku:[/bold red] {e}", file=sys.stderr)
        sys.exit(1)

    # Utworzenie tabeli rich
    table = Table(title="BMW Log Viewer", show_header=True, header_style="bold magenta")

    # Dodanie kolumn
    for col in df.columns:
        # Prosta heurystyka kolorowania kolumn
        style = "bold cyan" if col in ['RPM', 'Boost', 'AFR'] else "bold green"
        table.add_column(col, style=style, justify="right")

    # Dodanie wierszy
    # Ograniczenie do pierwszych 20 wierszy dla czytelności w terminalu
    for index, row in df.head(20).iterrows():
        row_data = [str(item) for item in row.values]
        # Dodanie prostego kolorowania wierszy (np. co drugi wiersz)
        row_style = Style(dim=True) if index % 2 != 0 else Style()
        table.add_row(*row_data, style=row_style)

    # Wyświetlenie tabeli
    console.print(table)

# Funkcja do generowania wykresu ASCII (do zaimplementowania)
def plot_data(file_path):
    console.print(f"[bold yellow]Generowanie wykresu ASCII dla pliku:[/bold yellow] {file_path} (Funkcjonalność w trakcie implementacji...)")
    # Tutaj będzie implementacja wykresu ASCII

def main():
    parser = argparse.ArgumentParser(description="BMW Log Viewer - Narzędzie CLI do przeglądania logów CSV.")
    parser.add_argument(
        '--file',
        type=str,
        required=True,
        help='Ścieżka do pliku logów CSV.'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Wyświetla prosty wykres ASCII zamiast tabeli.'
    )

    args = parser.parse_args()

    if args.plot:
        plot_data(args.file)
    else:
        display_table(args.file)

if __name__ == "__main__":
    main()
