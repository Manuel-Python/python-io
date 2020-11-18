import shelve

# with shelve.open('ShelfTest') as fruit:
# fruit = shelve.open('ShelfTest')
with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])
# fruit.close()

    print(fruit)


with shelve.open("bike2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    # del bike['engin_size']

    for key in bike:
        print(key)

    print('=' * 40)

    print(bike["engine_size"])
    # print(bike["engin_size"]) remove incorrect key
    print(bike["colour"])
