
"""
CRUD:

Create
Read
Update
Delete

Student CRUD:

#WRONG:  GET: students/1/delete -> 200, Student deleted

READ -> GET: students/1
UPDATE -> PUT: students/1
DELETE -> DELETE: students/1
CREATE -> POST: students

EDIT HOMEWORK -> PATCH students/1/homework/3
REQUEST BODY -> {"hw_url": "https://example.com/homework/3"}


"""

"""
HTTP RESPONSE CODES:
100 - informational
200 - success
300 - redirect
400 - client error
500 - server error


"""