# Charles Weber
# SDEV220
# This code will write to a file and then print the 

# Importing modules
import datetime
import time


# Open    file name  Writing  plc hldr

with open('today.txt','r+') as writeText:
    writeText.write(str(time.ctime()))
    writeText.close()



with open('today.txt','r') as readText:
    readText.read()
    today_string = readText
    readText.close()
    print(today_string)

'''
TTF = open('today.txt','r+')
TTF.write(str(time.ctime()))
r = TTF.read()
print(r)
TTF.close()
'''
