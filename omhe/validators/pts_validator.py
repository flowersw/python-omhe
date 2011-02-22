import re,sys
from datetime import datetime

from omhe.core.parseomhe import *
from omhe.validators.validator_errors import *
from omhe.validators.utils import *

def pts_validator(omhe_value):
    """validate positive or negative integer"""
    valdict={}
    negative=False
    if omhe_value[0]=="-":
        negative=True
        if omhe_value[1:].isdigit():
            valdict['pts_numeric']=omhe_value
            valdict['points']=omhe_value
        else:
            raise InvalidValueError("You must supply a whole number")
    
    else:
        if omhe_value[1:].isdigit():
            valdict['pts_numeric']=omhe_value
            valdict['points']=omhe_value
        else:
            raise InvalidValueError("You must supply a whole number")
    
    return valdict
