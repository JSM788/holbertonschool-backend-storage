#!/usr/bin/env python3
"""Defining the function top_students"""


def top_students(mongo_collection):
    """This function returns all students sorted by average score"""
    result = mongo_collection.aggregate([
        { "$unwind": "$topics" },
        { "$group": {
            "_id": "$_id",
            "name": { "$first": "$name" },
            "averageScore": { "$avg": "$topics.score" }
        }},
        { "$sort": { "averageScore": -1 } }
    ])
    return list(result)
