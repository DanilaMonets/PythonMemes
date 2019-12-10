import os
from DbOperations import DbOperations
from CrudOperations import CrudOperations

def main():
    os.system("cls")
    db = DbOperations()
    db.createReservoirsTable()
    crud = CrudOperations(db.getConnection())
    
    while True:
        print('''\nType 
        'G' - To get record  
        'I' - To insert record                            
        'U' - To update record
        'D' - To delete record
        'A' - To get all records\n''')
        choice = input("Your choice: ").lower()

        if choice == 'g':
            crud.GetRecord()
        elif choice == 'i':
            crud.InsertRecord()
        elif choice == 'u':
            crud.UpdateRecord()
        elif choice == 'd':
            crud.DeleteRecord()
        elif choice == 'a':
            crud.GetAllRecords()
        else:
            break

main()

