#
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
# under the License
#

"""
Utility classes to retrieve information from local docker environment.
"""
import docker


class DockerUtil(object):
    """
    Utility class to interact with local docker environment, providing
    basic information on images and containers.
    """

    CONTAINER_STATUS_RUNNING = "running"
    CONTAINER_STATUS_EXITED = "exited"

    cli = docker.from_env()

    @staticmethod
    def get_container(name):
        """
        Returns the container instance for the given name.
        A docker.errors.NotFound exception is raised in case the given
        container does not exist.
        :param name:
        :return:
        """
        return DockerUtil.cli.containers.get(name)

    @staticmethod
    def get_container_ip(name, network_name='bridge'):
        """
        Returns the IPAddress assigned to the given container name (on the given network).
        :param name:
        :param network_name:
        :return:
        """
        container = DockerUtil.get_container(name)
        return container.attrs['NetworkSettings']['Networks'][network_name]['IPAddress']

    @staticmethod
    def stop_container(name):
        """
        Stops a given container based on its name or id.
        :param self:
        :param name:
        :return:
        """
        container = DockerUtil.get_container(name)
        container.stop()

    @staticmethod
    def start_container(name):
        """
        Starts the given container based on its name or id.
        :param self:
        :param name:
        :return:
        """
        container = DockerUtil.get_container(name)
        container.start()