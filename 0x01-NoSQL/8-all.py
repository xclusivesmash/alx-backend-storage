#!/usr/bin/env python3
"""
module: 8-all
description: list all documents in a collection.
"""
import pymongo


def list_all(mongo_collection):
    """list all docs. in mongo_collection
    Args:
        mongo_collection (dict): contains all docs.
    Returns:
        empty list when no doc is found.
    """
    return mongo_collection.find()
