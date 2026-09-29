# -*- coding: utf-8 -*-
import argparse
import sys
from src.CalcRating import CalcRating
from src.CalcDebts import CalcDebts
from src.TextDataReader import TextDataReader
from src.JsonDataReader import JsonDataReader
from src.DataReader import DataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def get_reader(path: str) -> DataReader:
    if path.lower().endswith(".json"):
        return JsonDataReader()
    return TextDataReader()


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_reader(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    debts = CalcDebts(students).calc()
    print("Students with debts: ", debts)

    names = CalcDebts(students).students_with_debts()
    if names:
        print("Debtors:")
        for name in names:
            print(f"  - {name}")
    else:
        print("No students with debts.")


if __name__ == "__main__":
    main()
