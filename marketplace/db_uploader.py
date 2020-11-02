import argparse
import pathlib
import sys
from os.path import dirname

# Update root path for project
sys.path.append(dirname(pathlib.Path(__file__).parent))

from marketplace.utils.db_exec import DbExecutor, get_auth

category_name = [
     {"name": "яблоки", "cat": "фрукты"},
     {"name": "тыква", "cat": "овощи"},
     {"name": "томаты", "cat": "овощи"},
     {"name": "перец", "cat": "овощи"},
     {"name": "огурцы", "cat": "овощи"},
     {"name": "картофель", "cat": "овощи"},
     {"name": "баклажан", "cat": "овощи"},
     {"name": "кабачок", "cat": "овощи"},
     {"name": "спаржа", "cat": "овощи"},
     {"name": "капуста", "cat": "овощи"},
     {"name": "морковь", "cat": "овощи"},
     {"name": "лук", "cat": "овощи"},
     {"name": "слива", "cat": "фрукты"},
     {"name": "инжир", "cat": "фрукты"},
     {"name": "груша", "cat": "фрукты"},
     {"name": "айва", "cat": "фрукты"},
     {"name": "клубника", "cat": "фрукты"},
     {"name": "черешня", "cat": "фрукты"},
 ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='usage -c /path/dbconf.ini ', required=True)
    args = parser.parse_args()

    auth_dict = get_auth(args.config)
    db = DbExecutor(auth_dict)

    db_id = 4
    for d in category_name:

        query = "INSERT INTO category VALUES(%s, '%s', '/static/img/%s.jpg', '%s');" %(db_id, d['name'], d['name'], d['cat'] )
        db.query_insert(query)
        #print(query)
        db_id += 1


if __name__ == '__main__':
    main()
