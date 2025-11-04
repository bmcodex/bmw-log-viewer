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

# Funkcja do generowania wykresu ASCII
def plot_data(file_path, column='Boost', max_width=50):
    try:
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

    if column not in df.columns:
        console.print(f"[bold red]Błąd:[/bold red] Kolumna '{column}' nie została znaleziona w pliku logów.", file=sys.stderr)
        sys.exit(1)

    data = df[column].astype(float)
    min_val = data.min()
    max_val = data.max()
    range_val = max_val - min_val

    console.print(f"[bold yellow]Wykres ASCII dla kolumny '{column}'[/bold yellow] (Min: {min_val:.2f}, Max: {max_val:.2f})")
    console.print("-" * (max_width + 10))

    # Ograniczenie do pierwszych 50 wierszy dla czytelności wykresu
    for i, val in enumerate(data.head(50)):
        # Normalizacja wartości do szerokości terminala
        if range_val == 0:
            bar_length = 0
        else:
            bar_length = int(((val - min_val) / range_val) * max_width)

        bar = "█" * bar_length
        # Kolorowanie paska na podstawie wartości (np. czerwony dla wysokiego boostu)
        color = "red" if val > (min_val + range_val * 0.75) else "green"
        
        # Wyświetlenie indeksu, wartości i paska
        console.print(f"[dim]{i:02d}[/dim] | [{color}]{bar}[/{color}] {val:.2f}")

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
        help='Wyświetla prosty wykres ASCII zamiast tabeli. Domyślnie rysuje kolumnę "Boost".'
    )

    args = parser.parse_args()

    if args.plot:
        plot_data(args.file)
    else:
        display_table(args.file)

if __name__ == "__main__":
    main()
