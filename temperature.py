
'''
    You are given a list of temperature readings in Celsius for a week. Your task is to implement a function that calculates and returns the average temperature for the week. To achieve this, you will use the accumulator pattern to accumulate the sum of temperatures and then calculate the average.

    Input

    A list temperatures containing n floating-point numbers representing the temperature readings for the week.
    (1 <= n <= 7, -20 <= temperatures[i] <= 40)
    
    Input Example
    temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0]

    Output

    A single floating-point number representing the calculated average temperature.
    Example Output
    22.357142857142858

'''

from typing import List
# temperatures = [20.5, 22.0, 18.5, 25.5, 26.0, 23.5, 19.0]

def calculate_average_temperature(temperatures: List[float]) -> float:
     # 1.1 TODO: # Initialize an accumulator variable to keep track of the sum of temperatures.
    # temperatures = []
    # accum = 0

    # if len(temperatures) == 0:
    #     return 'Nothing can be done'

    accum = 0

    # try:
    #     for temps in temperatures:
    #     accum += temps
    # except ZeroDivisionError:
    #     return 'Nothing can be done'
    
    # print(accum)
    ''' Paul's complicated attempt'
    temperatures.append(0)
    # average_temp = ((sum(temperatures)) / (len(temperatures)-1))
    while len(temperatures) <9:
        today = float(input('What is the temp today?\n To stop enter 1111 '))
        # temperatures.append(today)
        if today <=-20 and today <=40:
            temperatures.append(today)
            continue
        else:
            # print((sum(temperatures)-1111) / (len(temperatures)-2))
            # average_temp = ((sum(temperatures)-1111) / (len(temperatures)-2))
            # return average_temp
            print(temperatures[1:len(temperatures)])
            break
    def average_temp():
        return print((sum(temperatures)) / (len(temperatures)-1))
    average_temp()
    ''' 
    
    # 1.2 TODO:# Iterate through the `temperatures` list, updating the accumulator with the current temperature.
    try:
        for temps in temperatures:
            accum += temps
    except ZeroDivisionError:
        print('Nothing can be done')

    # 1.3 TODO: # Calculate and return the average temperature using the accumulated sum and the total number of readings.

    try:
        mean_temp = accum/len(temperatures)
        return mean_temp 
    except ZeroDivisionError:
        print('nothing can be done')

    # 1.3 TODO: return the average temperature

# calculate_average_temperature(temperatures = [20.0, 15.0, 11.0])
