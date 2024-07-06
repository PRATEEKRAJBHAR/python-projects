from instabot import Bot
prateek=Bot()
prateek.login(username="pratikrajbhar238",password="beenu@123")
#prateek.follow("the_engineer_sahab")
#prateek.upload_photo("C:/Desktop/hari-om.jpg/hari-om")
#prateek.send_message("i love python",["babybhardwaj"])
'''followers=prateek.get_user_followers(username="pratikrajbhar238")
for follower in followers:
    print(prateek.get_user_info(follower))'''

following=prateek.get_user_following(username="pratikrajbhar238")
for Following in following:
    print(prateek.get_user_info(Following))
