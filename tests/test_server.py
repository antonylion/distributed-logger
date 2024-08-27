from src.Server import Server
from src.Aggregator import Aggregator
import pytest
import time

@pytest.fixture(scope="class")
def setup():
    agg = Aggregator()
    server = Server("test-server", 5, agg)
    yield server
    #server.stopServer()  # Cleanup code if necessary

class TestServer:

    def test_always_passes(self):
        assert True
    
    def test_server_run(self):
        #server = setup
        agg = Aggregator()
        server = Server("test-server", 5, agg)
        server.start()  # Start the server thread
        time.sleep(2)  # Let it run for a short period
        server.stopServer()  # Stop the server after a while
        server.join()  # Ensure the thread has finished
        
        # You could add assertions here to check if logs were produced, etc.
        assert not server.isWorking()
    
    def test_error_log_occurance(self, setup):
        server = setup
        severity, _ = server.pickSeverityMessage(0.15)
        assert severity == "ERROR"
    
    def test_info_log_occurance(self, setup):
        server = setup
        severity, _ = server.pickSeverityMessage(0.8)
        assert severity == "INFO"
    
    def test_warn_log_occurance(self, setup):
        server = setup
        severity, _ = server.pickSeverityMessage(0.4)
        assert severity == "WARN"
    
    def test_running_server(self, setup):
        server = setup
        assert server.isWorking() == True
    
    def test_stop_server(self, setup):
        server = setup
        server.stopServer()
        assert server.isWorking() == False
        # This test should be better, because after it the server is down. TEARDOWN phase of pytest?