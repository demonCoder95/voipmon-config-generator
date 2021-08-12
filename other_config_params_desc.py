
# A helper function to get description of a parameter
def get_description(param):
    return other_config_param_descriptions[param]

# A structure to store all the parameter descriptions
other_config_param_descriptions = {

    # Tunneling configuration options
    "udp_port_tzsp": """This parameter is used to configure tunnelling
detection for the MikroTik TaZman Sniffer Protocol. The standard value
for this is 37008 (0x9090) which enables processing of this protocol.
Set this to 0 to disable processing for this protocol.
This parameter accepts 0 (to disable) and 1-65535 port numbers.\n""",

    "udp_port_l2tp": """This parameter configures the Layer 2 Tunneling
Protocol detection port. The standard value for this is 1701. This can be
configured to 0 to disable processing for this protocol.
This parameter accepts values 0 (to disable) and 1-65535 port numbers.\n""",

    "udp_port_vxlan": """This parameter configures the processing of the
Virtual eXtensible Local Area Network protocol. The standard value of this is
4789. This can be configured to disable processing for this protocol.
This parameter accepts values 0 (to disable) and 1-65535 port numbers.\n""",

    "icmp_process_data": """This parameter enables searching for SIP data in
ICMP Type 3 packets. This is the 'Destination Unreachable' Type which has a
set of 16 codes for different types of unreachability. This is not typically
enabled unless specifically needed.
This parameter accepts values 'yes' and 'no'.\n""",

    # Audiocodes mirroring setup options for tunneling
    "audiocodes": """This parameter enables support for audiocodes in port
mirroring. AudioCodes is a VoIP software vendor which has a portfolio of VoIP
products for enterprises. This is typically disabled, unless you require
audiocodes processing in your traffic.
This parameter accepts values 'yes' and 'no'.\n""",

    "udp_port_audiocodes": """This parameter configures the UDP port to use
for doing audiocodes mirroring.
This parameter accepts port values 1-65535.\n""",

    "tcp_port_audiocodes": """This parameter configures the TCP port to use
for doing audiocodes mirroring.
This parameter accepts port values 1-65535.\n""",

    # Other tunneling options
    "save_ip_from_encaps_ipheader": """This parameter configures saving of the
IP Header information from IP-in-IP encapsulation in the database. This is
typically disabled unless needed.
This parameter accepts values 'yes' and 'no'.\n""",

    "save_ip_from_encaps_ipheader_only_gre": """This parameter configures
saving of the IP Header information from GRE encapsulation in the database.
This is typically disabled unless needed.
This parameter accepts values 'yes' and 'no'.\n""",

    # ====== START OF KAMILIO SETUP PARAMETERS ===============
    # The Kamailio SIP server can be setup with VoIP Monitor to generate SIP
    # traffic that can be forwarded to VoIP Monitor. The details of the setup
    # are given below:
    #
    # The parameters to add to kamailio.cfg are
    # loadmodule "siptrace.so"
    #
    # The module parameters to be set are :
    # modparam("siptrace", "trace_on", 1)
    # modparam("siptrace", "duplicate_uri", "sip:<sniffer_ip>:5888")
    # see the 'kamailio_dstip' param for 'sniffer_ip' field.
    # modparam("siptrace", "trace_to_database", 0)
    # modparam("siptrace", "trace_mode", 4)
    # modparam("siptrace", "xheaders_write", 1)
    # 
    # then put  sip_trace(); in request_route and other routes in kamailio.cfg
    # This will enable sending SIP traffic from the Kamailio server with added
    # headers for tracing. These include:
    #       X-Siptrace-Fromip
    #       X-Siptrace-Toip
    #       X-Siptrace-Time
    #       X-Siptrace-Method
    #       X-Siptrace-Dir
    #  The VoIP Monitor will then process these headers to interpret the
    # incoming data and construct tunneled/virtual UDP packets. This way
    # you can send encrypted data to the VoIP Monitor which removes the
    # trace headers and generates encrypted IP-in-UDP payloads to forward.
    "kamailio_port": """This parameter configures the port number used for
Kamailio server.
This parameter takes port numbers 1-65535.\n""",

    "kamailio_dstip": """This parameter configures the destination IP for the
Kamailio server. This is the IP of the VoIP Monitor sniffer.
This parameter accepts valid IP addresses of a VoIP Monitor sniffer host.\n""",

    "kamailio_srcip": """This parameter configures the source IP for the
Kamailio server. This is the IP address of the Kamailio host itself. This is
an optional parameter and can be skipped, to use the default interface.
This parameter accepts valid IP addresses of a Kamailio server.\n""",
    # ====== END OF KAMILIO SETUP PARAMETERS ===============

    "pcapcommand": """This parameter is used to specify a command that is run
after each PCAP is finished (upon call end). %pcap% can be used as a
substitution for the PCAP filename. Check the 'PCAP store' parameters for more
details on the file name formats. Execution is guaranteed to be serialized.

Note: The PCAP command is run using the 'fork' method which can generate a lot
of Translation Lookaside Buffer (TLB) misses on a multicore system, generating
upto 500,000 interrupts/second. This can result in packet drop. You can
monitor the virtual memory statistics with the folling command:
    
    vmstat 1; watch the column 'in'

This parameter accepts terminal commands, an example is:
    pcapcommand = echo %pcap% >> /tmp/pcap_list\n""",

    "filtercommand": """This paramter is used to specify a script/command that
is run after each PCAP is finished (upon call end). This will apply to any
Capture Rules set in the GUI which are stored in 'filter_ip' and
'filter_telnum' tables in the database.

Note: The filter command/script is run using the 'fork' method which can
generate a lot of Translation Lookaside Buffer (TLB) misses on a multicore
system, generating upto 500,000 interrupts/second. This can result in packet
drop. You can monitor the virtual memory statistics with the folling command:
  
    vmstat 1; watch the column 'in'

This parameter accepts terminal commands, an example is:
    filtercommand = myscript '%callid%' '%dirname%' '%caller%' '%called%'
        '%calldate%'

    Here, the callid, dirname, caller, called, calldate parameter values from
    the CDR are available to the script/command that you write. All
    non-alphanumeric characters except for '/', '#', ' ', '+', ':', '-', '.'
    and '@' are changed to an '_' in the values of these fields.\n""",

    "capture_rules_telnum_file": """This parameter provides the path to the
CSV file that stores the capture rules. These rules are loaded before the 
database rules. The first line of the file must have the appropriate column
name.
This parameter contains path to a CSV file of GUI Capture Rules.\n""",

    "capture_rules_sip_header_file": """This parameter provides the path to
the CSV file that stores the SIP Header capture rules. These rules are loaded
before the database rules. The first line of the file must have the
appropriate column names.
This parameter accepts path to a CSV file of GUI SIP Header Capture Rules.\n""",

    "printinsertid": """This parameter enables printing of CDRID:number to the
STDOUT upon each CDR INSERT in the database.
This parameter accepts values 'yes' and 'no'.\n""",

    "ipaccount": """This parameter enables IP traffic monitoring through IP
accounts. These enable IP based traffic usage analysis which can be used to
perform billing and other analyses as needed.
This parameter accepts values 'yes' and 'no'.\n""",

    "ipaccountport": """This parameter provides the ports for which the IP
accounting has to be enabled. For instace, if set to 80, all the port 80
traffic will be monitored based on IP accounting, and the used IP addresses
for those ports will be monitored and the usage will be recorded. 

This parameter can be specified multiple times to add multiple ports like:
    ipaccountport = 22
    ipaccountport = 80
    ipaccountport = 443
This parameter accepts port values 1-65535.\n""",

    "upgrade_try_http_if_https_fail": """This parameter is used when
upgrading the sniffer through the GUI. It configures usage of HTTP if HTTPS
fails for some reason during the upgrade.
This parameter accepts values 'yes' and 'no'.\n""",

    "curlproxy": """This parameter configures the HTTP proxy to be used when
performing a sniffer upgrade from the GUI.
This parameter accepts proxy like input e-g 'http://192.168.1.10:8080'.\n""",

    # Cannot understand what is the meaning of this sentence in the config
    # #-rpbsN:{file} for read packet in real speed (Read via Packet Buffer 
    # with speed N; N >= 1; 1 for real speed, 2 for speed x2 ...)

    "cloud_activecheck_period": """This parameter is used when using the VoIP
Monitor with 'cloudrouter' configuration in the cloud. It configures the
period for checking VoIP Monitor is active. If you want to disable this check
you can set this value to 0. 
This parameter accepts values in seconds > 0.\n""",


}