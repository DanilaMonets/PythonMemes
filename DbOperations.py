import pypyodbc

class DbOperations:
    DATABASE_CONFIG = {
        'Driver': 'SQL Server',
        'Server': 'DESKTOP-LHAIM07\MYLOCALDB',
        'Database': 'ReservoirsDB',
        'TrustedConnection': 'yes'
    }

    def getConnection(self):    
        connection = pypyodbc.connect(
            "Driver= {" + self.DATABASE_CONFIG["Driver"] + 
            "} ; Server=" + self.DATABASE_CONFIG["Server"] + 
            ";Database=" + self.DATABASE_CONFIG["Database"] +
            ";Trusted_Connection=" + self.DATABASE_CONFIG["TrustedConnection"])
        
        return connection

    def createReservoirsTable(self):
        dbContext = self.getConnection()
        try:
            cursor = dbContext.cursor()
            cursor.execute('''USE ReservoirsDB
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Reservoirs' and xtype='U')
            CREATE TABLE Reservoirs (
                [Id] INT PRIMARY KEY IDENTITY(1, 1),
                [Name] VARCHAR(50) NOT NULL,
                [Volume] INT NOT NULL
            );''')
            dbContext.commit()
            print("Table 'Reservoirs' created successfully")
        except:
            print("Exception has been thrown")
            dbContext.rollback()
        dbContext.close()