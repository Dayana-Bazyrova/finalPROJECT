#Базырова Даяна, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import sender_stand_request
import requests



def truck_order_assert():
    track = sender_stand_request.get_new_track()
    return requests.get(configuration.URL_SERVER + configuration.GET_ORDERS + track)
    assert response.truck_order_assert == 200

def test_order():
    truck_order_assert
