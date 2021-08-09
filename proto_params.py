# This module provides the configuration objects for the protocol based
# parameters. 
from typing import no_type_check_decorator
from params import ConfigParameter
from proto_param_desc import get_description

# Object definitions for all the configuration objects
proto_param_remote_party_id = ConfigParameter("remotepartyid", "", "no", get_description("remotepartyid"))
proto_param_remote_party_caller = ConfigParameter("remoteparty_caller", "", "", get_description("remoteparty_caller"))
proto_param_remote_party_called = ConfigParameter("remoteparty_called", "", "", get_description("remoteparty_called"))
proto_param_p_asserted_identity = ConfigParameter("passertedidentity", "", "no", get_description("passertedidentity"))
proto_param_caller_num_number_only = ConfigParameter("callernum_numberonly", "", "yes", get_description("callernum_numberonly"))
proto_param_p_preferred_identity = ConfigParameter("ppreferredidentity", "", "no", get_description("ppreferredidentity"))
proto_param_remote_party_priority = ConfigParameter("remotepartypriority", "", "no", get_description("remotepartypriority"))
proto_param_destination_number_mode = ConfigParameter("destination_number_mode", 0, 1, get_description("destination_number_mode"))
proto_param_absolute_timeout = ConfigParameter("absolute_timeout", 0, 14400, get_description("absolute_timeout"))
proto_param_destroy_call_at_bye = ConfigParameter("destroy_call_at_bye", 0, 1200, get_description("destroy_call_at_bye"))
proto_param_bye_timeout = ConfigParameter("bye_timeout", 0, 1200, get_description("bye_timeout"))
proto_param_bye_confirmed_timeout = ConfigParameter("bye_confirmed_timeout", 0, 600, get_description("bye_confirmed_timeout"))
proto_param_ignore_rtp_after_bye_confirmed = ConfigParameter("ignore_rtp_after_bye_confirmed", "", "no", get_description("ignore_rtp_after_bye_confirmed"))
proto_param_ignore_rtp_after_cancel_confirmed = ConfigParameter("ignore_rtp_after_cancel_confirmed", "", "no", get_description("ignore_rtp_after_cancel_confirmed"))
proto_param_get_reason_from_bye_cancel = ConfigParameter("get_reason_from_bye_cancel", "", "yes", get_description("get_reason_from_bye_cancel"))
proto_param_detect_alone_bye = ConfigParameter("detect_alone_bye", "", "no", get_description("detect_alone_bye"))
proto_param_one_way_timeout = ConfigParameter("onewaytimeout", 0, 15, get_description("onewaytimeout"))
proto_param_sip_without_rtp_timeout = ConfigParameter("sipwithoutrtptimeout", 0, 3600, get_description("sipwithoutrtptimeout"))
proto_param_rtp_timeout = ConfigParameter("rtptimeout", 0, 300, get_description("rtptimeout"))
proto_param_ring_buffer = ConfigParameter("ringbuffer", 0, 50, get_description("ringbuffer"))
proto_param_packet_buffer_enable = ConfigParameter("packetbuffer_enable", "", "yes", get_description("packetbuffer_enable"))
proto_param_packet_buffer_compress = ConfigParameter("packetbuffer_compress", "", "no", get_description("packetbuffer_compress"))
proto_param_packet_buffer_compress_ratio = ConfigParameter("packetbuffer_compress_ratio", 0, 100, get_description("packetbuffer_compress_ratio"))
proto_param_max_buffer_mem = ConfigParameter("max_buffer_mem", 0, 2000, get_description("max_buffer_mem"))
proto_param_memory_purge_interval = ConfigParameter("memory_purge_interval", 0, 30, get_description("memory_purge_interval"))
proto_param_memory_purge_if_release_gt = ConfigParameter("memory_purge_if_release_gt", 0, 500, get_description("memory_purge_if_release_gt"))
proto_param_rtp_threads = ConfigParameter("rtpthreads", None, None, get_description("rtpthreads"))
proto_param_rtp_threads_start = ConfigParameter("rtpthreads_start", None, 1, get_description("rtpthreads_start"))
proto_param_jitter_buffer_f1 = ConfigParameter("jitterbuffer_f1", None, "no", get_description("jitterbuffer_f1"))
proto_param_jitter_buffer_f2 = ConfigParameter("jitterbuffer_f2", None, "yes", get_description("jitterbuffer_f2"))
proto_param_jitter_buffer_adapt = ConfigParameter("jitterbuffer_adapt", None, "no", get_description("jitterbuffer_adapt"))
proto_param_ignore_rtcp_jitter = ConfigParameter("ignorertcpjitter", None, 0, get_description("ignorertcpjitter"))
proto_param_plc_disable = ConfigParameter("plcdisable", None, "no", get_description("plcdisable"))
proto_param_calls_limit = ConfigParameter("callslimit", None, 0, get_description("callslimit"))
proto_param_cdr_proxy = ConfigParameter("cdrproxy", None, "yes", get_description("cdrproxy"))
proto_param_cdr_ua_enable = ConfigParameter("cdr_ua_enable", None, "yes", get_description("cdr_ua_enable"))
proto_param_cdr_ua_reg_remove = ConfigParameter("cdr_ua_reg_remove", None, None, get_description("cdr_ua_reg_remove"))
proto_param_cdr_ua_reg_whitelist = ConfigParameter("cdr_ua_reg_whitelist", None, None, get_description("cdr_ua_reg_whitelist"))
proto_param_allow_zero_ssrc = ConfigParameter("allow-zerossrc", None, "no", get_description("allow-zerossrc"))
proto_param_deduplicate = ConfigParameter("deduplicate", None, "no", get_description("deduplicate"))
proto_param_deduplicate_ipheader_ignore_ttl = ConfigParameter("deduplicate_ipheader_ignore_ttl", None, "yes", get_description("deduplicate_ipheader_ignore_ttl"))
proto_param_auto_enable_use_blocks = ConfigParameter("auto_enable_use_blocks", None, "yes", get_description("auto_enable_use_blocks"))
proto_param_deduplicate_ipheader = ConfigParameter("deduplicate_ipheader", None, "yes", get_description("deduplicate_ipheader"))

    # start of SIP parameters
proto_param_sip_overlap = ConfigParameter("sipoverlap", None, "yes", get_description("sipoverlap"))
proto_param_last_dest_number = ConfigParameter("last_dest_number", None, "no", get_description("last_dest_number"))
proto_param_virtual_udp_packet = ConfigParameter("virtualudppacket", None, "no", get_description("virtualudppacket"))

proto_param_sip_register = ConfigParameter("sip-register", None, "no", get_description("sip-register"))
proto_param_sip_options = ConfigParameter("sip-options", None, "no", get_description("sip-options"))
proto_param_save_sip_options = ConfigParameter("save-sip-options", None, "no", get_description("save-sip-options"))
proto_param_sip_subscribe = ConfigParameter("sip-subscribe", None, "no", get_description("sip-subscribe"))
proto_param_save_sip_subscribe = ConfigParameter("save-sip-subscribe", None, "no", get_description("save-sip-subscribe"))
proto_param_sip_notify = ConfigParameter("sip-notify", None, "no", get_description("sip-notify"))
proto_param_save_sip_notify = ConfigParameter("save-sip-notify", None, "no", get_description("save-sip-notify"))

proto_param_sip_msg_compare_vlan = ConfigParameter("sip-msg-compare-vlan", None, "no", get_description("sip-msg-compare-vlan"))
proto_param_sip_msg_compare_ip_src = ConfigParameter("sip-msg-compare-ip-src", None, "yes", get_description("sip-msg-compare-ip-src"))
proto_param_sip_msg_compare_ip_dst = ConfigParameter("sip-msg-compare-ip-dst", None, "yes", get_description("sip-msg-compare-ip-dst"))
proto_param_sip_msg_compare_port_src = ConfigParameter("sip-msg-compare-port-src", None, "yes", get_description("sip-msg-compare-port-src"))
proto_param_sip_msg_compare_port_dst = ConfigParameter("sip-msg-compare-port-dst", None, "yes", get_description("sip-msg-compare-port-dst"))
proto_param_sip_msg_compare_number_src = ConfigParameter("sip-msg-compare-number-src", None, "yes", get_description("sip-msg-compare-number-src"))
proto_param_sip_msg_compare_number_dst = ConfigParameter("sip-msg-compare-number-dst", None, "yes", get_description("sip-msg-compare-number-dst"))
proto_param_sip_msg_compare_domain_src = ConfigParameter("sip-msg-compare-domain-src", None, "yes", get_description("sip-msg-compare-domain-src"))
proto_param_sip_msg_compare_domain_dst = ConfigParameter("sip-msg-compare-domain-dst", None, "yes", get_description("sip-msg-compare-domain-dst"))

proto_param_sip_register_timeout = ConfigParameter("sip-register-timeout", None, 5, get_description("sip-register-timeout"))
proto_param_sip_register_timeout_disable_save_failed = ConfigParameter("sip-register-timeout-disable_save_failed", None, "no", get_description("sip-register-timeout-disable_save_failed"))
proto_param_sip_register_active_no_log_bin = ConfigParameter("sip-register-active-nologbin", None, "yes", get_description("sip-register-active-nologbin"))
proto_param_sip_register_ignore_res_401 = ConfigParameter("sip-register-ignore-res401", None, "no", get_description("sip-register-ignore-res401"))
proto_param_sip_register_ignore_res_401_nonce_has_changed = ConfigParameter("sip-register-ignore-res401-nonce-has-changed", None, "no", get_description("sip-register-ignore-res401-nonce-has-changed"))

proto_param_sip_register_compare_sip_caller_ip = ConfigParameter("sip-register-compare-sipcallerip", None, "no", get_description("sip-register-compare-sipcallerip"))
proto_param_sip_register_compare_sip_caller_port = ConfigParameter("sip-register-compare-sipcallerport", None, "no", get_description("sip-register-compare-sipcallerport"))
proto_param_sip_register_compare_sip_called_ip = ConfigParameter("sip-register-compare-sipcalledip", None, "no", get_description("sip-register-compare-sipcalledip"))
proto_param_sip_register_compare_sip_called_port = ConfigParameter("sip-register-compare-sipcalledport", None, "no", get_description("sip-register-compare-sipcalledport"))
proto_param_sip_register_compare_to_domain = ConfigParameter("sip-register-compare-to_domain", None, "no", get_description("sip-register-compare-to_domain"))

proto_param_sip_register_state_compare_from_domain = ConfigParameter("sip-register-state-compare-from_domain", None, "no", get_description("sip-register-state-compare-from_domain"))
proto_param_sip_register_state_compare_digest_realm = ConfigParameter("sip-register-state-compare-digest_realm", None, "no", get_description("sip-register-state-compare-digest_realm"))
proto_param_sip_register_state_compare_contact_num = ConfigParameter("sip-register-state-compare-contact_num", None, "yes", get_description("sip-register-state-compare-contact_num"))
proto_param_sip_register_state_compare_contact_domain = ConfigParameter("sip-register-state-compare-contact_domain", None, "yes", get_description("sip-register-state-compare-contact_domain"))
proto_param_sip_register_max_registers = ConfigParameter("sip-register-max-registers", None, 4, get_description("sip-register-max-registers"))
proto_param_sip_register_max_messages = ConfigParameter("sip-register-max-messages", None, 20, get_description("sip-register-max-messages"))

proto_param_cdr_ignore_response = ConfigParameter("cdr_ignore_response", None, None, get_description("cdr_ignore_response"))
proto_param_cdr_sip_response_number_max_length = ConfigParameter("cdr_sip_response_number_max_length", None, None, get_description("cdr_sip_response_number_max_length"))
proto_param_cdr_sip_response_reg_remove = ConfigParameter("cdr_sip_response_reg_remove", None, None, get_description("cdr_sip_response_reg_remove"))
    # End of SIP parameters

proto_param_no_cdr = ConfigParameter("nocdr", None, "no", get_description("nocdr"))
proto_param_skip_default = ConfigParameter("skipdefault", None, "no", get_description("skipdefault"))
proto_param_enable_content_type_application_csta_xml = ConfigParameter("enable_content_type_application_csta_xml", None, "no", get_description("enable_content_type_application_csta_xml"))
proto_param_cdr_only_answered = ConfigParameter("cdronlyanswered", None, "no", get_description("cdronlyanswered"))
proto_param_cdr_check_exists_call_id = ConfigParameter("cdr_check_exists_callid", None, None, get_description("cdr_check_exists_callid"))
proto_param_cdr_check_unique_call_id_in_sensors = ConfigParameter("cdr_check_unique_callid_in_sensors", None, None, get_description("cdr_check_unique_callid_in_sensors"))
proto_param_cdr_only_rtp = ConfigParameter("cdronlyrtp", None, "no", get_description("cdronlyrtp"))
proto_param_vlan_sip_rtp_same = ConfigParameter("vlan_siprtpsame", None, "no", get_description("vlan_siprtpsame"))

    # Start of Skinny Parameters
proto_param_skinny = ConfigParameter("skinny", None, "no", get_description("skinny"))
proto_param_skinny_port = ConfigParameter("skinny_port", None, 2000, get_description("skinny_port"))
proto_param_skinny_ignore_rtp_ip = ConfigParameter("skinny_ignore_rtpip", None, None, get_description("skinny_ignore_rtpip"))

    # Start of MGCP Parameters
proto_pram_mgcp = ConfigParameter("mgcp", None, None, get_description("mgcp"))
proto_param_tcp_port_mgcp_gateway = ConfigParameter("tcp_port_mgcp_gateway", None, 2427, get_description("tcp_port_mgcp_gateway"))
proto_param_udp_port_mgcp_gateway = ConfigParameter("udp_port_mgcp_gateway", None, 2427, get_description("udp_port_mgcp_gateway"))
proto_param_tcp_port_mgcp_call_agent = ConfigParameter("tcp_port_mgcp_callagent", None, 2727, get_description("tcp_port_mgcp_callagent"))
proto_param_udp_port_mgcp_call_agent = ConfigParameter("udp_port_mgcp_callagent", None, 2727, get_description("udp_port_mgcp_callagent"))

    # End of protocol processing parameters


# A convenient data structure to bundle all the cofiguration parameter objects
proto_params = {
    "remotepartyid": proto_param_remote_party_id,
    "remoteparty_caller": proto_param_remote_party_caller,
    "remoteparty_called": proto_param_remote_party_called,
    "passertedidentity": proto_param_p_asserted_identity,
    "callernum_numberonly": proto_param_caller_num_number_only,
    "ppreferredidentity": proto_param_p_preferred_identity,
    "remotepartypriority": proto_param_remote_party_priority,
    "destination_number_mode": proto_param_destination_number_mode,
    "absolute_timeout": proto_param_absolute_timeout, 
    "destroy_call_at_bye": proto_param_destroy_call_at_bye,
    "bye_timeout": proto_param_bye_timeout,
    "bye_confirmed_timeout": proto_param_bye_confirmed_timeout,
    "ignore_rtp_after_bye_confirmed": proto_param_ignore_rtp_after_bye_confirmed,
    "ignore_rtp_after_cancel_confirmed": proto_param_ignore_rtp_after_cancel_confirmed,
    "get_reason_from_bye_cancel": proto_param_get_reason_from_bye_cancel,
    "detect_alone_bye": proto_param_detect_alone_bye,
    "onewaytimeout": proto_param_one_way_timeout,
    "sipwithoutrtptimeout": proto_param_sip_without_rtp_timeout,
    "rtptimeout": proto_param_rtp_timeout,
    "ringbuffer": proto_param_ring_buffer,
    "packetbuffer_enable": proto_param_packet_buffer_enable,
    "packetbuffer_compress": proto_param_packet_buffer_compress,
    "packetbuffer_compress_ratio": proto_param_packet_buffer_compress_ratio,
    "maxbuffer_mem": proto_param_max_buffer_mem,
    "memory_purge_interval": proto_param_memory_purge_interval,
    "memory_purge_if_release_gt": proto_param_memory_purge_if_release_gt,
    "rtpthreads": proto_param_rtp_threads,
    "rtpthreads_start": proto_param_rtp_threads_start,
    "jitterbuffer_f1": proto_param_jitter_buffer_f1,
    "jitterbuffer_f2": proto_param_jitter_buffer_f2,
    "jitterbuffer_adapt": proto_param_jitter_buffer_adapt,
    "ignorertcpjitter": proto_param_ignore_rtcp_jitter,
    "plcdisable": proto_param_plc_disable,
    "callslimit": proto_param_calls_limit,
    "cdrproxy": proto_param_cdr_proxy,
    "cdr_ua_enable": proto_param_cdr_ua_enable,
    "cdr_ua_reg_remote": proto_param_cdr_ua_reg_remove,
    "cdr_ua_reg_whitelist": proto_param_cdr_ua_reg_whitelist,
    "allow-zerossrc": proto_param_allow_zero_ssrc,
    "deduplicate": proto_param_deduplicate,
    "deduplicate_ipheader_ignore_ttl": proto_param_deduplicate_ipheader_ignore_ttl,
    "auto_enable_use_blocks": proto_param_auto_enable_use_blocks,
    "deduplicate_ipheader": proto_param_deduplicate_ipheader,

    # Start of SIP parameters
    "sipoverlap": proto_param_sip_overlap,
    "last_dest_number": proto_param_last_dest_number,
    "virtualudppacket": proto_param_virtual_udp_packet,
    "sip-register": proto_param_sip_register,
    "sip-options": proto_param_sip_options,
    "save-sip-options": proto_param_save_sip_options,
    "sip-subscribe": proto_param_sip_subscribe,
    "save-sip-subscribe": proto_param_save_sip_subscribe,
    "sip-notify": proto_param_sip_notify,
    "save-sip-notify": proto_param_save_sip_notify,

    "sip-msg-compare-vlan": proto_param_sip_msg_compare_vlan,
    "sip-msg-compare-ip-src": proto_param_sip_msg_compare_ip_src,
    "sip-msg-compare-ip-dst": proto_param_sip_msg_compare_ip_dst,
    "sip-msg-compare-port-src": proto_param_sip_msg_compare_port_src,
    "sip-msg-compare-port-dst": proto_param_sip_msg_compare_port_dst,
    "sip-msg-compare-number-src": proto_param_sip_msg_compare_number_src,
    "sip-msg-compare-number-dst": proto_param_sip_msg_compare_number_dst,
    "sip-msg-compare-domain-src": proto_param_sip_msg_compare_domain_src,
    "sip-msg-compare-domain-dst": proto_param_sip_msg_compare_domain_dst,

    "sip-register-timeout": proto_param_sip_register_timeout,
    "sip-register-timeout-disable_save_failed": proto_param_sip_register_timeout_disable_save_failed,
    "sip-register-active-nologbin": proto_param_sip_register_active_no_log_bin,
    "sip-register-ignore-res401": proto_param_sip_register_ignore_res_401,
    "sip-register-ignore-res401-nonce-has-changed": proto_param_sip_register_ignore_res_401_nonce_has_changed,

    "sip-register-compare-sipcallerip": proto_param_sip_register_compare_sip_caller_ip,
    "sip-register-compare-sipcallerport": proto_param_sip_register_compare_sip_caller_port,
    "sip-register-compare-sipcalledip": proto_param_sip_register_compare_sip_called_ip,
    "sip-register-compare-sipcalledport": proto_param_sip_register_compare_sip_called_port,
    "sip-register-compare-to_domain": proto_param_sip_register_compare_to_domain,

    "sip-register-state-compare-from_domain": proto_param_sip_register_state_compare_from_domain,
    "sip-register-state-compare-digest_realm": proto_param_sip_register_state_compare_digest_realm,
    "sip-register-state-compare-contanct_num": proto_param_sip_register_state_compare_contact_num,
    "sip-register-state-compare-contact_domain": proto_param_sip_register_state_compare_contact_domain,
    "sip-register-max-registers": proto_param_sip_register_max_registers,
    "sip-register-max-messages": proto_param_sip_register_max_messages,

    "cdr_ignore_response": proto_param_cdr_ignore_response,
    "cdr_sip_response_number_max_length": proto_param_cdr_sip_response_number_max_length,
    "cdr_sip_response_reg_remove": proto_param_cdr_sip_response_reg_remove,

    # end of SIP parameters
    "nocdr": proto_param_no_cdr,
    "skipdefault": proto_param_skip_default,
    "enable_content_type_application_csta_xml": proto_param_enable_content_type_application_csta_xml,
    "cdronlyanswered": proto_param_cdr_only_answered,
    "cdr_check_exists_callid": proto_param_cdr_check_exists_call_id,
    "cdr_check_unique_callid_in_sensors": proto_param_cdr_check_unique_call_id_in_sensors,
    "cdronlyrtp": proto_param_cdr_only_rtp,
    "vlan_siprtpsame": proto_param_vlan_sip_rtp_same,

    "skinny": proto_param_skinny,
    "skinny_port": proto_param_skinny_port,
    "skinny_ignore_rtpip": proto_param_skinny_ignore_rtp_ip,

    "mgcp": proto_pram_mgcp,
    "tcp_port_mgcp_gateway": proto_param_tcp_port_mgcp_gateway,
    "udp_port_mgcp_gateway": proto_param_udp_port_mgcp_gateway,
    "tcp_port_mgcp_callagent": proto_param_tcp_port_mgcp_call_agent,
    "udp_port_mgcp_callagent": proto_param_udp_port_mgcp_call_agent,

}