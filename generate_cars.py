import pandas as pd
import random
import string


# Funkcja losująca markę i model z pliku ceo_excel.xlsx
def losuj_marke_i_model():
    df = pd.read_excel('ceo_excel.xlsx', sheet_name='cars')
    wylosowany_wiersz = df.sample()
    marka = wylosowany_wiersz['Car manufacturer'].values[0]
    model = wylosowany_wiersz['Model'].values[0]
    return marka, model


# Funkcja generująca losowy numer rejestracyjny
def generuj_nr_rejestracyjny():
    litery = [ch for ch in string.ascii_uppercase if ch not in 'BDIOZ']
    return ''.join(random.choice(litery) for _ in range(2)) + ''.join(
        random.choice(string.digits + string.ascii_uppercase) for _ in range(5))


# Funkcja generująca losowy numer VIN
def generuj_nr_vin():
    litery_i_cyfry = [ch for ch in string.ascii_uppercase + string.digits if ch not in 'QOIZ']
    return ''.join(random.choice(litery_i_cyfry) for _ in range(17))


# Funkcja tworząca plik "vehicles.bulk"
def generuj_vehicles_bulk(liczba_danych):
    with open('vehicles.bulk', 'w', newline='', encoding='utf-8') as file:
        for _ in range(liczba_danych):
            marka, model = losuj_marke_i_model()
            nr_rejestracyjny = generuj_nr_rejestracyjny()
            nr_vin = generuj_nr_vin()
            file.write(f"|{marka}|{model}|{nr_rejestracyjny}|{nr_vin}\n")


# Główna część programu
def generate():
    ilosc_danych = int(input("Podaj ilość pojazdów do wygenerowania: "))
    generuj_vehicles_bulk(ilosc_danych)


def generate_default():
    generuj_vehicles_bulk(1000)

def generate_second():
    generuj_vehicles_bulk(200)