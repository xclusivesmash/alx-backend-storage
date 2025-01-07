#!/usr/bin/env python3
"""
module: 9-insert_school
description: inserts a new document.
"""


def insert_school(mongo_collection, **kwargs):
    """@description
    Args:
        mongo_collection (dict): collection in db.
        kwargs (dict): key-value items.
    Returns:
        new id
    """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
