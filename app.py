import DbOperation


def Operation():
    print("Enter your operation ID\n1=Create Table \n2= Read User Table; \n3=Add User; \n4=Delete User; \n5=Update User")
    user_input = int(input("Enter the number: "))

    while True:
        if(user_input ==  1):
            DbOperation.CreateTable()
            break
        
        elif(user_input == 2):
            DbOperation.ReadData()
            # break
            Operation()

        elif(user_input == 3):
            DbOperation.CreateData()
            break

        elif(user_input == 4):
            DbOperation.DeleteData()
            break

        elif(user_input == 5):
            DbOperation.UpdateData()
            break

        else:
            print("Invalid Input !! :( \n to exit press CTRL+C ")
            break


Operation()
