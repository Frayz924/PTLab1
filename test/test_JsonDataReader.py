# -*- coding: utf-8 -*-
import json
import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader


class TestJsonDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = json.dumps({
            "Иванов Константин Дмитриевич": {
                "математика": 91,
                "химия": 100
            },
            "Петров Петр Семенович": {
                "русский язык": 87,
                "литература": 78
            }
        }, ensure_ascii=False)
        data: DataType = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91),
                ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87),
                ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(
        self,
        file_and_data_content: tuple[str, DataType],
        tmpdir,
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_empty(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("empty.json")
        p.write_text("{}", encoding='utf-8')
        assert JsonDataReader().read(str(p)) == {}

    def test_read_single_student(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("one.json")
        p.write_text(
            json.dumps({"Сидоров": {"физика": 75}}, ensure_ascii=False),
            encoding='utf-8'
        )
        result = JsonDataReader().read(str(p))
        assert result == {"Сидоров": [("физика", 75)]}

    def test_read_only_one_subject(self, tmpdir) -> None:
        p = tmpdir.mkdir("datadir").join("one_subj.json")
        p.write_text(
            json.dumps(
                {"Иванов": {"математика": 50}},
                ensure_ascii=False
            ),
            encoding='utf-8'
        )
        assert JsonDataReader().read(str(p)) == {
            "Иванов": [("математика", 50)]
        }
