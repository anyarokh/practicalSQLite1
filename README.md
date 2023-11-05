# practicalSQLite1
This is a Python script that demonstrates the use of the `sqlite3` library to manage a SQLite database. The script performs the following operations:

1. Establishes a connection to a SQLite database and creates a cursor object.
2. Defines the structure of the database by creating tables for products, customers, orders, and order details, and inserts sample data into these tables.
3. Executes two SQL queries to retrieve information from the database.
4. Updates the status of orders from 'Очікується' to 'Відправлено'.
5. Executes the same SQL queries again to show the updated results.
6. Commits the changes to the database and closes the connection.

The tables were created and populated in sqlite3. Data in tables is inserted into the code.

The SQL queries used in this script are as follows:
### Query 1
![image](https://github.com/anyarokh/practicalSQLite1/assets/128834920/7d40ae34-5e86-4170-84eb-ad5afcf17b94)

This query retrieves the names of products and their quantities for orders with the status 'Очікується'.

### Query 2
![image](https://github.com/anyarokh/practicalSQLite1/assets/128834920/eb63d210-f25e-4c94-bfc5-87c8bafa96a6)

This query retrieves order details (ID, creation date, and status) for orders placed by a customer named 'Ольга'.

### Updating Records
The script updates the status of orders from 'Очікується' to 'Відправлено' using an SQL UPDATE statement.

### Running the Script
To run the script, you need to have the sqlite3 library installed and ensure that you have the my_first_db.db file in the same directory as the script.
