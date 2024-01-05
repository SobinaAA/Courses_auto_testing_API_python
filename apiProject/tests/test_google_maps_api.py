from requests import Response
from utils.api import GoogleMapsAPI
from utils.checking import Checking
import allure

"""Создание, изменение и удаление новой локации"""


@allure.epic('Test create place')
class TestCreatePlace():
    @allure.description('Test create, update and delete new location')
    def test_create_new_place(self):
        print('Метод POST')
        result_post = GoogleMapsAPI.create_new_place()
        place_id = result_post.json().get('place_id')
        Checking.check_status_code(result_post, 200)  # вызвали метод для проверки статус-кода, здесь он ожидается 200
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = result_post.json() #было надо, чтобы ручками не вбивать поля для функции проверки наличия полей
        # print(list(token)) #было надо, чтобы ручками не вбивать поля для функции проверки наличия полей
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Метод GET POST')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)  # вызвали метод для проверки статус-кода, здесь он ожидается 200
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', "Little kittens street, 88")

        print('Метод PUT')
        result_put = GoogleMapsAPI.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)  # вызвали метод для проверки статус-кода, здесь он ожидается 200
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', "Address successfully updated")

        print('Метод GET PUT')
        result_get_put = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get_put,
                                   200)  # вызвали метод для проверки статус-кода, здесь он ожидается 200
        Checking.check_json_token(result_get_put,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get_put, 'address', "Kitten meow-meow street, RU")

        print('Метод DELETE')
        result_delete = GoogleMapsAPI.delete_new_place(place_id)
        Checking.check_status_code(result_delete,
                                   200)  # вызвали метод для проверки статус-кода, здесь он ожидается 200
        Checking.check_json_token(result_delete,
                                  ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Метод GET DELETE')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)  # вызвали метод для проверки статус-кода, здесь он ожидается 404
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word(result_get, 'msg', 'failed')

        print('\033[1m' + 'Тестирование создания, изменения и удаления новой локации прошло успешно!')
