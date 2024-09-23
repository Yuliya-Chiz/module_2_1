number_first = int(input('Введите первое число:'))
number_second = int(input('Введите второе число:'))
number_third = int(input('Введите третье число:'))
if number_first == number_second and number_second == number_third:
     if number_first == number_third:
          print(3)
elif (number_first == number_second or number_first == number_third) or number_second == number_third:
          print (2)
else:
    print(0)

