import sys
sys.path.append('../')

import re
from umqttmonitor import MQTTMonitor

# see https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html
mqtt_client_params = {
  'client_id': 'my-id',
  'server': '10.0.0.37',
}
mqtt_topic = b'#'

monitor = MQTTMonitor(
  mqtt_client_params=mqtt_client_params,
  mqtt_topic=mqtt_topic,
  debug=True
)

def my_action(topic, msg):
    print('{} : {}'.format(topic, msg))

monitor.add_action(
  pattern=re.compile('.*deadbolt.*/lock$'),
  func=my_action
)

monitor.connect()
monitor.run()
