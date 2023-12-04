CREATE DATABASE Kachow;
GO

USE Kachow
GO

CREATE TABLE Uzytkownicy (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Imię VARCHAR(20),
    Nazwisko VARCHAR(20),
    Data_urodzenia DATE,
    Nr_prawa_jazdy VARCHAR(14)
);
GO

CREATE TABLE Pojazdy (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Marka VARCHAR(20),
    Model VARCHAR(30),
    Nr_Rejestracyjny VARCHAR(8),
    VIN VARCHAR(17)
);
GO

CREATE TABLE Przejazdy (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Data DATETIME,
    Czas TIME,
    Dystans NUMERIC,
    Pojazd_ID INT,
    Zużyte_paliwo NUMERIC,
    Cena NUMERIC,
    Miasto VARCHAR(30),
    ID_uzytkownika INT,
    FOREIGN KEY (Pojazd_ID) REFERENCES POJAZDY(ID),
    FOREIGN KEY (ID_uzytkownika) REFERENCES UZYTKOWNICY(ID)
);
GO

CREATE TABLE Problemy (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Plik VARCHAR(50),
    Opis VARCHAR(500)
);
GO

CREATE TABLE Operacje (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Imię_pracownika VARCHAR(20),
    Nazwisko_pracownika VARCHAR(20),
    Nazwa_operacji VARCHAR(50),
    Dodatkowe_informacje VARCHAR(300),
    Cena_Operacji NUMERIC,
    Czas_Operacji NUMERIC,
    Rodzaj_operacji VARCHAR(10),
    ID_problemu INT,
    Czas TIME,
    FOREIGN KEY (ID_problemu) REFERENCES PROBLEMY(ID)
);
GO
