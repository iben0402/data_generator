import generate_excel
import generate_users
import generate_cars
import generate_drives
import generate_problems_and_operations


def main():
    print("------------------------------------------------------")
    print("Wybierz tryb generowania: (wpisz numer)")
    print("1. Default")
    print("2. Manual")
    mode = input("mode: ")
    if int(mode) == 1:
        print("------------------------------------------------------")
        print("Wybrano generowanie domyślne")
        print("------------------------------------------------------")
        print("Generowanie excela")
        generate_excel.generate_default()
        print("------------------------------------------------------")
        print("Generowanie bazy danych")
        generate_users.generate_default()
        generate_cars.generate_default()
        generate_drives.generate_default()
        generate_problems_and_operations.generate_default()
        print("dane wygenerowane pomyslnie!")
        print("------------------------------------------------------")
    elif int(mode) == 2:
        print("------------------------------------------------------")
        print("Wybrano generowanie manualne")
        print("------------------------------------------------------")
        print("Generowanie excela, uzupełnij parametry:")
        generate_excel.generate()
        print("------------------------------------------------------")
        print("Generowanie bazy danych, uzupełnij parametry:")
        generate_users.generate()
        generate_cars.generate()
        generate_drives.generate()
        generate_problems_and_operations.generate()
        print("------------------------------------------------------")
    else:
        print("invalid number")





if __name__ == "__main__":
    main()
