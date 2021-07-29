# VoIP Monitor Configuration Generator v0.1
# Author: Noor
# Date: July 29, 2021
from db_params import db_params, total_db_parameters
from server_client_params import server_client_params, total_server_client_params

def main():
    print("="*10 + "Database Configuration Parameters" + "="*10)
    for each_entry in db_params:
        print(each_entry + ":\n" + db_params[each_entry].get_desc())
        print("Default value: {}".format(db_params[each_entry].get_def_value()))

    print("The database parameters available are {}.\n\n".format(total_db_parameters()))

    print("="*10 + "Server/Client Configuration Parameters" + "="*10)
    for each_entry in server_client_params:
        print(each_entry + ":\n" + server_client_params[each_entry].get_desc())
        print("Default value: {}".format(server_client_params[each_entry].get_def_value()))

    print("The server/client parameters available are {}".format(total_server_client_params()))
    
main()