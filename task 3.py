import requests as rq
import random as rd

class Test_New_Location():
    """Работа с новой локацией"""
    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = 'https://rahulshettyacademy.com'  # базовый юрл
        key = "?key=qaclick123"  # параметр для всех запросов
        post_res = "/maps/api/place/add/json"
        json_for_create_nlocation = {
            "location": {
            "lat": rd.random() * 90,
            "lng": rd.random() * 9
            }, "accuracy": 50,
            "name": "Little Kitten house",
            "phone_number": "(+7) 9090025387",
            "address": "29, little tails",
            "types": [
             "zoo",
            "shop"
             ],
             "website": "meow-meow.com",
            "language": "French-IN"
        }
        result_post = rq.post(base_url + post_res + key, json=json_for_create_nlocation)
        place_id = result_post.json().get("place_id")
        print("Добавляем в файлик: " + place_id)
        with open("id_places.txt", "a") as files:
            files.write(place_id + "\n")

    def test_get_new_location(self, place_id):
        base_url = 'https://rahulshettyacademy.com'  # базовый юрл
        key = "?key=qaclick123"  # параметр для всех запросов
        get_res: str = "/maps/api/place/get/json"
        result_get = rq.post(base_url + get_res + key + "&place_id=" + place_id)
        print("Статус-код при проверке созданной локации: " + str(result_get.status_code))


new_place = Test_New_Location() #создали экземпляр класса
for i in range(0, 5):
    new_place.test_create_new_location() #пять раз создали локацию
with open("id_places.txt", "r") as files:
    fd = files.readlines() #считали файл в список строк
    for line in fd:
        line = line[:-1] #убираем последний символ перевода строки
        new_place.test_get_new_location(line) #выполняем метод для нового id

