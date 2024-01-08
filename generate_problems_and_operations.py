import csv
from datetime import datetime

import pandas as pd
import random
import string


def losuj_opis():
    df = pd.read_csv('help_files/problems_and_operations.csv')
    opis = df['Opis'].sample().values[0]
    return opis


def losowy_string(dl):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(dl))


def generuj_problems_bulk(przejazdy_w_bazie, ilosc_przejazdow, ilosc_danych):
    opisy = []
    id_przejazdow = random.sample(range(przejazdy_w_bazie, przejazdy_w_bazie + ilosc_przejazdow), ilosc_danych)

    with open('problems.bulk', 'w') as file:
        for id_przejazdu in id_przejazdow:
            nazwa_pliku = losowy_string(50)
            opis = losuj_opis()
            opisy.append(opis)
            file.write(f"|{nazwa_pliku}|{opis}|{id_przejazdu}\n")

    return opisy


def losuj_problemy(dlugosc, opisy):
    ile_problemow = len(opisy)
    wylosowane_id = random.sample(range(1, ile_problemow + 1), dlugosc)
    wybrane_opisy = [opisy[num - 1] for num in wylosowane_id]

    return wylosowane_id, wybrane_opisy


def losuj_pracownika():
    try:
        # Wczytaj plik ceo_excel.xlsx i arkusz 'workers'
        ceo_excel = pd.read_excel('ceo_excel.xlsx', sheet_name='workers')

        # Losowanie indeksu wiersza
        losowy_indeks = random.randint(0, ceo_excel.shape[0] - 1)

        # Pobranie wartości z pierwszej i drugiej kolumny wylosowanego wiersza
        imie = ceo_excel.iloc[losowy_indeks, 0]
        nazwisko = ceo_excel.iloc[losowy_indeks, 1]

        return imie, nazwisko

    except FileNotFoundError:
        return None, None

def losuj_date_operacji(rok_start):
    data_start = datetime(rok_start, 1, 1)
    data_koniec = datetime.now()
    return data_start + (data_koniec - data_start) * random.random()


def generuj_operacje_bulk(ilosc_operacji, problemy_w_bazie, opisy, rok_start):
    with open('help_files/problems_and_operations.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        problems = list(reader)

    ilosc_problemow = len(opisy)
    wylosowane_id, wybrane_opisy = losuj_problemy(ilosc_operacji, opisy)
    index = 0
    with open('operations.bulk', 'w') as output_file:
        for opis in wybrane_opisy:
            for problem in problems:
                if problem['Opis'] == opis:
                    rozwiazanie = problem['Rozwiązanie']
                    cena = float(problem['Cena'])
                    cena += cena * random.uniform(-0.2, 0.2)
                    czas = float(problem['Czas'])
                    czas += czas * random.uniform(-0.2, 0.2)
                    rodzaj = problem['Rodzaj']
                    imie_pracownika, nazwisko_pracownika = losuj_pracownika()
                    dodatkowe_informacje = losowy_string(int(150 * (1 + random.uniform(-0.5, 0.5))))
                    id_problemu = wylosowane_id[index] + problemy_w_bazie
                    losowa_data = losuj_date_operacji(rok_start)
                    bulk_value = f"|{imie_pracownika}|{nazwisko_pracownika}|{rozwiazanie}|{dodatkowe_informacje}|{cena}|{czas}|{rodzaj}|{id_problemu}|{losowa_data.strftime('%Y-%m-%d')}"

                    # Zapis do pliku
                    output_file.write(f"{bulk_value}\n")
                    index += 1
                    break

def generate():
    przejazdy_w_bazie = int(input("Podaj ilosc przejazdow znajdujacych sie w bazie: "))
    ilosc_przejazdow = int(input("Podaj ilosc nowych przejazdow: "))
    problemy_w_bazie = int(input("Podaj ilosc problemow znajdujacych sie w bazie: "))
    ilosc_problemow = int(input("Podaj ilość problemow do wygenerowania: "))
    opisy = generuj_problems_bulk(przejazdy_w_bazie, ilosc_przejazdow, ilosc_problemow)
    while True:
        procent_rozw_problemow = int(input("Podaj procent (20-100) problemow ktore zostaly rozwiazane: "))
        if procent_rozw_problemow < 20 or procent_rozw_problemow > 100:
            print("Niewlasciwy procent (musi byc od 20 - 100!!)")
        else:
            break

    rok_start = int(input("Podaj rok startowy do generowania operacji: "))
    ilosc_operacji = int((procent_rozw_problemow/100)*ilosc_problemow)
    generuj_operacje_bulk(ilosc_operacji, problemy_w_bazie, opisy, rok_start)

def generate_default():
    przejazdy_w_bazie = 0
    ilosc_przejazdow = 250000
    problemy_w_bazie = 0
    ilosc_problemow = 70000
    opisy = generuj_problems_bulk(przejazdy_w_bazie, ilosc_przejazdow, ilosc_problemow)
    print(f"Wygenerowano {ilosc_problemow} problemow")
    procent_rozw_problemow = 80
    ilosc_operacji = int((procent_rozw_problemow/100)*ilosc_problemow)
    generuj_operacje_bulk(ilosc_operacji, problemy_w_bazie, opisy, 2015)
    print(f"Wygenerowano {ilosc_operacji} operacji")

def generate_second():
    przejazdy_w_bazie = 3000
    ilosc_przejazdow = 900
    problemy_w_bazie = 1000
    ilosc_problemow = 200
    opisy = generuj_problems_bulk(przejazdy_w_bazie, ilosc_przejazdow, ilosc_problemow)
    procent_rozw_problemow = 70
    ilosc_operacji = int((procent_rozw_problemow/100)*ilosc_problemow)
    generuj_operacje_bulk(ilosc_operacji, problemy_w_bazie, opisy, 2021)