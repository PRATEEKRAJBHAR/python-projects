#a-z
#0-9
#. _ only one or nothing
#@ one
#. one 2,3
import re
user_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w {2,3}$"
user_email=input('plz enter your email address : ')
if re.search(user_condition,user_email):
    print("valid email")
else: 
    print("Invalid email")



