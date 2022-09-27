import csv
import json
import os
from abc import ABC, abstractmethod
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConverterCSV(ABC):
    def __init__(self, model: str, name_csv_file: str, name_json_file: str) -> None:
        """
        :param model: имя модели. Пример: "ads.category"
        :param name_csv_file: имя csv файла который будем конвертировать
        :param name_json_file: имя которое получит JSON файл после конвертации
        """
        self.model = model
        self.path_csv = os.path.join(BASE_DIR, 'data', name_csv_file)
        self.json_path = os.path.join(BASE_DIR, 'fixtures', name_json_file)

    @abstractmethod
    def pattern_model(self, data_csv: csv.DictReader):
        """
        Шаблон по которому будет составляться словарь, в зависимости от модели

        :param data_csv: данные после прочтения CSV файла
        """
        pass

    def file_converter(self) -> None:
        """
        Чтение и перенос данных из CSV файла в JSON файл
        """
        with open(self.path_csv, 'r', encoding='utf-8') as csv_file:
            data_csv = csv.DictReader(csv_file)
            data_list = self.pattern_model(data_csv)
            self._write_json(data_list)

    def _write_json(self, data_csv: list):
        with open(self.json_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data_csv, indent=4, ensure_ascii=False))


class ADSConverterCSV(BaseConverterCSV):
    """
    Класс для конвертации данных из CSV файла в JSON для модели ADS
    """

    def pattern_model(self, data_csv: csv.DictReader) -> list[dict]:
        data_list = []
        for item in data_csv:
            data_add = {"model": self.model,
                        "fields": {"name": item['name'],
                                   "author": item['author'],
                                   "price": int(item['price']),
                                   "description": item['description'],
                                   "address": item['address'],
                                   "is_published": True if item["is_published"] == "TRUE" else False}}

            data_list.append(data_add)

        return data_list


class CatConverterCSV(BaseConverterCSV):
    """
    Класс для конвертации данных из CSV файла в JSON для модели Category
    """

    def pattern_model(self, data_csv: csv.DictReader) -> list[dict]:
        data_list = []
        for item in data_csv:
            data_add = {"model": self.model,
                        "fields": {"name": item['name']}}

            data_list.append(data_add)

        return data_list


convert_ads = ADSConverterCSV('ads.ads', "ads.csv", "ads.json")
convert_ads.file_converter()

convert_category = CatConverterCSV('ads.category', 'categories.csv', "categories.json")
convert_category.file_converter()
