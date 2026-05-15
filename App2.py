import sqlite3

con = sqlite3.connect("Data.db")

# con.execute('''
# DROP TABLE IF EXISTS Customers; 
#             ''')


# con.execute('''
# CREATE TABLE Customers(
#             ID INT PRIMARY KEY NOT NULL, 
#             name VARCAHR(50),
#             age INT NOT NULL,
#             );
# ''')

con.execute("""
INSERT INTO Customers (ID, name, age) 
            VALUES
                (1, "Divaynshu Singh" , 16),
                (2,"Pankaj Dwivedi", 17)
            """)

#We need to close the connection to free the resources that were allocated
con.close()