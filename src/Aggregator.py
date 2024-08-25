from threading import Lock
import datetime

class Aggregator():
    logsByTimestamp = {}
    logsBySeverity = {}
    logs = []

    def __init__(self):
        self.lock = Lock()
    
    def put(self, log):
        with self.lock:
            if log["timestamp"] not in self.logsByTimestamp:
                self.logsByTimestamp[log["timestamp"]] = []
            self.logsByTimestamp[log["timestamp"]].append(log)
            
            if log["severity"] not in self.logsBySeverity:
                self.logsBySeverity[log["severity"]] = []
            self.logsBySeverity[log["severity"]].append(log)

            self.logs.append(log)
    
    def display(self):
        print("This is the list of logs")
        print(self.logs)
    
    def displayBetween(self, timestamps):
        timestamp1 = timestamps[0]
        timestamp2 = timestamps[1]
        output = []
        for k in self.logsByTimestamp:
            if k >= timestamp1 and k <= timestamp2:
                output.append(self.logsByTimestamp[k])
        
        print(output)
    
    def displayBySeverity(self, severity):
        print(self.logsBySeverity[severity])
    
    def displayByMessageContent(self, subcontent):
        output = []
        for t_logs in self.logsByTimestamp.values():
            for log in t_logs:
                if subcontent in log["message"]:
                    output.append(log)
        print(output)