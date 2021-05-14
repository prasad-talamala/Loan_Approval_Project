from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User

from userenquiry.forms import SignUpForm, LoginForm
from userenquiry.models import UserEnquiry
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def add_pagination(request, all_data):
    page = request.GET.get('page', 1)
    paginator = Paginator(all_data, 10)
    try:
        all_data = paginator.page(page)
    except PageNotAnInteger:
        all_data = paginator.page(1)
    except EmptyPage:
        all_data = paginator.page(paginator.num_pages)
    return all_data


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": SignUpForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['firstname'],
                                                last_name=request.POST['lastname'])
                user.save()
                auth_login(request, user)
                return redirect("userform")
            except IntegrityError:
                return render(request, "register.html",
                              {"form": SignUpForm(), 'error': "username already taken.."})
        else:
            return render(request, "register.html",
                          {"form": SignUpForm(), 'error': "The two password fields didn't match."})


def login(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": LoginForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "login.html",
                          {"form": LoginForm(), 'error': "username and password didn't match.."})
        else:
            auth_login(request, user)
            return redirect("userform")


def logout(request):
    auth_logout(request)
    return redirect("home")


def userform(request):
    if request.method == "GET":
        return render(request, "userform.html")
    else:
        enquiry_id = request.POST["enquiryid"]
        customer_name = request.POST["customername"]
        job_type = request.POST["jobtype"]
        loan_amount = request.POST["loanamount"]
        interest_rate = request.POST["interestrate"]

        userform_obj = UserEnquiry.objects.create(enquiry_id=enquiry_id, customer_name=customer_name,
                                                  job_type=job_type,
                                                  loan_amount=loan_amount, interest_rate=interest_rate)
        userform_obj.save()

        return redirect("finaldata")


def finaldata(request):
    if request.method == "GET":
        f = UserEnquiry.objects.get_queryset().order_by('-id')
        data = add_pagination(request, f)
        return render(request, "final_data.html", {"data": data})


def updatestatus(request, id):
    if request.method == "POST":
        usr_obj = UserEnquiry.objects.get(id=id)
        action = request.POST["mybtns"]

        if action == "recommend":
            usr_obj.status = "Recommended"
        else:
            usr_obj.status = "Approved"

        usr_obj.save()
        return redirect("finaldata")
