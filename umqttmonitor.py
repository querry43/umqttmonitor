"""
This module provides MQTTMonitor.
"""

import time
from umqtt.simple import MQTTClient

class MQTTMonitor:
    """
    MQTTMonitor is a wrapper around umqtt.simple.MQTTClient making it easy to dispatch actions from
    mqtt messages.
    """

    def __init__(self, mqtt_client_params, mqtt_topic, debug=False):
        self.mqtt_client_params = mqtt_client_params
        self.mqtt_topic = mqtt_topic
        self.debug = debug

        self.action_table = []
        self.mqtt_client = None
        self.version = '0.1'

    def add_action(self, pattern, func):
        """
        Add actions to the dispatch table.  If the regex pattern matches the topic, the function is
        called with the topic and message as arguments.
        """
        self.action_table.append((pattern, func))

    def connect(self):
        """
        Connect to the mqtt server.
        """
        self.mqtt_client = MQTTClient(**self.mqtt_client_params)
        self.mqtt_client.set_callback(self.__mqtt_callback)
        self.mqtt_client.connect()
        self.mqtt_client.subscribe(self.mqtt_topic)

    def __mqtt_callback(self, topic, msg):
        if self.debug:
            print('{} : {} - {}'.format(time.time(), topic, msg))
        for (pattern, func) in self.action_table:
            if pattern.match(topic):
                func(topic, msg)

    def run(self):
        """
        Begin running the monitor.  This method loops forever and does not return.
        """
        while True:
            self.mqtt_client.wait_msg()

    def run_once(self):
        """
        Receive and respond to a single message from mqtt.
        """
        self.mqtt_client.check_msg()
