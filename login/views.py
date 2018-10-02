from django.shortcuts import render
from .models import AuthUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .models import Report


# Create your views here.

def loginView(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "login.html")


@login_required(login_url='loginView')
def home(request):
    return render(request, "home.html")


@login_required(login_url='loginView')
def admin(request):
    viewAlluser = AuthUser.objects.all()
    num_post = AuthUser.objects.filter(is_staff=0).count()
    return render(request, 'admin.html', {'viewAlluser': viewAlluser, 'num_post': num_post})


@login_required(login_url='loginView')
def editUserInfo(request):
    return render(request, "editUserInfo.html")


@login_required(login_url='loginView')
def addReport(request):
    return render(request, "addReport.html")


@login_required(login_url='loginView')
def addReportInformation(request):
    checkTitle = Report.objects.filter(report_title=request.POST.get('report_title'))
    if not checkTitle:
        report = Report(
            report_title=request.POST.get('report_title'),
            date=request.POST.get('report_date'),
            report_discription=request.POST.get('report_discription'),
            user_id=request.POST.get('user_id'),
        )
        report.save()
        messages.add_message(request, messages.INFO, 'Report Saved Successfully')
        return redirect('addReport')
    else:
        messages.add_message(request, messages.INFO, 'Report Title Already Exists')
        return redirect('addReport')


@login_required(login_url='loginView')
def editReportInfo(request, id):
    editReportInfo = Report.objects.filter(report_id=id)
    return render(request, 'editReportInfo.html', {'editReportInfo': editReportInfo})


@login_required(login_url='loginView')
def UpdateReportInfo(request):
    checkTitle = Report.objects.filter(report_title=request.POST.get('report_title'),
                                       user_id=request.POST.get('user_id'))
    if not checkTitle:
        Report_Update = Report.objects.get(report_id=request.POST.get('report_id'))
        Report_Update.report_title = request.POST.get('report_title')
        Report_Update.report_discription = request.POST.get('report_discription')
        Report_Update.user_id = request.POST.get('user_id')
        Report_Update.save()
        messages.add_message(request, messages.INFO, 'Report Updated Successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.add_message(request, messages.INFO, 'Report Title Already Exists')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginView')
def viewAllReport(request, id):
    viewAllReport = Report.objects.filter(user_id=id)
    return render(request, 'viewAllReport.html', {'viewAllReport': viewAllReport})


@login_required(login_url="loginView")
def updateUserInfo(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        current_password = request.POST.get('current_password')
        user = authenticate(request, username=username, password=current_password)
        if user is not None:
            newPassword = request.POST.get('new_password')
            confmPassword = request.POST.get('confirm_password')
            if (newPassword == confmPassword):
                user_update = User.objects.get(id=request.POST.get('user_id'))
                user_update.set_password(request.POST.get('confirm_password'))
                user_update.save()
                messages.add_message(request, messages.INFO, 'Password Updated Successfully')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.add_message(request, messages.INFO, 'Password and Confirm Password Not Match')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.add_message(request, messages.INFO, 'Current Password Wrong')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginCheck(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff is False:
            login(request, user)
            return redirect('home')
        elif user and user.is_staff is True:
            login(request, user)
            return redirect('admin')
        else:
            messages.add_message(request, messages.INFO, 'Wrong User Name Or Password')
            return redirect('loginView')
    messages.add_message(request, messages.INFO, 'You Have To Login First')
    return redirect('loginView')


def registration(request):
    checkData = AuthUser.objects.filter(email=request.POST.get('email'))
    if not checkData:
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=(request.POST.get('password')),
        )
        messages.add_message(request, messages.INFO, 'User Saved Successfully')
        return redirect('loginView')
    else:
        messages.add_message(request, messages.INFO, 'Email Already Exists')
        return redirect('loginView')


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successfully logout')
    return redirect('loginView')


@login_required(login_url='loginView')
def deleteReportInfo(request, id):
    product = Report.objects.filter(report_id=id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
