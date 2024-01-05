from utils.http_methods import HTTPMethods

base_url = 'https://rahulshettyacademy.com'  # базовый url Google Maps API
key = "?key=qaclick123"  # параметр для всех запросов Google Maps API

"""Методы для тестирования Google Maps API"""


class GoogleMapsAPI():
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        post_res = "/maps/api/place/add/json"  # ресурс метода POST
        json_for_create_nlocation = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "Little kittens street, 88",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = HTTPMethods.post(base_url + post_res + key, json_for_create_nlocation)
        #print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place(place_id):
        get_res: str = "/maps/api/place/get/json"
        result_get = HTTPMethods.get(base_url + get_res + key + "&place_id=" + place_id)
        #print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""

    @staticmethod
    def put_new_place(place_id):
        put_res: str = "/maps/api/place/update/json"
        json_for_update_nlocation = {"place_id": place_id, "address": "Kitten meow-meow street, RU",
                                     "key": "qaclick123"}  # вставили сразу place_id
        result_put = HTTPMethods.put(base_url + put_res + key, json_for_update_nlocation)
        #print(result_put.text)
        return result_put

    """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):
        del_res: str = "/maps/api/place/delete/json"
        json_for_delete_nlocation = {"place_id": place_id}
        result_del = HTTPMethods.delete(base_url + del_res + key, json_for_delete_nlocation)
        #print(result_del.text)
        return result_del
