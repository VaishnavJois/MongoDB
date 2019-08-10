#import pymongo
import database as dbase

#########################

#while True:
print('********************************')

print('1.Add new faculty')
print('2.Add subject to faculty')
print('3.Remove subject from faculty')
print('4.Increment experience by one year')
print('5.Update qualification')
print('6.Delete faculty')
print('7.Display total duration by faculty')
print('8.Display subject with faculty name')
print('9.Display all faculty information')
print('0.EXIT')
d = int(input('Enter choice : '))


if d == 1:
    dbase.add_new_faculty()
    print('Faculty inserted successfully')

elif d == 2:
    id = int(input('Enter id: '))
    dbase.add_subject_to_faculty(id)
    print(f'Subject added successfully')

elif d == 3:
    dbase.remove_subject_from_faculty()
    print('Subject removed successfully')

elif d == 4:
    dbase.increment_exp_by_one_year()
    print('Experience incremented successfully')
elif d == 5:
    dbase.update_qualification()
    print('Qualification updated successfully')

elif d == 6:
    dbase.del_faculty()
    print(f'Faculty removed successfully')
elif d == 7:
    dbase.total_duration_by_faculty()

elif d == 8:
    dbase.subject_with_faculty_name()

elif d == 9:
    dbase.display_all()

else:
    exit(0)