# VoIP Monitor Configuration Generator v0.1
# Author: Noor
# Date: July 29, 2021
from db_params import db_params, total_db_parameters

def main():
    print("="*10 + "Database Configuration Parameters" + "="*10)
    for each_entry in db_params:
        print(each_entry + ":\n" + db_params[each_entry].get_desc())
        print("Default value: {}".format(db_params[each_entry].get_def_value()))

    print("The database parameters available are {}".format(total_db_parameters()))

    
main()