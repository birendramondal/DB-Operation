import mysql.connector #Import MySql Connector

# assigning data for the SQL connector 
url = "mytestdatabase.cme7o154w5f8.ap-south-1.rds.amazonaws.com"
username = input("Enter User name ")
password = input("Inser your password ")
db = "MyTESTDB"

mydb = mysql.connector.connect(
    host=url, user=username, passwd=password, database=db)



# Create connection 
def DBConnection():
    try:
        if (mydb.is_connected() == True):
            # print("DB connection Sucessful !!!")
            return True


    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))



            
# Insert Data
def CreateData():
    name=input("Enter the name of the employee: ")
    Profile=input("Enter the Profile of the employee: ")
    Role=input("Enter the Role of the employee: ")
    Sex=input("Enter the Sex of the employee: ")
    DOBirth=input("Enter the DOB of the employee: ")

    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO MyTable (name, Profile, Role, sex, DOB) VALUES ('{name}','{Profile}','{Role}','{Sex}','{DOBirth}')")
        mydb.commit()
        ReadData() 

    else:
        print("Connection field unable to read :( !!") 

# Read Data
def ReadData():
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute("Select * from MyTable")
        for i in mycursor:
            print(i)  
        # return True    

    else:
        print("Connection field unable to read :( !!")  



# Creat the Main Table 
def CreateTable():
    try: 
        if(DBConnection == True):
            print("Table already present !")
        
        else:
            DBConnection()
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE MyTable (name varchar(20), Profile varchar(20), Role varchar(20),sex char(1),DOB date)")
            print("MyTable Created Sucessfully !!") 

         

    
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

# Update Data
def UpdateData():
    name=("Enter the Name of employee: ")
    profile=input("Enter new profile: ")
    role=input("Enter new role: ")
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute(f"UPDATE MyTable SET Profile='{profile}', Role='{role}' WHERE name={name};")
        mydb.commit()
    
   
    

# Delete Data
def DeleteData():
    name=input("Enter the name that you want to Delete : ")
    if(DBConnection() == True):
        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM MyTable WHERE name='{name}'")
        mydb.commit()
        ReadData()
    
    

