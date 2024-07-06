import smtplib as s
obj=s.SMTP('smtp.gmail.com',587)#587 email code
obj.ehlo() #predefined
obj.starttls()#predefined
obj.login("pratikrajbhar238@gmail.com","9919093311")
sub="hello world"
body="welcome to kashi"
massage="sub:{}\n\n{}".format(sub, body)
list=["prateekrajbhar238@gmail.com",
      "sunilrajbhar264@gmail.com"]
obj.sendmail=("pratikrajbhar238@gmail.com", list,massage)
print("Sent mail successfully")
obj.quit()