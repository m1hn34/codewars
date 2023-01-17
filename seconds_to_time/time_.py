'''
Your task in order to complete this Kata is to write a function which formats a
 duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns
 "now". Otherwise, the duration is expressed as a combination of years, days, 
 hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

'''


def format_duration(seconds):
    result = ''
    time = [31536000, 86400, 3600, 60, 1, ]
    units = [' years', ' days', ' hours', ' minutes', ' seconds', ]
    i = 0
    count = 0

    if seconds == 0:
        return 'now'

    while seconds > 0:
        if (seconds // time[i]) > 1:
            if (seconds % time[i]) > 0:
                result += str(seconds // time[i]) + units[i] + ', '
            elif (seconds % time[i]) == 0 and count > 0:
                result = result.strip()[:-1] + ' and ' + \
                    str(seconds // time[i]) + units[i]
            else:
                result += str(seconds // time[i]) + units[i]
            count += 1

        if (seconds // time[i]) == 1:
            if (seconds % time[i]) > 0:
                result += str(seconds // time[i]) + units[i][:-1] + ', '
            elif (seconds % time[i]) == 0 and count > 0:
                result = result.strip()[:-1] + ' and ' + \
                    str(seconds // time[i]) + units[i][:-1]
            else:
                result += str(seconds // time[i]) + units[i][:-1]
            count += 1

        seconds = seconds % time[i]
        i += 1

    return result


# driver
print(format_duration(1297635))
