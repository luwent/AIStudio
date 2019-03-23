import os
import sys
import random
import datetime
from .ftp_service import FTPHandler

class IVUser():
    def __init__(self, psw, homedir):
        self.psw = psw
        self.cookie = ""
        self.login = False
        self.homedir = homedir
        self.ftp_handle = FTPHandler(homedir)
        
class IVAuthorizer(object):

    def __init__(self):
        self.user_table = {}
        self.load_user_table()
    
    def load_user_table(self): 
        self.user_table.clear()
        try:
            for line in open("users.ivu","r").readlines():
                login_info = line.split()
                dic = IVUser("", "")
            self.user_table[login_info[0]] = dic
        except:
            return		
 
    def add_user(self, username, password, homedir):
        if self.has_user(username):
            print('user %r already exists' % username)
        if(not homedir):    
            homedir = os.getcwd()
        if not isinstance(homedir, str):
            homedir = homedir.decode('utf8')
        if not os.path.isdir(homedir):
            print('no such directory: %r' % homedir)
        homedir = os.path.realpath(homedir)
        dic = IVUser(password, homedir)
        self.user_table[username] = dic

    def remove_user(self, username):
        if self.has_user(username):
            del self.user_table[username]

    def create_cookie(self):
        return str(random.random())
        
    def login_user(self, username, password):
        if not self.has_user(username):
            if len(self.user_table) == 0:
                self.add_user(username, password, os.getcwd())
                self.user_table[username].login = True
                self.user_table[username].cookie = self.create_cookie()
                print(username + ": login at " + str(datetime.datetime.now()))
                return 1, self.user_table[username].cookie
            return 0, "incorrect user name"
        if self.user_table[username].psw != password:
            return 0, "incorrect password"
        self.user_table[username].login = True
        self.user_table[username].cookie = self.create_cookie()
        print(username + ": login at " + str(datetime.datetime.now()))
        return 2, self.user_table[username].cookie

    def logout_user(self, username, cookie):
        if not self.has_user(username):
            return "You have log out"
        if(self.user_table[username].cookie == cookie):
            self.user_table[username].login = False
            print(username + ": logout at " + str(datetime.datetime.now()))
        return "You have log out"
        
    def get_home_dir(self, username):
        return self.user_table[username].homedir
        
    def get_ftp_handler(self, username, cookie):   
        if(username in self.user_table):
            if(self.user_table[username].login):
                if(self.user_table[username].cookie == cookie):
                    return self.user_table[username].ftp_handle
        return None 
        
    def has_user(self, username):
        return username in self.user_table
