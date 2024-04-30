#!/usr/bin/env python3
""" Top students """


def top_students(mongo_collection):
    lst = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }},
        {"$sort": {"averageScore": -1}}
        ]
    return mongo_collection.aggregate(lst)
