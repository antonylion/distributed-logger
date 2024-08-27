from threading import Thread
from time import sleep
import logging
import random
import datetime
from .Aggregator import Aggregator

class Server(Thread):
    
    def __init__(self, name, maxLogInterval, aggregator: Aggregator):
        super().__init__()
        self.name = name # instance attribute
        self.maxLogInterval = maxLogInterval
        self.format = "%(asctime)s: %(message)s"
        self.aggregator = aggregator
        self.running = True
        logging.basicConfig(format=self.format, level=logging.INFO, datefmt="%H:%M:%S")
    
    def pickSeverityMessage(self, probability):
        if probability < 0.2:
            return "ERROR", "An error has occured"
        elif probability >= 0.2 and probability < 0.6:
            return "WARN", "This is a warning"
        else:
            return "INFO", "This is a general information"
    
    def stopServer(self):
        self.running = False
    
    def isWorking(self):
        return self.running
    
    def run(self):
        # Infinite loop for producing logs
        while(self.isWorking):
            if self.running == False:
                break
            nextWait = int(random.random()*10) + 1
            sleep(nextWait)
            p = random.random()
            severity, message = self.pickSeverityMessage(p)
            timestamp = datetime.datetime.utcnow()#.strftime("%Y-%m-%dT%H:%M:%SZ")
            serviceName = self.name
            log = {
                "timestamp": timestamp,
                "serviceName": serviceName,
                "severity": severity,
                "message": message
            }
            # load the log into the Aggregator
            self.aggregator.put(log)
            print(f"Server {self.name}:")
            print(log)