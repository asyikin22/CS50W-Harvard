# provide another way to create functions in python

things = [
    {"color": "red", "weather": "hot"},
    {"color": "blue", "weather": "cold"},
    {"color": "orange", "weather": "mild"}
]

#def f(thing):
#    return thing["weather"]

things.sort(key=lambda thing: thing["color"])

print(things)
