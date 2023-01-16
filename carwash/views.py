import random
from datetime import date

from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout, login


def index(request):
    washingpoints = Washingpoints.objects.all()
    return render(request, "index.html", locals())


def customerBook(request):
    error = ""
    washingpoints = Washingpoints.objects.all()
    if request.method == "POST":
        bid = str(random.randint(10000000, 99999999))
        pt = request.POST["packageType"]
        cwp = request.POST["carWashPoint"]
        fn = request.POST["fullName"]
        mob = request.POST["mobileNumber"]
        wd = request.POST["washDate"]
        wt = request.POST["washTime"]
        msg = request.POST["message"]
        status = "New"

        try:
            Carwashbooking.objects.create(
                bookingId=bid,
                packageType=pt,
                carWashPoint=cwp,
                fullName=fn,
                mobileNumber=mob,
                washDate=wd,
                washTime=wt,
                message=msg,
                status=status,
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "customerBook.html", locals())


def contact(request):
    error = ""
    if request.method == "POST":
        fn = request.POST["FullName"]
        eid = request.POST["EmailId"]
        c = request.POST["Contact"]
        s = request.POST["Subject"]
        des = request.POST["Description"]
        try:
            Enquiry.objects.create(
                FullName=fn,
                EmailId=eid,
                Contact=c,
                Subject=s,
                Description=des,
                PostingDate=date.today(),
                Status="no",
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "contact.html", locals())


def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect("login")
    enquiry = Enquiry.objects.filter(Status="no")
    return render(request, "unread_queries.html", locals())


def read_queries(request):
    if not request.user.is_authenticated:
        return redirect("login")
    enquiry = Enquiry.objects.filter(Status="yes")
    return render(request, "read_queries.html", locals())


def view_queries(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.Status = "yes"
    enquiry.save()
    return render(request, "view_queries.html", locals())


def adminlogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, "login.html", locals())


def admin_home(request):
    if not request.user.is_staff:
        return redirect("admin_login")
    bnew = Carwashbooking.objects.filter(status="New").count()
    bcom = Carwashbooking.objects.filter(status="Completed").count()
    ball = Carwashbooking.objects.all().count()
    ur = Enquiry.objects.filter(Status="no").count()
    r = Enquiry.objects.filter(Status="yes").count()
    allwash = Washingpoints.objects.all().count()
    d = {"bnew": bnew, "bcom": bcom, "ball": ball, "ur": ur, "r": r, "allwash": allwash}
    return render(request, "admin_home.html", d)


def addCarWashpoint(request):
    error = ""
    if request.method == "POST":
        wpn = request.POST["washingPointName"]
        wpa = request.POST["washingPointAddress"]
        cn = request.POST["contactNumber"]

        try:
            Washingpoints.objects.create(
                washingPointName=wpn, washingPointAddress=wpa, contactNumber=cn
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "addCarWashpoint.html", locals())


def manageCarWashpoint(request):
    if not request.user.is_authenticated:
        return redirect("login")
    washingpoints = Washingpoints.objects.all()
    return render(request, "manageCarWashpoint.html", locals())


def editCarWashPoint(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")
    error = ""
    washingpoints = Washingpoints.objects.get(id=pid)
    if request.method == "POST":
        wpn = request.POST["washingPointName"]
        wpa = request.POST["washingPointAddress"]
        cn = request.POST["contactNumber"]

        washingpoints.washingPointName = wpn
        washingpoints.washingPointAddress = wpa
        washingpoints.contactNumber = cn
        try:
            washingpoints.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "editCarWashPoint.html", locals())


def delete_CarWash(request, pid):
    washingpoints = Washingpoints.objects.get(id=pid)
    washingpoints.delete()
    return redirect("manageCarWashpoint")


def addBooking(request):
    if not request.user.is_authenticated:
        return redirect("login")
    error = ""
    washingpoints = Washingpoints.objects.all()
    if request.method == "POST":
        bid = str(random.randint(10000000, 99999999))
        pt = request.POST["packageType"]
        cwp = request.POST["carWashPoint"]
        fn = request.POST["fullName"]
        mob = request.POST["mobileNumber"]
        wd = request.POST["washDate"]
        wt = request.POST["washTime"]
        msg = request.POST["message"]
        status = "New"

        try:
            Carwashbooking.objects.create(
                bookingId=bid,
                packageType=pt,
                carWashPoint=cwp,
                fullName=fn,
                mobileNumber=mob,
                washDate=wd,
                washTime=wt,
                message=msg,
                status=status,
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "addBooking.html", locals())


def newBooking(request):
    if not request.user.is_authenticated:
        return redirect("login")
    carwashbooking = Carwashbooking.objects.filter(status="New")
    return render(request, "newBooking.html", locals())


def completeBooking(request):
    if not request.user.is_authenticated:
        return redirect("login")
    carwashbooking = Carwashbooking.objects.filter(status="Completed")
    return render(request, "completeBooking.html", locals())


def delete_booking(request, pid):
    carwashbooking = Carwashbooking.objects.get(id=pid)
    carwashbooking.delete()
    return redirect("completeBooking")


def allBooking(request):
    if not request.user.is_authenticated:
        return redirect("login")
    carwashbooking = Carwashbooking.objects.all()
    return render(request, "allBooking.html", locals())


def view_BookingDtls(request, pid):
    if not request.user.is_authenticated:
        return redirect("login")
    carwashbooking = Carwashbooking.objects.get(id=pid)
    if request.method == "POST":
        pm = request.POST["paymentMode"]
        tn = request.POST["txnNumber"]
        aremark = request.POST["adminRemark"]
        try:
            carwashbooking.paymentMode = pm
            carwashbooking.txnNumber = tn
            carwashbooking.adminRemark = aremark
            carwashbooking.status = "Completed"
            carwashbooking.lastUpdationDate = date.today()
            carwashbooking.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "view_BookingDtls.html", locals())


def ChangePassword(request):
    if not request.user.is_authenticated:
        return redirect("index")
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST["oldpassword"]
        n = request.POST["newpassword"]
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, "ChangePassword.html", locals())


def Logout(request):
    logout(request)
    return redirect("index")
