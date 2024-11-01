#!/usr/bin/env python3
"""Function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """
        Updates the topics list for a school in the MongoDB collection.

        Args:
            mongo_collection: A PyMongo collection object.
            name: The name of the school to update.
            topics: A list of strings representing
                    the topics approached in the school.

        Returns:
            None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
