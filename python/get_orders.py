"""
You are given a database table called orders with the following columns:

order_id (integer)
customer_id (integer)
order_date (date)
total_amount (float)
Write a Python function get_total_spent(customer_id) that takes a customer_id as input and returns the total amount spent by that customer across all their orders. The function should first query the database using SQL to fetch all orders for the given customer, and then sum the total_amount column to calculate the total spent.

Your task is to:

Write the SQL query to fetch all orders for a given customer.
Write the get_total_spent(customer_id) function in Python that uses the SQL query to fetch orders and calculate the total spent.
Write unit tests for the get_total_spent(customer_id) function using unittest module in Python.
"""

import sqlite3
import unittest

# Create a connection to the database
conn = sqlite3.connect('orders.db')

sql_query = '''
SELECT total_amount
FROM orders
WHERE customer_id = ?
'''

conn = sqlite3.connect('orders.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date DATE,
    total_amount FLOAT
)
''')

def get_total_spent(customer_id):
    cursor = conn.cursor()
    cursor.execute(sql_query, (customer_id,))
    orders = cursor.fetchall()

    # Calculate the total amount spent across all orders
    total_spent = sum(order[0] for order in orders)

    return total_spent

class TestGetTotalSpent(unittest.TestCase):
    def setUp(self):
        # Insert some sample data into the orders table
        conn.execute("INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES (1, 1, '2022-01-01', 20.0)")
        conn.execute("INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES (2, 2, '2022-02-01', 20.0)")
        conn.execute("INSERT INTO orders (order_id, customer_id, order_date, total_amount) VALUES (3, 1, '2022-03-01', 28.0)")
        conn.commit()

    def tearDown(self):
        # Remove the sample data from the orders table
        conn.execute("DELETE FROM orders WHERE order_id IN (1, 2, 3)")
        conn.commit()
      

    def test_get_total_spent(self):
        self.assertEqual(get_total_spent(1), 48.0)

        self.assertEqual(get_total_spent(2), 20.0)

        self.assertEqual(get_total_spent(3), 0.0)

if __name__ == '__main__':
    unittest.main()
