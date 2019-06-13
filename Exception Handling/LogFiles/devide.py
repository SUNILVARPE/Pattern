'''
Created on Jun 13, 2019

@author: BlissI5
'''
import logging 
logging.basicConfig(level=logging.DEBUG,filename='new.log', filemode='a', format='%(asctime)s - %(message)s')

x=int(input('Enter The No'))
if x!=0:
    logging.error('Error')
else:
   print('zero')