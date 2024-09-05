from datetime import datetime


def convert_date(timestamp_string):
    #Convert String to date-time format
    parsed_date = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S")

    #Collect the relevant information about the formatted string
    minute = parsed_date.minute
    second = parsed_date.second
    month = parsed_date.month
    hour = parsed_date.hour
    year = parsed_date.year
    day = parsed_date.day


    #Initialise the encoded string
    encoded_string= ''

    #Part 1. 

    #Shifts ends at there exact times so any minutes or seconds after will count as the next shift.
    #For this reason, we will make a new system to consider the time stamp.
    time = hour*10000 + minute*100 +second
 
    if (70000<time<=1500000): 
        encoded_string+='A'

    elif 1500000<time<=2300000: 
        encoded_string += 'B'

    else:
        encoded_string += 'C'

    #Part 2
    
    if day<10:
        encoded_string +='0' + str(day)
    else:
        encoded_string += str(day)


    #Part 3 

    new_list = ['A','B','C','D','E','F','G','H','J','K','L','M']

    encoded_string += new_list[month-1]
    
    

    #Part 4
    # done in two ways 
    #Assuming we are working from the year 2000 and we will not be looking at the year 3000 or below 2000
    # encoded_string += str(year%2000)

    #Though, if this code persists for 1000+ years, that might cause some confusion.
    encoded_string += str(year)[-2:]
    #This should work even if we hit quintuple digits in years, but date_time will have to update before that happens.


    print(encoded_string)
    return(encoded_string)


if __name__=='__main__':
    #Input string as a date
    timestamp_string = '2015-01-05 07:00:01'
    convert_date(timestamp_string)
