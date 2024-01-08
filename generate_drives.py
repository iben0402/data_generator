import pandas as pd
import random
from datetime import datetime, timedelta

def losuj_date_przejazdu(rok_start):
    data_start = datetime(rok_start, 1, 1)
    data_koniec = datetime.now()
    return data_start + (data_koniec - data_start) * random.random()

def losuj_czas():
    return random.randint(10, 240)

def generuj_dystans(czas):
    srednia_predkosc = 40  # km/h
    dystans = (srednia_predkosc / 60) * czas  # w godzinach
    dystans += dystans * random.uniform(-0.2, 0.2)  # modyfikacja dystansu
    return dystans

def generuj_zuzyte_paliwo(dystans):
    srednie_spalanie = 8
    zuzyte_paliwo = (dystans / 100) * srednie_spalanie
    zuzyte_paliwo += zuzyte_paliwo * random.uniform(-0.2, 0.2)
    return zuzyte_paliwo
def losuj_miasto():
    df = pd.read_excel('ceo_excel.xlsx', sheet_name='cities')
    miasto = df['City'].sample().values[0]
    return miasto


def losuj_id_pojazdu(liczba_pojazdow):
    return random.randint(1, liczba_pojazdow)


def losuj_id_uzytkownika(liczba_uzytkownikow):
    return random.randint(1, liczba_uzytkownikow)


def generuj_drives_bulk(liczba_przejazdow, liczba_pojazdow, liczba_uzytkownikow, rok_start):
    with open('drives.bulk', 'w') as file:
        for _ in range(liczba_przejazdow):
            losowa_data = losuj_date_przejazdu(rok_start)
            czas = losuj_czas()
            dystans = generuj_dystans(czas)
            cena = dystans * 2 + 5
            zuzyte_paliwo = generuj_zuzyte_paliwo(dystans)
            miasto = losuj_miasto()
            id_pojazdu = losuj_id_pojazdu(liczba_pojazdow)
            id_uzytkownika = losuj_id_uzytkownika(liczba_uzytkownikow)
            file.write(
                f"|{losowa_data.strftime('%Y-%m-%d')}|{czas}|{dystans}|{cena}|{zuzyte_paliwo}|{miasto}|{id_pojazdu}|{id_uzytkownika}\n")



def generate():
    liczba_uzytkownikow = int(input("Podaj liczbe uzytkownikow w bazie: "))
    liczba_pojazdow = int(input("Podaj liczbe pojazdow w bazie: "))
    ilosc_danych = int(input("Podaj ilość przejazdow do wygenerowania: "))
    rok_start = int(input("Podaj rok startowy do generowania przejazdow: "))
    generuj_drives_bulk(ilosc_danych, liczba_pojazdow, liczba_uzytkownikow, rok_start)

def generate_default():
    liczba_uzytkownikow = 80000
    liczba_pojazdow = 50000
    ilosc_danych = 250000
    rok_start = 2015
    generuj_drives_bulk(ilosc_danych, liczba_pojazdow, liczba_uzytkownikow, rok_start)
    print(f"Wygenerowano {ilosc_danych} przejazdów")

def generate_second():
    liczba_uzytkownikow = 1200
    liczba_pojazdow = 1200
    ilosc_danych = 900
    rok_start = 2021
    generuj_drives_bulk(ilosc_danych, liczba_pojazdow, liczba_uzytkownikow, rok_start)