# This module provides configuration parameters that are used for general
# configuration of the VoIP Monitor and don't necessarily belong to any
# other category.
from os import get_blocking
from params import ConfigParameter
from other_config_params_desc import get_description

# parameter objects for all the config parameters
oc_param_udp_port_tzsp = ConfigParameter("udp_port_tzsp", None, 37008, get_description("udp_port_tzsp"))
oc_param_udp_port_l2tp = ConfigParameter("udp_port_l2tp", None, 1701, get_description("udp_port_l2tp"))
oc_param_udp_port_vxlan = ConfigParameter("udp_port_vxlan", None, 4789, get_description("udp_port_vxlan"))
oc_param_icmp_process_data = ConfigParameter("icmp_process_data", None, "no", get_description("icmp_process_data"))
oc_param_audio_codes = ConfigParameter("audiocodes", None, "no", get_description("audiocodes"))
oc_param_udp_port_audio_codes = ConfigParameter("udp_port_audiocodes", None, 925, get_description("udp_port_audiocodes"))
oc_param_tcp_port_audio_codes = ConfigParameter("tcp_port_audiocodes", None, 925, get_description("tcp_port_audiocodes"))
oc_param_save_ip_from_encaps_ip_header = ConfigParameter("save_ip_from_encaps_ipheader", None, "no", get_description("save_ip_from_encaps_ipheader"))
oc_param_save_ip_from_encaps_ip_header_only_gre = ConfigParameter("save_ip_from_encaps_ipheader_only_gre", None, "no", get_description("save_ip_from_encaps_ipheader_only_gre"))

# Kamailio SIP tracing configuration parameters
oc_param_kamailio_port = ConfigParameter("kamailio_port", None, 5888, get_description("kamailio_port"))
oc_param_kamailio_dstip = ConfigParameter("kamailio_dstip", None, None, get_description("kamailio_dstip"))
oc_param_kamailio_srcip = ConfigParameter("kamailio_srcip", None, None, get_description("kamailio_srcip"))

oc_param_pcap_command = ConfigParameter("pcapcommand", None, None, get_description("pcapcommand"))
oc_param_filter_command = ConfigParameter("filtercommand", None, None ,get_description("filtercommand"))
oc_param_capture_rules_telnum_file = ConfigParameter("capture_rules_telnum_file", None, None, get_description("capture_rules_telnum_file"))
oc_param_capture_rules_sip_header_file = ConfigParameter("capture_rules_sip_header_file", None, None, get_description("capture_rules_sip_header_file"))
oc_param_print_insert_id = ConfigParameter("printinsertid", None, "yes", get_description("printinsertid"))
oc_param_ip_account = ConfigParameter("ipaccount", None, "no", get_description("ipaccount"))
oc_param_ip_account_port = ConfigParameter("ipaccountport", None, None, get_description("ipaccountport"))
oc_param_upgrade_try_http_if_https_fail = ConfigParameter("upgrade_try_http_if_https_fail", None, "yes", get_description("upgrade_try_http_if_https_fail"))
oc_param_curl_proxy = ConfigParameter("curlproxy", None, None, get_description("curlproxy"))
oc_param_cloud_active_check_period = ConfigParameter("cloud_activecheck_period", None, 60, get_description("cloud_activecheck_period"))


other_config_params = {
    "udp_port_tzsp": oc_param_udp_port_tzsp,
    "udp_port_l2tp": oc_param_udp_port_l2tp,
    "udp_port_vxlan": oc_param_udp_port_vxlan,
    "icmp_process_data": oc_param_icmp_process_data,
    "audiocodes": oc_param_audio_codes,
    "udp_port_audiocodes": oc_param_udp_port_audio_codes,
    "tcp_port_audiocodes": oc_param_tcp_port_audio_codes,
    "save_ip_from_encaps_ipheader": oc_param_save_ip_from_encaps_ip_header,
    "save_ip_from_encaps_ipheader_only_gre": oc_param_save_ip_from_encaps_ip_header_only_gre,

    "kamailio_port": oc_param_kamailio_port,
    "kamailio_dstip": oc_param_kamailio_dstip,
    "kamailio_srcip": oc_param_kamailio_srcip,

    "pcapcommand": oc_param_pcap_command,
    "filtercommand": oc_param_filter_command,
    "capture_rules_telnum_file": oc_param_capture_rules_telnum_file,
    "capture_rules_sip_header_file": oc_param_capture_rules_sip_header_file,
    "printinsertid": oc_param_print_insert_id,
    "ipaccount": oc_param_ip_account,
    "ipaccountport": oc_param_ip_account_port,
    "upgrade_try_http_if_https_fail": oc_param_upgrade_try_http_if_https_fail,
    "curlproxy": oc_param_curl_proxy,
    "cloud_activecheck_period": oc_param_cloud_active_check_period,
    

}