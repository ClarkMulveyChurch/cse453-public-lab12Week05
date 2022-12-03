########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Nate Duncan, Clark Mulvey
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################
from enum import Enum
# you may need to put something here...
class Control(Enum):
    Public = 1
    Confidential = 2
    Privileged = 3
    Secret = 4

def securityConditionRead(subject, asset):
    if(subject.value >= asset.value):
        return True
    else:
        print("Read Access Denied")
        return False

def securityConditionWrite(subject, asset):
    if(subject.value <= asset.value):
        return True
    else:
        print("Write access denied")
        return False
    
