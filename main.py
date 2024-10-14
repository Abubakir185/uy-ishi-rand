men = ["Ivan", "Aleksey", "Ali", "Tom"]
women = ["Anna", "Ketrin", "Mariya"]

def rand_name():
    import random
    name = random.choice(men + women)
    return name


print(rand_name())
print(rand_name())
print(rand_name())