import datetime
import sys



def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def my_func(arg):

	if arg == True:
		print(list(range(0,100,2)))

	elif arg == False:
		print(list(range(1,100,2)))

