#!/usr/bin/env python3
"""Defining the function schools_by_topic"""

def schools_by_topic(mongo_collection, topic):
    """This function returns the list of school having a specific topic"""
    result = []
    documents = mongo_collection.find({"topics": topic})
    for document in documents:
        result.append(document)
    return result
