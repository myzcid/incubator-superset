# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import os


def get_env_variable(var_name, default=None):
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = 'The environment variable {} was missing, abort...'\
                        .format(var_name)
            raise EnvironmentError(error_msg)

MYSQL_USER = get_env_variable('MYSQL_USER')
MYSQL_PASSWORD = get_env_variable('MYSQL_PASSWORD')
MYSQL_DATABASE = get_env_variable('MYSQL_DATABASE')

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@127.0.0.1:3306/%s' % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)

# SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.100.26:3306/superset"

REDIS_HOST = get_env_variable('REDIS_HOST')
REDIS_PORT = get_env_variable('REDIS_PORT')


class CeleryConfig(object):
    BROKER_URL = 'redis://%s:%s/0' % (REDIS_HOST, REDIS_PORT)
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'redis://%s:%s/1' % (REDIS_HOST, REDIS_PORT)
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
    CELERY_TASK_PROTOCOL = 1


CELERY_CONFIG = CeleryConfig

BABEL_DEFAULT_LOCALE = "zh"

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = "pk.eyJ1IjoieGluZ2NhbiIsImEiOiJjazA0bTF0eWEyMGh6M25wZGNtdmJxZXpzIn0.4MOlFD_220-v9nyvkVfqYg"
AUTH_USER_REGISTRATION_ROLE = 'Alpha'