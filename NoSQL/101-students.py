#!/usr/bin/env python3
'''
NoSQL
'''


from pymongo import MongoClient

def top_students(mongo_collection):
    """
    script that provides stats about Nginx logs stored in MongoDB
    """
    students = mongo_collection.find()
    for student in students:
        total = 0
        count = 0
        for score in student['scores']:
            total += score['score']
            count += 1
        student['averageScore'] = total / count

    sorted_students = sorted(list(students), key=lambda student: student['averageScore'], reverse=True)
    return sorted_students
