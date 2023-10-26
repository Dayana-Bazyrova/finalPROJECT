#Базырова Даяна, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import configuration
import requests



# cоздать заказ
def post_create_orders(body):
   return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDERS,
                        json=body)

# получить заказ по треку
def get_new_track():
    new_order = post_create_orders(data.order_body)
    track_number = new_order.json()['track']
    return track_number





