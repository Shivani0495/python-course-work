class hotstar():
    def __init__(self,username,pwd):
        self.username=username
        self.__pwd=pwd
        print(f"Hello {self.username}.yu=ou have successfully logged in")
    def content_access(self):
        print("Welcome to hotstar\nlimited content")
    def ads(self):
        print('ads.... are running')
    def videoqua(self):
        print("video is playing in 720p")
    def livesport(self):
        print("you dont have access to live sports")
    def download(self):
        print("you can't able to download the videos")
    def logins(self):
        print("you can login in single device at a time")

class premium(hotstar):
    def __init__(self,username,pwd):
        self.username=username
        self.__pwd=pwd
        print(f"Hello {self.username}.you have successfully logged in")
    def content_access(self):
        print("Welcome to hotstar\nall content")
    def ads(self):
        print('No ads.... enjoy the content')
    def videoqua(self):
        print("video is playing in 4k")
    def livesport(self):
        print("you  have access to live sports")
    def download(self):
        print("you can download the video and see in offline also")
    def logins(self):
        print("you can login in multiple device at a time")

shivani=hotstar("shivani","shivani123")
shivani.content_access()
shivani.ads()
shivani.videoqua()
shivani.livesport()
shivani.download()
shivani.logins()

bhavani=premium("bhavani","bhavani123")
bhavani.content_access()
bhavani.ads()
bhavani.videoqua()
bhavani.livesport()
bhavani.download()
bhavani.logins()
