from datadog import initialize, statsd
import time

options = {
    'statsd_host': "192.168.49.2", #ip of the node, in this case minikube
    'statsd_port':8125
}

initialize(**options)

while(1):
  statsd.increment('example_metric.increment', tags=["mytag:dev"])
  statsd.decrement('example_metric.decrement', tags=["mytag:dev"])
  time.sleep(10)