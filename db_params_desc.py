# This module provides parameter descriptions for each configuration parameter

# a simple lookup method to facilitate searching into the descriptions structure
def get_description(param_name):
    return db_param_descriptions[param_name]

# The exhaustive list of descriptions of all parameters
db_param_descriptions = {

    "sqldriver" : """This is the SQL driver used for the database. Can be 'mysql'
or 'odbc'.\n""",

    "cdr_partition_by_hours": """By default, partitions in the CDR table of
the database are created per day. This parameter allows to create
partitions on a hourly basis. This is helpful if CDR inserts/second is
too large and frequent partitioning reduces I/O and CPU usage. Can be 'yes' or
'no'.\n""",

    "query_cache" : """All queries to the database are queued in the program
memory by default. As the database becomes unreachable or busy the queries
start to pile up in the memory, increasing memory usage, which can ultimately
lead to the sniffer crashing. All queued queries are lost. By enabling this
parameter, the queries in the queue are cached onto the disk, which not only
saves memory but also makes the queries persistent to sniffer crashes. This
option can generate I/O pressure, as queries are written on the disk. Can be
'yes', or 'no'.\n""",

    "server_sql_queue_limit" : """In a distributed client/server architecture
of sniffers, where sniffer clients send data to a central sniffer for
processing and storage, this parameter applies. It sets the limit on the
server side, which when reached, prompts the clients to start queuing the
queries locally, and not send them to the central sniffer. This ensures that
the central sniffer doesn't run out of memory, by queuing an abnormally large
amount of queries from clients. It is suggested that the 'query_cache' be
enabled on clients/central sniffer when using a distributed client/server
model for optimal performance. This parameter accepts integer values > 0.\n""",

    "server_sql_concat_limit" : """In a distributed client/server archirtecture
of sniffers, where sniffer clients send data to a central sniffer for
processing and storage, this parameter applies. When there is a significant
Round Trip Time (RTT) between a central sniffer and client, the queries can be
concatenated when sent from the client, to better utilize the bandwidth of the
network. This parameter accepts integer values > 0.\n""",

    "server_sql_redirect_queue_limit" : """In a distributed client/server
architecture, where sniffer clients send data to a central sniffer for
processing and storage, this parameter applies. When using a sniffer server
for SQL redirection purposes (not process queries locally but forward them
to the central sniffer - which could be setup behind a proxy, for instance)
this parameter determines the queue size for the queries that are to be queued
on this redirection server. This is functionally similar to the central server
parameter 'server_sql_queue_limit' and will trigger query queuing on the
client side, if this parameter is exceeded, in an aggregate. This parameter
accepts integer values > 0.\n""",

    "mysqlhost" : """IP address or Hostname of the MySQL server to use. This is
typically an IP address, unless the deployment has a name server configured.\n""",
    
    "mysqlsocket" : """A local UNIX socket for database connection. This is
only applicable when MySQL server is being run locally on the sniffer server.
This form of a connection is faster than the TCP/IP based 'mysqlhost'
connection, so in scenarios of local MySQL this should be preferred. This
parameter usually takes the form similar to  '/var/run/mysqld/mysqld.sock'
which is essentially a socket file accessible to the sniffer.\n""",

    "mysqlport" : """The port number to use for MySQL server connection. This
is typically set to '3306'.\n""",

    "mysqlusername" : """The user for connecting to the MySQL server. This is
typically set to 'root'.\n""",

    "mysqlpassword" : """The password for the user to connect to MySQL server.
This is typically set to ''.\n""",

    "mysqldb" : "Name of the database to be created on the MySQL server.\n",

    "mysqlsslkey" : """If the MySQL server is configured to use SSL encryption
for connectivity, this parameter applies. It specifies the location of the
file containing the SSL Private Key of the client that wishes to connect to the
MySQL server. It can be of the form '/etc/ssl/client-key.pem'.\n""",

    "mysqlsslcert" : """If the MySQL server is configured to use SSL encryption
for connectivity, this parameter applies. It specifies the location of the file
containing the SSL Public Key Certificate of the client that wishes to connect
to the MySQL server. It can be of the form '/etc/ssl/client-cert.pem'.\n""",

    "mysqlsslcacert" : """If the MySQL server is configured to use SSL
encryption for connectivity, this parameter applies. It specifies the location
of the file containing the SSL Certificate Authority Certificate. This is
needed to verify the authenticity of the Public Key Certificate of the client
as specified by the 'mysqlsslcert' parameter. The Public Key certificate must
be signed by the Public Key CA Certificate, otherwise, it is considered
invalid. This parameter can be of the form '/etc/ssl/ca-cert.pem'.\n""",

    "mysqlsslcapath" : """If the MySQL server is configured to use SSL
encryption for connectivity, this parameter applies. It specifies the directory
which contains more then one SSL Certificate Authority certificates for
determining the authenticity of the client's Public Key Certificate as indicated
by 'mysqlsslcert' parameter. This parameter can be of the form '/etc/ssl/capath'
.\n""",

    "mysqlsslciphers" : """This is a colon separated list of ciphers that are
allowed to be used for encrypted connection with the MySQL server. The values
it can contain are 'AES128-SHA' and 'DHE-RSA-AES128-GCM-SHA256'.\n""",

    "quick_save_cdr" : """When CDRs are to be stored in the database. By
default, every write is delayed by approx. 10 seconds. In order to speed up
this process, to reduce delay to 3 seconds, set this to 'yes' and to 1 second,
set this to 'quick'. This parameter has the potential to increase I/O activity
on the storage, so don't use this unless realtime CDR generation is needed.
The values of this parameter can be 'yes', 'no' and 'quick'.\n""",

    "disable_dbupgradecheck" : """When the MySQL service restarts, the tables
in the database are checked and upgraded. This can be disabled if needed in
order to speed up database initialization. The parameter can take values 'yes'
and 'no'.\n""",

    # what happens if this timeout expires? Does the sniffer need to be
    # restarted?
    "mysql_connect_timeout" : """The timeout setting for MySQL database
connection for the sniffer. The parameter accepts values in seconds > 0.\n""",

    "cdr_partition" : """The tables with names 'cdr*' are partitioned on per day
basis by default, if this parameter is enabled. If you have an existing schema
in the database that is not partition based, you MUST drop all tables before
starting the sniffer with this parameter enabled. The parameter can take
values 'yes' and 'no'.\n""",

    "mysql_client_compress" : """The connection with the MySQL server can be
compressed if this parameter is enabled. The compression is governed by a
mutually agreed upon algorithm between the client(sniffer) and the MySQL
server. This causes compression of data when sent to the server. It is only
beneficial when network bandwidth is limited or there is high latency between
the sniffer and the MySQL server. Enabling this parameter causes additional
CPU usage on both the sniffer and the MySQL server since compression and
decompression happens on both sides. This parameter can take values 'yes' and
'no'.\n""",

    "mysqlcompress" : """The table compression in the database is enabled
using this parameter. The data inside tables is written in the backing storage
of the database in the form of data structures called 'pages'. Compressing
these 'pages' can result in efficiency in bandwidth usage of disk I/O since
less data needs to be exchanged with disk as well as saving of disk space. This
is especially beneficial for SSD storage which is typically more expensive than
HDD storage. All of this happens at the cost of increased CPU usage (to
perform compression on write and decompression on read operations). This is
generally acceptable since CPU cost is much less than storage cost, for the
amount of tradeoff incurred.\n""",

    "mysqlcompress_type" : """
When this parameter takes value of 'ROW_FORMAT=COMPRESSED'. This has been the
default compression configuration for earlier releases i.e. MySQL < 5.6 and
MariaDB < 10.1.22. It uses the gzip compression scheme (which is slower as
compared with the lz4 compression - newer). MySQL keeps a buffer pool of the
pages which store recently accessed rows in both compressed and uncompressed 
format, in order to speed up database operations. This data structure is a ring
buffer, where newer entries flush out the older ones, in the limited buffer pool
size. This value can be used if the number of CDR entries/second in the database
is <= 5000. For a rate higher than this, consider the options below.

A recommended configuration for this parameter is 'compression=\"lz4\"'. This
applies when you are using MySQL >= 5.6 as your database. This enables the
much faster InnoDB Page compression using the lz4 algorithm. Which has the
advantage of only storing the uncompressed data in the buffer pool (thereby
increasing pool utilization) as well as lz4 which is a much faster compression
algorithm compared with the older gzip.

If you're using MariaDB >= 10.1.22, as your database instead of MySQL, this
parameter can take a value of 'PAGE_COMPRESSED=1'. This will enable similar
functionality as discussed above for MySQL.

In order to alter your existing database tables to comply with the newer
algorithm scheme, you need to run the following query for all your 'cdr*'
tables in the database:
    ALTER TABLE cdr ROW_FORMAT=dynamic compression=\"lz4\"\n""",

    "mysqlloadconfig" : """Decide whether to load configuration from the
database. The sensor(sniffer) configuration is stored in the database in the
table 'sensor_config'. If this parameter is enabled, the configurations are
pulled from the database. If the 'sensor_id' has not been set, an empty row
will be pulled from the database and the configuration parameters from the
file will overwrite these parameters (since sensor_id = NULL in that case).
The query that runs to fetch the configuration parameters is the following:

(FROM TABLE sensor_conf) BY id_sensor 
(SELECT * FROM sensor_conf WHERE id_sensor = N)

here, N is the 'sensor_id' as configured. This parameter takes values 'yes'
and 'no'.\n""",

    "disable_partition_operations" : """The operations performed to create
partitions in the database (if enabled with 'cdr_partition' parameter) will
be performed every 12 hours by all the sniffers. If there are multiple sniffers
in the deployment and they all write to the same database, there is no need to
have them all perform partitioning. This parameter can be used to disable
partition creation in that case. This parameter takes values 'yes' and 'no.\n""",


    "create_old_partitions" : """If you wish to migrate older data out of your
current database to a backup, or for some other purposes, you can create
partitions of the older data for this purpose. This only works if the database
does not have any tables when the sniffer starts. If tables already exist, the
partitioning parameter will not be in effect. This parameter allows you to set
a partitioning interval, for this purpose. It accepts values in days > 0. A
value of 0 disables this parameter.\n""",

    "create_old_partitions_from" : """Partitioning of older data can be done
on the basis of date specified as well. This parameter accepts a date in the
format YYYY-MM-DD.\n""",

    "sqlcallend" : """If you wish to store the timestamp of 'callend' in the
CDR table, you can use this parameter. This 'callend' is calculated as 
'calldate' + 'duration'. This parameter accepts 'yes' and 'no' values.\n""",

    # Need to study the stored procedures in databases to determine the
    # exact usage of this concept.
    "mysql_enable_newstore" : """There is a built-in MySQL procedure which
performs aggregated storage of queries, named 'store_001'. When enabled, the
queries are passed as arguments to this stored procedure and not directly
applied as 'INSERT' queries. This helps in efficiency when number of new CDRs
per second >= 2000. This parameter accepts values 'yes' and 'per_query'. In
case of 'per_query' the queries are applied directly without being sent to the
stored procedure 'store_001'. For MySQL >= 8, this parameter should be set to
'per_query'.\n""",

    "mysql_enable_set_id" : """This configures the sniffer to generate a unique
'cdr.id' for each CDR record written, which helps coordinate simultaneous inserts
across various 'cdr*' tables through concatenation. If this option is to be
used, you MUST configure all sniffers to send CDR data through a single central
sniffer (client/server model). It is applicable when CDRs per second >= 10000.
This parameter accepts values 'yes' and 'no'.\n""",

    
    # The 'store_001' procedure concatenates multiple queries when sending to the
    # sniffer that writes to the database. This concatenation helps overcome
    # the hard latency limits when CDRs/sec in the DB increases >= 10000. The
    # following parameters help fine tune this procedure for better performance
    # gains.
    "mysqlstore_concat_limit" : """This parameter specifies a general limit on
the number of entries to concatenate when using the 'store_001' procedure for
bundling up queries, when 'mysql_enable_newstore' is being used. This needs
to be tuned to match the CDR/sec load on the database as well as the latency
between the client and server sniffers. This parameter accepts integers > 0
typically in hundreds.\n""",

    "mysqlstore_concat_limit_cdr" : """This parameter specifies the limit
exclusively for the 'cdr' table in the database. When 'mysql_enable_newstore'
is in effect, this parameter determines how many messages to concatenate when
using the 'store_001' procedure. This overrides the general 'mysqlstore_concat_limit'
parameter. This accepts integers > 0 typically in hundreds. You have to fine
tune this parameter depending on the CDR/sec to the database and the network
latency between the client and server sniffers.\n""",

    # The 'message' table in the database populates the SIP Message payloads
    # as they are parsed from the received SIP traffic.

    "mysqlstore_concat_limit_message" : """This parameter specifies the limit
exclusively for the 'message' table in the database. When 'mysql_enable_newstore'
is in effect, this parameter determines how many messages to concatenate when
using the 'store_001' procedure. This overrides the general 'mysqlstore_concat_limit'
parameter. This accepts integers > 0 typically in hundreds. You have to fine
tune this parameter depending on the CDR/sec to the database and the network
latency between the client and server sniffers.\n""",

    "mysqlstore_concat_limit_register" : """This parameter specifies the limit
exclusively for the 'register' table in the database. When 'mysql_enable_newstore'
is in effect, this parameter determines how many messages to concatenate when
using the 'store_001' procedure. This overrides the general 'mysqlstore_concat_limit'
parameter. This accepts integers > 0 typically in hundreds. You have to fine
tune this parameter depending on the CDR/sec to the database and the network
latency between the client and server sniffers.\n""",

    "mysqlstore_concat_limit_http" : """This parameter specifies the limit
exclusively for the 'http' table in the database. When 'mysql_enable_newstore'
is in effect, this parameter determines how many messages to concatenate when
using the 'store_001' procedure. This overrides the general 'mysqlstore_concat_limit'
parameter. This accepts integers > 0 typically in hundreds. You have to fine
tune this parameter depending on the CDR/sec to the database and the network
latency between the client and server sniffers.\n""",

    "mysqlstore_concat_limit_ipacc" : """This parameter specifies the limit
exclusively for the 'ipaccount' table in the database. When 'mysql_enable_newstore'
is in effect, this parameter determines how many messages to concatenate when
using the 'store_001' procedure. This overrides the general 'mysqlstore_concat_limit'
parameter. This accepts integers > 0 typically in hundreds. You have to fine
tune this parameter depending on the CDR/sec to the database and the network
latency between the client and server sniffers.\n""",

    "mysqlstore_limit_queue_register" : """This parameter sets the queue limit
for 'register' table on the server side, when using the client/server method
for deployment of VoIP Monitor. When the number of queries exceeds
this limit, the clients sending CDRs to the central sniffer server start to
queue queries locally. This is done in order to not overrun the central sniffer
with CDRs which can result in the server running out of memory. This parameter
accepts integer values > 0. Typically this is in hundreds of thousands.\n""",

    # The 'innodb_flush_log_trx_commit=2' can lead for a loss of upto 1 sec
    # of transaction committed in the log, in case of a crash. This parameter
    # essentially controls the tradeoff between ACID compliance (atomic
    # trasactions that are guaranteed to be written) and performance tuning
    # where transactions are bundled and flushed out together for better
    # throughput utilization, under high pressures.

    "mysqlstore_max_threads_cdr" : """The number of threads serving the 'cdr'
table queue in the sniffer. For large number of CDRs/sec this needs to be
increased to maintain high processing requirement of queuing queries. On the
server side, you can set the 'innodb_flush_log_at_trx_commit=2', to force
flushing of the 'binary log' of the database to the disk at the end of each
transaction being committed every second. This will ensure queue is being
properly addressed on the server side. Note that this is the max thread count
and there is no guarantee that this count will be maintained throughout. In
fact, new threads are only created if queue_size >= 1000 and these threads
are destroyed, along with the MySQL connection when the queue_size < 1000.
This parameter accepts values 1-9. Values greater than 9 are forced to 9.\n""",

    "mysqlstore_max_threads_message" : """The number of threads serving the
'message' table queue in the sniffer. For large number of CDRs/sec this needs
to be increased to maintain high processing requirement of queuing queries. On
the server side, you can set the 'innodb_flush_log_at_trx_commit=2', to force
flushing of the 'binary log' of the database to the disk at the end of each
transaction being committed every second. This will ensure queue is being
properly addressed on the server side. Note that this is the max thread count
and there is no guarantee that this count will be maintained throughout. In
fact, new threads are only created if queue_size >= 1000 and these threads
are destroyed, along with the MySQL connection when the queue_size < 1000.
This parameter accepts values 1-9. Values greater than 9 are forced to 9.\n""",

    "mysqlstore_max_threads_register" : """The number of threads serving the
'register' table queue in the sniffer. For large number of CDRs/sec this needs
to be increased to maintain high processing requirement of queuing queries. On
the server side, you can set the 'innodb_flush_log_at_trx_commit=2', to force
flushing of the 'binary log' of the database to the disk at the end of each
transaction being committed every second. This will ensure queue is being
properly addressed on the server side. Note that this is the max thread count
and there is no guarantee that this count will be maintained throughout. In
fact, new threads are only created if queue_size >= 1000 and these threads
are destroyed, along with the MySQL connection when the queue_size < 1000.
This parameter accepts values 1-9. Values greater than 9 are forced to 9.\n""",
    
    "mysqlstore_max_threads_http" : """The number of threads serving the 'http'
table queue in the sniffer. For large number of CDRs/sec this needs to be
increased to maintain high processing requirement of queuing queries. On the
server side, you can set the 'innodb_flush_log_at_trx_commit=2', to force
flushing of the 'binary log' of the database to the disk at the end of each
transaction being committed every second. This will ensure queue is being
properly addressed on the server side. Note that this is the max thread count
and there is no guarantee that this count will be maintained throughout. In
fact, new threads are only created if queue_size >= 1000 and these threads
are destroyed, along with the MySQL connection when the queue_size < 1000.
This parameter accepts values 1-9. Values greater than 9 are forced to 9.\n""",

    # Database cleaning parameters
    "cleandatabase_cdr" : """In order to delete partitions of the 'cdr' table,
this parameter can be used. It configures deletion of all partitions of the
table that are older than N days. N can be an integer > 0. Setting this
parameter to 0 disables the cleaning of 'cdr' table.\n""",

    "cleandatabase_rtp_stat" : """In order to delete partitions of the 'rtp_stat'
table, this parameter can be used. It configures deletion of all partitions of
the table that are older than N days. N can be an integer > 0. Setting this
parameter to 0 disables the cleaning of 'rtp_stat' table.\n""",

    "cleandatabase_register_state" : """In order to delete partitions of the
'register_state' table, this parameter can be used. It configures deletion of
all partitions of the table that are older than N days. N can be an integer > 0.
Setting this parameter to 0 disables the cleaning of 'register_state' table.\n""",

    "cleandatabase_register_failed" : """In order to delete partitions of the
'register_failed' table, this parameter can be used. It configures deletion of
all partitions of the table that are older than N days. N can be an integer > 0.
Setting this parameter to 0 disables the cleaning of 'register_failed' table.\n""",

    # The 'sip_msg' stores data parsed from the SIP packets of type 'OPTIONS',
    # 'SUBSCRIBE' and 'NOTIFY'.
    "cleandatabase_sip_msg" : """In order to delete partitions of the 'sip_msg'
table, this parameter can be used. It configures deletion of all partitions of
the table that are older than N days. N can be an integer > 0. Setting this
parameter to 0 disables the cleaning of 'sip_msg' table.\n""",

    "cleandatabase" : """This parameter can be set to control all the
'cleandatabase_*' type of parameters. This is a global setting that is checked
first by the VoIP Monitor. The specific parameters override this global value.
It governs the cleaning interval of the partitions from the 'cdr', 'rtp_stat',
'register_state', 'register_failed' and 'sip_msg' tables. It configures the
VoIP Monitor to delete all partitions in the tables that are older than N days.
N can be an integer > 0. Setting this parameter to 0 disables cleaning of all
the tables mentioned above.\n""",

    "cleandatabase_cdr_rtp_energylevels" : """In order to delete partitions of
the 'cdr_rtp_energylevels' table, this parameter can be used. It configures
deletion of all partitions of the table that are older than N days. N can be
an integer > 0. Setting this parameter to 0 disables the cleaning of
'cdr_rtp_energylevels' table.\n""",

    "cleandatabase_ss7" : """In order to delete partitions of the 'ss7'
table, this parameter can be used. It configures deletion of all partitions of
the table that are older than N days. N can be an integer > 0. Setting this
parameter to 0 disables the cleaning of 'ss7' table.\n""",

    "partition_operations_enable_fromto" : """This parameter is used to control
the scheduling of the cleaning of the database partitions as configured in the
'cleandatabase_*' parameters. Dropping large partitions generates a lot of I/O
and therefor the timings to be set for cleaning should be off-peak hours. This
parameter accepts time ranges in 24-hr format (0 is 12 AM and 23 is 11 PM) e-g
1AM - 5AM will be a value '1-5'.\n""",

    "partition_operations_in_thread" : """This parameter enables partition
operations to be performed in a separate thread. It is recommended not to
configure this parameter unless absolutely required. This parameter takes
values 'yes' and 'no'.\n""",

}

