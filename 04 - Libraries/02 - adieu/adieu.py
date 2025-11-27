import inflect

modifier = inflect.engine()
names = []




while True:
    try:
        names.append(input("Name: "))
    except KeyboardInterrupt:
        break
print(f"Adieu, adieu, to {modifier.join((names))}")