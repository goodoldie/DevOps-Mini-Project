# Scientific Calculator Functions
import math as m
import logging

logging.basicConfig(filename='calcy.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def square_root(x):
    if x >= 0:
        ans = m.sqrt(x)
        logging.debug('Square root of {} = {}'.format(x, ans))
        return ans
    else:
        print('Cannot calculate sqrt of Negative Numbers')
        logging.debug('Square Root of {} = Cannot be calculated'.format(x))
        return float(x)


def factorial(x):
    temp = float(x)
    if temp >= 0:
        if temp == float(round(temp)):
            ans = m.factorial(int(temp))
            logging.debug('Factorial of {} = {}'.format(temp, ans))
        else:
            ans = round(temp)
            print("Factorial of Decimals not valid. Converting to Int")
            logging.debug("Fact. of {} invalid as it's Decimal".format(temp))
    else:
        ans = 0.0
        print('Factorial of negative number cannot be calculated')
        logging.debug("Factorial of {} invalid as it's negative".format(x))
    return ans


def natural_log(x):
    temp = float(x)
    if(temp > 0):
        temp = m.log(float(temp))
        logging.debug('Natural Log of {} = {}'.format(x, temp))
    else:
        temp = 0
        logging.debug("{} can't be zero/negative to calculate log".format(x))
    return temp


def power(x, y):
    ans = (x ** y)
    logging.debug('{} to power of {} = {}'.format(x, y, ans))
    return ans
