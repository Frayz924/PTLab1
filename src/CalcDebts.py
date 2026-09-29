# -*- coding: utf-8 -*-
from src.Types import DataType


class CalcDebts:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> int:
        count = 0
        for student, subjects in self.data.items():
            if any(score < 61 for _, score in subjects):
                count += 1
        return count

    def students_with_debts(self) -> list[str]:
        result = []
        for student, subjects in self.data.items():
            if any(score < 61 for _, score in subjects):
                result.append(student)
        return result
