#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
        Returns a list of school names that have a specific topic.

        Args:
            mongo_collection: A PyMongo collection object.
            topic: The topic to search for.

        Returns:
            A list of school names.
    """
    return mongo_collection.find({"topics": topic})
