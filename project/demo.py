#prateekrajbhar238@gmail.com
#lenth maximum of  6 digits
#.(dot) only one use count reverse
#@ only one use
#first letter is alphabet
#without any spaces
#not upper alphabet
#email always .,@,_ and digit used
email=input("plz enter a valid email address :--")
k,j,l=0,0,0
if len(email)>=6:
    if (email[-4]==".") ^ (email[-3]=="."):
        if("@" in email) and (email.count("@")==1):
             if email[0].isalpha():
                  for i in email:
                       if i==i.isspace():
                            k=1
                       elif i.isalpha():
                            if i==i.upper():
                                 j=1
                            elif i.isdigit():
                                 continue      
                            elif i=="_" or i=="." or i=="@":
                                 continue
                            else:
                                 l=1
                       if k==1 or j==1 or l==1:
                        print("invalid email address 5")
                       else:
                            print("right email address")
             else:
                  print("invalid email address 4")
        else:
            print("invalid email address 3")
    else:
            print("invalid email address 2")
else:
    print("invalid email address 1")