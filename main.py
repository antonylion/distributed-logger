from src.Aggregator import Aggregator
from src.Server import Server
from time import sleep
import datetime

def main():
    sharedAggregator = Aggregator()

    service1 = Server("Service1", 10, sharedAggregator)
    service2 = Server("Service2", 8, sharedAggregator)
    service3 = Server("Service3", 5, sharedAggregator)
    service1.start()
    service2.start()
    service3.start()
    sleep(10)

    service1.stopServer()
    service2.stopServer()
    service3.stopServer()

    service1.join()
    service2.join()
    service3.join()

    sharedAggregator.display()
    print()
    print("Now let's search in a timestamp range")
    now = datetime.datetime.utcnow()
    now_starting_minute = datetime.datetime(
        int(now.year),
        int(now.month),
        int(now.day),
        int(now.hour),
        int(now.minute),
        0,
        0
    )

    sharedAggregator.displayBetween([now_starting_minute,now])

    print()
    print("These are all the WARN logs")
    sharedAggregator.displayBySeverity("WARN")

    print()
    subcontent = input("Enter what you want to search in messages: ")
    sharedAggregator.displayByMessageContent(subcontent)


if __name__ == '__main__':
    main()