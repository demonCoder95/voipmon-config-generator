#  This module provides descriptions of all the parameters that are related to
#  storage of PCAP files on the sniffers. 

# =========== PROLOGUE OF PCAP STORAGE =======================================
# Sniffers have the ability to store the data stream inside RTP protocol into
# packet streams. There are various configuration options that can govern the
# nature of this storage. These PCAPs are primarily used to generate the audio
# from the stream of packets which can then either be exported from the GUI or
# played there.
# ============================================================================

# a small helper function to perform lookup
def get_description(param):
    return pcap_store_param_descriptions[param]

pcap_store_param_descriptions = {
    "maxpcapsize" : """The parameter to control the maximum size of the PCAP
file which will record the stream packets. When the size exceeds this limit,
the stream packets are still processed for statistics to be populated in the
database (like the jitter/mos entries for the 'rtp*' tables), but the PCAPs of
the packets will no longer be stored anywhere. This parameter accepts values
in MB > 0. Not setting this disables this parameter.\n""",

    "spooldir" : """The directory on the sniffer which will be used for
storage of data. This will store the PCAPs, as well as Graph and Wav (audio)
files that are exported from the dashboard. This is a generic parameter that
can be used to configure the master spool directory for the sniffer.
An example can be '/var/spool/voipmonitor'.\n""",

    "spooldir_rtp" : """A specific/separate directory for RTP PCAP storage
can be specified using this parameter. This helps organize the data that is
collected by the sniffer. If this parameter is used, it has to be configured
in the GUI to allow the sniffer to download PCAPs from it.
An example can be '/var/spool/voipmonitor/rtp'.\n""",

    "spooldir_graph" : """A specific/separate directory for graph storage can
be specified using this parameter. This directory must be properly configured
in the GUI, if changed, in order to correctly place the Graph download.
An example can be '/var/spool/voipmonitor/graph'.\n""",

    "spooldir_audio" : """A specific/separate directory for audio storage can
be specified using this parameter. This directory must be properly configured
in the GUI, if changed, in order to correctly download the audio from PCAPs,
through the GUI.
An example can be '/var/spool/voipmonitor/audio'.\n""",

    "spooldir_2" : """A secondary storage directory for rtp/audio/graph. This
parameter is helpful if you wish to have a hot/cold storage system - where the
'hot' storage is faster/smaller in size containing recent data where as the
'cold' stroage is slower/larger in size containing older data. These storages
can also be configured to have separate cleaning schemes configured.
An example can be '/var/spool/voipmonitor2' which is a mount point for a
separate backing storage.\n""",

    "spooldir_file_permission" : """The octet representation of the UNIX
permissions that are to be applied to all the files inside the spool directory.
An example is '0666' - read/write permission for owner, owner group and others.
""",

    "spooldir_dir_permission" : """The octect representation of the UNIX
permissions that are to be applied to the spool directory.
An example if '0777' - read/write/execute permission for owner, owner group
and others.\n""",

    "spooldir_owner" : """The user name to be set as the 'owner' of the
directory and all the files inside. An example is 'root'. If the supplied
user name is invalid, an 'error' level entry in the log will be generated and
the owner will be reverted to 'root' (uid=0).\n""",

    "spooldir_group" : """The group name to be set as the 'owner group' of the
directory and all the files inside. An example is 'root'. If the supplied
group name is invalid, an 'error' level entry in the log will be generated and
the owner group will be reverted to 'root' (gid=0).\n""",

    "spooldir_by_sensorname" : """The PCAPs stored in the spool directory can
be divided in folders using the 'name_sensor' as the folder name. This is only
useful when a database is not used to store PCAPs. It helps when you have a
central storage configured and mounted across all sensors and they all share
the 'spooldir*' configuration parameters. This parameter can take values 'yes'
or 'no'.\n""",

    "name_sensor" : """When using the 'spooldir_by_sensorname' parameter, this
parameter is configured to provide a name to the sensor being configured. This
name value is only relevant for 'spooldir' configurations and is irrelevant
otherwise. In all other scenarios, the 'sensor_id' parameter is used to
identify this sensor - especially the database related operations.
An example can be 'sensor-1'.\n""",

    "pcap_dump_bufflength" : """The size of the buffer to use when writing the
PCAP/Graph data to files in the 'spooldir'. This helps optimize the I/O
behavior of the write operations, since data inside a single packet is
insufficient to optimally utilize the I/O write capacity. For this purpose, a
buffer which can store data from multiple packets is more optimal. The entire
buffer is then written to disk (in spooldir) in an operation that utilizes the
I/O in a sequential manner and provides better throughput performance - since
'spooldir' writes are throughput sensitive (bulks of data are written).
An example of this is an optimal value of 8184 bytes.\n""",

    # Parameters related to compression
    "pcap_dump_zip" : """This parameter is used to enable ZIP based compression
for the stored files in the spool directory. The PCAP/Graph data is compressed
when in the memory before being written to disk. This improves I/O efficiency
as well as saves disk space, at the cost of additional CPU usage. This
parameter takes values 'yes' and 'no' and must be enabled for other compression
parameters to be valid.\n""",

    "pcap_dump_zip_sip" : """This parameter enables compression only for SIP
PCAPs. It can take the values 'gzip', 'lzo', and 'no' (no compression). This
is typically set to 'gzip', this provides lesser compression ratio but is
faster and adequate for SIP PCAPs.\n""",

    "pcap_dump_ziplevel_sip" : """This parameter governs the compression level
for the ZIP compression for SIP PCAPs. Lower compression levels achieve lesser
degrees of compression (less storage saving) but faster compression (less CPU
usage). The higher levels of compression save space but are much slower and
use a lot of CPU. The ZIP compression levels are typically:
0 - no compression. Only archiving is performed.
1 - very little compression, the fastest. (63% faster than level 6)
6 - 7% more compression than level 1, more compute intensive. (Typically used)
9 - maximum compression, the slowest and most CPU intensive.

SIP PCAPs are generally not large in size compared to RTP PCAPs, therefore
lesser compression serves the purpose and 'gzip' compression with level 6 is
typically used.\n""",

    "pcap_dump_zip_rtp" : """This parameter enables compression only for RTP
PCAPs. it can take values 'gzip', 'lzo' and 'no' (no compression). This is
typically set to 'lzo', which provides a lower compression ratio, which is
suitable for RTP PCAPs which can comparatively bulkier and need to be
compressed quickly.

If the parameter is set to 'lzo' a few things are to be noted. The 'lzo'
implementation inside the VoIP Monitor is not compatible with standard 'lzo'
tools. Therefore, you will have to decompress your pcaps using the VoIP Monitor
binary. You can do that as follows:

    voipmonitor -kc --unlzo-gui='input.pcap output.pcap'

where 'input.pcap' is your compressed PCAP file and the 'output.pcap' is the
filename for the output uncompressed PCAP file.

Additionally, you might also need to unTAR the PCAPs that have been bundled
into an archive, prior to performing the decompression . You can do that as
follows:

    tar --wildcards -xOf tar.tar 'somename.pcap*' > merged_rtp.pcap

where --wildcards options allows you to specify a wildcard for the files to
extract from the archive. In this example, the archive has been set to
'tar.tar' and all the filenames inside the archive that match the wildcard of
'somename.pcap*' will be extracted and concatenated to be pushed to the stdout
(due to -O parameter). This is then redirected into a single 'merged_rtp.pcap'
file which is the PCAP file you can use (after decompression, as directed
previously), for instance, inside of Wireshark for analysis.

Also, the path names inside the archive to the files, if they are not absolute,
they will be relative to the 'spooldir' as set in the other parameter.

Note: If you use the GUI, all of this extraction is handled inside of it,
and none of it is necessary. The GUI uses 'gzip' for compression, which you can
easily decompress with standard tools, once you download the PCAP.\n""",

    # Need to verify the point about 'gzip' compression in PCAPs downloaded
    # from the GUI

    "pcap_dump_ziplevel_rtp" : """This parameter governs the compression level
of the ZIP compression for RTP PCAPs. Typically set to '1' for faster
compression in conjuction with the compression scheme of 'lzo' which has a
comparatively lower compression ratio than 'gzip' (and is therefore faster than
'gzip' for the same level of compression). However, if larger space saving is
required and CPU computation is available, feel free to set this to '6'
(sufficient) or '9' (maximum) compression.\n""",

    "pcap_dump_zip_graph" : """This parameter enables compression only for
Graph files. It can take values of 'gzip', 'lzo' and 'no' (no compression).
This is typically set to 'lzo' since higher compression ratio isn't needed.
Look at the 'lzo' notes in the 'pcap_dump_zip_rtp' parameter for more details
on setting compression scheme to 'lzo'.\n""",

    "pcap_dump_ziplevel_graph" : """This parameter determines the level of
compression for the Graph files as they are written to disk. Level '1' is
little compression and fastest, '6' is medium while '9' is maximum compression
but most CPU and memory intensive and the slowest. You can configure this as per
need and resource availability. Typically this is '1'.\n""",

    "pcap_dump_ziplevel" : """This is a global parameter that can set all 3 of
the ziplevel parameters to the same value. These are 'pcap_dump_ziplevel_sip',
 'pcap_dump_ziplevel_rtp' and 'pcap_dump_ziplevel_graph'. See the parameter 
 'pcap_dump_ziplevel_sip' for details on compression levels. This is typically
 set to '1' for fastest compression with smallest compression ratio to conserve
 CPU and memory resources and time to write PCAPs to disk.\n""",

    "pcap_dump_writethreads" : """The 'initial' number of threads to use when
performing compression with the parameters specified. Note that this is only
the initial thread count, the number of threads used in compression grow
automatically as the CPU usage is > 95%. Typically set to 1.\n""",

    "pcap_dump_writethreads_max" : """This parameter controls the maximum
number of threads allowed for performing the ZIP compression of files as set
in the other parameters. This parameter is limited by the following formula:
    
    MIN( # of CPU threads, pcap_dump_writethreads_max, 32)

In other words, even if you have more than 32 threads in the CPU, you cannot
use more than 32 threads to perform compression. This is more than reasonable.
Configure this parameter properly to avoid CPU overload due to a large
compression workload.\n""",

    "pcap_dump_asyncwrite" : """This parameter configures asynchronous write
for the I/O. This allows the writer to write the compressed data blocks into
the 'asyncbuffer' and continue working while the 'asyncbuffer' is slowly
flushed by the I/O layer as data blocks are written to disk. This should always
be enabled to avoid the writer to be blocked when waiting for the I/O layer to
finish processing the blocks of data. This parameter takes values 'yes' and
'no'.\n""",

    # TAR parameters
    # Look into the 'concurrent calls data' given below
    "tar" : """When writing PCAPs to file, instead of writing each call to a
separate file, you can choose to bundle them together in a TAR archive. The
TAR file naming is derived on the basis of call start time, in the following
format:

    YYYY-MM-DD/hour/min/sip.tar

TAR files are created separately for SIP, RTP and graph data types, prefixed
appropriately in the filename. This method is available since sniffer 11.0.

In workloads upto 2,000 concurrent calls, the IOPS in storage can drop from
200 to 40, we typically store SIP+RTP+Graph all types. However, for higher
than 40,000 concurrent calls, IOPS can drop from 4,000 to 10, so, we store
SIP PCAPs only.

This parameter accepts values 'yes' and 'no'.\n""",

    "tar_maxthreads" : """Maximum number of threads allowed for performing
TAR compression. This value is typically 8. The number of threads currently
being used for TAR compression can be checked in the logs, under the parameter
tarCPU[A|B|C|D...]. Be sure to tune this value appropriate to the workload
to avoid overload on the CPU.
The maximum value for this parameter is the number of threads in the CPU.
""",

    # You can use the 'pcap_dump*' parameters to perform compression on a 
    # PCAP level. If you choose to perform compression in the TAR archive
    # the per file compression is disabled.
    "tar_compress_sip" : """This parameter enables compression for SIP PCAPs
inside the TAR archive. If enabled, this disables the parameter for individual
compression parameter 'pcap_dump_zip[level]_sip'. 

If TAR compression is disabled, sniffer keeps track of the offset of each file
inside the archive, in the database. This allows for quick seeking when files
are required to be downloaded from the GUI, or accessed otherwise. In the event
that TAR compression is enabled for SIP, the offset can no longer be maintained
due to compression of the archived data, therefore this can result in large I/O
activity when files are to be downloaded from GUI or extracted from the archive.
This effect becomes worse under higher loads, due to high I/O and CPU usage.

'lzma' compression has a 40% higher compression ratio, but is 10x slower and
uses a lot more memory. It also results in a longer time required to flush PCAP
data from memory to the TAR archive, therefore, user needs to wait for a longer
time in order to be able to download a PCAP after a call has ended. Use it only
if the benefit of saving space is required and the extra resource usage and
delay is affordable.

This parameter can take values 'gzip', 'lzma' and 'no' (no compression).\n""",

    # Files are put in the memory until the size grows to 150kB, upon which
    # the file is flushed out to a TAR file. For larger workloads, memory can
    # be saved by performing compression inside memory using a fast
    # compression algorithm called 'snappy'. However, this will increase the
    # time required to flush data from memory to disk. This can be disabled.

    "tar_sip_level" : """This is the ZIP compression level for the SIP PCAP
inside the TAR archive. It is typically set to 6.
See 'pcap_dump_ziplevel_sip' parameter for more details on compression levels.
""",

    "tar_compress_rtp" : """This parameter enables compression for RTP PCAPs
inside the TAR archive. If enabled, this disables the parameter for individual
compression parameter 'pcap_dump_zip[level]_rtp'.

It is recommeded that TAR compression be disabled for RTP PCAPs since they
are bulkier and extracting bulky files from an archive is a seek-intensive
operation, which can be costly on slower media like HDD spinners. If disabled,
I/O can be made faster since the sniffer stores each file offset in the
database, which makes TAR extraction very fast, and ultimately faster PCAP
downloads from the GUI.

A recommended approach for RTP is to compress them individually and then
bundle them into an uncompressed archive. You can do this using the individual
compression parameters 'pcap_dump_zip[level]_rtp' and set this parameter to
'no'.

'lzma' compression has a 40% higher compression ratio, but is 10x slower and
uses a lot more memory. It also results in a longer time required to flush PCAP
data from memory to the TAR archive, therefore, user needs to wait for a longer
time in order to be able to download a PCAP after a call has ended. Use it only
if the benefit of saving space is required and the extra resource usage and
delay is affordable.

This parameter can take values 'gzip', 'lzma' and 'no' (no compression).\n""",

    "tar_rtp_level" : """This parameter sets the compression level for RTP
PCAPs inside the TAR archive. It's not recommended that this compression be
used, however, if it is, this is typically set to 1.
See 'pcap_dump_ziplevel_sip' parameter for more details on compression levels.
""",

    "tar_compress_graph" : """This parameter enables compression for the 
graph data inside the TAR archive. Typically set to 'gzip'.

'lzma' compression has a 40% higher compression ratio, but is 10x slower and
uses a lot more memory. It also results in a longer time required to flush data
from memory to the TAR archive. Use it only if the benefit of saving space is
required and the extra resource usage and delay is affordable.

This parameter can take value 'gzip', 'lzma' and 'no' (no compression).\n""",

    "tar_graph_level" : """This parameter sets the compression level for
graph data in the TAR archive. Typically set to 1.\n""",

    # End of TAR compression parameters

    "cachedir" : """The PCAP and graph files are first written to the cache
before being written to the spooldir. Typically, this can be a shared memory
location '/dev/shm/voipmonitor' in RAM or an SSD backed mount point like 
'/mnt/ssd/voipmonitor', which can be SATA/SAS SSD based network storage
or some RAID configuration in the server. If your 'spooldir' is a slow
medium like spinner HDD, the movement of data from 'cachedir' to 'spooldir'
is guaranteed to be serialized, ensuring sequential writes which are faster
than random writes for spinning media since it removes seek times.\n""",

    "openfile_max" : """In Linux systems, the number of open file descriptors
allowed per process are by default 65535. This includes all the open regular
files for reading/writing as well as sockets open for multi-threaded
applications. In high performance applications like the VoIP Monitor sniffer,
this count needs to be increased. This is typically set to hundreds of
thousands.\n""",

    "convert_char" : """List of characters that are to be converted to '_' in
the PCAP filenames. For space, enclose it between other characters like ': :',
this will convert both ':' and ' ' into '_'. An example of this could be:
convert_char: :
this can be used to remove ':' from filenames which are based on Call-IDs that
have port numbers in them.\n""",

    # SIP storage parameters

    "fbasenameheader" : """By default, SIP PCAP filenames are created using the
SIP.Call-ID header as the base. This can be overridden to a custom header in
the format 'X-custom-filename'. This parameter can be set to a SIP message
header value.\n""",

    "savesip" : """This parameter enables saving of SIP packets to PCAPs.
This parameter accepts values 'yes' and 'no'.\n""",

    "save_sip_history" : """This parameter can be used to enable storage of
SIP request/response messages of all types during the call. This is done in the
database in the 'cdr_siphistory' table (without body). This can be used to
search the database for calls specific to a request or response packet in the
dialogue. 
If this parameter is disabled, SIP responses are always stored, and SIP
request type stored is only BYE. This parameter enables storing of all SIP
requests and all SIP responses (with additional timestamps). Only enable this
parameter if needed.

This parameter accepts values 'requests,responses' and 'all'.\n""",

    "save_sip_responses" : """This parameter enables storing of all SIP
responses into the 'cdr_sipresp' table in the database. Be careful, this
parameter creates a lot of pressure on the database under high SIP traffic
throughput. That's why this parameter is typically disabled. Only use this if
specifically required.

This parameter takes values 'yes' and 'no'.\n""",

    "time_precision_in_ms" : """This parameters enables storing SIP messages in
the database with timestamp precision of ms. This is a special configuration to
be used only if specifically required, and is typically disabled.

This parameter takes values 'yes' and 'no'.\n""",

    # RTP storage parameters
    "savertp" : """This parameter controls storage of RTP packets in PCAPs. If
enabled, it also stores RTCP and UDPTL packets (needed for T.38 Fax). You can
set this parameter to 'header' to only store header data and no audio data, if
required. Additionally, you can set this to 'no' and control which calls store
the RTP related protocols through capture configurations in the GUI -> Capture
rules. Alternatively, you can set this parameter to 'yes' and block RTP storage
of certain calls based on 'filter_*' filters.

These rules are stored in the database in 'filter_ip' and 'filter_telnum' 
tables. You can reload these filtering rules with the 'reload' option in the
GUI.
This parameter accepts values 'yes', 'header' and 'no'. \n""",

    "null_rtppayload" : """This parameter can be used to fill RTP payloads
with zeroes, essentially zeroing all the audio. You cannot listen to audio
if this parameter is set. Also any of the DSP processing elements will not
work since they get zeroed data (Dual Tone Multi Frequency - DTMF, silence
detection etc.). Typically, you do not need to set this parameter since you
can control the RTP payload storage with the capture rules in the GUI.

This parameter accetps values 'yes' and 'no'.\n""",

    "savertp_video" : """This parameter configures RTP video packet storage.
If set to 'cdr_only' only the CDR entries are created for RTP video packets in
the database, and no data is stored in PCAPs. If set to 'header' the behavior
is similar to that of 'savertp', where only the header data is stored in PCAPs.
If set to 'no', RTP video capture is disabled. This is typically disabled
unless needed. 
This parameter accepts values 'cdr_only', 'header', 'yes' and 'no'.\n""",

    "pcapsplit" : """This parameter configures splitting of PCAP files for SIP
 and RTP streams. This is desired by default, to allow you to store both PCAPs
separately in their subdirectories (see parameter details for 'tar'). This also
allows separate spool cleaning policies for both PCAP types.

If desired, you can merge these PCAPs using the 'mergecap' CLI utility which is
part of the Wireshark package.

Note that this parameter requires that the 'spooldiroldschema' parameter be set
to 'no'. Since in the old schema, all the data was stored in a single directory
'/var/spool/voipmonitor/YYYY-MM-DD/*'.

This parameter accepts values 'yes' and 'no'.\n""",

    "saveudptl" : """This parameter controls storage of T.38 Fax protocol
packets. If you choose to do so, you can set 'savertp' to 'no' and 'saveudptl'
to 'yes'. This will save only T.38 Fax packets in the PCAPs.
This parameter accepts values 'yes' and 'no'.\n""",

    "faxdetect" : """This parameter is used to perform T.38 Fax detection over
IP. In Fax over IP, the flow starts with a 'CNG' tone of 1100 Hz. The receiver
responds with a 'CED' tone of 2100 Hz. Currently, these tones are detectable
only if coded with G.711 codec (a-law/u-law based). This, however, requires
extra CPU usage. Only enable this if required. This is typically set to 'no'.

This parameter accepts values 'yes' and 'no'.\n""",

    "savertcp" : """This parameter controls storing of the RTP Control Protocol
(RTCP) packets. Similar to 'saveudptl' you can choose to set 'savertp' to 'no'
and 'savertcp' to 'yes' to store only RTCP packets in PCAPs.

This parameter accepts values 'yes' and 'no'.\n""",

    "saveaudio" : """This parameter configures saving RTP payload as compressed
audio instead of raw payload. 
If set to 'wav', the audio will be compressed with the Microsoft Waveform Audio
File format.
If set to 'ogg' the audio will be compressed with the OGG Vorbis audio
compression @25kbps data rate. The OGG open source format is for media file
containerization (like MP3 or MP4) and uses the Vorbis compression to compress
high-quality audio.

Note that enabling this parameter will generate additional I/O pressure and
consume more resources. A recommended approach is to disable this and store raw
payloads, which can be compressed on demand, to listen to audio payloads.
This parameter can be set to 'wav' and 'ogg'. Setting no value disables this.
""",

    "saveaudio_afterconnect" : """This parameter configures audio saving only
after the call has been answered. This is typically set to 'no'.
This parameter accepts values 'yes' and 'no'.\n""",

    "saveaudio_answeronly" : """This parameter configures audio saving only
for connected calls. Tyically set to 'no'.
This parameter accepts values 'yes' and 'no'.

THIS PARAMETER IS BEING DEPRECATED IN FAVOR OF 'saveaudio_afterconnect'.\n""",

    "saveaudio_from_first_invite" : """This parameter is used to enable saving
audio from the time the first 'Invite' packet is received. This allows the
audio length to be equal to the SIP serialization length (used to measure size
of the SIP stream when writing SIP packets from memory to the PCAPs). This is
typically set to 'yes' to generate silence audio, which helps in matching
audio length with SIP length. This is helpful when you want to combine SIP and
RTP PCAPs of a call, for your analysis.
This parameter accepts values 'yes' and 'no'.\n""",

    "saveaudio_stereo" : """This parameter controls audio storing in separate
channels for 'called' and 'caller' party audios. If set to 'yes' the caller
party audio will be stored in the 'left' channel and called party audio in the
'right' channel. If disabled, both audios will be mixed into a single channel
'mono' audio. This is typically set to 'yes'.

This parameter accepts values 'yes' and 'no'.\n""",

    "saveaudio_reversestereo" : """This parameter can be used to reverse the
audio channels as set in the 'saveaudio_stereo' parameter. If set to 'yes', it
configured the caller party audio to the 'right' and the called party audio to
the 'left' channel. This is typically not used, if not specifically required.

This parameter accepts values 'yes' and 'no'.\n""",

    "ogg_quality" : """This parameter controls the quality parameter for the
OGG Vorbis compressed audio. Higher values mean better quality, at the cost
of larger file size. This value is typically set to '0.6'.
This parameter accepts values in the range -0.1 to 1.0.\n""",

    "audioqueue_threads_max" : """This parameter controls the maximum number
threads allowed to process audio compression. This is typically set to 10.
If not set, the maximum value will be the total number of threads in the CPU.
""",

    "saveaudio_dedup_seq" : """This parameter configures deduplication for RTP
packets based on the sequence number. This will not allow processing of RTP
packets that have the same sequence number. This is typically set to 'no'.
Only enable this if requried.
This parameter accepts values 'yes' and 'no'.\n""",

    "liveaudio" : """This parameter configures listening to live audio. This is
typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "keycheck" : """This parameter specifies the default directory which holds
the Web GUI code for codec. This it typically set to:

keycheck = '/var/www/html/voipmonitor/php/lib/keycheck.php' or
keycheck = '/var/www/voipmonitor/php/lib/keycheck.php

This file contains an encrypted program payload which performs license key
check for the Web GUI. This is required since processing of certain codecs
for generating audio for listening is a licensed functionality.

Similar encrypted functionality is put throughout the Web GUI and is only
useable if a proper license has been configured in the Web GUI.\n""",

    "saverfc2833" : """This parameter configures saving of Dual Tone Multi
Frequency (DTMF) telephony signalling carried in RTP packets (RFC 2833). You
can choose to disable RTP saving and enable 'saverfc2833' to store only DTMF.
This is functionally similar to setting 'savertp' to 'no' and setting 'savertcp'
or 'saveudptl' to 'yes'. 
One note of caution, when VoIP Monitor sniffer is reading packets in multiple
threads, enabling this can cause slowing down of the main read thread of the
sniffer. That's why this parameter is typically disabled.
This parameter accepts values 1 and 0.\n""",

    "dtmf2db" : """This parameter configures saving of DTMF signalling in the
database in the 'cdr_dtmf' table. The DTMF signalling can be transmitted in
the following ways:

1. Through the SIP INFO packet using 'Method - DTMF". This allows the DTMF
codes to be carried as payloads in a SIP message.

2. Through the RFC 2388 compliant DTMF over RTP. This allows DTMF codes to be
carried as payloads inside an RTP stream.

3. Through 'inband' signalling. In this setup, the DTMF codes are transmitted
as voice. This is done for compatibility purposes and is hard to listen to due
to high-compression enabled on audio by default. Therefore, this requires some
processing to listen to.

The information stored in the database is the time of the dialing as well as
the key pressed on the phone. These values stored in the database are then
available in the GUI as 'SIP History'.
Since this parameter generates a lot of overhead on packet processing as well
as database, only enable this if you expect DTMF traffic in your system.
This parameter accepts values 'yes' and 'no'.\n""",

    "dtmf2pcap": """This parameter configures saving of DTMF signalling
types SIP INFO and RTP into PCAPs (See parameter 'dtmf2db' for details of
DTMF Signalling types). This is typically enabled. 
This parameter accepts values 'yes' and 'no'.\n""",

    "inbanddtmf" : """If you desire inband detection of DTMF tones in the
G.711 (a-law/u-law) audio only, in the incoming streams, you can enable this
parameter. This is typically only useful when 'dtmf2db' is set to 'yes' and
you can store the DTMF data detected from audio stream, otherwise, keep it
disabled. This generates additional CPU load, since G.711 decoding into linear
format is performed to extract the discerete phone key values from the DTMF
signal. Since a-law and u-law are logarithmic encoding schemes. 
This parameter accepts values 'yes' and 'no'.\n""",

    "silencedetect" : """This parameter configures silence detection in audio
that is encoded with G.711 codec (a-law/u-law) only. This is calculated using
audio energy level information. The silence is stored as the noise percentage
ratio. A silence ratio of > 0.8 (80%) implies silence. This information is then
used to populate two new fields in the CDR  which specify how many seconds
of silence was detected from the caller and called side.
This also detects what is termed as 'absolute silence', which is treated as
dropped packets. This also affects the Mean Opinion Score (MOS) mininum and
average values of the call (explained in other parameters).

This enables the Discrete Signal Processor (DSP) component for G.711 (a-law/
u-law) processing which can generate additional CPU load. Therefore, this is
typically disabled. Enable it only if required.
Ths parameter accepts values 'yes' and 'no'.\n""",

    "silencethreshold" : """This parameter controls the sensitivity of silence
detection. Higher values imply higher silence sensitivity, meaning lesser noise
is needed to detect silence. This is typically set to 512.
This parameter accepts values between 1 and 32767.\n""",

    # Need to improve this explanation with more details of clipped values.
    "clippingdetect" : """"This parameter enables clipping detection, which
counts the number of frames detected that are clipped. This is stored in the
form of number of milliseconds, in the database under CDR parameters
'cdr.caller_clipping_mult100' and 'cdr.called_clipping_mult100'.

The clipped packets are the 8kHz audio packets with maximum clipped values of
32124 for u-law and 32256 for a-law delimited by a factor of 100. The column
value inside the database is type TINYINT which implies a maximum value of 255.
Since this value is delimited by a factor of 100, the maximum implied value is
25,500 frames clipped. These are the frames detected by human hearing as
distortion.

Enabling this parameter also enables the DSP component for G.711 (a-law/u-law)
processing which requires additional CPU. Therefore, this is parameter is 
typically disabled. Enable this only if you want to precisely detect clipping
in packet for purposes of analysis.
This parameter accepts values 'yes' and 'no'.\n""",

    "fasdetect" : """This parameter enables the 'False Answer Supervision'
detection. This is a practice of detecting when the call has actually been
answered to ensure correct call duration is stored on the operator end. This
is typically done by detecting the ring tones after the call has been dialed
but before it has been answered. If the call hasn't been answered, the call
duration is set to 0. If not done, this can sometime lead to a call duration
value of larger than the actual duration. This is a protection mechanism to
protect customers from VoIP billing fraud, where the answer packets can be
modified to charge customers for non-conversation time.
Since this requires additional processing for ring tone detection, it will
consume additional CPU if enabled. This is typically disabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "save-energylevels" : """This parameter enables saving energy level data
for each received RTP packet. This data is used to perform other functions as
well, such as silence detection when 'silencedetect' is set to 'yes'. This
level is a 16-bit encoded value. These values are stored in the database table
named 'cdr_rtp_energylevels'. This table is automatically created if this
parameter is enabled. This only works for RTP streams encoded with G.711 (a-law
/u-law) codec.
As is the case with other features requiring G.711 (a-law/u-law) processing,
enabling this parameter results in additional CPU usage. A set of SQL queries
that can allow you to utilize these energy level data is the follows:

        SELECT cdr_rtp_energylevels.*, cdr_rtp.*,
        IF(cdr_rtp.flags & (1<<2), "caller", 
          IF(cdr_rtp.flags & (1<<3), "called", "unknown")) AS direction
        FROM cdr_rtp_energylevels
        LEFT JOIN cdr_rtp ON (cdr_rtp.cdr_id = cdr_rtp_energylevels.cdr_id 
                          AND cdr_rtp.index = cdr_rtp_energylevels.index)
        WHERE cdr_rtp_energylevels.cdr_id = 2177862

This parameter accepts values 'yes' and 'no'.\n""",

    "energylevelheader" : """This parameter specifies the header which triggers
energy level calculation for a packet. Packets with missing header will not be
processed for energy level calculation. This is typically set to 'X-energlvl'.
This parameter accepts any valid RTP header. Set this only if needed.\n""",

    "save-energylevels-via-jb" : """Energy levels are typically calculated
using the packets from the jitter buffers. Empty payloads count as 0. If the
jitter buffers have been disabled, the energy level detection is done without
them and silence is not counted as an energy level of 0. This parameter is
typically enabled. It accepts values 'yes' and 'no'.\n""",

    "sipalg_detect" : """If the SIP clients are hidden behind a router or a
firewall as an 'Application Level Gateway', this parameter enables the
functionality to detect the ALG. This is used in the scenarios when the SIP
clients are not using public IP addresses. This is typically disabled, unless
needed. 
This parameter accepts values 'yes' and 'no'.\n""",

    "savegraph" : """This parameter enables saving of the graph data from the
Web GUI.
This parameter accepts values 'yes' and 'no'.\n""",

    # Parameters to control call recording and other related parameters
    "norecord-header" : """When the call stream is being processed, if any of
the packets contain the header 'X-VoipMonitor-norecord', the call will not be
converted to audio (given that the 'saveaudio' is set to 'yes') and the PCAP
file will be deleted. This parameter enables this functionality and is
typically disabled unless specifically needed, i.e. it is expected that the
incoming traffic will have this header set.
This parameter accepts values 'yes' and 'no'.\n""",

    "norecord-dtmf" : """When processing DTMF in SIP streams (see the parameter
'dtmf2db' for more details on DTMF processing), and any SIP INFO packet
contains the DTMF sequence of '*0' the call will not be converted to audio
(given that 'saveaudio' is set to 'yes') and the associated PCAP file will be
deleted. This is typically disabled, unless specifically needed in the stream
processing.
This parameter accepts values 'yes' and 'no'.\n""",

    "pauserecordingdtmf" : """This parameter allows you to specify a DTMF
sequence of your choice to pause a call recording. If any packet received
has this DTMF sequence, the recording will be paused for that call (RTP if
raw audio is being written to PCAP or WAV/OGG if 'saveaudio' is set to 'yes').
For instance, this could be set to '*9'. Not setting any value disables this
parameter. It is typically disabled unless required specifically.\n""",

    "pauserecordingdtmf_timeout" : """This parameter controls the timeout
between DTMF sequences detected if 'pauserecordingdtmf' is set. This is
typically set to a small value like 4.
This parameter accepts values in seconds > 0.\n""",

    "182queuedpauserecording" : """This parameter enables pausing the call
recording based on a SIP message '182 Queued avaya-cm-data'. The breakdown of
this message is as follows:

SIP servers can respond with a status code of '182' which means the request has
been 'Queued' for later processing (due to several reasons) and not outright
rejected.
The 'avaya-cm-data' field corresponds to the 'Avaya Communication Manager'.
This is a unified management system for IP Telephony by Avaya Solutions.

This parameter, therefore, provides compatibility with Avaya CM and is
irrelevent if the VoIP system does not have the Avaya CM in it. Therefore,
this is typically disabled.
This parameter accepts values 'yes' and 'no'.\n""",

    "pauserecordingheader" : """This parameter allows you to set a custom
header to pause recordings. The header must have the value 'pause' inside
of it. Any other values will be treated as 'unpause' and recording will resume.
For instance, one way of setting this parameter is:
    
    pauserecordingheader = MyCustomPauseHeader

Once set, any SIP packet with this header can be used to trigger recording
pause. This is typically disabled, unless this functionality is distinctly
required. 
This parameter accepts any valid SIP custom header.\n""",

    # End of call recording parameters

    "convert_dlt_sll2en10" : """If you've set the 'interface' parameter for a
sniffer to 'any', it is possible that interface encapsulations are different
for different interfaces, and consequently, the captured packets will not be
compatible to be stored in the same PCAP file.  Therefore, this parameter
enables encapsulation conversion between different Data Link Types (DLT).

Unless you plan to merge PCAPs together, this parameter is not needed.
Some information regarding the two DLTs mentioned is as follows:

1. Sockaddr Link Layer (sll): When processing packets captured on a generic
interface like 'any', in the linux network stack, the synthetic link layer is
generated using the 'sockaddr' structures. This is typically used when the
specific functionality for the link layer to be used is either specified or is
not supported.

2. Ethernet 10 (en10): This corresponds to a standard Ethernet Link Layer
interface that is aptly named 'en10' in some linux environments.
This parameter accepts values 'yes' and 'no'.\n""",

    "dumpallpackets" : """This parameter enables dumping of all the captured
packets in one large dump file
'[spooldir]/dump-[interface]-[UNIX_TIMESTAMP].pcap'. This is helpful if you
want to transfer transfer all the captured PCAPs by the sniffer for analysis to
another location.
This parameter accepts values 'yes' and 'no'.\n""",

    "spooldiroldschema" : """The old schema for spool stored files in a
directory structure as '[spooldir]/YYYY-MM-DD/*'. Enabling this parameter will
enable this structure for the 'spooldir'. However, this will disable the newer
features like TAR archiving (with compression, if configured) and spool cleaning
policies, both of which rely on the new 'spooldir' schema. Therefore, this is
typically set to 'no'.
Also see the related parameters 'pcapsplit' and 'tar' for more details of this.
This parameter accepts values 'yes' and 'no'.\n""",

    # Spool directory cleaning policies parameters
    "cleanspool" : """This parameter configures 'spooldir' cleaning. This is
an operation of removing older files, once a preconfigured limit has been
reached. This is done in order to not overrun the storage capacity of the
'spooldir'. This is typically enabled with a proper cleaning policy. This is
available since sniffer v8.0.

Every file created in 'spooldir' is indexed in the file '[spooldir]/filesindex'
in an hourly interval. The size of the files, aggregated, is stored in the
database table 'files'. When the cleaning procedure starts, it directly unlinks
the desired files using these index values, without the need to scan any
directories. This significantly speeds up cleaning especially when the spool
grows very large.

Cleaning procedures are evaluated every 5 minutes, to detect triggering. In
case a rule is triggered, data is deleted on an hourly basis until the trigger
is silenced (i.e. the spool size/day is in range). The evaluation order of the
rules is as follows:

1. The 'maxpool*size' parameters are evaluated first.
2. The 'maxpool*days' parameters are evaluated afterwards.

Note: For storage sizing, since rule trigerring is checked every 5 minutes, the
amount of data generated in 5 minutes might be a factor in sizing of storage.
Keep a safe margin of 5-10% to avoid storage exhaustion and possible crash.

You can better control cleaning with more specific parameter values. Multiple
rules can be set at once, for better cleaning policies configuration. So you
can apply multiple policies, and triggering any one will result in a cleaning
action. More details in the specific parameters.
This parameter accepts values 'yes' and 'no'.\n""",

    "cleanspool_enable_fromto" : """Cleaning files is a highly I/O intensive
operation. It is recommended to schedule this to off-peak hours, in order to
avoid resource exhaustion on the sniffer.

This is similar to the database parameter 'partition_operations_enable_fromto'.
The idea is to offload resource intensive housekeeping work to off-peak hours.

This parameter accepts hour values in 24-hour format, in the form of a range
of hours which are off-peak. For instance, a setting of 1AM - 5AM would look
like this:
    cleanspool_enable_fromto = 1-5
""",

    # All parameters could be interpreted as 'maxspool*', since they all govern
    # the spool size (in MB) to be configured for cleaning policies.

    # Primary 'spooldir' configuration parameters
    "maxpoolsize" : """This parameter controls the maximum size of the
'spooldir', measured in Megabytes (MB). Set this to be the amount of space you
wish the sniffer to use as an aggregate of allowed storage space. This is
typically in 100s of GBs, depending on your data sizing.
This parameter accepts MB values > 0.\n""",

    "maxpooldays" : """This parameter configures the cleaning policy based on
the number of days. This is typically set to 30 days. One word of caution,
must be made sure that the storage sizing is appropriately done to not overrun
the storage with the amount of data generated in this period.
One way to do this is to use a combination of 'maxpoolsize' and 'maxpooldays'.
In this case, triggering any one will result in cleaning, and storage capacity
will not be exhausted.
This parameter accepts day values > 0.\n""",

    "maxpoolsipsize" : """This parameter controls maximum size of the SIP
PCAPs stored in the 'spooldir'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolsipdays" : """This parameter controls the maximum number of days
the SIP PCAPs are stored. This parameter accepts day values > 0.\n""",

    "maxpoolrtpsize" : """This parameter controls maximum size of the RTP
PCAPs stored in the 'spooldir'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolrtpdays" : """This parameter controls the maximum number of days
the RTP PCAPs are stored. This parameter accepts day values > 0.\n""",

    "maxpoolgraphsize" : """This parameter controls maximum size of the graph
data stored in the 'spooldir'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolgraphdays" : """This parameter controls the maximum number of days
the graph data is stored. This parameter accepts day values > 0.\n""",

    "maxpoolaudiosize" : """This parameter controls maximum size of the audio
data stored in the 'spooldir'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolaudiodays" : """This parameter controls the maximum number of days
the audio data is stored. This parameter accepts day values > 0.\n""",


    # secondary 'spooldir' configuration parameters
    "maxpoolsize_2" : """This parameter controls the maximum size of the
'spooldir_2', measured in Megabytes (MB). Set this to be the amount of space
you wish the sniffer to use as an aggregate of allowed storage space. This is
typically in 100s of GBs, depending on your data sizing.
This parameter accepts MB values > 0.\n""",

    "maxpooldays_2" : """This parameter configures the cleaning policy based on
the number of days. This is typically set to 30 days. One word of caution,
must be made sure that the storage sizing is appropriately done to not overrun
the storage with the amount of data generated in this period.
One way to do this is to use a combination of 'maxpoolsize_2' and 
'maxpooldays_2'.
In this case, triggering any one will result in cleaning, and storage capacity
will not be exhausted.
This parameter accepts day values > 0.\n""",

    "maxpoolsipsize_2" : """This parameter controls maximum size of the SIP
PCAPs stored in the 'spooldir_2'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolsipdays_2" : """This parameter controls the maximum number of days
the SIP PCAPs are stored. This parameter accepts day values > 0.\n""",

    "maxpoolrtpsize_2" : """This parameter controls maximum size of the RTP
PCAPs stored in the 'spooldir_2'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolrtpdays_2" : """This parameter controls the maximum number of days
the RTP PCAPs are stored. This parameter accepts day values > 0.\n""",

    "maxpoolgraphsize_2" : """This parameter controls maximum size of the graph
data stored in the 'spooldir_2'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolgraphdays_2" : """This parameter controls the maximum number of days
the graph data is stored. This parameter accepts day values > 0.\n""",

    "maxpoolaudiosize_2" : """This parameter controls maximum size of the audio
data stored in the 'spooldir_2'. This parameter accepts MB values > 0.\n""",
    
    "maxpoolaudiodays_2" : """This parameter controls the maximum number of days
the audio data is stored. This parameter accepts day values > 0.\n""",

    "maxpool_clean_obsolete" : """This parameter enables the absolute method
of spool cleaning, which is not indexed, therefore based on absolute paths,
which is slower since it requires a lot of directory scanning for larger sets
of spool data. It's not recommended by default. 
This parameter accepts values 'yes' and 'no'.\n""",

    "autocleanspoolminpercent" : """This parameter controls triggering of the
auto cleaning function based on the minimum % storage left in the 'spooldir'.
When auto cleaning is started, it reindexes the files and runs the cleaning
procedure again. This is typically set to 1 (for 1%), you can choose to set
otherwise. This functionality is enabled by default, to protect against
storage overrun.

In the event that the autocleaning doesn't work (the useable storage is still
insufficient), the 'maxpoolsize' is set to size of the 'spooldir' with the
maximum space set to MIN(autocleanspoolminpercent, autocleanmingb).
This parameter accepts values > 0.\n""",

    "autocleanmingb" : """This parameter controls triggering of auto cleaning
function based on the minimum storage left in GBs in 'spooldir'. When auto
cleaning starts, it reindexes the files and runs the cleaning procedure again.
This is typically set to a low value like 5 (for 5GB). This functionality is
enabled by default, to protect against storage overrun.

In the event that the autocleaning doesn't work (the useable storage is still
insufficient), the 'maxpoolsize' is set to size of the 'spooldir' with the
maximum space set to MIN(autocleanspoolminpercent, autocleanmingb).
This parameter accepts GB values > 0.\n""",

    # A useful command to manually clean all RTP type files that are 7 days or
    # older.
    # find /var/spool/voipmonitor -maxdepth 1 -type d -mtime +7 -name '20*' | 
    #   (while read d; do rm -rf $d/*/*/RTP; done)
    # You can replace 'RTP' with 'SIP', 'graph', 'audio' to delete respective
    # data files. Also, you can configure the value of the 'mtime' parameter to
    # configure the maximum age of the files to delete.

}