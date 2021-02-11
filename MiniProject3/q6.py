import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password1!",
    database="SalesOrdersExampleTest"
)
print(db_connection)

mycursor = db_connection.cursor()

mycursor.execute("SELECT Customers.CustomerID, Customers.CustFirstName, Customers.CustLastName FROM Customers WHERE Customers.CustomerID NOT IN (SELECT CustomerID FROM (Orders INNER JOIN Order_Details ON Orders.OrderNumber = Order_Details.OrderNumber) INNER JOIN Products ON Order_Details.ProductNumber = Products.ProductNumber WHERE Products.CategoryID IN (2, 6));")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT CustomerID, CustFirstName, CustLastName FROM Customers WHERE (CustomerID IN (SELECT Orders.CustomerID FROM (Orders INNER JOIN Order_Details ON Orders.OrderNumber = Order_Details.OrderNumber) INNER JOIN Products ON Products.ProductNumber = Order_Details.ProductNumber WHERE Products.CategoryID = 2)) AND (CustomerID NOT IN (SELECT Orders.CustomerID FROM (Orders INNER JOIN Order_Details ON Orders.OrderNumber = Order_Details.OrderNumber) INNER JOIN Products ON Products.ProductNumber = Order_Details.ProductNumber WHERE Products.ProductName LIKE '%Helmet'));")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT Customers.CustomerID, Customers.CustFirstName, Customers.CustLastName, Orders.OrderNumber, Orders.OrderDate FROM Customers INNER JOIN Orders ON Customers.CustomerID=Orders.CustomerID WHERE EXISTS  (SELECT OrderNumber  FROM (Order_Details INNER JOIN Products ON Order_Details.ProductNumber = Products.ProductNumber) INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID WHERE Categories.CategoryDescription = 'Bikes' AND Order_Details.OrderNumber = Orders.OrderNumber) AND NOT EXISTS  (SELECT *  FROM Order_Details INNER JOIN Products ON Order_Details.ProductNumber = Products.ProductNumber WHERE Products.ProductName LIKE '%Helmet' AND Order_Details.OrderNumber = Orders.OrderNumber);")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT Customers.CustomerID, Customers.CustFirstName, Customers.CustLastName, Orders.OrderNumber, Orders.OrderDate FROM Customers INNER JOIN Orders ON Customers.CustomerID=Orders.CustomerID WHERE EXISTS  (SELECT * FROM (Orders As O2 INNER JOIN Order_Details ON O2.OrderNumber = Order_Details.OrderNumber) INNER JOIN Products ON Products.ProductNumber = Order_Details.ProductNumber WHERE Products.CategoryID = 2 AND Orders.CustomerID = Customers.CustomerID AND O2.OrderNumber = Orders.OrderNumber) AND EXISTS (SELECT * FROM (Orders As O3  INNER JOIN Order_Details ON O3.OrderNumber = Order_Details.OrderNumber) INNER JOIN Products ON Products.ProductNumber = Order_Details.ProductNumber WHERE Products.ProductName LIKE '%Helmet' AND Orders.CustomerID = Customers.CustomerID AND O3.OrderNumber = Orders.OrderNumber);")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT Vendors.VendorID, Vendors.VendName FROM Vendors WHERE Vendors.VendorID IN (SELECT VendorID FROM (Product_Vendors INNER JOIN Products ON Product_Vendors.ProductNumber = Products.ProductNumber) INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID WHERE Categories.CategoryDescription = 'Accessories') AND Vendors.VendorID IN (SELECT VendorID FROM (Product_Vendors INNER JOIN Products ON Product_Vendors.ProductNumber = Products.ProductNumber) INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID WHERE Categories.CategoryDescription = 'Car racks') AND Vendors.VendorID IN (SELECT VendorID FROM (Product_Vendors INNER JOIN Products ON Product_Vendors.ProductNumber = Products.ProductNumber) INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID WHERE Categories.CategoryDescription = 'Clothing');")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
