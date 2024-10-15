import sys 
import os

# Get the absolute path to the src directory
src_dir = os.path.dirname(os.path.abspath(__file__))

# Add the src directory to the Python path
sys.path.insert(0, src_dir)

# Now you can import modules from src
from logger import logging
# from src.logger import logging

'''
1) Get information about the computer we're using, 
like what kind of computer it is (Windows, Mac, Linux, etc.)
2)Exit the program
'''
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error) )

    return error_message
   
class CustomException(Exception):
    def __init__(self,error_message,error_datail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_datail)

    def __str__(self):
         return self.error_message

if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("divide by Zero")
        raise CustomException(e,sys)