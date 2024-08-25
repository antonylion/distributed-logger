### Problem: **Distributed Log Aggregator**

#### **Context:**
You are working for a company that has multiple microservices running on different servers. Each microservice logs its operations, errors, and other relevant information to local log files. Your task is to design and implement a distributed log aggregator system that can:

1. **Collect logs** from multiple servers in real-time.
2. **Aggregate** these logs by timestamp and severity level.
3. **Query** aggregated logs based on various filters (e.g., time range, severity level, message content).
4. **Scale** to handle large amounts of log data efficiently.

#### **Requirements:**

1. **Log Collection:**
   - Implement a system that can continuously collect logs from multiple servers.
   - Each server produces logs with the following structure:
     ```json
     {
       "timestamp": "2024-08-24T15:03:17Z",
       "service_name": "service_1",
       "severity": "ERROR",
       "message": "An error occurred."
     }
     ```
   - Assume logs are generated in JSON format and can be streamed to a central aggregator.

2. **Log Aggregation:**
   - Design a data structure to store logs efficiently in memory for quick access.
   - Logs should be aggregated by timestamp and severity level.

3. **Log Querying:**
   - Implement a query interface that allows for the following types of queries:
     - Retrieve all logs within a specific time range.
     - Retrieve logs based on severity (e.g., "ERROR", "WARN", "INFO").
     - Search logs by message content using keyword matching.

4. **Scalability:**
   - Your system should be capable of handling large volumes of log data.
   - Consider how you would scale the system to handle logs from hundreds or thousands of servers.
   - Think about partitioning logs by time, service, or other criteria to ensure efficient querying and storage.

5. **Concurrency:**
   - Ensure that your system can handle concurrent log writes and queries.
   - Implement appropriate locking or synchronization mechanisms to avoid race conditions.

#### **Bonus Challenges:**
- Implement the log collector as a distributed system using Python's `asyncio` or multithreading/multiprocessing.
- Store aggregated logs in a persistent database and ensure that queries can be performed across both in-memory and persisted data.
- Implement a basic front-end API (e.g., using Flask or FastAPI) to allow users to interact with the log aggregator.

#### **Deliverables:**
- A Python module or set of modules that implement the log aggregator system.
- Unit tests to verify the functionality of each component.
- Documentation explaining the design decisions, how to run the system, and how to query the logs.

#### **Example Scenario:**
```python
# Example Log Entry
log_entry = {
    "timestamp": "2024-08-24T15:03:17Z",
    "service_name": "service_1",
    "severity": "ERROR",
    "message": "An error occurred."
}

# Example Queries
aggregator.query_logs(time_range=("2024-08-24T15:00:00Z", "2024-08-24T16:00:00Z"))
aggregator.query_logs(severity="ERROR")
aggregator.query_logs(message_contains="error")
```

---

### Key Concepts to Focus On:
- **Concurrency and Parallelism:** How to handle multiple log sources concurrently.
- **Data Structures:** Efficient storage and retrieval of log data.
- **Scalability:** Designing systems that can scale out horizontally.
- **Testing:** Ensuring robustness and correctness with unit and integration tests.

This problem is designed to test your ability to design scalable systems, work with concurrency, and manage large datasets—all key skills for a software engineer. Good luck!