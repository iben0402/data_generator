import time
import generate_excel
import generate_users
import generate_cars
import generate_drives
import generate_problems_and_operations
import file_mover


def main():
    print("------------------------------------------------------")
    print("Wybierz tryb generowania: (wpisz numer)")
    print("1. Default")
    print("2. Manual")
    print("3. Default 2 przedzialy czasu")
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
        file_mover.move_files(folder_name="generated")
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
        file_mover.move_files(folder_name="generated")
    elif int(mode) == 3:
        print("------------------------------------------------------")
        print("Wybrano generowanie z przedzialami czasu")
        print("------------------------------------------------------")
        print("Generowanie excela")
        generate_excel.generate_default()
        print("------------------------------------------------------")
        print("Generowanie pierwszej partii bazy danych")
        generate_users.generate_default()
        generate_cars.generate_default()
        generate_drives.generate_default()
        generate_problems_and_operations.generate_default()
        print("pierwsze dane wygenerowane pomyslnie!")
        file_mover.move_files(folder_name="generated")
        # wait for 5 seconds
        time.sleep(5)
        print("------------------------------------------------------")
        print("Generowanie drugiej partii danych")
        generate_users.generate_second()
        generate_cars.generate_second()
        generate_drives.generate_second()
        generate_problems_and_operations.generate_second()
        print("druga partia danych wygenerowana pomyslnie!")
        print("------------------------------------------------------")
        file_mover.move_files(folder_name="generated_2")

    else:
        print("invalid number")
        return


def add_pipe_to_start_of_each_line(file_path):
    try:
        # Otworzenie pliku do czytania
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Dodanie znaku "|" na początku każdej linii
        modified_lines = ['|' + line for line in lines]

        # Zapisanie zmodyfikowanych linii do pliku
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        return "Znak '|' został dodany na początku każdej linii w pliku."
    except Exception as e:
        return f"Wystąpił błąd: {e}"


if __name__ == "__main__":
    #main()
    print(add_pipe_to_start_of_each_line("C:/Users/iwona/Data-warehouse-implementation/sqls/kachow_master_and_excel/generated_2/problems.bulk"))
