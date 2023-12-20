#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient
from collections import Counter


def log_stats():
    """
    Retrieves and displays statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Count total logs
    total_logs = collection.count_documents({})

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Count status check (method=GET, path=/status)
    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"})

    # Count IPs
    ips = [log['ip'] for log in collection.find({}, {"ip": 1})]
    top_ips = Counter(ips).most_common(10)

    # Display stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_count.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip, count in top_ips:
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log_stats()
