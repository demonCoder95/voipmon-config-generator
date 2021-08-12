# This provides a list of all the DB Configuration Params
from params import ConfigParameter
from db_params_desc import get_description

# Creating configuration parameter objects for each parameter
db_param_sqldriver = ConfigParameter("sqldriver", "", "mysql", get_description("sqldriver"))
db_param_cdr_partition_by_hours = ConfigParameter("cdr_partition_by_hours", "", "no", get_description("cdr_partition_by_hours"))
db_param_query_cache = ConfigParameter("query_cache", "", "no", get_description("query_cache"))
db_param_server_sql_queue_limit = ConfigParameter("server_sql_queue_limit", 0, 0, get_description("server_sql_queue_limit"))
db_param_server_sql_concat_limit = ConfigParameter("server_sql_concat_limit", 0, 1000, get_description("server_sql_concat_limit"))
db_param_server_sql_redirect_queue_limit = ConfigParameter("server_sql_redirect_queue_limit", 0, 0, get_description("server_sql_redirect_queue_limit"))

db_param_mysql_host = ConfigParameter("mysqlhost", "", "", get_description("mysqlhost"))
db_param_mysql_socket = ConfigParameter("mysqlsocket", "", "", get_description("mysqlsocket"))
db_param_mysql_port = ConfigParameter("mysqlport", 0, 3306, get_description("mysqlport"))
db_param_mysql_username = ConfigParameter("mysqlusername", "", "root", get_description("mysqlusername"))
db_param_mysql_password = ConfigParameter("mysqlpassword", "", "", get_description("mysqlpassword"))
db_param_mysql_db = ConfigParameter("mysqldb", "", "voipmonitor", get_description("mysqldb"))

db_param_mysql_ssl_key = ConfigParameter("mysqlsslkey", "", "", get_description("mysqlsslkey"))
db_param_mysql_ssl_cert = ConfigParameter("mysqlsslcert", "", "", get_description("mysqlsslcert"))
db_param_mysql_ssl_cacert = ConfigParameter("mysqlsslcacert", "", "", get_description("mysqlsslcacert"))
db_param_mysql_ssl_capath = ConfigParameter("mysqlsslcapath", "", "", get_description("mysqlsslcapath"))
db_param_mysql_ssl_ciphers = ConfigParameter("mysqlsslciphers", "", "", get_description("mysqlsslciphers"))

db_param_quick_save_cdr = ConfigParameter("quick_save_cdr", "", "no", get_description("quick_save_cdr"))
db_param_disable_db_upgrade_check = ConfigParameter("disable_dbupgradecheck", "", "no", get_description("disable_dbupgradecheck"))
db_param_mysql_connect_timeout = ConfigParameter("mysql_connect_timeout", 0, 60, get_description("mysql_connect_timeout"))
db_param_cdr_partition = ConfigParameter("cdr_partition", "", "yes", get_description("cdr_partition"))
db_param_mysql_client_compress = ConfigParameter("mysql_client_compress", "", "no", get_description("mysql_client_compress"))
db_param_mysql_compress = ConfigParameter("mysqlcompress", "", "yes", get_description("mysqlcompress"))
db_param_mysql_compress_type = ConfigParameter("mysqlcompress_type", "", "ROW_FORMAT=COMPRESSED", get_description("mysqlcompress_type"))

db_param_mysql_load_config = ConfigParameter("mysqlloadconfig", "", "yes", get_description("mysqlloadconfig"))
db_param_disable_partition_operations = ConfigParameter("disable_partition_operations", "", "no", get_description("disable_partition_operations"))
db_param_create_old_partitions = ConfigParameter("create_old_partitions", 0, 90, get_description("create_old_partitions"))
db_param_create_old_partitions_from = ConfigParameter("create_old_partitions_from", "", "", get_description("create_old_partitions_from"))
db_param_sql_call_end = ConfigParameter("sqlcallend", "", "yes", get_description("sqlcallend"))
db_param_mysql_enable_new_store = ConfigParameter("mysql_enable_newstore", "", "per_query", get_description("mysql_enable_newstore"))
db_param_mysql_enable_set_id = ConfigParameter("mysql_enable_set_id", "", "no", get_description("mysql_enable_set_id"))

# Sniffer SQL queues tuning parameters
db_param_mysql_store_concat_limit = ConfigParameter("mysqlstore_concat_limit", 0, 400, get_description("mysqlstore_concat_limit"))
db_param_mysql_store_concat_limit_cdr = ConfigParameter("mysqlstore_concat_limit_cdr", 0, 400, get_description("mysqlstore_concat_limit_cdr"))
db_param_mysql_store_concat_limit_message = ConfigParameter("mysqlstore_concat_limit_message", 0, 400, get_description("mysqlstore_concat_limit_message"))
db_param_mysql_store_concat_limit_register = ConfigParameter("mysqlstore_concat_limit_register", 0, 400, get_description("mysqlstore_concat_limit_register"))
db_param_mysql_store_concat_limit_http = ConfigParameter("mysqlstore_concat_limit_http", 0, 400, get_description("mysqlstore_concat_limit_http"))
db_param_mysql_store_concat_limit_ipaccount = ConfigParameter("mysqlstore_concat_limit_ipacc", 0, 400, get_description("mysqlstore_concat_limit_ipacc"))
db_param_mysql_store_limit_queue_register = ConfigParameter("mysqlstore_limit_queue_register", 0, 1000000, get_description("mysqlstore_limit_queue_register"))

db_param_mysql_store_max_threads_cdr = ConfigParameter("mysqlstore_max_threads_cdr", 0, 1, get_description("mysqlstore_max_threads_cdr"))
db_param_mysql_store_max_threads_message = ConfigParameter("mysqlstore_max_threads_message", 0, 1, get_description("mysqlstore_max_threads_message"))
db_param_mysql_store_max_threads_register = ConfigParameter("mysqlstore_max_threads_register", 0, 1, get_description("mysqlstore_max_threads_register"))
db_param_mysql_store_max_threads_http = ConfigParameter("mysqlstore_max_threads_http", 0, 1, get_description("mysqlstore_max_threads_http"))


# Database cleaning parameters
db_param_clean_database_cdr = ConfigParameter("cleandatabase_cdr", 0, 0, get_description("cleandatabase_cdr"))
db_param_clean_database_rtp_stat = ConfigParameter("cleandatabase_rtp_stat", 0, 2, get_description("cleandatabase_rtp_stat"))
db_param_clean_database_register_failed = ConfigParameter("cleandatabase_register_failed", 0, 0, get_description("cleandatabase_register_failed"))
db_param_clean_database_register_state = ConfigParameter("cleandatabase_register_state", 0, 0, get_description("cleandatabase_register_state"))
db_param_clean_database_sip_msg = ConfigParameter("cleandatabase_sip_msg", 0, 0, get_description("cleandatabase_sip_msg"))
db_param_clean_database = ConfigParameter("cleandatabase", 0, 0, get_description("cleandatabase"))
db_param_clean_database_cdr_rtp_energylevels = ConfigParameter("cleandatabase_cdr_rtp_energylevels", 0, 0, get_description("cleandatabase_cdr_rtp_energylevels"))
db_param_clean_database_ss7 = ConfigParameter("cleandatabase_ss7", 0, 0, get_description("cleandatabase_ss7"))

db_param_partition_operations_enable_from_to = ConfigParameter("partition_operations_enable_fromto", "", "", get_description("partition_operations_enable_fromto"))
db_param_partition_operations_in_thread = ConfigParameter("partition_operations_in_thread", "", "no", get_description("partition_operations_in_thread"))

# Database backup parameters
db_param_database_backup_from_date = ConfigParameter("database_backup_from_date", None, None, get_description("database_backup_from_date"))
db_param_database_backup_to_date = ConfigParameter("database_backup_to_date", None, None, get_description("database_backup_to_date"))
db_param_database_backup_from_mysqlhost = ConfigParameter("database_backup_from_mysqlhost", None, None, get_description("database_backup_from_mysqlhost"))
db_param_database_backup_from_mysqldb = ConfigParameter("database_backup_from_mysqldb", None, None, get_description("database_backup_from_mysqldb"))
db_param_database_backup_from_mysqlusername = ConfigParameter("database_backup_from_mysqlusername", None, None, get_description("database_backup_from_mysqlusername"))
db_param_database_backup_from_mysqlpassword = ConfigParameter("database_backup_from_mysqlpassword", None, None, get_description("database_backup_from_mysqlpassword"))
db_param_database_backup_pause = ConfigParameter("database_backup_pause", None, 300, get_description("database_backup_pause"))
db_param_database_backup_insert_threads = ConfigParameter("database_backup_insert_threads", None, 1, get_description("database_backup_insert_threads"))

# Database backup SSL/TLS parameters
db_param_database_backup_from_mysql_ssl_key = ConfigParameter("database_backup_from_mysqlsslkey", None, None, get_description("database_backup_from_mysqlsslkey"))
db_param_database_backup_from_mysql_ssl_cert = ConfigParameter("database_backup_from_mysqlsslcert", None, None, get_description("database_backup_from_mysqlsslcert"))
db_param_database_backup_from_mysql_ssl_cacert = ConfigParameter("database_backup_from_mysqlsslcacert", None, None, get_description("database_backup_from_mysqlsslcacert"))
db_param_database_backup_from_mysql_ssl_capath = ConfigParameter("database_backup_from_mysqlsslcapath", None, None, get_description("database_backup_from_mysqlsslcapath"))
db_param_database_backup_from_mysql_ssl_ciphers = ConfigParameter("database_backup_from_mysqlsslciphers", None, None, get_description("database_backup_from_mysqlsslciphers"))

db_param_database_backup_pass_rows = ConfigParameter("database_backup_pass_rows", None, 10000, get_description("database_backup_pass_rows"))
db_param_database_backup_desc_dir = ConfigParameter("database_backup_desc_dir", None, "no", get_description("database_backup_desc_dir"))
db_param_database_backup_skip_register = ConfigParameter("database_backup_skip_register", None, "no", get_description("database_backup_skip_register"))

# A convenient data structure to iterate over DB configuration parameters
db_params = {
    "sqldriver" : db_param_sqldriver,
    "cdr_partition_by_hours" : db_param_cdr_partition_by_hours,
    "query_cache" : db_param_query_cache,
    "server_sql_queue_limit" : db_param_server_sql_queue_limit,
    "server_sql_concat_limit" : db_param_server_sql_concat_limit,
    "server_sql_redirect_queue_limit" : db_param_server_sql_redirect_queue_limit,
    
    "mysqlhost" : db_param_mysql_host,
    "mysqlsocket" : db_param_mysql_socket,
    "mysqlusername" : db_param_mysql_username,
    "mysqlpassword" : db_param_mysql_password,
    "mysqldb" : db_param_mysql_db,

    "mysqlsslkey" : db_param_mysql_ssl_key,
    "mysqlsslcert" : db_param_mysql_ssl_cert,
    "mysqlsslcacert" : db_param_mysql_ssl_cacert,
    "mysqlsslcapath" : db_param_mysql_ssl_capath,
    "mysqlsslciphers" : db_param_mysql_ssl_ciphers,

    "quick_save_cdr" : db_param_quick_save_cdr,
    "disable_dbupgradecheck" : db_param_disable_db_upgrade_check,
    "mysql_connect_timeout" : db_param_mysql_connect_timeout,
    "cdr_partition" : db_param_cdr_partition,
    "mysql_client_compress" : db_param_mysql_client_compress,
    "mysqlcompress" : db_param_mysql_compress,
    "mysqlcompress_type" : db_param_mysql_compress_type,

    "mysqlloadconfig" : db_param_mysql_load_config,
    "disable_partition_operations" : db_param_disable_partition_operations,
    "create_old_partitions" : db_param_create_old_partitions,
    "create_old_partitions_from" : db_param_create_old_partitions_from,
    "sqlcallend" : db_param_sql_call_end,
    "mysql_enable_newstore" : db_param_mysql_enable_new_store,

    "mysqlstore_concat_limit" : db_param_mysql_store_concat_limit,
    "mysqlstore_concat_limit_cdr" : db_param_mysql_store_concat_limit_cdr,
    "mysqlstore_concat_limit_message" : db_param_mysql_store_concat_limit_message,
    "mysqlstore_concat_limit_register" : db_param_mysql_store_concat_limit_register,
    "mysqlstore_concat_limit_http" : db_param_mysql_store_concat_limit_http,
    "mysqlstore_concat_limit_ipacc" : db_param_mysql_store_concat_limit_ipaccount,
    "mysqlstore_limit_queue_register" : db_param_mysql_store_limit_queue_register,

    "mysqlstore_max_threads_cdr" : db_param_mysql_store_max_threads_cdr,
    "mysqlstore_max_threads_message" : db_param_mysql_store_max_threads_message,
    "mysqlstore_max_threads_register" : db_param_mysql_store_max_threads_register,
    "mysqlstore_max_threads_http" : db_param_mysql_store_max_threads_http,

    "cleandatabase_cdr" : db_param_clean_database_cdr,
    "cleandatabase_rtp_stat" : db_param_clean_database_rtp_stat,
    "cleandatabase_register_state" : db_param_clean_database_register_state,
    "cleandatabase_register_failed" : db_param_clean_database_register_failed,
    "cleandatabase_sip_msg" : db_param_clean_database_sip_msg,
    "cleandatabase" : db_param_clean_database,
    "cleandatabase_cdr_rtp_energylevels" : db_param_clean_database_cdr_rtp_energylevels,
    "cleandatabase_ss7" : db_param_clean_database_ss7,

    "partition_operations_enable_fromto" : db_param_partition_operations_enable_from_to,
    "partition_operations_in_thread" : db_param_partition_operations_in_thread,

    # Database backup parameters
    "database_backup_from_date": db_param_database_backup_from_date,
    "database_backup_to_date": db_param_database_backup_to_date,
    "database_backup_from_mysqlhost": db_param_database_backup_from_mysqlhost,
    "database_backup_from_mysqldb": db_param_database_backup_from_mysqldb,
    "database_backup_from_mysqlusername": db_param_database_backup_from_mysqlusername,
    "database_backup_from_mysqlpassword": db_param_database_backup_from_mysqlpassword,
    "database_backup_pause": db_param_database_backup_pause,
    "database_backup_insert_threads": db_param_database_backup_insert_threads,
    "database_backup_from_mysqlsslkey": db_param_database_backup_from_mysql_ssl_key,
    "database_backup_from_mysqlsslcert": db_param_database_backup_from_mysql_ssl_cert,
    "database_backup_from_mysqlsslcacert": db_param_database_backup_from_mysql_ssl_cacert,
    "database_backup_from_mysqlsslcapath": db_param_database_backup_from_mysql_ssl_capath,
    "database_backup_from_mysqlsslciphers": db_param_database_backup_from_mysql_ssl_ciphers,
    "database_backup_pass_rows": db_param_database_backup_pass_rows,
    "database_backup_desc_dir": db_param_database_backup_desc_dir,
    "database_backup_skip_register": db_param_database_backup_skip_register,
    
}

# A small helper function to count number of parameters
def total_db_parameters():
    return len(db_params)

# Testing
# for each_db_param in db_params:
#     print(db_params[each_db_param].get_desc())