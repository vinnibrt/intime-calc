def timetobuy(item_cost:float,hour_tax:float,hours:float,days:int) -> str:
    # Calculate the amount of time necessary to buy the item based on it's cost
    time_to_buy = item_cost/hour_tax
    minutes = 60 * hours
    hours_in_day = hours #hours of work in a day
    days_in_month = days 
    days_in_year = days*12 #Days of work per year

    years = int(time_to_buy // (hours_in_day * days_in_year))
    months = int((time_to_buy % (hours_in_day * days_in_year)) // (hours_in_day * days_in_month))
    days = int(((time_to_buy % (hours_in_day * days_in_year)) % (hours_in_day * days_in_month)) // hours_in_day)
    remaining_hours = int(((time_to_buy % (hours_in_day * days_in_year)) % (hours_in_day * days_in_month)) % hours_in_day)
    minutes = int(((((time_to_buy % (hours_in_day * days_in_year)) % (hours_in_day * days_in_month)) % hours_in_day - remaining_hours) * 60))


    if item_cost <= 0:
        print('Item cost must be more than 0.')
    else:
        #return (round(time_to_buy,2))
        result = f"{years} years, {months} months, {days} days, {remaining_hours} hours and {minutes} minutes."
        return result
        