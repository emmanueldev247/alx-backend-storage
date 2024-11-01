#!/usr/bin/env python3
"""Function that inserts a new document in a collection based on `kwargs`"""


def def insert_school(mongo_collection, **kwargs):
    """
        Inserts a school document into the specified MongoDB collection.

        Args:
            mongo_collection: A PyMongo collection object.
            **kwargs: Keyword arguments representing the fields and
                      values of the school document.

        Returns:
            The inserted document ID.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
