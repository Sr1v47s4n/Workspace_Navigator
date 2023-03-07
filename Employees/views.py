from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from .models import AdminData, EmployeeData
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from utility.usrCodegen import usr_code

# Base page which holds(perview and search options within it but can't add Employees)
def preview(request):
    return render(request, "preview.html")


# The page which displays after login
def home(request, usrCode):  # Need to get the id of logeed in user
    emps = EmployeeData.objects.filter(
        usrCode=usrCode
    )  # Need to add filter with usrcode
    usr = AdminData.objects.get(usrCode=usrCode)  # To Print the Admin Name
    context = {"emps": emps, "usr": usr}  # Need to add the name of loged in user also
    return render(request, "home.html", context)


# Login Page
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def login_usr(request):
    if request.method == "POST":
        adminUsername = request.POST.get("userName")
        password = request.POST.get("password")
        try:
            user = AdminData.objects.get(adminUsername=adminUsername)
            user = authenticate(adminUsername=adminUsername, password=password)
            if user is not None:
                login(request, user)
                print(user.usrCode)
                return redirect("home", user.usrCode)
            else:
                messages.error(request, "Password Not Matched")
                print("Pwd Error")
                return redirect("login_usr")
        except AdminData.DoesNotExist:
            messages.error(request, "User Not Found")
            return reverse_lazy("login_usr")

    return render(request, "login.html")


def logout_usr(request):
    logout(request)
    return redirect("login_usr")

def signup_usr(request):
    if request.method == "POST":
        adminUsername = request.POST.get("userName")
        password = make_password(request.POST.get("password"))
        adminName = request.POST.get("fullName")
        adminPhNo = request.POST.get("phNo")
        adminEmail = request.POST.get("emailAddress")
        usrCode = usr_code()
        adminData = AdminData(
            adminUsername=adminUsername,
            adminEmail=adminEmail,
            adminName=adminName,
            adminPhNo=adminPhNo,
            password=password,
            usrCode=usrCode,
    )
        adminData.save()
    return render(request, "signup.html")


def addEmp(request, usrCode):
    usr= AdminData.objects.get(usrCode=usrCode)
    context = {"usr":usr}
    if request.method == "POST":
        staffName = request.POST.get("fullName")
        staffDob = request.POST.get("dob")
        staffId = request.POST.get("staffId")
        staffBranch = request.POST.get("branch")
        staffExp = request.POST.get("exp")
        staffSalary = request.POST.get("salary")
        staffPhNo = request.POST.get("phNo")
        staffEmail = request.POST.get("email")
        staffQualification = request.POST.get("qual")
        usrCode = usrCode
        staff = EmployeeData(
            staffName=staffName,
            staffDob=staffDob,
            staffBranch=staffBranch,
            staffId=staffId,
            staffExp=staffExp,
            staffSalary=staffSalary,
            staffPhNo=staffPhNo,
            staffEmail=staffEmail,
            staffQualification=staffQualification,
            usrCode=usrCode,
        )
        staff.save()
    return render(request, "newEmp.html",context)


def search(request, usrCode):
    usr = AdminData.objects.get(usrCode=usrCode)
    query = request.POST.get("search") if request.POST.get("search") != None else ""
    emps = EmployeeData.objects.filter(
        Q(staffName__icontains=query)
        | Q(staffId__icontains=query)
        | Q(staffEmail__icontains=query)
        | Q(staffPhNo__icontains=query)
        | Q(staffBranch__icontains=query)

    )
    context = {"usr":usr,"emps":emps}
    
    
    return render(request, "home.html", context)


def knowMore(request, usrCode, staffId):
    try:
        emp = EmployeeData.objects.get(staffId=staffId)
        usr = AdminData.objects.get(usrCode=usrCode)  # To Print the Admin Name
        context = {
            "emp": emp,
            "usr": usr
        }  # Need to add the name of loged in user also
    except EmployeeData.DoesNotExist:
        context = {"msg":"404"}
        return render(request, "knowmore.html", context)
    return render(request, "knowmore.html", context)


def myAcc(request, usrCode):
    acc = AdminData.objects.get(usrCode=usrCode)
    context = {"acc": acc}
    if request.method == "POST":
        adminUsername = request.POST.get("userName")
        password = make_password(request.POST.get("password"))
        adminName = request.POST.get("fullName")
        adminPhNo = request.POST.get("phNo")
        adminEmail = request.POST.get("emailAddress")
        adminData = AdminData(
            adminUsername=adminUsername,
            adminEmail=adminEmail,
            adminName=adminName,
            adminPhNo=adminPhNo,
            password=password,
            
    )
        adminData.save(update_fields=["adminUsername","password","adminEmail","adminPhNo","adminName"])
        
    return render(request, "myAcc.html",context)

def editEmp(request,staffId,usrCode):
    usr = AdminData.objects.get(usrCode=usrCode)
    emp= EmployeeData.objects.get(staffId=staffId)
    if request.method == "POST":
        emp.staffName = request.POST.get("fullName")
        emp.staffDob = request.POST.get("dob")
        emp.staffId = request.POST.get("staffId")
        emp.staffBranch = request.POST.get("branch")
        emp.staffExp = request.POST.get("exp")
        emp.staffSalary = request.POST.get("salary")
        emp.staffPhNo = request.POST.get("phNo")
        emp.staffEmail = request.POST.get("email")
        emp.staffQualification = request.POST.get("qual")
        emp.save(update_fields=["staffName","staffPhNo","staffEmail","staffQualification","staffDob","staffBranch","staffId","staffExp","staffSalary"])
        return redirect("home",usrCode=usrCode)
    context = {"emp":emp,"usr":usr}
    return render(request,"editEmp.html",context)

def changePwd(request):
    if request.method == "POST":
        adminUsername = request.POST.get("usrName")
        curPwd = request.POST.get("curPwd")
        newPwd1 = request.POST.get("newPwd1")
        newPwd2 = request.POST.get("newPwd2")

        try:
            user = AdminData.objects.get(adminUsername=adminUsername)
            if check_password(curPwd, user.password):
                if curPwd == newPwd1:
                    messages.error(request, "Give New Password")
                    print("Give New Password")
                    return render(request, "forgotpwd.html")
                elif curPwd != newPwd1:
                    if newPwd2 == newPwd1:
                        user.password = make_password(newPwd1)
                        user.save(update_fields=["password"])
                        messages.success(request, "Password Changed Successful")
                        print("Success")
                        return reverse_lazy("login_usr")
                    else:
                        messages.error(request, "Confirm Password Not Matched")
                        print("Confirm Pwd Not Matched")
                        return render(request, "forgotpwd.html")

            else:
                messages.error(request, "Password Not Matched")
                print("Pwd Not Matched")
                return render(request, "forgotpwd.html")

        except AdminData.DoesNotExist:
            messages.error(request, "User Not Found")
            return render(request, "forgotpwd.html")        
        
    return render(request,"forgotpwd.html")

# Create a forgot pass fun -> Done

def team(request):
    return render(request,"team.html")