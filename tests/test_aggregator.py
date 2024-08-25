from src.Server import Server
from src.Aggregator import Aggregator
import datetime

class TestAggregator:

    def test_always_passes(self):
        assert True
    
    def test_put(self):
        agg = Aggregator()
        log1 = {
                "timestamp": datetime.datetime(2024, 8, 25, 15, 9, 52, 630978),
                "serviceName": "test-service",
                "severity": "INFO",
                "message": "Test info message"
            }
        log2 = {
                "timestamp": datetime.datetime(2024, 8, 25, 15, 14, 52, 630978),
                "serviceName": "test-service N",
                "severity": "ERROR",
                "message": "Messaggio di test di errore"
            }
        agg.put(log1)
        agg.put(log2)
        logsAfterPut = agg.getLogs()
        assert logsAfterPut == [log1, log2]
    
    #TODO: def test_get_between(self):