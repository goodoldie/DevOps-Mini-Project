# Scientific Calculator Functions
import math as m
import logging

logging.basicConfig(filename='calcy.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def square_root(x):
    return m.sqrt(x)


def factorial(x):
    return m.factorial(x)


def natural_log(x):
    return m.log(x)


def power(x, y):
    return (x ** y)


num1 = 144
num2 = 3
num3 = -4
num4 = 8

sqrt_result = square_root(num1)
logging.debug('Square Root of {} = {}'.format(num1, sqrt_result))

# Un-comment this block to get exception in log
# try:
#     fact_result = factorial(num3)
# except Exception as e:
#     logging.exception("Exception Occured")

fact_result = factorial(num4)
logging.debug('Factorial of {} = {}'.format(num4, fact_result))

ln_result = natural_log(num1)
logging.debug('Natural Log of {} = {}'.format(num1, ln_result))

pow_result = power(num1, num2)
logging.debug('{} Raised to Power {} = {}'.format(num2, num4, sqrt_result))
