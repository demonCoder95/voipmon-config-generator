# Description of all parameters that are needed to configure the server/client setup of sniffers

# =============== PROLOGUE OF SERVER/CLIENT SENSOR ARCHITECTURE ===============
# Since version 19.6, sniffer supports a distributed client/server
# architecture of deployment. Each client or server is also termed as a 'sensor'
# and can be a client or a server. There is only 1 server in this architecture,
# all the rest of the sensors will be clients.

# There is an option to encrypt the communication between the client sensors
# and the server sensor. This is especially beneficial since sensors can be
# remote and the link between them might not be a secure link, especially in
# deployments where the sensors are geographically apart.

# All the client sensors only need to remotely connect with the server sensor.
# For the purposes of a GUI setup, reachability only needs to be configred with
# the server sensor, client sensors need not be directly reachable by the GUI.

# The server sensor handles all the database operations on behalf of the
# clients. In a typical operation, the clients perform all the packet
# processing and store the PCAPs of the data streams in their local spool
# directory. For the database operations, all the INSERT queries are sent to
# the server sensor, which is the only sensor with access to the database.
# Hence, no database configurations are necessary on the client sensors.
# This operation is controlled through client sensor configurations.
# =============================================================================

# a small helper function to lookup descriptions in the data structure below
def get_description(param):
    return server_client_param_descriptions[param]

server_client_param_descriptions = {
    
    # Configurations to be done on the server sensor
    "server_bind" : """The IP address of the server sensor, which has to be
utilized in the socket that will be used to connect to the server.\n""",

    "server_bind_port" : """The TCP/IP port value to be used when binding to
create the socket for the server sensor. This is typically a high value 
> 60000.\n""",

    "server_password" : """A string used as a password when connecting with
the server. This will be utilized by the clients when they connect in order
to secure the communication between the server and client sensors. Therefore,
the same parameter MUST BE a part of the server and the client sensor(s)
configuration files.\n""",

    # Configurations to be done on the client sensor
    "server_destination" : """The IP address of the server that was used in
the binding to create the socket.\n""",

    "server_destination_port" : """The TCP/IP port value that was used in
binding to create a server socket. Typically a value > 60000.\n""",

    # Other parameters
    "packetbuffer_sender" : """This parameter controls whether the client
sensors should process the incoming packets. If set to 'no', they process
the packets locally, store stream (RTP) data in local spool as PCAPs and
forward CDR queries to the server sensor. If set to 'yes', they act only as
traffic mirrors and forward all the raw traffic to the server sensor, without
processing anything. This option is not typically used unless explicitly
required.

If you have 'deduplicate*' parameters configured in the server sensor, you 
will have to copy the identical values for these parameters to both client
sensors and the server sensor if you've set the parameter to 'yes'. Also,
copy the 'use_blocks' parameter value form the server to the client(s) as
well.

Note: In the event of such a configuration, the client sensor(s) sending the
mirrored packet streams are called 'senders' and the server sensor is called
the 'receiver'. This configuration is called a 'mirroring' configuration.\n""",

    # Time difference parameters
    "mirror_connect_maximum_time_diff_s" : """Maximum time difference tolerated
between senders when they are set to forward traffic using the
'packetbuffer_sender' parameter. This parameter accepts values in seconds > 0.

In the event the timeout value is exceeded, the connection between sensors is
terminated and an 'error' level entry in the log is generated which prompts
that the times on sensors to be synchronized, and sensor services to be
restarted.\n""",

    "client_server_connect_maximum_time_diff_s" : """Maximum time difference
tolerated between client(s) and server sensors when they operate. This
parameter accepts values in seconds > 0.

In the event the timeout value is exceeded, the connection between sensors is
terminated and an 'error' level entry in the log is generated which prompts
that the times on sensors to be synchronized, and sensor services to be
restarted.\n""",

    "receive_packetbuffer_maximum_time_diff_s" : """Maximum time difference
tolerated between the receiver of the mirrored packet streams and the sender.
This parameter accepts values in seconds > 0.

In the event the timeout value is exceeded, the connection between sensors is
terminated and an 'error' level entry in the log is generated which prompts
that the times on sensors to be synchronized, and sensor services to be
restarted.\n""",

    "mirror_require_confirmation" : """When mirroring is configured, this
parameter controls the confirmation for each mirrored packet. When the system
is under high pressure, consider disabling this to avoid Round Trip traffic as
well as system resource usage. This parameter can take values 'yes' and 'no'.
""",

    "server_type_compress" : """The connection between the client sensors and
the server sensor can be compressed in order to save bandwidth as well as
overcome large Round Trip delay in the network. All this is done at a cost of
an increase in CPU usage. This parameter determines the compression algorithm
to use (if compression is required). The parameter can take values 'GZIP',
'lzo' and 'no' (meaning no compression).\n""",

}