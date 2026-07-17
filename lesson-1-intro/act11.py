from pprint import pprint

student = {
    'name' : 'David',
    'grade' : '12th',
    'school_name' : 'Skylark High School',
    'address' : {
        'pin' : 17526,
        'city' : "NYC",
        'Country' : "USA"
        
    }

}

print(student['name'])
print(student['address']['city'])

student['favcolor'] = "Green"

student.pop("favcolor")
pprint(student, sort_dicts=False)

_ids = ["1001","1002","1003","1004"]
names = ["John","Tim","Walter","Bruce"]
emp_records = dict(zip(_ids,names))

pprint(emp_records)