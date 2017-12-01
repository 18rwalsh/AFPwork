#create a main function that runs when this file is executed
def main():
    print('Hello')
    print('This program will ask you for a temperature in fahrenheit')
    print('_________________________________________________________')
    val = int(input('Enter a value: '))
    cel = ftoc(val)
    print('{0} Fahrenheit = {1:.2f} Celcius'.format(val,cel))

#create a function to convert farenheight to celcius
def ftoc(fah):
    cel = (fah-32)*5/9
    return cel
#----------------------------------------------------------------------------------#

#create a function
def calc():
    print('This program will calculate speed in mph to kph')
    print('--------------------------------------------------------------')
    speed = int(input('Enter a value: '))
    kph = m2k(speed)
    print('{0} Miles per Hour = {1:.2f} Kilometres per Hour'.format(speed,kph))

#mph to kph
def m2k(mph):
    kph = mph*1.60934
    return kph
#---------------------------------------------------------------------------------#
def calc2():
    print('This program will convert USD to AUD')
    print('--------------------------------------------------------------')
    usd = int(input('Enter a value: '))
    aud = u2a(usd)
    print('{0} USD = {1:.2f} Aud'.format(usd, aud))

#mph to kph
def u2a(usd):
    aud = usd*1.318317
    return aud
#---------------------------------------------------------------------------------#

def menu():
    choice = '0'
    while choice == '0':
        print("1: Fahrenheit to Celcius")
        print("2: Miles to Kilometers")
        print("3: USD to Aud")
        print('4: To Quit')
        choice = input("Please make a choice: ")
        #quits
        if choice == "4":
            print("Quitting.. ")
            break
        #run USD to AUD Calculator
        elif choice == "3":
            calc2()
            menu()
        #run mph to kmph Calculator
        elif choice == "2":
            calc()
            menu()
        #run Fahrenheit to Celcius Calculator
        elif choice == "1":
            main()
            menu()
        else:
            print("I don't understand your choice.")
            menu()
menu()