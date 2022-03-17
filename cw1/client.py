from cmd import Cmd
import os
import sys
import requests

#todo 改URL
url = 'http://127.0.0.1:8000'

class Client(Cmd):
    prompt = 'CW1>'
    intro = 'This is CW1 by Yunjia Feng'

    def __init(self):
        # reload(sys)
        sys.setdefaultencoding('utf-8')
        Cmd.__init__(self)

    def do_exit(self,arg):
        print('See you.')
        return True

    def do_register(self,arg):
        username = input("Please enter username:")
        email = input("Please enter email:")
        password = input("Please enter password:")
        url = "http://127.0.0.1:8000/viewRegister"
        p = {"username": username,
             "email": email,
             "password": password}
        a = requests.get(url, params=p)
        print(a.text)

    def do_login(self,arg):
        arg = arg.strip().split(" ")
        if len(arg) != 1:
            print("Wrong number of parameters! use syntax 'login url'")
        else:
            url = arg[0]
            username = input("Please enter username:")
            password = input("Please enter password:")
            url += "/viewLogin"
            p = {"username": username,
                 "password": password}
            a = requests.get(url, params=p)
            print(a.text)

    def do_logout(self,arg):
        url = "http://127.0.0.1:8000/viewLogout"
        a = requests.get(url)
        print(a.text)

    def do_list(self,arg):
        url = "http://127.0.0.1:8000/viewModules"
        a = requests.get(url)
        print(a.text)

    def do_view(self,arg):
        url = "http://127.0.0.1:8000/viewProfessors"
        a = requests.get(url)
        print(a.text)

    def do_average(self,arg):
        arg = arg.strip().split(" ")
        if len(arg)!=2:
            print("Wrong number of parameters! use syntax 'average professor_id module_code'")
        else:
            url = "http://127.0.0.1:8000/viewAverage"
            p = {"professor_uid": arg[0],
                 "code": arg[1]}
            a = requests.get(url,params=p)
            print(a.text)


    def do_rate(self,arg):
        arg = arg.strip().split(" ")
        if len(arg) != 5:
            print("Wrong number of parameters! use syntax 'rate professor_id module_code year semester rating'")
        else:
            if not 0 <= float(arg[4]) <= 5:
                print("rating must in the range of (0,5)")
            else:
                url = "http://127.0.0.1:8000/viewRating"
                p = {"professor_uid": arg[0],
                     "code": arg[1],
                     "year":arg[2],
                     "semester":arg[3],
                     "rating":float(arg[4])}
                a = requests.get(url, params=p)
                print(a.text)


if __name__ == '__main__':
    try:
        os.system('cls')
        client = Client()
        client.cmdloop()
    except:
        exit()