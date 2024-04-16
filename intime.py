def hpaid(salary:float,hours:float,days:int) -> float:
    # Here we calculate hour tax based on the salary, worked hours and days
    x = days * hours
    hour = salary/x
    if salary <= 0:
        raise ValueError('Salary must be more than 0.')
    else:
        return(round(hour,2))
def timetobuy(item_cost:float,hour_tax:float,hours:float,days:int) -> str:
    # Calculate the amount of time necessary to buy the item based on it's cost
    time_to_buy = item_cost/hour_tax
    
    hours_in_day = hours #hours of work in a day
    days_in_month = days 
    days_in_year = days*12 #Days of work per year

    years = int(time_to_buy // (hours_in_day * days_in_year))
    months = int((time_to_buy % (hours_in_day * days_in_year)) // (hours_in_day * days_in_month))
    days = int(((time_to_buy % (hours_in_day * days_in_year)) % (hours_in_day * days_in_month)) // hours_in_day)
    remaining_hours = int(((time_to_buy % (hours_in_day * days_in_year)) % (hours_in_day * days_in_month)) % hours_in_day)

    if item_cost <= 0:
        print('Item cost must be more than 0.')
    else:
        #return (round(time_to_buy,2))
        result = f"{years} years and {months} months and {days} days and {remaining_hours}"
        return result
        
def main():
    #Acquiring some user informations
    salary = float(input('What is your salary? '))
    hours = float(input('How many hours do you work a day? '))
    days = float(input('For how long(days)? '))
    
    #Calculating hour tax
    hour_tax = hpaid(salary,hours,days)
    print('That leads us with',hour_tax,'$ per hour')
    #Requiring item cost
    item_cost = float(input('How much the thing you wanna buy costs? '))
    #Calculating needed time to buy the item
    hour = timetobuy(item_cost,hour_tax,hours,days)
    print('Thats gonna cost you',hour,'Hours!')
    
if __name__=='__main__':
    main()