#!/usr/bin/env python3
""" 8-all.py """

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Returns:
    list: A list of documents, or an empty
    list if the collection is empty.
    """
    return list(mongo_collection.find())

