# This module provides the configuration parameter configurations that are used
# to configure protocol related parameters.

# Helper function for lookup
def get_description(param):
    return proto_params_descriptions[param]

proto_params_descriptions = {
    # parameters starting line 560 in voip-monitor.conf
    "remotepartyid" : """This parameter configures usage of SIP Remote-Party-ID
to get caller name/number from the first SIP INVITE packet. In case of an
anonymous caller, if a value is present in SIP Remote-Party-ID, it will be used
for caller name/number extraction, regardless of the value of this parameter.
This parameter accepts values 'yes' and 'no'.\n""",

    "remoteparty_caller" : """This parameter configures the Remote-Party-ID tag
to use for determining the caller number. Any SIP packet with this tag will
be used for this, not just first SIP INVITE packet. Multiple values can be
provided (with , or ; as separator). An example of setting this would be:
    
    remoteparty_caller = x-cisco-original,caller

This parameter is helpful if your call manager in the system is expected to
insert certain tags in the Remote-Party-ID header, which you can use to make
VoIP Monitor compatible with your system. This parameter is not typically
used.\n""",

    "remoteparty_called" : """This parameter configures the Remote-Party-ID tag
to use for determining the called number. Any SIP packet with this tag will be
used for this, not just first SIP INVITE packet. Multiple values can be
provided (with , or ; as separator). An example of this setting would be:

    remoteparty_called = x-cisco-original,called
    
This parameter is helpful if your Call Manager in the system is expected to
insert certain tags in the Remote-Party-ID header field. This parameter is
not typically used.\n""",

    "passertedidentity" : """This parameter is used to configure SIP
P-Asserted-Identity header field for determining the caller name/number. In
case of anonymous caller, the caller name/number is NOT extracted based on
this header field unless the parameter is specifically enabled. This can be
compared with 'remotepartyid' field.
This parameter accepts values 'yes' and 'no'.\n""",

    "callernum_numberonly" : """Parse only the number and ignore the ID string
after the ;. For example, consider the following header field is presentin the
SIP packet:
    P-Asserted-Identity: <sip: +0001234545;cpc=ordinary@domain;user=phone>
if the parameter is enabled, the identity extracted will only be '+0001234545'.
This is typically enabled, and is helpful in extracting only number from the ID
string.
This parameter accepts values 'yes' and' no'.\n""",

    "ppreferredidentity" : """This parameter is used to configure SIP
P-Preferred-Identity header field for determining the caller name/number. In
case of anonymous caller, the caller name/number is NOT extracted based on this
header field unless the parameter is specifically enabled. This parameter can
be compared with 'remotepartyid' and 'passertedidentity' parameters.
This parameter accepts values 'yes' and 'no'.\n""",

    "remotepartypriority" : """This parameter is used to give priority to the
usage of SIP Remote-Party-ID header field for caller name/number identification.
If this field is enabled, the 'P-Asserted-Identity' and 'P-Preferred-Identity'
headers will be ignored, and only 'Remote-Party-ID' header will be used. 
This parameter accepts values 'yes' and 'no'.\n""",

    "destination_number_mode" : """This parameter provides 2 modes for
determining the called number. The details of these modes is the following:

destination_number_mode = 1 - The called number value is saved from the 'To:'
header from SIP packets.
destination_number_mode = 2 - The called number value is saved from the 
'INVITE URI' SIP packet.

Typically, mode 1 is used. 
This parameter accepts values 1 and 2.\n""",

    "absolute_timeout" : """This parameter is used to set an absolute timeout
for ending calls. In the event the RTP stream is stuck, this timeout is used
to forcely end the calls to stop PCAPs from growing abnormally large and also
saving memory on the sniffer by flushing the data to disk.
If a call is ended by this timeout trigger, the value of 'cdr.bye' column of
the generated CDR record will be 102. This is typically set to 4 hours which
is 4 * 3600 = 14400 seconds.
This parameter accepts values in seconds > 0.\n""",

    "destroy_call_at_bye" : """This parameter is used to set a timeout
for ending calls after SIP BYE is received. This timeout is used to force a
call to end regardless of the amount of RTP packets received, once SIP BYE
has been received. 
This parameter accepts values in seconds > 0.\n""",

    "bye_timeout" : """This parameter is used to set a timeout for ending
calls for which BYE has not been confirmed, and RTP can still be flowing to
increase call length.
This parameter accepts values in seconds > 0.\n""",

    "bye_confirmed_timeout" : """This parameter is used to set a timeout for
ending call for which BYE has been confirmed, yet RTP is still flowing to
increase call length.
This parameter accepts values in seconds > 0.\n""",

    "ignore_rtp_after_bye_confirmed" : """In order to stop RTP processing
once BYE has been confirmed, this parameter can be used. This is typically
set to 'no' to capture all RTP traffic of a call.
This parameter accepts values 'yes' and 'no'.\n""",

    "ignore_rtp_after_cancel_confirmed" : """In order to stop RTP processing
once CANCEL has been confirmed, this parameter can be used. This is typically
set to 'no' to capture all RTP traffic of a call. This SIP method is used in
a scenario where the caller ends the call before the called party has answered
it.
This parameter accepts values 'yes' and 'no'.\n""",

    "get_reason_from_bye_cancel" : """Typically, the 'Reason' header is set
through the SIP BYE or SIP CANCEL packet and the value is not updated with any
subsequent packets in the SIP stream. If you wish to update the 'Reason'
header value from all packets, set this to 'no'.
According to RFC 3326 - Reason Header for SIP, this header can have the
following values:
    for SIP: A SIP status code which specifies the reason for connection
             termination.
    for Q.580: A 'cause' code from the ITU-T Q.580 cause value. This is used
               in SS7 systems.
The 'reason_*' parameters in the 'cdr' table of the database are populated
based on this parameter.
This parameter accepts values 'yes' and 'no'.\n""",

    "detect_alone_bye" : """This parameter allows you to mark CDR entries that
have a BYE packet in a dialog that has 'Transaction does not exist' reply from
a SIP client. This is typically disabled, unless you require to detect SIP BYE
packets from a stream with incomplete transactions.
THis parameter accepts values 'yes' and 'no'.\n""",

    "onewaytimeout" : """This timeout is used to end a SIP call that does not
receive a response within specified number of seconds. This is implemented by
first recording the INVITE/REGISTER source IP address. If within the specified
timeout, there are no more packtes from another source IP address destined to
this IP address, the call will be forced to end. 

If a call is terminated by this timeout, the value in 'cdr.bye' will be 101. 
This timeout serves as a protection against INVITE/REGISTER packet flood with
no replies, and it releases memory quickly by ending the call. 

Also, if there is a misconfiguration in the packet mirroring setup, which
causes only one side of the SIP stream to be forwarded to the monitoring
system, this parameter ensures that the system doesn't run out of memory.
This parameter accepts values in seconds > 0.\n""",

    "sipwithoutrtptimeout" : """This parameter is used to set a timeout to end
a call that has a missig BYE or CANCEL packet, and there is no RTP stream
associated with the call. These calls are called 'zombie calls' and this timeout
helps prevent buildup of zombie calls in memory of the sniffer. 
This parameter accepts values in seconds > 0.\n""",

    "rtptimeout" : """This parameter is used to end a call that has previously
registered RTP activity, but has not received any SIP/RTP/RTCP in the specified
timeout. This is another example of a 'zombie call' and this parameter helps
prevent zombie call buildup in sniffer memory.
This parameter accepts values in seconds > 0.\n""",

    "ringbuffer" : """This parameter controls the size of the kernel's ring
buffer. This data structure is a circular queue in the kernel memory space. It
buffers data and libpcap uses it to send packets to the sniffer for processing. 
Sizing of this parameter depends on the network rate. For a rate > 100Mbps,
this value should be at least 500. Maximum value for this parameter is 2000.
This parameter accepts values in MB > 0.\n""",

    "packetbuffer_enable" : """The packet buffer is used to buffer the packets
in the user space, from the kernel ring buffer (see 'ringbuffer parameter').
This buffer keeps the packets till they are consumed by the process unit in
the sniffer, and this unit can be blocked either by insufficient CPU
availability or by the write buffers being full.
Since sniffer v11, this buffer can be kept small, since write buffers are now
asynchronous and non-blocking. Hence there is a lesser chance of the read
buffers being overflown.
This parameter accepts values 'yes' and 'no'.\n""",

    "packetbuffer_compress" : """The packetbuffer can be configured to
compress the data that it stores, for increased efficiency.
This parameter accepts values 'yes' and 'no'.\n""",

    "packetbuffer_compress_ratio" : """This parameter controls the depth of
compression performed on the packet buffer data. This is typically set to
100, and lowered as needed, according to the available CPU resources.
This parameter accepts percentage values >=0 and <= 100.\n""",

    "max_buffer_mem" : """This parameter controls the maximum memory used
by buffers when I/O or CPU processing blocks packet input. Since sniffer v11,
this parameter replaces the parameters 'packet_buffer_total_maxheap' and 
'pcap_dump_asyncwrite_maxsize'. Typically set to a value of 2000 (for 2GB).
This parameter accepts values in MB > 0.\n""",

    "memory_purge_interval" : """This parameter controls how frequently memory
should be freed. Typically set to 30s.
This parameter accepts values in seconds > 0.\n""",

    "memory_purge_if_release_gt" : """This parameter is used to trigger memory
purging by using the amount of memory to be purged as the criterion. If the
total memory to be purged is greater than this specified limit, the purging
action starts.
This parameter accepts values in MB > 0.\n""",

    "rtpthreads" : """This is the number of threads which will process the RTP
traffic. If not specified, this defaults to the total number of CPU threads
available in the machine. Setting this to 0 disables the multi-threading
functionality for RTP.
This parameter accepts values > 0 and <= max number of CPU threads.\n""",

    "rtpthreads_start" : """This parameter is used to configure the starting
threads for RTP processing. This is only used when a large load of traffic is
provided to the sniffer. If there is insufficient traffic, the starting
threads will still be less than this. This parameter is only used when the
sniffer is being tested by synthetic workloads.
This parameter accepts values > 0 and <= max number of CPU threads.\n""",

    "jitterbuffer_f1" : """This is the first variant of the jitter buffer
variants used by the sniffer to compute Mean Opinion Score (MOS) for call
quality. This is saved into the 'cdr' table in columns *f1. This corresponds
to a fixed jitter buffer size of 50ms.
This parameter accepts values 'yes' and 'no'.\n""",

    "jitterbuffer_f2" : """This is the second variant of the jitter buffer
variants used by the sniffer to compute Mean Opinion Score (MOS) for call
quality. This is saved into the 'cdr' table in columne *f2. This corresponds
to a fixed jitter buffer size of 200ms.
This parameter accepts values 'yes' and 'no'.\n""",

    "jitterbuffer_adapt" : """This is the third variant of the jitter buffer
variants that provides an adaptive simulation of jitter buffer to compute
Mean Opinion Score (MOS) for call quality. This can simulate upto 500ms of a
jitter buffer. A word of caution, this can use a lot of CPU resources.
Therefore, if you observe 100% CPU usage on your sniffer, consider using a
lesser intensive version of the jitterbuffer simulation.
This parameter accepts values 'yes' and 'no'.\n""",

    "ignorertcpjitter" : """This threshold is used to set a value of jitter
in order to normalize the jitter calculations by ignoring abnormal values.
This is useful in cases like DSL/Cable Modems where jitter in initial RTCP
values is an incorrent. This is typically disabled with a value of 0, unless
specifically needed. All the packets with jitter values greater than this are
ignored when calculating Avg/Max values of jitter to be stored into the CDR
table.
This parameter accepts values in ms > 0.\n""",

    "plcdisable" : """This parameter configures the Packet Loss Concealment
(PLC) technique in the VoIP Monitor. In VoIP systems, due to packet switched
nature of the network, packets can arrive out of order, malformed or even be
missing (for instance the server rejected packets due to buffer overflow).
One of the way this technique works is by creating a payload with zeroes to
fill the missing packets of the voice stream. This is typically enabled, by
setting it to 'no'.
This parameter accepts values 'yes' and 'no'.\n""",

    "callslimit" : """This parameter configures the limit of the number of
calls to be processed by VoIP Monitor per second. Calls received, greater
than this number will simply not be processed. New calls are identified by
SIP INVITE packets.
This parameter accepts values > 0.\n""",

    "cdrproxy" : """In case the SIP traffic travels across many SIP proxy
servers, and in cases it DOES NOT cause a change in the 'Call-ID' header of
the packet, this parameter can be used to keep track of all the proxies that
the traffic passes through, and the IP addresses get stores in the database.
These are also searchable through the GUI.
If this parameter is disabled, the 'cdr' table will store the destination IP
from the first SIP INVITE received. It can also overwrite this entry with
data from another SIP INVITE that has the same source IP address. If enabled,
the destination IP will be saved from the latest SIP INVITE packet and the
proxy information will be stored in the 'cdr_proxy' table of the database.
This parameter accepts values 'yes' and 'no'.\n""",

    "cdr_ua_enable" : """This parameter enables saving of User Agent data in
the database. More specifically the 'cdr.a_ua' and 'cdr.b_ua' columns. This is
typically disabled when the User Agent count in the system is > 1000 and the
CDR generation rate is too high and there is insufficient CPU capacity to
process this data.
Note: This parameter is expected to be removed in the future. 
This parameter accepts values 'yes' and 'no'.\n""",

    "cdr_ua_reg_remove" : """This parameter helps remove strings from a User
Agent entry before it is stored in the database. This can be used to remove
unique strings from the entries so that the total size of the table doesn't
grow too large.
This parameter accepts RegEx patterns for matching strings for removal, e-g
    cdr_ua_reg_remove = \([0-9a-z\-]+\)$
    cdr_ua_reg_remove = -RMR[0-9a-z\-]+$\n""",

    "cdr_ua_reg_whitelist" : """This parameter is used to match the User Agent
entries that are whitelisted to be stored in the database. If the parameter
'cdr_ua_reg_remove' is set, it will be processed first, before applying this
filter on the User Agent field. 
This parameter accepts RegEx patterns for matching UA names, e-g
    cdr_ua_reg_whitelist = ^Cisco
    cdr_ua_reg_whitelist = C610\n""",

    "allow-zerossrc" : """This parameter enables processing of RTP packets
with 0 in the SSRC (Source Synchronization) field. This is not allowed by
RFC 3350, therefore this option is typically disabled and such RTP packets
are discarded.
    The Source Synchronization header field was added to RTP to allow RTP
streams to carry data from multiple sources of the same end-point, or from
different endpoints, or from different codecs of the same endpoint. This field
helps identify the source of the data in a shared/mixed RTP stream.
This parameter accepts values 'yes' and 'no'.\n""",

    "deduplicate" : """This parameter enables Message Digest 5 (MD-5) hash
based deduplication logic in the sniffer. If a duplicate hash has been
calculated, that packet will be dropped. 
    Note that MD5 is an expensive operation to perform per packet and can
increase the over computing requirement of the sniffer by 3 times. Therefore,
use this parameter only when you have sufficient resources or with PCAP
generation. This is typically disabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "deduplicate_ipheader_ignore_ttl" : """When performing deduplication as
per the 'deduplicate' parameter, the Time To Live (TTL) field in the IP header
is ignored. If you desire to disable deduplication for varying TTL values of
an otherwise identical packet, you can chose to disable this parameter, which
will disable deduplication for TTL headers. 
This parameter accepts values 'yes' and 'no'.\n""",

    "auto_enable_use_blocks" : """This parameter is used to enable
deduplication and defragmentation logic for packets received from all the
interfaces (if the sniffer has multiple interfaces) or when you have multiple
sniffer receivers setup (in a mirroring setup).
This parameter accepts values 'yes' and 'no'.\n""",

    "deduplicate_ipheader" : """This parameter enables deduplication logic to
utilize the IP header as well.
    Prior to sniffer version 8.0.1, the deduplication logic ignored the IP and
UDP headers and only processed payloads, this allowed missing of a lot of RTP
traffic, therefore, not this parameter is typically enable to allow IP header
based processing to capture all the RTP streams.
This parameter accepts values 'yes' and 'no'.\n""",

    # ===== START OF SIP CONFIGURATION PARAMETERS =======
    
    "sipoverlap" : """This parameter enables the processing of Overlap Dialing
RFC 3578. In this procedure, a partial phone number is used to initiate an SS7
call with an Initial Address Message (IAM), a gateway between the SS7 based
PSTN and a VoIP based SIP network converts this and/or Subsequent Address
Message (SAM)s to generate a SIP INVITE to be routed in the VoIP network. This
can result in multiple SIP INVITEs to have varying 'To:' fields in the header.

When this option is enabled, the database of the CDR is updated upon each
successive 'To:' header field change, in order to support overlap dialing.
However, if you wish to only record the 'To:' field of the first SIP INVITe,
you can disable this parameter.

This parameter accepts values 'yes' and 'no'.\n""",

    "last_dest_number" : """This option is similar to the 'sipoverlap' option
in that it also configures the called/destination number to be processed from
the last SIP INVITE. However the two are different. 'sipoverlap' only updates
the called/destination number when the source IP address of the SIP INVITEs
is the same. However, with 'last_dest_number' the source IP address processing
is not done, and the number is ALWAYS taken from the last SIP INVITE.
This parameter accepts values 'yes' and 'no'.\n""",

    "virtualudppacket" : """The User Datagram Protocol (UDP) is often used to
encapsulate other packets for loadbalancing purposes, since UDP header
processing is the fastest. One of these variants is IP-in-UDP, in which an IP
packet is encapsulated inside a UDP header to allow for faster load balancing
and better bandwidth utilization. When such an encapsulated packet is received
it is important to reconstruct the 'large UDP packet' in order to process the
payload properly as an IP packet. This parameter is used to enable processing
of such IP-in-UDP encapsulation. If you expect such traffic on your network,
enable this parameter.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register": """This parameter enables processing for SIP REGISTER
packets. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-options": """This parameter enables processing of SIP OPTIONS method. 
The OPTIONS method is used in the SIP protocol for a client to query a SIP
server to gather the supported capabilities information.

These can be stored in the active calls (memory), the finished calls
(in the database) or in archived calls (the PCAPs on disk). The parameter can
be configured in the following ways:
    'yes' - active and database storage, PCAP according to 'save-sip-options'
    'nodb' - only active storage, no database storage, PCAP according to
        'save-sip-options'
    'no' - no active/database/PCAP storage, regardless of 'save-sip-options'.

This parameter accepts values 'yes', 'nodb' and 'no'.\n""",

    "save-sip-options": """This parameter enables SIP OPTIONS storage in PCAPs.
See 'sip-options' for more details on SIP OPTIONS. Under heavy load, the I/O
on the sniffer can be loaded significantly, use this with caution.

This parameter can have values 'yes' and 'no'.\n""",

    "sip-subscribe": """This parameter enables processing of SIP SUBSCRIBE
messages. The SIP SUBSCRIBE method is used for a client to 'subscribe' to
the asynchronous 'events' from a SIP server. This is done by establishing a
'dialog' between the SIP client and server. Any subsequent events are sent
to the client as alerts in SIP NOTIFY messages (see 'sip-notify' parameter).
These event types can be statistics information, any parameter change
notifications etc.

This parameter accepts values 'yes', 'nodb' and 'no' as described in
'sip-options' parameter.\n""",

    "save-sip-subscribe": """This parameter enables PCAP storage for SIP
SUBSCRIBE messages. Under heavy load, this can stress the sniffer I/O, so use
this with caution.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-notify": """This parameter enables processing of SIP NOTIFY messages.
SIP NOTIFY messages are used to deliver the asynchronous alerts information
from the SIP server using the dialog established by the SIP SUBSCRIBE method
(see 'sip-subscribe' for details).

This parameter accepts values 'yes', 'nodb' and 'no' as described in
'sip-options' parameter.\n""",

    "save-sip-notify": """This parameter enable PCAP storage for SIP NOTIFY
messages. Under heavy load, this can stress the sniffer I/O, so use this with
caution.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-vlan": """This parameter enables VLAN based SIP
if they are sent on the same VLAN as the SIP request. This forces the SIP
message packets to be on the same VLAN, to be processed by the sniffer. They
are discarded otherwise.

This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-ip-src": """This parameter enables source IP address
as a condition to track packets of the same SIP message. This is typically
enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-ip-dst": """This parameter enables destination IP
address as a condition to track packets of the same SIP message. This is
typically enabled. 

This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-port-src": """This parameter enables source port
number as a condition to track packets of the same SIP message. This is
typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-port-dst": """This parameter enables destination
port number as a condition to track packets of the same SIP message. This is
typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-number-src": """This parameter enables source number
number as a condition to track packets of the same SIP message. This is
typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-number-dst": """This parameter enables destination
number as a condition to track packets of the same SIP message. This is
typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-domain-src": """This parameter enables source domain
as a condition to track packets of the same SIP message. This is typically
enabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-msg-compare-domain-dst": """This parameter enables destination
domain as a condition to track packets of the same SIP message. This is
typically enabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-timeout": """This parameter controls the SIP REGISTER packet
timeout. The sniffer waits for this amount of time for a response, if no
response is received, the entry is deleted from the memory.
This parameter accepts values in seconds > 0.\n""",

    "sip-register-timeout-disable_save_failed": """This parameter is used to
disable storage of REGISTER FAILED messages due to timeout.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-active-nologbin": """The Binary Log (binlog) is a space in
storage that keep track of all the changes made to a database in a format that
allows state update. All instructions/row-changes (depending on binlog format)
are recorded in this log. This can be used in replication setups to ensure
identical global state for all slave nodes.

The 'active' calls are stored in the 'active' table, which is a 'memory' type
table i.e. it is made in memory, and is therefore temporary. In situations
where 'binlog' is enabled, the changes made to this in-memory table will also
be logged into binlog on the disk, which can generate large amounts of I/O.

This parameter allows to skip logging of entries into the 'active' table which
is memory based, and doesn't need logging as a means of optimization. This is
typically enabled.

This parameter accepts values 'yes' and 'no'.\n """,

    "sip-register-ignore-res401": """This parameter allows to ignore the
processing of SIP REGISTER messages where a response code 401 has been
received. This is typically disabled, meaning the 401 response code packets
will be processed by the sniffer. The response code 401 responds to the
HTTP message 'Unauthorized".

This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-ignore-res401-nonce-has-changed": """This parameter allows
to ignore the processing of SIP REGISTER messages with response code of 401.
Additionally, it also checks for a change of 'Nonce' value used in SIP
authentication.
This is typically disabled, meaning the 401 Unauthorized packets with nonce
change condition will be processed by the sniffer.

This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-compare-sipcallerip": """This parameter is used to enable
SIP REGISTER packet identification of same user from different source SIP IP
addresses.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-compare-sipcallerport": """This parameter is used to enable
SIP REGISTER packet identification of same user from different source SIP
ports.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-compare-sipcalledip": """This parameter is used to enable
SIP REGISTER packet identification of same user from different destination SIP
IP addresses.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-compare-sipcalledport": """This parameter is used to enable
SIP REGISTER packet identification of same user from different destination SIP
ports. 
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-compare-to_domain": """This parameter is used to enable SIP
REGISTER packet identification of the same user from domain part of the 'To:'
SIP header.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-state-compare-from_domain": """This parameter is used to
enable SIP REGISTER packet identification of the same user from domain part of
the 'From:' SIP header.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-state-compare-digest_realm": """This parameter is used to
enable SIP REGISTER packet identification of the same user from SIP
Authentication Realm.
This parameter accepts values 'yes' and 'no'\n.""",

    "sip-register-state-compare-contact_num": """This parameter is used to
enable SIP REGISTER packet distinction of a user from number in the 'Contact'
header.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-state-compare-contact_domain": """This parameter is used to
enable SIP REGISTER packet distinction of a user from domain in the 'Contact'
header.
This parameter accepts values 'yes' and 'no'.\n""",

    "sip-register-max-registers": """This parameter configures the maximum
number of SIP REGISTER messages by the same callID without appropriate
response. If this number exceeds, existing REGISTER session is terminated
and a new session is created.
This parameter accepts values > 0.\n""",

    "sip-register-max-messages": """This parameter configures the maximum
number of SIP REGISTER 'packets' by the same CallID without appropriate 
response. If this number exceeds, existing REGISTER session is terminated
and a new session is created.
This parameter accepts values > 0.\n""",

    "cdr_ignore_response": """This parameter is used to skip CDR generation
based on 'Last SIP Response' (LSR). It accepts multiple response codes
delimited by comma. Additionally,
    A single digit response code serves as a wildcard for all response codes
    that start with that digit, i.e. 4 -> 4xx. 
    Other values that the parameter accepts are; name, number, ip and lsr.

Some examples of this parameter configuration are:
    1. cdr_ignore_response = 302,303,4
    2. cdr_ignore_response = 503 lsr=Call\sThrottled
    3. cdr_ignore_response = 403 name=abc ip=1.2.3.4, 404 number=%123%
    4. cdr_ignore_response = 405 number=.*123.* ip=1.2.3.0/24
    etc.\n""",

    "cdr_sip_response_number_max_length": """This parameter is used to strip
the number in a SIP response message. For example, if this is set to 3, for
a SIP response '503 No Service for 12345678' will become '503 No Service for
123'. This is typically disabled unless needed.
This parameter accepts value > 0. Setting to 0 disables this parameter.\n""",

    "cdr_sip_response_reg_remove": """This parameter can be used to remove
certain strings from a SIP response before being stored into the database.
This helps in keeping database to the minimum size, by removing unique string
possibilities from SIP messages.
This parameter accepts RegEx values of the following kind:
    cdr_sip_response_reg_remove = \([0-9a-z\-]+\)$\n""",

    # ===== END OF SIP CONFIGURATION PARAMETERS =======

    "nocdr": """This parameter is used to disble CDR generation in the
database. 
This parameter accepts values 'yes' and 'no'.\n""",

    "skipdefault": """This parameter enables default skipping behavior which
is 'skip all calls'. This can be overwritten by capture rules in the GUI where
you can set IP/Phone Number based skip rules. These rules are stored in the
'filter_*' tables in the database.

This parameter accepts values 'yes' and 'no'.\n""",

    "enable_content_type_application_csta_xml": """This parameter is used to
enable the Computer Supported Telecommunications Applications (CSTA) data +
XML MIME type in the SIP INVITE packets. This is typically disabled, which
means CSTA based payloads are not processed.
This parameter accepts values 'yes' and 'no'.\n""",

    "cdronlyanswered": """This parameter allows CDR generation to only be
done for answered calls. This is typically disabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "cdr_check_exists_callid": """This parameter is used to check CallID of
the generated CDR against the CallID of the existing CDRs stored in the
database. And if an entry exists with the same CallID, replace that entry by
the newly generated CDR if the new one has an RTP stream associated with it.

This is typically the case when using the mirroring mechanism of VoIP Monitor
to forward SIP signalling to RTP media nodes. This results in the RTP nodes
generating additional CDRs that have an associated RTP as well, resulting in
CDR duplication in the database.

For the Client/Server mode of the VoIP Monitor, set this option to 'lock'.
This parameter accepts values 'yes', 'no' and 'lock'.\n""",

    "cdr_check_unique_callid_in_sensors": """This parameter is used to provide
a list of 'sensor_id's where the unique CallID check has to be performed. If
a sensor doesn't have an ID set, use value 'NULL' for it. For insance, this
parameter can be set as:
    cdr_check_unique_callid_in_sensors = 1,3,NULL,5.
This parameter accepts comma separated list of integers > 0 and NULL.\n""",

    "cdronlyrtp": """This parameter is used to confine CDR generation to the
calls that have an associated RTP stream.
This parameter accepts values 'yes' and 'no'.\n""",

    "vlan_siprtpsame": """This parameter is used to configure the sniffer to
use the first SIP packet's VLAN tag to process associated RTP packets. So, it
requires that SIP and associated RTP should be transmitted on the same VLAN.

This is used in situations when different Private Branch Exchange (PBX)
software instanes share an IP address and segregate their traffic based on
VLANs. If this is not configured, the RTP streams are mixed together.
This parameter accepts values 'yes' and 'no'.\n""",

    # ====== START OF SKINNY PROTOCOL PARAMETERS ========
    "skinny": """This parameter is used to enable the 'skinny' protocol.
Also known as Skinny Client Control Protocol (SCCP), is a propriatary protocol
by Cisco. This parameter enables the processing for Cisco Skinny protocol.
This parameter accepts values 'yes' and 'no'.\n""",

    "skinny_port": """The port to use to detect Skinny protocol. This is
typically a value of 2000. Multiple such entries can be added to add extra
Skinny ports, like this:
    
    skinny_port: 2000
    skinny_port: 12000
    etc.

This parameter accepts values in the standard port range of 1-65535.\n""",

    "skinny_ignore_rtpip": """This parameter is used in a scenario where a
Cisco call manager is configured to receive all the calls with the same UDP
port. Additionally, the Cisco phones must also be using the same UDP port
for receiving and sending RTP. This is also referred to as 'Symmetric RTP'.

In this situation, there is a chance of a one-way recording, or of mixed 
ecordings. If this is not desired, providing the Cisco call manager IP address
in this field will allow the sniffer to skip the RTP from this call manager
which very much is mixed up and has only one way recording ability.
This parameter accepts values 'yes' and 'no'.\n""",

    # ====== END OF SKINNY PROTOCOL PARAMETERS =======
    # ====== START OF MGCP PROTOCOL PARAMETERS ========
    "mgcp": """This parameter is used to enable processing for the Media
Gateway Control Protocol (MGCP). It is used to manage signalling and media
traffic in VoIP systems.
This parameter accepts values 'yes' and 'no'.\n""",

    "tcp_port_mgcp_gateway": """This is the TCP port of the MGCP gateway.
This parameter accepts values in the standard port range of 1-65535.\n""",

    "udp_port_mgcp_gateway": """This is the UDP port of the MGCP gateway.
This parameter accepts values in the standard port range of 1-65535.\n""",

    "tcp_port_mgcp_callagent": """This is the TCP port of the Call Agent.
This parameter accepts values in the standard port range of 1-65535.\n""",

    "udp_port_mgcp_callagent": """This is the UDP port of the Call Agent.
This parameter accepts values in the standard port range of 1-65535.\n""",

    # ====== END OF MGCP PROTOCOL PARAMETERS =======
    # ======= END OF PROTOCOL PARAMETERS ===========
}
