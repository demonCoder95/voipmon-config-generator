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
has been received. """


}

