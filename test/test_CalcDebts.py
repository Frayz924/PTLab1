# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.CalcDebts import CalcDebts


class TestCalcDebts:

    @pytest.fixture()
    def data_no_debts(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90),
                ("литература", 76)
            ]
        }

    @pytest.fixture()
    def data_one_debt(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 80),
                ("программирование", 90)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("социология", 90),
                ("химия", 60)
            ]
        }

    @pytest.fixture()
    def data_all_debts(self) -> DataType:
        return {
            "А": [("математика", 50)],
            "Б": [("физика", 30)],
            "В": [("химия", 61)]
        }

    def test_calc_no_debts(self, data_no_debts: DataType) -> None:
        assert CalcDebts(data_no_debts).calc() == 0

    def test_calc_one_debt(self, data_one_debt: DataType) -> None:
        assert CalcDebts(data_one_debt).calc() == 1

    def test_calc_all_debts(self, data_all_debts: DataType) -> None:
        assert CalcDebts(data_all_debts).calc() == 2

    def test_students_with_debts(self, data_one_debt: DataType) -> None:
        result = CalcDebts(data_one_debt).students_with_debts()
        assert result == ["Петров Петр Петрович"]

    def test_boundary_61_not_debt(self) -> None:
        data: DataType = {"X": [("математика", 61)]}
        assert CalcDebts(data).calc() == 0

    def test_boundary_60_is_debt(self) -> None:
        data: DataType = {"X": [("математика", 60)]}
        assert CalcDebts(data).calc() == 1

    def test_empty_data(self) -> None:
        assert CalcDebts({}).calc() == 0

    def test_no_students_with_debts_list(
        self,
        data_no_debts: DataType,
    ) -> None:
        assert CalcDebts(data_no_debts).students_with_debts() == []
