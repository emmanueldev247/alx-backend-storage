#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
        Lists all documents in a MongoDB collection.

        Args:
            mongo_collection: A PyMongo collection object.

        Returns:
            A list of dictionaries, where each dictionary represents
            a document in the collection.
            If the collection is empty, an empty list is returned.
    """
    doc_list = []
    for doc in mongo_collection.find():
        doc_list.append(doc)
    return doc_list
