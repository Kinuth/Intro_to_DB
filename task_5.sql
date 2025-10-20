-- This script inserts a single row into the Customers table
-- in the alx_book_store database.
USE alx_book_store;
INSERT INTO Customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
