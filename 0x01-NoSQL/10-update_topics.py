#!/usr/bin/env python3
"""
module: 10-update_topics
description: changes all topics of a school
document based on the name given.
"""


def update_topics(mongo_collection, name, topics):
    """@description.
    Args:
        mongo_collection (dict): pymongo object.
        name (string): field to update.
        topics (list): list of strings.
    Returns:
        Nothing.
    """
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
