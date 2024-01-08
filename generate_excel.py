import pandas as pd


def losuj_dane_z_pliku(nazwa_pliku, ilosc_wierszy, wylosowane_miasta):
    folder_name = "help_files"
    df = pd.read_csv(folder_name+"/"+nazwa_pliku)

    # Jeśli plik to workers.csv, wybierz pracowników z wylosowanych miast
    if 'City' in df.columns and nazwa_pliku == 'workers.csv' and len(wylosowane_miasta) > 0:
        df = df[df['City'].isin(wylosowane_miasta)]

    if ilosc_wierszy >= len(df):
        return df
    else:
        return df.sample(n=ilosc_wierszy)


def generuj_excela(ilosci):
    nazwy_plikow = ['cars.csv', 'cities.csv', 'workers.csv']
    nazwy_arkuszy = ['cars', 'cities', 'workers']
    wylosowane_miasta = set()

    wylosowane_dane = {}
    for nazwa, ilosc in ilosci.items():
        if nazwa == 'cities.csv':
            wylosowane_dane[nazwa] = losuj_dane_z_pliku(nazwa, ilosc, [])
            wylosowane_miasta = set(wylosowane_dane[nazwa]['City'])
        else:
            wylosowane_dane[nazwa] = losuj_dane_z_pliku(nazwa, ilosc, list(wylosowane_miasta))


    # Tworzenie pliku Excel
    excel_writer = pd.ExcelWriter('ceo_excel.xlsx', engine='openpyxl')

    for nazwa, df in wylosowane_dane.items():
        df.to_excel(excel_writer, sheet_name=nazwy_arkuszy[nazwy_plikow.index(nazwa)], index=False)

    excel_writer._save()
    excel_writer.close()
    print("Excel poprawnie wygenerowany")


def generate_default():
    nazwy_plikow = ['cars.csv', 'cities.csv', 'workers.csv']
    ilosci = {}
    ilosci['cars.csv'] = 20
    ilosci['cities.csv'] = 10
    ilosci['workers.csv'] = 50
    generuj_excela(ilosci)


def generate():
    nazwy_plikow = ['cars.csv', 'cities.csv', 'workers.csv']
    ilosci = {}
    for nazwa in nazwy_plikow:
        ilosc = int(input(f"Ile wierszy wylosować z pliku {nazwa}? "))
        ilosci[nazwa] = ilosc

    generuj_excela(ilosci)