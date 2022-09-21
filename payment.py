'''subject payment calculator. takes in minutes and returns
payment amount rounded up to the nearest dollar.'''

import math

def subjectPayment():

    payAmount = input('Please enter the amount of time in minutes: ')
    if payAmount == '':
        print('Error. Empty input. Please try again.')
        return
    if payAmount == '0':
        print('Error. Amount cannot be 0 minutes. Please try again.')
        return
    print('Please pay the subject', str(math.ceil(int(payAmount)/60*20)),'Dollars.')

if __name__ == '__main__':
    subjectPayment()
