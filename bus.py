from queue import Queue
from collections import defaultdict

class Bus:
    def __init__(self):
        self.queues = defaultdict(Queue)

    def publish(self, topic, msg):
        if topic in self.queues:
            self.queues[topic].put(msg)
        else:
            q = Queue()
            q.put(msg)
            self.queues[topic] = q

    def subscribe(self, topic):
        return self.queues[topic]
