def menu():
    opt = input('''
                MENU
    A. ODD/EVEN NUMBER CALCULATOR
    B. ROLLER COASTER
    C. BODY MASS INDEX (BMI) CALCULATOR
    D. MULTIPLICATION TABLE
    E. EXIT
        
    Enter option (letter only): ''')
    if len(opt) != 0:  # if the length of the option is not 0 or if input is not empty
        if opt.lower() == 'a':
            print('ODD/EVEN NUMBER CALCULATOR')
            odd_even_calc()
        elif opt.lower() == 'b':
            print('ROLLER COASTER')
            roller_coaster()
        elif opt.lower() == 'c':
            print('BODY MASS INDEX (BMI) CALCULATOR')
            bmi_calc()
        elif opt.lower() == 'd':
            print('MULTIPLICATION TABLE')
            multiplication_tbl()
        elif opt.lower() == 'e':
            exit()
        else:
            print('Input not counted. Please try again.')
            menu()
    else:
        print('Empty input. Please try again.')
        menu()


def odd_even_calc():
    while True:
        try:
            num = int(input('Enter a number: '))
            if (num % 2) == 0:  # if the remainder of the num input divided by 2 is 0 //modulo
                print(f'The number {num} is EVEN.')
            else:
                print(f'The number {num} is ODD.')
            try_again()
            break
        except ValueError:
            print('Invalid input.')
            continue


def roller_coaster():
    while True:
        try:
            hgt = float(input('Enter Height(cm): '))
            if hgt >= 120:
                break
            else:
                print('Sorry, you have to grow taller before you can ride.')
                try_again()
            break
        except ValueError:
            print('Invalid input.')
            continue
    while True:
        try:
            age = int(input('Enter age: '))
            if age >= 0:
                break
            else:
                print('Invalid age. Try again.')
                continue
        except ValueError:
            print('Invalid input.')
            continue

    while True:
        try:
            qty = int(input('Enter number of person/s: '))
            if qty > 0:
                break
            else:
                print('QTY can\'t be lesser than 0. Try again.')
                continue
        except ValueError:
            print('Invalid input.')
            continue

    if 0 <= age <= 3:
        tckt_price = 'FREE'
        total = float(0)
    elif 4 <= age <= 10:
        tckt_price = 100
        total = float(round(qty * tckt_price, 2))
    elif 11 <= age < 18:
        tckt_price = 150
        total = float(round(qty * tckt_price, 2))
    elif 18 <= age <= 120:
        tckt_price = 250
        total = float(round(qty * tckt_price, 2))

    print(f''' 
        ROLLER COASTER SLIP
    ============================
     Height: {hgt} cm
     Age: {age} y/o
     Number of person/s: {qty}
     Ticket Price: {tckt_price}
    
     Total Payment: PHP {total}
    ============================''')
    try_again()


def bmi_calc():
    while True:
        try:
            hgt = float(input('Enter Height(m): '))
            if hgt > 0:
                break
            else:
                print('Invalid height.')
                continue
        except ValueError:
            print('Invalid input.')
            continue
    while True:
        try:
            wgt = float(input('Enter Weight(kg): '))
            if wgt > 0:
                break
            else:
                print('Invalid weight.')
                continue
        except ValueError:
            print('Invalid input.')
            continue
    hgt_sqrd = hgt * hgt
    bmi_val = round(wgt / hgt_sqrd, 2)
    if bmi_val < 18.5:
        bmi = 'UNDERWEIGHT'
    elif 18.5 <= bmi_val < 25:
        bmi = 'NORMAL WEIGHT'
    elif 25 <= bmi_val < 30:
        bmi = 'SLIGHTLY OVERWEIGHT'
    elif 30 <= bmi_val < 35:
        bmi = 'OBESE'
    elif bmi_val > 35:
        bmi = 'CLINICALLY OBESE'

    print(f'A person with a height of {hgt}m and a weight of {wgt}kg is {bmi} with a BMI of {bmi_val}.')
    try_again()


def multiplication_tbl():
    while True:
        try:
            num = int(input('Input a number: '))
            if num != 0:
                for mul in range(11):
                    print(f'\t{num} x {mul} = {num * mul}')
                    continue
            else:
                print('Any number multiplied by zero is equals to zero.')
            try_again()
            break
        except ValueError:
            print('Invalid input.')
            continue


def try_again():
    run = input('Try again? (y/n): ')
    if run.lower() == 'y':
        menu()
    elif run.lower() == 'n':
        print('Thank you.')
        exit()
    else:
        print('Invalid input')
        try_again()


menu()
