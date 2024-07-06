import smtplib as sp
obj=sp.SMTP("smtp.gmail.com",587)
obj.ehlo()
obj.starttls()

obj.login("prateekrajbhar3311@gmail.com",'9919093311')
subject="python development"
body="you are selected from python development"
massage="subject:{}\n\n{}".format(subject, body)
list_files=["pratikrajbhar238@gmail.com",'sunilrajbhar264@gmail.com']
obj.sendmail('prateekrajbbhar3311@gmail.com',list_files,massage)
print('send main succefully')
obj.quit()
