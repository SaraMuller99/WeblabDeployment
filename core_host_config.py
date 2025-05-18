# It must be here to retrieve this information from the dummy
core_universal_identifier       = 'bc8573c9-fe84-416c-898c-26ee13fe4615'
core_universal_identifier_human = u'Generic system; not identified'

db_engine          = u'sqlite'
db_host            = u'localhost'
db_port            = None # None for default
db_database        = u'WebLab'
weblab_db_username = u'weblab'
weblab_db_password = u'weblab'

debug_mode   = True



#########################
# General configuration #
#########################

server_hostaddress = u'localhost'
server_admin       = u''

################################
# Admin Notifier configuration #
################################

mail_notification_enabled = False

##########################
# Sessions configuration #
##########################

core_session_type = u'Memory'

# session_sqlalchemy_engine   = u'sqlite'
# session_sqlalchemy_host     = u'localhost'
# session_sqlalchemy_username = u''
# session_sqlalchemy_password = u''

# session_lock_sqlalchemy_engine   = u'sqlite'
# session_lock_sqlalchemy_host     = u'localhost'
# session_lock_sqlalchemy_username = u''
# session_lock_sqlalchemy_password = u''

# session_redis_host = u'localhost'
# session_redis_port = 6379
# core_session_pool_id = 1
# core_alive_users_session_pool_id = 1

##############################
# Core generic configuration #
##############################
core_store_students_programs      = False
core_store_students_programs_path = 'files_stored'
core_experiment_poll_time         = 350 # seconds

core_server_url = u'http://localhost/weblab/'

############################
# Scheduling configuration #
############################

core_coordination_impl = u'sqlalchemy'

# coordinator_redis_db       = None
# coordinator_redis_password = None
# coordinator_redis_port     = None
# coordinator_redis_host     = None

core_coordinator_db_name      = u'WebLabCoordination'
core_coordinator_db_engine    = u'sqlite'
core_coordinator_db_host      = u'localhost'
core_coordinator_db_username  = u'weblab'
core_coordinator_db_password  = u'weblab'

core_coordinator_laboratory_servers = {
    'laboratory1:laboratory1@core_host' : {
            'exp1|electronics|Electronics experiments' : 'electronics1@electronics_queue',
        },

}

core_scheduling_systems = {
        'electronics_queue'            : ('PRIORITY_QUEUE', {}),
    }

