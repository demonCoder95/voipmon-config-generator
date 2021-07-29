# This module provides all the parameters needed for configuring the client/server installation
# of the VoIP Monitor.
from server_client_params_desc import server_client_param_descriptions, get_description
from params import ConfigParameter

# Creating class objects of the server client parameters
sc_param_server_bind = ConfigParameter("server_bind", "", "", get_description("server_bind"))
sc_param_server_bind_port = ConfigParameter("server_bind_port", 0, 60024, get_description("server_bind_port"))
sc_param_server_password = ConfigParameter("server_password", "", "", get_description("server_password"))

sc_param_server_destination = ConfigParameter("server_destination", "", "", get_description("server_destination"))
sc_param_server_destination_port = ConfigParameter("server_destination_port", 0, 60024, get_description("server_destination_port"))

server_client_params = {
    "server_bind" : sc_param_server_bind,
    "server_bind_port" : sc_param_server_bind_port,
    "server_password" : sc_param_server_password,

    "server_destination" : sc_param_server_destination,
    "server_destination_port" : sc_param_server_destination_port,

}

def total_server_client_params():
    return len(server_client_params)
# Testing
# for each_param in server_client_params:
#     print(each_param + ":\n" + server_client_params[each_param].get_desc())
#     print("Default value: {}\n".format(server_client_params[each_param].get_def_value()))

