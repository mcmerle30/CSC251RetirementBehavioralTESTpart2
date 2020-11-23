import datetime
import sys


def social_security_cal():
    while 1:
        b_year = input("\nEnter the year of birth or to exit ")
        if b_year == "":
            sys.exit("Process finished with exit code 0")
        else:
            b_year = int(b_year)
            b_month = int(input("Enter the month of birth "))
            current_year = datetime.datetime.now().strftime("%Y")
            if b_year < 1937 or b_year == 1937 and b_year > 1899:
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1938:
                b_month = 2 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 and 2 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1939:
                b_month = 4 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 and 4 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1940:
                b_month = 6 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 and 6 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1941:
                b_month = 8 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 and 8 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1942:
                b_month = 10 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 65 and 10 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 65))
            elif b_year == 1943 or b_year > 1943 and b_year == 1954 or b_year < 1954:
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1955:
                b_month = 2 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66 and 2 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1956:
                b_month = 4 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66 and 4 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1957:
                b_month = 6 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66 and 6 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1958:
                b_month = 8 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66 and 8 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1959:
                b_month = 10 + b_month
                if b_month > 12:
                    b_month = b_month - 12
                    b_year = b_year + 1
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 66 and 10 months ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 66))
            elif b_year == 1960 or b_year > 1960 and b_year < int(current_year):
                month = datetime.date(1900, b_month, 1).strftime('%B')
                print("your full retirement age is 67 ")
                print("this will be in {} of".format(month) + " {}".format(b_year + 67))

print("Social Security Full Retirement Age Calculator")
c = social_security_cal()