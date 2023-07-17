import os
import pickle
import numpy as np
import pandas as pd
from django.shortcuts import render


price=""



with open("Model/model.pickle", "rb") as f:
    model = pickle.load(f)

input_format = ['ambassador', 'audi', 'bentley', 'bmw', 'chevrolet', 'datsun', 'fiat',
                'force', 'ford', 'honda', 'hyundai', 'isuzu', 'jaguar', 'jeep',
                'lamborghini', 'land', 'mahindra', 'maruti', 'mercedes-benz', 'mini',
                'mitsubishi', 'nissan', 'porsche', 'renault', 'skoda', 'tata', 'toyota',
                'volkswagen', 'volvo', 'Year', 'Kilometers_Driven', 'Mileage', 'Engine',
                'Power', 'Seats', 'CNG', 'Diesel', 'LPG', 'Petrol', 'Automatic',
                'Manual', 'First', 'Fourth & Above', 'Second', 'Third']

cars = ['ambassador', 'audi', 'bentley', 'bmw', 'chevrolet', 'datsun', 'fiat',
        'force', 'ford', 'honda', 'hyundai', 'isuzu', 'jaguar', 'jeep',
        'lamborghini', 'land', 'mahindra', 'maruti', 'mercedes-benz', 'mini',
        'mitsubishi', 'nissan', 'porsche', 'renault', 'skoda', 'tata', 'toyota',
        'volkswagen', 'volvo']

other_features = ['Year', 'Kilometers_Driven', 'Mileage', 'Engine',
                  'Power', 'Seats']

fuel_type = ['CNG', 'Diesel', 'LPG', 'Petrol']

transmission_type = ['Automatic', 'Manual']

user = ['First', 'Second', 'Third', 'Fourth & Above']

context = {
    'cars': cars,
    'Seats': [2, 4, 5, 7, 8],
    "fuel_type": fuel_type,
    "transmission_type": transmission_type,
    "users": user,
    "price": str(price)
}


def index(request):
    global price,model

    return render(request,"index.html",context)



def predict_price(request):

    global price,model

    car = str(request.POST["car"])
    year = request.POST["year"]
    Kilometers_Driven = request.POST["Kilometers_Driven"]
    Mileage = request.POST["Mileage"]
    engine_v = request.POST["Engine_cc"]
    power = request.POST["power"]
    Seat = request.POST["Seat"]
    fuel = str(request.POST["fuel"])
    transmission = str(request.POST["transmission"])
    user_value = str(request.POST["user"])

    cars_f = np.zeros(len(cars))
    other_f = np.zeros(len(other_features))
    fuel_f = np.zeros(len(fuel_type))
    transmission_f = np.zeros(len(transmission_type))
    users_f = np.zeros(len(user))

    try:

        if int(year)>0 and int(Kilometers_Driven)>0 and int(Mileage)>0 and int(engine_v)>0 and int(power)>0 and int(Seat)>0:

            cars_f[cars.index(car)]=1
            other_f[0]=-2023-int(year)
            other_f[1] =int(Kilometers_Driven)
            other_f[2] =int(Mileage)
            other_f[3] =int(engine_v)
            other_f[4] =int(power)
            other_f[5] =int(Seat)
            fuel_f[fuel_type.index(fuel)]=1
            transmission_f[transmission_type.index(transmission)]=1
            users_f[user.index(user_value)]=1

            input_f=np.concatenate((cars_f, other_f, fuel_f, transmission_f, users_f), axis=None)

            price=model.predict([input_f])[0]

            price=f"Predicted price {str(price)}"

    except:
        price=""
        pass

    context = {
        'cars': cars,
        'Seats': [2, 4, 5, 7, 8],
        "fuel_type": fuel_type,
        "transmission_type": transmission_type,
        "users": user,
        "price": price
    }

    return render(request, "index.html", context)


























# def home(request):
#     elements = ['Element 1', 'Element 2', 'Element 3', 'Element 4']
#     context = {
#         'elements': elements
#     }
#
#     return render(request,"home.html",context)
#
# def new(request):
#     elements = ['Element 1', 'Element 2', 'Element 3', 'Element 4']
#     context = {
#         'elements': elements
#     }
#
#     return render(request, "home.html", context)
#
#
# def add(request):
#     n1=int(request.POST["num1"])
#     n2=int(request.POST["num2"])
#     sum=n1+n2
#     return render(request,"answer.html",{"answer":sum})
#
#
# def selection_form(request):
#     elements = ['Element 1', 'Element 2', 'Element 3', 'Element 4']  # Your list of elements
#
#     if request.method == 'POST':
#         selected_element = request.POST.get('element')
#     context = {
#         'elements': elements
#     }
#
#     return render(request, 'your_app/selection_form.html', context)
#
#
# def show(request):
#     n = request.POST["element"]
#
#     return render(request,"answer.html",{"answer":n})