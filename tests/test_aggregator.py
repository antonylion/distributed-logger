from src.Aggregator import Aggregator
import datetime
from io import StringIO
import sys

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
    
    #This is a nice test because it tests what will appear on the STDOUT, by redirecting it :)
    #def test_display(self): 
    #    capturedOutput = StringIO()         # Make StringIO.
    #    sys.stdout = capturedOutput                  # Redirect stdout.
    #    print("Foooo!")
    #    sys.stdout = sys.__stdout__                  # Reset redirect.
    #    #print 'Captured', capturedOutput.getvalue()  # Now works.
    #    print("Captured output:")
    #    print(capturedOutput.getvalue())
    
    #TODO: def test_get_between(self):

    #def temp_display(self):
    #    agg = Aggregator()
    #    log1 = {
    #            "timestamp": datetime.datetime(2024, 8, 25, 15, 9, 52, 630978),
    #            "serviceName": "test-service",
    #            "severity": "INFO",
    #            "message": "Test info message"
    #        }
    #    log2 = {
    #            "timestamp": datetime.datetime(2024, 8, 25, 15, 14, 52, 630978),
    #            "serviceName": "test-service N",
    #            "severity": "ERROR",
    #             "message": "Messaggio di test di errore"
    #        }
    #    agg.put(log1)
    #    agg.put(log2)
    #    with open('expected_display.txt', 'r') as f:
    #        expected_display = f.readline()
    #        capturedOutput = StringIO()         # Make StringIO.
    #        sys.stdout = capturedOutput                  # Redirect stdout.
    #        agg.display()
    #        received_display = capturedOutput.getvalue()
    #       sys.stdout = sys.__stdout__                  # Reset redirect.
    #        assert received_display == expected_display
