def bmi():
    weight = float(input("please input your weight: "))
    hight = float(input("please input your hight in meter: "))

    if hight > 3 :
        raise ValueError("Height can not be more than 3 ")
    return weight/hight**2

print(bmi())

