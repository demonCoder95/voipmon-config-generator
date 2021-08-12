# VoIP Monitor Configuration Generator
# Author: Noor
# Date: July 29, 2021
from db_params import db_params
from server_client_params import server_client_params
from pcap_store_params import pcap_store_params
from proto_params import proto_params
from other_config_params import other_config_params


def print_parameters(param_list, param_type):
    print("=" * 21 + "{} Configuration Parameters".format(param_type) + \
        "=" * 21)

    for each_entry in param_list:
        print(each_entry + ":\n" + param_list[each_entry].get_desc(), end='')
        print("Default value: {}\n".format(
            param_list[each_entry].get_def_value()))

    print("=" * 80)
    print("Total {} parameters available are {}.".format(param_type, 
        len(param_list)))
    print("=" * 80 + "\n")


def main():
    print_parameters(db_params, "Database")
    print_parameters(server_client_params, "Server/Client")
    print_parameters(pcap_store_params, "PCAP Store")
    print_parameters(proto_params, "Protocol")
    print_parameters(other_config_params, "Other Config")

    total_param_count = len(db_params) + len(server_client_params) + \
        len(pcap_store_params) + len(proto_params) + len(other_config_params)

    print("Total parameters in the program database: {}".format(
        total_param_count))


main()
