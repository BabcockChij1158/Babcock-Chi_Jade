def printf(info, other):
    print("*{:>15}{:>15} *".format(info, other))

fname = input("Enter your first name:")
lname = input("Enter your last name:")
title = input("Enter your title:")
school = input("Enter your school site:")
year = input("Enter the school year:")
subject = input("Enter your subject:")

print("*********************************")
printf(school, year)
printf(fname, lname)
printf(title, subject)
print("*********************************")
