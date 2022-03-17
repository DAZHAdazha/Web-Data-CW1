from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor,Rating,Module,User
# Create your views here.

valid = 0


def viewRegister(request):
    try:
        username = request.GET.get('username')
        email = request.GET.get('email')
        password = request.GET.get('password')
        serach_user = User.objects.filter(username=username)
        if serach_user:
            return HttpResponse("This username had been registered already!")
        else:
            user = User.objects.create(username=username,email=email,password=password)
            return HttpResponse("Register Successfully!")
    except:
        return HttpResponse("Something goes wrong...")


def viewLogin(request):
    global valid
    username = request.GET.get('username')
    password = request.GET.get('password')
    serach_user = User.objects.filter(username=username)
    if serach_user:
        if(serach_user[0].password==password):
            valid = username
            return HttpResponse("Login successfully!")
        else:
            return HttpResponse("Wrong password!")
    else:
        return HttpResponse("Wrong username!")

def viewLogout(request):
    global valid
    if valid==0:
        return HttpResponse("Please Login first")
    valid = 0
    print('valid:' + str(valid))
    return HttpResponse("logout successfully!")

def viewProfessors(request):
    global valid
    if valid==0:
        return HttpResponse("Please Login first")
    professors = Professor.objects.all()
    temp = ""
    for i in professors:
        all_ratings = Rating.objects.filter(professor_uid=i.UID)
        sum = 0
        count = 0
        for j in all_ratings:
            sum += j.rating
            count += 1
        if(count!=0):
            star = round(sum/count)
            temp += "The rating of " + i.name + " (" + str(i.UID) +")is "
            for k in range(star):
                temp += "*"
            temp += '\n'
        else:
            temp += i.name + " (" + str(i.UID) +")does not have rating records yet.\n"
    print(temp)
    return HttpResponse(temp)


def viewAverage(request):
    global valid
    if valid==0:
        return HttpResponse("Please Login first")
    professor_uid = request.GET.get('professor_uid')
    code = request.GET.get('code')
    all_ratings = Rating.objects.filter(professor_uid=professor_uid,code=code)
    temp = ''
    if all_ratings:
        sum = 0
        count = 0
        for i in all_ratings:
            sum += i.rating
            count += 1
        star = round(sum / count)
        all_modules = Module.objects.filter(code=code)
        all_professors = Professor.objects.filter(UID=professor_uid)
        temp += "The rating of " + all_professors[0].name + "(" + str(all_professors[0].UID) + ") in module " + all_modules[0].name + "(" + all_modules[0].code + ")is "
        for k in range(star):
            temp += "*"
        temp += '\n'
    else:
        temp = 'No records! Wrong professor_uid or code!'
    print(temp)
    return HttpResponse(temp)


def viewModules(request):
    global valid
    if valid==0:
        return HttpResponse("Please Login first")
    modules = Module.objects.all()
    temp = "Code	               Name			            Year		     Semester	               Taught by\n"
    for i in modules:
        temp += '%s%35s%14s%17s%15s'%(i.code,i.name,str(i.year),str(i.semester),'')
        index = 0
        for j in i.professors.all():
            if index==0:
                temp += '%0s'%(str(j)) +'\n'
            else:
                temp += '%106s' % (str(j)) + '\n'
            index+=1

    temp+='\n-------------------------------------------------------------------------------------------------------------------------------------------------------------'
    print(temp)
    return HttpResponse(temp)


def viewRating(request):
    global valid
    if valid==0:
        return HttpResponse("Please Login first")
    professor_uid = request.GET.get('professor_uid')
    code = request.GET.get('code')
    year = request.GET.get('year')
    semester = request.GET.get('semester')
    rating = request.GET.get('rating')
    username = valid
    temp = ''
    all_ratings = Rating.objects.filter(professor_uid=professor_uid, code=code,year=year,semester=semester,username=username)
    if all_ratings:
        temp = 'You had already rate this module and professor already!'
    else:
        rate = Rating.objects.create(professor_uid=professor_uid, code=code,year=year,semester=semester,rating=rating,username=username)
        temp = 'Rate successfully!'
    print(temp)
    return HttpResponse(temp)