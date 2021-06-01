import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("venv/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

'''student_data = {}

for x in range(10):
    name = input('Enter name: ')
    age = input('Enter age: ')
    gender = input('enter gender')
    city = input('enter city')
    student_data['name'] = name
    student_data['age'] = age
    student_data['gender'] = gender
    student_data['city'] = city
    db.collection('student').add(student_data)

data1={'name':'neetu', 'age':23, 'gender':'female'}
db.collection('student').document('a1').set(data1)

db.collection('student').document('a1').set({'city':'kolkata'},merge=True)

student_marks ={}
for x in range(3) :
    subject = input('enter subject: ')
    marks = input('marks')
    student_marks['subject'] = subject
    student_marks['marks'] = marks
    db.collection('student').document('a1').collection('subject_marks').add(student_marks)'''

'''dat = db.collection('student').get()
for data in dat:
    print(data.to_dict())'''

'''result = db.collection('student').document("p1").get()
print(result.to_dict())'''

'''result = db.collection('student').document("a1").get()
print(result.to_dict())'''

'''dat = db.collection('student').document("a1").collection('subject_marks').get()
for data in dat:
    print(data.to_dict())'''

'''dat = db.collection('student').where("age", "==", "21").get()
for data in dat:
    print(data.to_dict())'''

'''dat = db.collection('student').where("age", ">", "22").get()
for data in dat:
    print(data.to_dict())'''

'''dat = db.collection('student').where("city", "==", "delhi").get()
for data in dat:
    print(data.to_dict())'''


#db.collection('student').document("a1").update({"age": 50})

#db.collection('student').document("p1").update({"age": firestore.Increment(2)})

#db.collection('student').document("7qephQgRoDlGbJHPyeJc").update({"gender": "female"})

#db.collection('student').document("p1").update({"occupation": "engineer"})

'''dat = db.collection('student').where("age", ">", 20).get() # Get all documents with age >=40
for data in dat:
    key = data.id
    db.collection('student').document(key).update({"age_group":"youth"})'''

#db.collection('student').document("p1").delete()

#db.collection('student').document("a1").update({"age":firestore.DELETE_FIELD})

