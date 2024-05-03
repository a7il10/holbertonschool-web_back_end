#!/usr/bin/env python3
'''
NoSQL
'''

from operator import itemgetter


def top_students(mongo_collection):
    '''
    function that inserts a new document in a collection based on kwargs
    '''
    students = mongo_collection.find()
    student_scores = []

    for student in students:

        total_score = 0
        for course in student['scores']:
            total_score += course['score']
        average_score = total_score / len(student['scores'])
        student_scores.append({'_id': student['_id'], 'name': student['name'], 'averageScore': average_score})

    # Sort students by average score in descending order
    student_scores.sort(key=itemgetter('averageScore'), reverse=True)

    return student_scores
