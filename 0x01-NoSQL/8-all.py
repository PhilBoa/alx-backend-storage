#!/usr/bin/env python3
"""
Module to interact with MongoDB collections.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object.

    Returns:
        list: A list containing all documents in the collection.
              Returns an empty list if there are no documents.
    """
    return mongo_collection.find()
