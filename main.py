#!/usr/bin/python

import student_grades
import sys

sys.path.append('C:/Users/running.gao/OneDrive - Neato Robotics, Inc/Programming_Study/Python/BIABIA_Python_Practice')
num = 100

def test_scope():
    global num
    print("visit num: ", num)
    print(f'num is:{num}')
    num = 0

def find_prime():
    for num in range(10,20):
        for i in range (2, num):
            if num % i == 0:
                j = num/i
                print('%d equals %d * %d' % (num, i, j))
                break
        else:
                print(num, ' is a prime')

def str_test():
    a = '   Hello World Biabia! AA'
    print(a[:6], 'Python')
    print('H' in a)
    print(a, 'my name is %s with age %d' % ('Biabia', 21))
    print('Return true is string contains only digits and false otherwise. ', a.isdigit())
    print('spilt function:', a.split(' ', 1))
    print('strip function:', a.strip('Biabia! AA'))
    print('strip function:', a.strip())
    print('H' in a)
    long_string = '''  
    /****************************************************************************\
* Copyright (C) 2017 Infineon Technologies & pmdtechnologies ag \n * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
* KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
\t * PARTICULAR PURPOSE.'''
    print(long_string)

def io_interaction():
    x = input('Enter your name:')
    print('Hello, ' + x) 

    
if __name__ == '__main__':
    #test_scope()
    #print(num, 'in main function')
    #find_prime()
    #str_test()
    #student_grades.student_grades() #module calls a function; cannot just call module (no function inside)?
    io_interaction()
