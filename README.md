# umqttmonitor

MQTTMonitor is a tool for micropython based on umqtt.simple.MQTTClient.

## Synposis
```
import re
import umqttmonitor import MQTTMonitor

# see umqtt.simple.MQTTClient for parameters
mqtt_client_params = {
    'client_id': 'my-id',
    'server': '10.0.0.123',
}

mqtt_topic = b'some/topic/#'

monitor = MQTTMonitor(
    mqtt_client_params=mqtt_client_params,
    mqtt_topic=mqtt_topic,
)

def my_action(topic, msg):
    print('{} : {}'.format(topic, msg))

# if the topic matches the regex, my_action is called
monitor.add_action(
    pattern=re.compile('.*/my-door/lock$'),
    func=my_action
)

# connect to the mqtt broker
monitor.connect()

# fetch and respond to a single mqtt message (if one is available)
monitor.run_once()

# run a loop forever
monitor.run()
```

## Installation

Copy the umqttmonitor.py file to your micropython device.

## MQTTMonitor

### Constructor

Parameters:

* `mqtt_client_params` - dictionary of parameters passed to umqtt.simple.MQTTClient.
* `mqtt_topic` - mqtt topic to subscribe to, can include * and # wildcards.
* `debug=False` - enables debug prints.

### add_action

Add a pattern and a function. When the pattern matches the topic, the function is called.

Parameters:

* `pattern` - compiled regex to compare with message topics.
* `func` - a function accepting two arguments: topic and message.

### connect

Connect to the mqtt service.

### run_once

If any messages are available, fetch one message and run any matching actions.

### run

Like `run_once`, except this loops forever running any matching actions.
