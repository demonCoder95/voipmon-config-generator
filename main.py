# VoIP Monitor Configuration Generator v0.1
# Author: Noor
# Date: July 29, 2021
from db_params import db_params
from server_client_params import server_client_params
from pcap_store_params import pcap_store_params
from proto_params import proto_params


def print_parameters(param_list, param_type):
    print("=" * 21 + "{} Configuration Parameters".format(param_type) + "=" * 21)

    for each_entry in param_list:
        print(each_entry + ":\n" + param_list[each_entry].get_desc(), end='')
        print("Default value: {}\n".format(param_list[each_entry].get_def_value()))

    print("=" * 80)
    print("Total {} parameters available are {}.".format(param_type, len(param_list)))
    print("=" * 80 + "\n")


def main():
    print_parameters(db_params, "Database")
    print_parameters(server_client_params, "Server/Client")
    print_parameters(pcap_store_params, "PCAP Store")
    print_parameters(proto_params, "Protocol")


main()
