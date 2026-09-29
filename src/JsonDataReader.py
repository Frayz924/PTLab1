# -*- coding: utf-8 -*-
import json
from src.DataReader import DataReader
from src.Types import DataType


class JsonDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            raw = json.load(file)

        data: DataType = {}
        for student, subjects in raw.items():
            data[student] = [
                (subject, int(score))
                for subject, score in subjects.items()
            ]
        return data
