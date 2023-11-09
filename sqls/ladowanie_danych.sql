USE Kachow
GO

BULK INSERT dbo.Uzytkownicy FROM '../generated/users.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Pojazdy FROM '../generated/vehicles.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Przejazdy FROM '../generated/drives.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Problemy FROM '../generated/problems.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Operacje FROM '../generated/operations.bulk' WITH (FIELDTERMINATOR='|')

GO

BULK INSERT dbo.Uzytkownicy FROM '../generated_2/users.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Pojazdy FROM '../generated_2/vehicles.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Przejazdy FROM '../generated_2/drives.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Problemy FROM '../generated_2/problems.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.Operacje FROM '../generated_2/operations.bulk' WITH (FIELDTERMINATOR='|')

GO