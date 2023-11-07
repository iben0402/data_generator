import shutil
import os


def move_files():
    # Pobierz bieżącą ścieżkę
    bieżący_folder = os.getcwd()

    # Ścieżki plików i folderów
    ścieżka_folderu_docelowego = os.path.join(bieżący_folder, 'generated')

    # Utwórz folder docelowy, jeśli nie istnieje
    if not os.path.exists(ścieżka_folderu_docelowego):
        os.makedirs(ścieżka_folderu_docelowego)

    # Lista plików do przeniesienia
    pliki_do_przeniesienia = ['ceo_excel.xlsx', 'drives.bulk', 'operations.bulk', 'problems.bulk', 'users.bulk',
                              'vehicles.bulk']

    for plik in pliki_do_przeniesienia:
        ścieżka_pliku_zrodlowego = os.path.join(bieżący_folder, plik)
        ścieżka_pliku_docelowego = os.path.join(ścieżka_folderu_docelowego, plik)

        if os.path.exists(ścieżka_pliku_zrodlowego):
            shutil.move(ścieżka_pliku_zrodlowego, ścieżka_pliku_docelowego)
        else:
            print(f"Plik {plik} nie istnieje w bieżącym folderze.")