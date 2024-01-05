import json

from requests import Response
import json
"""Методы для проверки ответов запросов (статусы, сообщения и т.д.)"""


class Checking:
    """Метод для проверки статус-кодов"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f'Успешно! Статус код = {result.status_code}!')

    """Метод для проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        #token = json.loads(result.text)
        token = result.json()
        assert list(token) == expected_value
        print(f'Успешно! Все необходимые поля на месте: {expected_value}.' )

    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Успешно! Значение поля {field_name} = {expected_value}.' )

    """Метод для поиска значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_search_word(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert expected_value in check_info
        print(f'Успешно! Слово "{expected_value}" в значении поля {field_name}.')
