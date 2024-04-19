import hourtax
import timetobuy
def main():
    #Acquiring some user informations
    print("\n--I present you a program in which your worked days are converted into a currency!--\nProvide some information for the calculions be done.\n\n")
    salary = float(input('What is your salary? '))
    hours = float(input('How many hours do you work a day (or on average)?? '))
    days = float(input('How many days do you work in a month (or on average): '))
    
    #Calculating hour tax
    hour_tax = hourtax.hpaid(salary,hours,days)
    print('That leads us to',hour_tax,'$ per hour\n')
    #Requiring item cost
    item_cost = float(input('How much the thing you wanna buy costs? '))
    #Calculating needed time to buy the item
    amount = timetobuy.timetobuy(item_cost,hour_tax,hours,days)
    print("That's gonna cost you",amount)
    
if __name__=='__main__':
    main()