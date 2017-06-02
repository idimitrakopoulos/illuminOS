from lib.Stepper import Stepper
from lib.PropertyManager import PropertyManager

profile_properties = PropertyManager("conf/profile.properties")
stepper = Stepper("pstep", 2)



if stepper.get_current_step() == 1:
    print("step 1 code")
    pass
elif stepper.get_current_step() == 2:
    print("step 2 code")
    pass
else:
    pass