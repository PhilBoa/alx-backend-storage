#!/usr/bin/env python3
"""
Module to interact with MongoDB collections.
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object.

    Returns:
        list: List of students sorted by their average score in descending
        order.
    """
    students = list(mongo_collection.find())

    for student in students:
        total_score = sum(subject['score'] for subject in student['topics'])
        average_score = total_score / len(student['topics']) if \
            student['topics'] else 0
        student['averageScore'] = average_score

    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
