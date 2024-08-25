from src.Server import Server
from src.Aggregator import Aggregator
import pytest

@pytest.fixture(scope="class")
def setup():
    agg = Aggregator()
    server = Server("test-server", 5, agg)
    yield server
    #server.stopServer()  # Cleanup code if necessary

class TestServer:

    def test_always_passes(self):
        assert True
    
    def test_error_log_occurance(self, setup):
        server = setup
        severity, _ = server.pickSeverityMessage(0.15)
        assert severity == "ERROR"
    
    def test_running_server(self, setup):
        server = setup
        assert server.isWorking() == True
    
    def test_stop_server(self, setup):
        server = setup
        server.stopServer()
        assert server.isWorking() == False
        # This test should be better, because after it the server is down. TEARDOWN phase of pytest?