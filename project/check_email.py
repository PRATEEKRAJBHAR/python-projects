email=input("plz enter your email address :")#pratik123@gmail.com
k,j,l=0,0,0
if len(email)>=6:#1
    if (email[-4]==".") ^ (email[-3]=="."):#2
        if email[0].isalpha():#3
            if ("@" in email) and (email.count("@")==1):#4
                    
                #if ("." in email) and (email.count()==1):
                    for i in email:
                        if i==i.isspace():#5
                            k==1
                        elif i.isalpha():
                            if i==i.upper():#5
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            l=1
                    if k==1 or j==1 or l==1:
                    #else:
                     print("wrong email id 5")

                    else:
                     print("right email")
            else:
                print("wrong email id 4")
        else:
            print("wrong email id 3")
    else:
        print("wrong email id 2")
else:
    print("wrong email id 1")