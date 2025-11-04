import argparse
import sys

# Funkcja do wyświetlania danych w tabeli (do zaimplementowania)
def display_table(file_path):
    print(f"Wyświetlanie danych z pliku: {file_path} w tabeli...")
    # Tutaj będzie implementacja rich.Table

# Funkcja do generowania wykresu ASCII (do zaimplementowania)
def plot_data(file_path):
    print(f"Generowanie wykresu ASCII dla pliku: {file_path}...")
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
