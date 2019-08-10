import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017")

db = conn["assignment"]

collection = db["employee"]

######################################################################

def add_new_faculty():
    id = int(input('Enter id : '))
    name = input('Enter the name : ')
    age = int(input('Enter age : '))
    gender = input('Gender : ')
    qual = input('Qualification: ')
    exp = int(input('Experience :'))
    type = input('FT/PT : ')
    if type[0]=='F':
        type = 'Full Time'
    else:
        type = 'Part Time'
    sub = input('Enter the name of subject : ')
    hrs = int(input('Enter the number of hours : '))
    subjects = [{'sub_name':sub,'s_hours':hrs}]

    ls = {"_id":id,
        "name":name,
        "age":age,
        "gender":gender,
        "exp":exp,
        "type":type,
        "subjects":subjects,
        "qualification":qual}
    
    collection.insert_one(ls)

def add_subject_to_faculty(id):
    name = input('Enter subject name: ')
    hours = int(input('Enter number of hours: '))
    n_sub = {'sub_name':name,'s_hours':hours}

    collection.update_one( {"_id":id}, {'$push' : {"subjects" : n_sub } })


def remove_subject_from_faculty():
    id = int(input('Enter id: '))
    sub = input('Enter subject: ')
    db.collection.update_one({'_id':id},{'$pull':{'subjects.sub_name':sub}})


def increment_exp_by_one_year():
    id = int(input('Enter ID of the employee:'))
    collection.update_one({'_id':id},{'$inc':{'exp':1}})
    

def update_qualification():
    id = int(input('Enter id: '))
    n_qual = input('Enter new qualification:')
    collection.update_one({'_id':id},{'$set':{'qualification':n_qual}})

def del_faculty():
    id = int(input('Enter id: '))

    collection.delete_one({'_id':id})

def total_duration_by_faculty():
    pipe = [
        {'$unwind':"$subjects"},
        {'$group':{'_id':'$name',"t_hours":{'$sum':"$subjects.s_hours"}}},
        {'$project':{'name':'$_id','_id':0,'hours':'$t_hours'}}
    ]
    
    td = collection.aggregate(pipe)
    td = list(td)
    # print(td)
    for t in td:
        print(f'Name: {t["name"]}\tTotal Duration: {t["hours"]}')

def subject_with_faculty_name():
    pipe = [{"$unwind":"$subjects"},
             {'$project':{'_id':0,'name':1,'sub':'$subjects.sub_name'}}
            ]
    sf = collection.aggregate(pipe)
    sf = list(sf)
    # print(sf)
    for i in sf:
        print(f'Name: {i["name"]}\tSubject: {i["sub"]}')


def display_all():
    print('**********DETAILS**********')
    for doc in collection.find({}):
        print('***************')
        print(f'Name: {doc["name"]} \nAge: {doc["age"]} \nExperience: {doc["exp"]}')
        print(f'Type: {doc["type"]}')
        print(f'Qualification: {doc["qualification"]}')
        print('Subjects:')
        for this in doc["subjects"]:
            print(f'**Subject name: {this["sub_name"]}')
            print(f'**Hours: {this["s_hours"]}')


