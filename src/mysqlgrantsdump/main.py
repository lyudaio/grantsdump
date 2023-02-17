#!/usr/bin/env python

"""
Author: lyudaio
Version: 0.0.4
"""

import argparse
import getpass
import mysql.connector
from prettytable import PrettyTable

def connect_to_database(host, user, password, database, port):
    """
    Connect to the MySQL database and return a tuple of (connection, cursor) objects.

    Args:
    host: The MySQL database host name or IP address.
    user: The MySQL database user name.
    password: The MySQL database password.
    database: The MySQL database name.
    port: The MySQL database port number.

    Returns:
    A tuple of (connection, cursor) objects.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        cursor = conn.cursor()
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        exit(1)

    return (conn, cursor)

def fetch_all_users_grants(cursor):
    """
    Fetch a list of all users and their grants on each database.

    Args:
    cursor: A cursor object to execute SQL queries.

    Returns:
    A list of tuples, where each tuple contains the user, host, and their permissions on each database.
    """
    try:
        cursor.execute("SELECT User, Host, Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv, Grant_priv, Super_priv FROM mysql.user")
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print(f"Error fetching users grants: {error}")
        exit(1)

def print_grants_table(users_grants):
    """
    Create a pretty table to output the results.

    Args:
    users_grants: A list of tuples, where each tuple contains the user, host, and their permissions on each database.
    """
    table = PrettyTable()
    table.field_names = ["User", "Host", "Select", "Insert", "Update", "Delete", "Create", "Drop", "Grant", "Super"]
    for row in users_grants:
        table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])

    print(table)

def main():
    # Define the command-line arguments
    parser = argparse.ArgumentParser(
        description="A command-line tool to dump a list of all MySQL users and their grants.")
    parser.add_argument("-H", "--host", type=str, default="localhost",
                        help="The MySQL database host name or IP address. Default is localhost.")
    parser.add_argument("-u", "--user", type=str, default="root",
                        help="The MySQL database user name. Default is root.")
    parser.add_argument("-d", "--database", type=str, default="",
                        help="The MySQL database name.")
    parser.add_argument("-P", "--port", type=int, default=3306,
                        help="The MySQL database port number. Default is 3306.")

    args = parser.parse_args()

    # Prompt for the MySQL database password
    password = getpass.getpass(prompt="Enter the MySQL database password: ")

    # Connect to the MySQL database
    conn, cursor = connect_to_database(args.host, args.user, password, args.database, args.port)

    # Fetch a list of all users and their grants on each database
    users_grants = fetch_all_users_grants(cursor)

    # Create a pretty table to output the results
    print_grants_table(users_grants)

    # Close the cursor and database connections
    cursor.close()

if __name__ == "__main__":
   main()

