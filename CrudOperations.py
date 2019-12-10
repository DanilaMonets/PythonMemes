class CrudOperations:
    def __init__(self, _connection):
        self.connection = _connection
        self.cursor = _connection.cursor()

    def GetRecord(self):
        print()
        name = input("Input reservoir's name: ")

        query = ("SELECT TOP(1) * FROM [dbo].[Reservoirs] WHERE [Name] = ?")
        self.cursor.execute(query, [name])

        for record in self.cursor:
            print('\nRecord: %r' % (record,))

    def InsertRecord(self):
        print()
        reservoirName = input("Input reservoir name: ")
        reservoirVolume = input("Input reservoir volume: ")

        try:
            query = "INSERT INTO [dbo].[Reservoirs]([Name], [Volume]) VALUES(?, ?)"

            self.cursor.execute(query, [reservoirName, reservoirVolume])

            self.connection.commit()
            print("Record inserted successfully")

        except:
            self.connection.rollback()
            print("Exception has been thrown")

    def GetAllRecords(self):
        print()
        self.cursor.execute("SELECT * FROM [dbo].[Reservoirs]")
        for record in self.cursor:
            print('Record ' + str(record[0]) + ': %r' % (record,))

    def UpdateRecord(self):
        print()
        id = input("Input id of reservoir to be updated: ")

        try:
            query = "SELECT * FROM [dbo].[Reservoirs] WHERE [Id] = ?"
            self.cursor.execute(query, [id])
            item = self.cursor.fetchone()

            if (item[0]):
                print("Reservoir")
                print("Id: " + str(item[0]))
                print("Name: " + str(item[1]))
                print("Volume: " + str(item[2]))

                print("\nUpdated record's data")

                name = input("Input new name: ")
                volume = input("Input new volume: ")

                query = "UPDATE [dbo].[Reservoirs] SET [Name] = ?, [Volume] = ? WHERE [Id] = ?"
                self.cursor.execute(query, [name, volume, id])
                self.connection.commit()
                print("Record has been updated successfully")

        except:
            self.connection.rollback()
            print("Exception has been thrown")

    def DeleteRecord(self):
        print()
        id = input("Input id of reservoir to be deleted: ")

        try:
            query = "SELECT * FROM [dbo].[Reservoirs] WHERE [Id] = ?"
            self.cursor.execute(query, [id])
            item = self.cursor.fetchone()

            if (item[0]):
                print("Reservoir")
                print("Id: " + str(item[0]))
                print("Name: " + str(item[1]))
                print("Volume: " + str(item[2]))

                answer = input("Delete this record? (Y/N)\n")
                if(answer.lower() == 'y'):
                    query = "DELETE FROM [dbo].[Reservoirs] WHERE [Id] = ?"
                    self.cursor.execute(query, [id])
                    self.connection.commit()
                    print("Record has been deleted successfully")
                else:
                    print("Operation has not been confirmed")

        except:
            self.connection.rollback()
            print("Exception has been thrown")

    def __del__(self):
        self.connection.close()