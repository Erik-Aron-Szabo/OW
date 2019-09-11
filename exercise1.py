try:
    apple = float(input("How much does is 1kg of apples cost? \n (in korona): "))
    how_much = float(input("How much apples do you want to buy? \n (in kilogramms): "))
    price = apple * how_much
    print(price)
except ValueError:
    print("Invalid input.")
