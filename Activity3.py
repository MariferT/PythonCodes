def first_prompt():  # define function first_prompt
    prompt = input('A. Simple Calculator\nB. Simple Salary Calculator\n\nPlease choose (letter only): ')

    if prompt.lower() == 'a':  # lower() ignores the case - it's the same as prompt = A or prompt = a
        simple_calculator()
    elif prompt.lower() == 'b':
        simple_salary_calculation()
    else:
        print('\nInvalid input\n')
        first_prompt()  # this will loop the function


def simple_calculator():
    print('\n\tA. Addition \n\tB. Subtraction \n\tC. Multiplication \n\tD. Division')
    optn = input('Choose 1 operation (letter only): ')

    if optn in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'):  # can also be used to ignore case | includes either values
        while True:
            # float value is both pos and neg real numbers
            try:
                x = float(input('Enter first number: '))
                break
            except ValueError:
                print('Invalid input')
                continue
        while True:
            try:
                y = float(input('Enter second number: '))
                if y == 0 and optn.lower() == 'd':
                    raise ZeroDivisionError
                break
            except ValueError:
                print('Invalid input')
                continue
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                continue

        if optn.lower() == 'a':  # opted to not use functions(return values) in calculating to lessen code
            print('The sum of {} and {1} is {2}' .format(x, y, round(x+y, 3)))
        elif optn.lower() == 'b':
            print('The difference of {0} and {1} is {2}' .format(x, y, round(x-y, 3)))
        elif optn.lower() == 'c':
            print('The product of {0} and {1} is {2}' .format(x, y, round(x*y, 3)))
        elif optn.lower() == 'd':
            print('The quotient of {0} and {1} is {2}' .format(x, y, round(x/y, 3)))

        try_again()

    else:
        print('\nInvalid input')
        simple_calculator()


def try_again():
    while True:
        run = input('Try again? (y/n): ')

        if run.lower() == 'y':
            first_prompt()
            break
        elif run.lower() == 'n':
            print('Thank you.')
            break
        else:
            print('Invalid input')
            continue


def simple_salary_calculation():
    name = input('Employee Name: ')
    while True:
        try:
            hour_count = int(input('Enter number of hours: '))
            if hour_count == 0:  # not using ZeroDivError to shorten code
                print('Can\'t be zero.')
                continue
            break
        except ValueError:
            print('Invalid input')
            continue
    while True:
        try:
            hour_rate = float(input('Enter Rate per Hour: PHP '))
            if hour_rate == 0:
                print('That\'s very illegal!')
                continue
            break
        except ValueError:
            print('Invalid input')
            continue
    while True:
        try:
            sss_cont = float(input('SSS Contribution: PHP '))
            if sss_cont == 0:
                print('All employees must have SSS contribution.')
                continue
            break
        except ValueError:
            print('Invalid input')
            continue
    while True:
        try:
            phil_health = float(input('PhilHealth Contribution: PHP '))
            if phil_health == 0:
                print('All employees must have PhilHealth contribution.')
                continue
            break
        except ValueError:
            print('Invalid input')
            continue
    while True:
        try:
            housing_loan = float(input('Housing loan: PHP '))
            break
        except ValueError:
            print('Invalid input')
            continue

    gross_salary = round(hour_count * hour_rate, 2)

    if 0 <= gross_salary < 10000:  # simplified expression | if gross is greater than or equal to # and lesser than #
        tax = round(gross_salary * 0.05, 2)
    elif 10000 <= gross_salary < 30000:
        tax = round(gross_salary * 0.10, 2)
    elif 30000 <= gross_salary < 70000:
        tax = round(gross_salary * 0.15, 2)
    elif 70000 <= gross_salary < 140000:
        tax = round(gross_salary * 0.20, 2)
    elif 140000 <= gross_salary < 250000:
        tax = round(gross_salary * 0.25, 2)
    elif 250000 <= gross_salary < 500000:
        tax = round(gross_salary * 0.30, 2)
    elif gross_salary >= 500000:
        tax = round(gross_salary * 0.32, 2)
    else:  # to conclude if-else statement
        tax = 0
        print('Cannot compute tax.')

    deductions = round(sss_cont + phil_health + housing_loan + tax, 2)
    net_salary = round(gross_salary - deductions, 2)

    if net_salary > 0:
        cashflow = 'Income'
    else:
        cashflow = 'Loss'

    print(f'''
    ============PAYSLIP============
    =====EMPLOYEE INFORMATION=====
    Employee Name: {name.upper()}
    Rendered Hours: {hour_count}
    Rate per Hour: PHP {hour_rate}
    Gross Salary: PHP {gross_salary}
    ==========DEDUCTIONS==========
    SSS: PHP {round(sss_cont, 2)}
    PhilHealth: PHP {round (phil_health, 2)}
    Other Loan: PHP {round(housing_loan, 2)}
    Tax: {tax}
    Total Deductions: PHP {deductions}
    
    Net Salary ({cashflow}): PHP {net_salary}  
    
    ''')

    try_again()


first_prompt()
