
    #start se condition ko rakhanek k liye ^ ka use karte hai
    #string ke ander regEx ke though koi characters search karte hai to o (\)slash ke though karte hai
    #iske baad []? ka use karte h ye ? zero and one par kaam karta hai.koi char hoga to ek hi nhi to ek bhi nhi
    # \w string ke ander specific value ko serach karne ka kaam karta hai.
    #reverse condition search krne ke liye $ ka use karte hai
#1> a-z
#2> 0-9
#3> . _ only one time
#4> @ only one time
#5> . reverse se 2,3 index par aana chahiye
import re
user_email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_input=input("Please enter your email address:")
if re.search(user_email, user_input):
    print("this is a valid email address")
else:
    print("this is not a valid email address")
