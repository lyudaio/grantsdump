# mysql-grants-dump

## Description

`mysql-grants-dump` is a command-line tool that allows you to dump a list of all MySQL users and their grants. It connects to a MySQL database and retrieves the users and their associated permissions, and outputs them in a table format using the `prettytable` module.

## Getting Started

1. Install the required dependencies by running `pip install -r requirements.txt`
2. Run the tool using the following command: `python mysql_grants_dump.py [OPTIONS]`
3. The available options are as follows:
   - `-H, --host`: The MySQL database host name or IP address. Default is `localhost`.
   - `-u, --user`: The MySQL database user name. Default is `root`.
   - `-d, --database`: The MySQL database name.
   - `-P, --port`: The MySQL database port number. Default is `3306`.

## Example Usage

```bash
cd granstdump/
pip install -r requirements.txt
python3 mysql_grants_dump.py -u root -p
```

### Example Output

```bash
+------------------+-----------+--------+--------+--------+--------+--------+------+-------+-------+
|       User       |    Host   | Select | Insert | Update | Delete | Create | Drop | Grant | Super |
+------------------+-----------+--------+--------+--------+--------+--------+------+-------+-------+
|   andrewhoward   |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|    carsonlisa    |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|      dsmith      |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|  elizabethbrown  |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|     grant03      |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|      ilopez      |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|   jeanneconrad   |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|     johngray     |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|  joshuawhitaker  |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|    kimolivia     |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|    krystal52     |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|     larry00      |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|   monicaadams    |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
| rodrigueznicole  |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|    uhernandez    |     %     |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
| mysql.infoschema | localhost |   Y    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|  mysql.session   | localhost |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   Y   |
|    mysql.sys     | localhost |   N    |   N    |   N    |   N    |   N    |  N   |   N   |   N   |
|       root       | localhost |   Y    |   Y    |   Y    |   Y    |   Y    |  Y   |   Y   |   Y   |
+------------------+-----------+--------+--------+--------+--------+--------+------+-------+-------+
```

## License

`mysql-grants-dump` is released under the MIT License. See `LICENSE` for more information.
