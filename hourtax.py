def hpaid(salary:float,hours:float,days:int) -> float:
    # Here we calculate hour tax based on the salary, worked hours and days
    x = days * hours
    hour = salary/x
    if salary <= 0:
        raise ValueError('Salary must be more than 0.')
    else:
        return(round(hour,2))