#!/usr/bin/env python3
"""
Module to interact with MongoDB collections.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object.
        topic (str): The topic to search.

    Returns:
        list: A list of school documents having the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
