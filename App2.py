import sqlite3

con = sqlite3.connect("Data.db")
cursor= con.cursor()

# con.execute('''
# DROP TABLE IF EXISTS Customers; 
#             ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers(
            ID INT PRIMARY KEY NOT NULL, 
            name VARCAHR(50),
            age INT NOT NULL
            );
''')

cursor.execute('''INSERT INTO Customers (ID, name, age) VALUES (1,"Divaynshu Singh",16), (2, "Pankaj Dwivedi", 17); ''')

all_data= cursor.execute('''SELECT * FROM Customers; ''')
for row in all_data:
    print(row)

con.commit()
 
#We need to close the connection to free the resources that were allocated
con.close()

#Additionalyy we can use the CONTEXT MANAGER (with) statement to automatically close the connection and commits or rolls back transactions if errors occur.