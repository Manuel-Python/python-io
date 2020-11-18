import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])

# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have this key" + shelf_key)
#     print(description)

print("*"*80)

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " = " + fruit[f])

print("*"*80)

for f in fruit.values():
    print(f )

print(fruit.values())

for f in fruit.items():
    print(f )

print(fruit.items())

fruit.close()

print(fruit)