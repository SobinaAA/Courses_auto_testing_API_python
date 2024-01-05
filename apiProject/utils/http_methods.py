import allure
import requests as rq
from utils.logging import Logger
import allure

"""Список HTTP методов"""
class HTTPMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_request(url, "GET")
            result = rq.get(url, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            Logger.add_request(url, "POST")
            result = rq.post(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('PUT'):
            Logger.add_request(url, "PUT")
            result = rq.put(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE'):
            Logger.add_request(url, "DELETE")
            result = rq.delete(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
            Logger.add_response(result)
            return result
