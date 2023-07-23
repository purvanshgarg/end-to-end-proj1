import os
import sys
from src.logger import logging


def error_message(error,detail:sys):
    _, _, exc_tb= detail.exc_info()

    file_name= exc_tb.tb_frame.f_code.co_filename

    e_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
        )
    
    return e_message

class CustomException(Exception):
    def __init__(self, e_message, detail:sys):
        super().__init__(e_message)
        self.e_message = error_message(e_message, detail= detail)

    def __str__(self):
        return self.e_message
    

if __name__== "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division By Zero")
        raise CustomException(e, sys)
    