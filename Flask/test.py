cars = [
    {
        'id': 1,
        'model': 'Mersedes CLK 500',
        'description': "Color - white",

    },
    {
        'id': 2,
        'model': "KIA Sorento",
        'description': "Color - black",

    }
]


print(cars)

for i, val in enumerate(cars):

    if cars[i]["id"] == 2:
        del cars[i]


print(cars)