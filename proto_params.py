# This module provides the configuration objects for the protocol based
# parameters. 
from params import ConfigParameter
from proto_param_desc import get_description

# Object definitions for all the configuration objects
proto_param_remote_party_id = ConfigParameter("remotepartyid", "", "no", get_description("remotepartyid"))

# A convenient data structure to bundle all the cofiguration parameter objects
proto_params = {
    "remotepartyid" : proto_param_remote_party_id,
}