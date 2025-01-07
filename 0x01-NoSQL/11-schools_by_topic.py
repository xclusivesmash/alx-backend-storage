#!/usr/bin/env python3
"""
module: 11-schools_by_topic
description: returns a list of schools having a specific
topic.
"""


def schools_by_topic(mongo_collection, topic):
    """@description.
    Args:
        mongo_collection (dict): pymongo object.
        topic (str): topic searched.
    Returns:
        list of schools.
    """
    myList = mongo_collection.find(
            {'topics': {
                '$elemMatch': {
                    '$eq': topic,
                    },
                },
             },
            )
    return [document for document in myList]
