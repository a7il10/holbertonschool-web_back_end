#!/usr/bin/env python3
'''
NoSQL
'''


def top_students(mongo_collection):
    '''
    function that inserts a new document in a collection based on kwargs
    '''
    students = mongo_collection.find()
    for student in students:
        total_score = 0
        count = 0
        for topic in student['topics']:
            total_score += topic['score']
            count += 1
        student['averageScore'] = total_score / count

    sorted_students = sorted(students, key=lambda student: student['averageScore'], reverse=True)
    return sorted_students
