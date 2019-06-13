'''
Created on Jun 13, 2019

@author: BlissI5
'''
import logging
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='a', format='%(asctime)s - %(message)s')
logging.warning('This will get logged to a file')
logging.info('INFO MSG')
logging.debug('Debugg MSG')
logging.warning('warning msg')
logging.critical('critical msg')
logging.error('error msg')
print('log File ')
