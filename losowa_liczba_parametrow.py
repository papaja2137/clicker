# def black_hole(*args):
#     print(args)

# black_hole(1, 2, 3, "Piotrek", "Milana")

# def black_hole_named(**kwargs):
#     print(kwargs)

# black_hole_named(name="Maciek", age="13", city="Wrocław")

def black_hole_mixed(zmienna, *args, **kwargs):
    print("Pierwszy argument: ", zmienna)
    print("Dodatkowe elementy: ", args)
    print("Argumenty nazwane: ", kwargs)

black_hole_mixed(1, 2, 3, 4, 5, 6, 7, 8, name="Szymon", age="14")    