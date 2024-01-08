import csv
import random


# Funkcja losująca imię
def losuj_imie():
    with open('help_files/names.csv', newline='', encoding='utf-8') as file:
        imiona = [row['Imię'] for row in csv.DictReader(file)]
        return random.choice(imiona)


# Funkcja losująca nazwisko
def losuj_nazwisko():
    with open('help_files/surnames.csv', newline='', encoding='utf-8') as file:
        nazwiska = [row['Nazwisko'] for row in csv.DictReader(file)]
        return random.choice(nazwiska)


# Funkcja generująca losową datę urodzenia
def generuj_date_urodzenia():
    rok = random.randint(1950, 2005)
    miesiac = random.randint(1, 12)
    dzien = random.randint(1, 28)  # Uproszczona obsługa miesięcy o stałej liczbie dni
    return f"{rok}-{miesiac:02d}-{dzien:02d}"


# Funkcja generująca numer prawa jazdy
def generuj_nr_prawa_jazdy():
    numer = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    numer += '/' + ''.join([str(random.randint(0, 9)) for _ in range(2)])
    numer += '/' + ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return numer


# Funkcja tworząca plik "users.bulk"
def generuj_users_bulk(liczba_danych):
    with open('users.bulk', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')

        for _ in range(liczba_danych):
            imie = losuj_imie()
            nazwisko = losuj_nazwisko()
            data_urodzenia = generuj_date_urodzenia()
            nr_prawa_jazdy = generuj_nr_prawa_jazdy()

            writer.writerow(["",imie, nazwisko, data_urodzenia, nr_prawa_jazdy])


def generate():
    ilosc_danych = int(input("Podaj ilość uzytkownikow do wygenerowania: "))
    generuj_users_bulk(ilosc_danych)


def generate_default():
    amount = 80000
    generuj_users_bulk(amount)
    print(f"Wygenerowano {amount} uzytkownikow")

def generate_second():
    generuj_users_bulk(200)