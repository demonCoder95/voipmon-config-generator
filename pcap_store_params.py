from pcap_store_params_desc import get_description
from params import ConfigParameter

# Define the configuration objects of each config entry
ps_param_max_pcap_size = ConfigParameter("maxpcapsize", 0, 0, get_description("maxpcapsize"))

ps_param_spool_dir = ConfigParameter("spooldir", "", "/var/spool/voipmonitor", get_description("spooldir"))
ps_param_spool_dir_rtp = ConfigParameter("spooldir_rtp", "", "", get_description("spooldir_rtp"))
ps_param_spool_dir_graph = ConfigParameter("spooldir_graph", "", "", get_description("spooldir_graph"))
ps_param_spool_dir_audio = ConfigParameter("spooldir_audio", "", "", get_description("spooldir_audio"))
ps_param_spool_dir_2 = ConfigParameter("spooldir_2", "", "", get_description("spooldir_2"))
ps_param_spool_dir_file_permission = ConfigParameter("spooldir_file_permission", "", "0666", get_description("spooldir_file_permission"))
ps_param_spool_dir_dir_permission = ConfigParameter("spooldir_dir_permission", "", "0777", get_description("spooldir_dir_permission"))
ps_param_spool_dir_owner = ConfigParameter("spooldir_owner", "", "root", get_description("spooldir_owner"))
ps_param_spool_dir_group = ConfigParameter("spooldir_group", "", "root", get_description("spooldir_group"))
ps_param_spool_dir_by_sensor_name = ConfigParameter("spooldir_by_sensorname", "", "no", get_description("spooldir_by_sensorname"))

ps_param_name_sensor = ConfigParameter("name_sensor", "", "", get_description("name_sensor"))
ps_param_pcap_dump_buff_length = ConfigParameter("pcap_dump_bufflength", 0, 8184, get_description("pcap_dump_bufflength"))

# parameters related to compression
ps_param_pcap_dump_zip = ConfigParameter("pcap_dump_zip", "", "yes", get_description("pcap_dump_zip"))
ps_param_pcap_dump_zip_sip = ConfigParameter("pcap_dump_zip_sip", "", "gzip", get_description("pcap_dump_zip_sip"))
ps_param_pcap_dump_zip_level_sip = ConfigParameter("pcap_dump_ziplevel_sip", 0, 6, get_description("pcap_dump_ziplevel_sip"))
ps_param_pcap_dump_zip_rtp = ConfigParameter("pcap_dump_zip_rtp", "", "lzo", get_description("pcap_dump_zip_rtp"))
ps_param_pcap_dump_zip_level_rtp = ConfigParameter("pcap_dump_ziplevel_rtp", 0, 1, get_description("pcap_dump_ziplevel_rtp"))
ps_param_pcap_dump_zip_graph = ConfigParameter("pcap_dump_zip_graph", "", "lzo", get_description("pcap_dump_zip_graph"))
ps_param_pcap_dump_zip_level_graph = ConfigParameter("pcap_dump_ziplevel_graph", 0, 1, get_description("pcap_dump_ziplevel_graph"))
ps_param_pcap_dump_zip_level = ConfigParameter("pcap_dump_ziplevel", 0, 6, get_description("pcap_dump_ziplevel"))

ps_param_pcap_dump_write_threads = ConfigParameter("pcap_dump_writethreads", 0, 1, get_description("pcap_dump_writethreads"))
ps_param_pcap_dump_write_threads_max = ConfigParameter("pcap_dump_writethreads_max", 0, 32, get_description("pcap_dump_writethreads_max"))
ps_param_pcap_dump_async_write = ConfigParameter("pcap_dump_asyncwrite", "", "yes", get_description("pcap_dump_asyncwrite"))

# TAR configuraion parameters
ps_param_tar = ConfigParameter("tar", "", "yes", get_description("tar"))
ps_param_tar_max_threads = ConfigParameter("tar_maxthreads", 0, 8, get_description("tar_maxthreads"))
ps_param_tar_compress_sip = ConfigParameter("tar_compress_sip", "", "gzip", get_description("tar_compress_sip"))
ps_param_tar_sip_level = ConfigParameter("tar_sip_level", 0, 6, get_description("tar_sip_level"))
ps_param_tar_compress_rtp = ConfigParameter("tar_compress_rtp", "", "no", get_description("tar_compress_rtp"))
ps_param_tar_rtp_level = ConfigParameter("tar_rtp_level", 0, 1, get_description("tar_rtp_level"))
ps_param_tar_compress_graph = ConfigParameter("tar_compress_graph", "", "gzip", get_description("tar_compress_graph"))
ps_param_tar_graph_level = ConfigParameter("tar_graph_level", 0, 1, get_description("tar_graph_level"))

ps_param_cache_dir = ConfigParameter("cachedir", "", "/dev/shm/voipmonitor", get_description("cachedir"))
ps_param_open_file_max = ConfigParameter("openfile_max", 0, 300000, get_description("openfile_max"))
ps_param_convert_char = ConfigParameter("convert_char", "", "", get_description("convert_char"))

ps_param_f_base_name_header = ConfigParameter("fbasenameheader", "", "", get_description("fbasenameheader"))
ps_param_save_sip = ConfigParameter("savesip", "", "yes", get_description("savesip"))
ps_param_save_sip_history = ConfigParameter("save_sip_history", "", "", get_description("save_sip_history"))
ps_param_save_sip_responses = ConfigParameter("save_sip_responses", "", "no", get_description("save_sip_responses"))
ps_param_time_precision_in_ms = ConfigParameter("time_precision_in_ms", "", "no", get_description("time_precision_in_ms"))

# RTP storage parameters
ps_param_save_rtp = ConfigParameter("savertp", "", "yes", get_description("savertp"))
ps_param_null_rtp_payload = ConfigParameter("null_rtppayload", "", "no", get_description("null_rtppayload"))
ps_param_save_rtp_video = ConfigParameter("savertp_video", "", "no", get_description("savertp_video"))
ps_param_pcap_split = ConfigParameter("pcapsplit", "", "yes", get_description("pcapsplit"))
ps_param_save_udptl = ConfigParameter("saveudptl", "", "no", get_description("saveudptl"))
ps_param_fax_detect = ConfigParameter("faxdetect", "", "no", get_description("faxdetect"))
ps_param_save_rtcp = ConfigParameter("savertcp", "", "yes", get_description("savertcp"))
ps_param_save_audio = ConfigParameter("saveaudio", "", "", get_description("saveaudio"))
ps_param_save_audio_after_connect = ConfigParameter("saveaudio_afterconnect", "", "no", get_description("saveaudio_afterconnect"))
ps_param_save_audio_answer_only = ConfigParameter("saveaudio_answeronly", "", "no", get_description("saveaudio_answeronly"))
ps_param_save_audio_from_first_invite = ConfigParameter("saveaudio_from_first_invite", "", "yes", get_description("saveaudio_from_first_invite"))
ps_param_save_audio_stereo = ConfigParameter("saveaudio_stereo", "", "yes", get_description("saveaudio_stereo"))
ps_param_save_audio_reverse_stereo = ConfigParameter("saveaudio_reversestereo", "","no", get_description("saveaudio_reversestereo"))
ps_param_ogg_quality = ConfigParameter("ogg_quality", 0.0, 0.6, get_description("ogg_quality"))
ps_param_audio_queue_threads_max = ConfigParameter("audioqueue_threads_max", 0, 10, get_description("audioqueue_threads_max"))
ps_param_save_audio_dedup_seq = ConfigParameter("saveaudio_dedup_seq", "", "no", get_description("saveaudio_dedup_seq"))
ps_param_live_audio = ConfigParameter("liveaudio", "", "yes", get_description("liveaudio"))
ps_param_key_check = ConfigParameter("keycheck", "", "/var/www/voipmonitor/php/lib/keycheck.php", get_description("keycheck"))
ps_param_save_rfc_2833 = ConfigParameter("saverfc2833", 0, 0, get_description("saverfc2833"))
ps_param_dtmf_2_db = ConfigParameter("dtmf2db", "", "no", get_description("dtmf2db"))
ps_param_dtmf_2_pcap = ConfigParameter("dtmf2pcap", "", "yes", get_description("dtmf2pcap"))
ps_param_inband_dtmf = ConfigParameter("inbanddtmf", "", "no", get_description("inbanddtmf"))
ps_param_silence_detect = ConfigParameter("silencedetect", "", "no", get_description("silencedetect"))
ps_param_silence_threshold = ConfigParameter("silencethreshold", 0, 512, get_description("silencethreshold"))
ps_param_clipping_detect = ConfigParameter("clippingdetect", "", "no", get_description("clippingdetect"))
ps_param_fas_detect = ConfigParameter("fasdetect", "", "no", get_description("fasdetect"))
ps_param_save_energy_levels = ConfigParameter("save-energylevels", "", "no", get_description("save-energylevels"))
ps_param_energy_level_header = ConfigParameter("energylevelheader", "", "", get_description("energylevelheader"))
ps_param_save_energy_levels_via_jb = ConfigParameter("save-energylevels-via-jb", "", "yes", get_description("save-energylevels-via-jb"))
ps_param_sip_alg_detect = ConfigParameter("sipalg_detect", "", "no", get_description("sipalg_detect"))
ps_param_save_graph = ConfigParameter("savegraph", "", "yes", get_description('savegraph'))

# Call recording pausing parameters
ps_param_no_record_header = ConfigParameter("norecord-header", "", "no", get_description("norecord-header"))
ps_param_no_record_dtmf = ConfigParameter("norecord-dtmf", "", "no", get_description("norecord-dtmf"))
ps_param_pause_recording_dtmf = ConfigParameter("pauserecordingdtmf", "", "*9", get_description("pauserecordingdtmf"))
ps_param_pause_recording_dtmf_timeout = ConfigParameter("pauserecordingdtmf_timeout", 0, 4, get_description("pauserecordingdtmf_timeout"))
ps_param_182_queued_pause_recording = ConfigParameter("182queuedpauserecording", "", "no", get_description("182queuedpauserecording"))
ps_param_pause_recording_header = ConfigParameter("pauserecordingheader", "", "", get_description("pauserecordingheader"))
ps_param_convert_dlt_sll_2_en10 = ConfigParameter("convert_dlt_sll2en10", "", "no", get_description("convert_dlt_sll2en10"))
ps_param_dump_all_packets = ConfigParameter("dumpallpackets", "", "yes", get_description("dumpallpackets"))
ps_param_spool_dir_old_schema = ConfigParameter("spooldiroldschema", "", "no", get_description("spooldiroldschema"))

# Spool cleaning parameters
ps_param_clean_spool = ConfigParameter("cleanspool", "", "yes", get_description("cleanspool"))
ps_param_clean_spool_enable_from_to = ConfigParameter("cleanspool_enable_fromto", "", "", get_description("cleanspool_enable_fromto"))

# 'spooldir' configuration parameters
ps_param_max_pool_size = ConfigParameter("maxpoolsize", 0, 102400, get_description("maxpoolsize"))
ps_param_max_pool_days = ConfigParameter("maxpooldays", 0, 30, get_description("maxpooldays"))
ps_param_max_pool_sip_size = ConfigParameter("maxpoolsipsize", 0, 0, get_description("maxpoolsipsize"))
ps_param_max_pool_sip_days = ConfigParameter("maxpoolsipdays", 0, 0, get_description("maxpoolsipdays"))
ps_param_max_pool_rtp_size = ConfigParameter("maxpoolrtpsize", 0, 0, get_description("maxpoolrtpsize"))
ps_param_max_pool_rtp_days = ConfigParameter("maxpoolrtpdays", 0, 0, get_description("maxpoolrtpdays"))
ps_param_max_pool_graph_size = ConfigParameter("maxpoolgraphsize", 0, 0, get_description("maxpoolgraphsize"))
ps_param_max_pool_graph_days = ConfigParameter("maxpoolgraphdays", 0, 0, get_description("maxpoolgraphdays"))
ps_param_max_pool_audio_size = ConfigParameter("maxpoolaudiosize", 0, 0, get_description("maxpoolaudiosize"))
ps_param_max_pool_audio_days = ConfigParameter("maxpoolaudiodays", 0, 0, get_description("maxpoolaudiodays"))

# 'spooldir_2' configuration parameters
ps_param_max_pool_size_2 = ConfigParameter("maxpoolsize_2", 0, 102400, get_description("maxpoolsize_2"))
ps_param_max_pool_days_2 = ConfigParameter("maxpooldays_2", 0, 30, get_description("maxpooldays_2"))
ps_param_max_pool_sip_size_2 = ConfigParameter("maxpoolsipsize_2", 0, 0, get_description("maxpoolsipsize_2"))
ps_param_max_pool_sip_days_2 = ConfigParameter("maxpoolsipdays_2", 0, 0, get_description("maxpoolsipdays_2"))
ps_param_max_pool_rtp_size_2 = ConfigParameter("maxpoolrtpsize_2", 0, 0, get_description("maxpoolrtpsize_2"))
ps_param_max_pool_rtp_days_2 = ConfigParameter("maxpoolrtpdays_2", 0, 0, get_description("maxpoolrtpdays_2"))
ps_param_max_pool_graph_size_2 = ConfigParameter("maxpoolgraphsize_2", 0, 0, get_description("maxpoolgraphsize_2"))
ps_param_max_pool_graph_days_2 = ConfigParameter("maxpoolgraphdays_2", 0, 0, get_description("maxpoolgraphdays_2"))
ps_param_max_pool_audio_size_2 = ConfigParameter("maxpoolaudiosize_2", 0, 0, get_description("maxpoolaudiosize_2"))
ps_param_max_pool_audio_days_2 = ConfigParameter("maxpoolaudiodays_2", 0, 0, get_description("maxpoolaudiodays_2"))

# other parameters
ps_param_max_pool_clean_obsolete = ConfigParameter("maxpool_clean_obsolete", "", "no", get_description("maxpool_clean_obsolete"))
ps_param_auto_clean_spool_min_percent = ConfigParameter("autocleanspoolminpercent", 0, 1, get_description("autocleanspoolminpercent"))
ps_param_auto_clean_min_gb = ConfigParameter("autocleanmingb", 0, 5, get_description("autocleanmingb"))

# A convenient data structure group all the configuration objects
pcap_store_params = {
    "maxpcapsize" : ps_param_max_pcap_size,
    "spooldir" : ps_param_spool_dir,
    "spooldir_rtp" : ps_param_spool_dir_rtp,
    "spooldir_graph" : ps_param_spool_dir_graph,
    "spooldir_audio" : ps_param_spool_dir_audio,
    "spooldir_2" : ps_param_spool_dir_2,
    "spooldir_file_permission" : ps_param_spool_dir_file_permission,
    "spooldir_dir_permission" : ps_param_spool_dir_dir_permission,
    "spooldir_owner" : ps_param_spool_dir_owner,
    "spooldir_group" : ps_param_spool_dir_group,
    "spooldir_by_sensorname" : ps_param_spool_dir_by_sensor_name,
    "name_sensor" : ps_param_name_sensor,
    "pcap_dump_bufflength" : ps_param_pcap_dump_buff_length,

    "pcap_dump_zip" : ps_param_pcap_dump_zip,
    "pcap_dump_zip_sip" : ps_param_pcap_dump_zip_sip,
    "pcap_dump_ziplevel_sip" : ps_param_pcap_dump_zip_level_sip,
    "pcap_dump_zip_rtp" : ps_param_pcap_dump_zip_rtp,
    "pcap_dump_ziplevel_rtp" : ps_param_pcap_dump_zip_level_rtp,
    "pcap_dump_zip_graph" : ps_param_pcap_dump_zip_graph,
    "pcap_dump_ziplevel_graph" : ps_param_pcap_dump_zip_level_graph,
    "pcap_dump_ziplevel" : ps_param_pcap_dump_zip_level,

    "pcap_dump_writethreads" : ps_param_pcap_dump_write_threads,
    "pcap_dump_writethreads_max" : ps_param_pcap_dump_write_threads_max,
    "pcap_dump_asyncwrite" : ps_param_pcap_dump_async_write,

    # tar configuration parameters
    "tar" : ps_param_tar,
    "tar_maxthreads" : ps_param_tar_max_threads,
    "tar_compress_sip" : ps_param_tar_compress_sip,
    "tar_sip_level" : ps_param_tar_sip_level,
    "tar_compress_rtp" : ps_param_tar_compress_rtp,
    "tar_rtp_level" : ps_param_tar_rtp_level,
    "tar_compress_graph" : ps_param_tar_compress_graph,
    "tar_graph_level" : ps_param_tar_graph_level,

    "cachedir" : ps_param_cache_dir,
    "openfile_max" : ps_param_open_file_max,
    "convert_char" : ps_param_convert_char,
    "fbasenameheader" : ps_param_f_base_name_header,
    "savesip" : ps_param_save_sip,
    "save_sip_history" : ps_param_save_sip_history,
    "save_sip_responses" : ps_param_save_sip_responses,
    "time_precision_in_ms" : ps_param_time_precision_in_ms,

    # RTP storage parameters
    "savertp" : ps_param_save_rtp,
    "null_rtppayload" : ps_param_null_rtp_payload,
    "savertp_video" : ps_param_save_rtp_video,
    "pcapsplit" : ps_param_pcap_split,
    "saveudptl" : ps_param_save_udptl,
    "faxdetect" : ps_param_fax_detect,
    "savertcp" : ps_param_save_rtcp,
    "saveaudio" : ps_param_save_audio,
    "saveaudio_afterconnect" : ps_param_save_audio_after_connect,
    "saveaudio_answeronly" : ps_param_save_audio_answer_only,
    "saveaudio_from_first_invite" : ps_param_save_audio_from_first_invite,
    "saveaudio_stereo" : ps_param_save_audio_stereo,
    "saveaudio_reversestereo" : ps_param_save_audio_reverse_stereo,
    "ogg_quality" : ps_param_ogg_quality,
    "audioqueue_threads_max" : ps_param_audio_queue_threads_max,
    "saveaudio_dedup_seq" : ps_param_save_audio_dedup_seq,
    "liveaudio" : ps_param_live_audio,
    "keycheck" : ps_param_key_check,
    "saverfc2833" : ps_param_save_rfc_2833,
    "dtmf2db" : ps_param_dtmf_2_db,
    "dtmf2pcap" : ps_param_dtmf_2_pcap,
    "inbanddtmf" : ps_param_inband_dtmf,
    "silencedetect" : ps_param_silence_detect,
    "silecethreshold" : ps_param_silence_threshold,
    "clippingdetect" : ps_param_clipping_detect,
    "fasdetect" : ps_param_fas_detect,
    "save-energylevels" : ps_param_save_energy_levels,
    "energylevelheader" : ps_param_energy_level_header,
    "save-energylevels-via-jb" : ps_param_save_energy_levels_via_jb,
    
    "sipalg_detect" : ps_param_sip_alg_detect,
    "savegraph" : ps_param_save_graph,

    # Call recording pausing parameters
    "norecord-header" : ps_param_no_record_header,
    "norecord-dtmf" : ps_param_no_record_dtmf,
    "pauserecordingdtmf" : ps_param_pause_recording_dtmf,
    "pauserecordingdtmf_timeout" : ps_param_pause_recording_dtmf_timeout,
    "182queuedpauserecording" : ps_param_182_queued_pause_recording,
    "pauserecordingheader" : ps_param_pause_recording_header,
    
    "convert_dlt_sll2en10" : ps_param_convert_dlt_sll_2_en10,
    "dumpallpackets" : ps_param_dump_all_packets,
    "spooldiroldschema" : ps_param_spool_dir_old_schema,

    # Spool cleaning parameters
    "cleanspool" : ps_param_clean_spool,
    "cleanspool_enable_fromto" : ps_param_clean_spool_enable_from_to,
    # 'spooldir' configuration parameters
    "maxpoolsize" : ps_param_max_pool_size,
    "maxpooldays" : ps_param_max_pool_days,
    "maxpoolsipsize" : ps_param_max_pool_sip_size,
    "maxpoolsipdays" : ps_param_max_pool_sip_days,
    "maxpoolrtpsize" : ps_param_max_pool_rtp_size,
    "maxpoolrtpdays" : ps_param_max_pool_rtp_days,
    "maxpoolgraphsize" : ps_param_max_pool_graph_size,
    "maxpoolgraphdays" : ps_param_max_pool_graph_days,
    "maxpoolaudiosize" : ps_param_max_pool_audio_size,
    "maxpoolaudiodays" : ps_param_max_pool_audio_days,
    
    # 'spooldir_2' configuration parameters
    "maxpoolsize_2" : ps_param_max_pool_size_2,
    "maxpooldays_2" : ps_param_max_pool_days_2,
    "maxpoolsipsize_2" : ps_param_max_pool_sip_size_2,
    "maxpoolsipdays_2" : ps_param_max_pool_sip_days_2,
    "maxpoolrtpsize_2" : ps_param_max_pool_rtp_size_2,
    "maxpoolrtpdays_2" : ps_param_max_pool_rtp_days_2,
    "maxpoolgraphsize_2" : ps_param_max_pool_graph_size_2,
    "maxpoolgraphdays_2" : ps_param_max_pool_graph_days_2,
    "maxpoolaudiosize_2" : ps_param_max_pool_audio_size_2,
    "maxpoolaudiodays_2" : ps_param_max_pool_audio_days_2,

    # Other parameters
    "maxpool_clean_obsolete" : ps_param_max_pool_clean_obsolete,
    "autocleanspoolminpercent" : ps_param_auto_clean_spool_min_percent,
    "autocleanmingb" : ps_param_auto_clean_min_gb,
}

# A helper function to count the number of parameters
def total_pcap_store_params():
    return len(pcap_store_params)