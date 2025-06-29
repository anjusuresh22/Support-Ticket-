import csv
from decimal import Decimal
import json
import os
import pickle
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect ,HttpResponse
import datetime
from datetime import date
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.db import connection
from EDP_intimate import settings
# Create your views here.
from .models import login as log,User as usr,Staff as stf,Complaint as comp,Amc as am
from .models import menutype as typ, menu as mnu ,menustock as mst,cart as crt,bill as bl,orderlist as ol, chat as cht,rating as rate
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Avg, Count, F, Q
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE 

def login(request):
     return render(request, "login.html")
def registration(request):
     return render(request, "registration.html")
def index(request):

        if(request.session.get('role', '')=="admin"):
            response = redirect('/Adminhome')
            return response
        elif (request.session.get('role', '')== "staff"):
            response = redirect('/Staffhome')
            return response
        elif (request.session.get('role', '')== "user"):
            response = redirect('/Userhome')
            return response

        else:
            if request.POST:
                t1=request.POST["t1"]
                t2=request.POST["t2"]
                try:
                        data=log.objects.get(username=t1,password=t2)
                        if(data.role=="admin"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/Adminhome')
                                return response
                        elif (data.role=="user"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/Userhome')
                                return response
                        elif (data.role=="staff"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/Staffhome')
                                return response
                        else:
                                return render(request, "index.html", {"msg":"invalid account Details"})
                except:
                        return render(request, "index.html", {"msg":"invalid user name of password"})

            return render(request, "index.html",{"msg":""})

def SignUp(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        t3=request.POST["t3"]
        t4=request.POST["t4"]
        t5=request.POST["t5"]
        t6=request.POST["t6"]
        t7=request.POST["t7"]
        log.objects.create(username=t6, password=t7, role="user")
        data=log.objects.last()
        messages.add_message(request, messages.INFO, 'Registered  successfully.')
      
        usr.objects.create(User_name=t1,User_address=t2,User_email=t3,User_phone=t4,User_alt_No=t5,Log_id=data,User_status="approved")
    return redirect("/registration")
    
    


def Logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index")
        return response
    except:
        response = redirect("/index")
        return response

def Privacy(request):
    msg=""
    cart=2
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session["id"]
        data=log.objects.get(log_id=id)
        if data.password==t1:
            msg="sucessfully updated"
            log.objects.filter(log_id=id).update(password=t2)
        else:
            msg="invalid current password"
    returnpage="adminhead.html"
    if request.session["role"] == "user":
        returnpage="Userhead.html"
    elif request.session["role"] =="staff":
        returnpage="staffhead.html"
    return render(request, "privacy.html",{"role":returnpage,"msg":msg,"cart":cart})
def Profile(request):
    msg=""
    cart=2
    ids=request.session["id"]
    if request.POST:
        if request.session["role"] =="staff":
            t2 = request.POST["t2"]
            t3 = request.POST["t3"]
            t4 = request.POST["t4"]
            stf.objects.filter(Staff_logid=ids).update(Staff_address=t2,Staff_email=t3,Staff_phone=t4)
        elif request.session["role"] =="user":
            t2 = request.POST["t2"]
            t3 = request.POST["t3"]
            t4 = request.POST["t4"]
            t5 = request.POST["t5"]
            usr.objects.filter(Log_id=ids).update(User_address=t2,User_email=t3,User_phone=t4,User_alt_No=t5)


    if request.session["role"] =="staff":
        data1=stf.objects.get(Staff_logid=ids)
        returnpage="StaffProfile.html"
    elif request.session["role"] =="user":
        data1=usr.objects.get(Log_id=ids)

        returnpage="UserProfile.html"
    else:
        response = redirect('/index'+"?msg=session expired login again")
        return response
    return render(request,returnpage,{"msg":msg,"data":data1,"cart":cart})

def Appoint_Staff(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.POST["t4"]
        t5 = request.POST["t5"]
        t6=",".join(request.POST.getlist('t6'))

        t7 = request.POST["t7"]
        t8 = request.FILES["t8"]
        fs = FileSystemStorage()
        fnm=fs.save(t8.name, t8)
        t9 = request.POST["t9"]
        t10 = request.POST["t10"]
        log.objects.create(username=t9, password=t10, role="staff")
        data=log.objects.last()
        stf.objects.create(Staff_name=t1,Staff_address=t2,Staff_email=t3,Staff_phone=t4,Staff_qualification=t6, Staff_designation=t5,Staff_experience=t7,Staff_photo=fnm,Staff_status="approved",Staff_logid=data)
        msg="updated successfuly"
        #return HttpResponse(t6)
    else:
        msg = ""
    data1=stf.objects.all()
    return render(request,"Add_staff.html",{"msg":msg,"data":data1})
def delete_staff(request):
    stf.objects.filter(Staff_id=request.GET["id"]).delete()
    response = redirect('/List_Staff')
    return response
def List_Staff(request):
    msg = ""
    data1=stf.objects.all()
    return render(request,"List_staff.html",{"msg":msg,"data":data1})
def All_Users(request):
    msg=""
    data=usr.objects.all()
    return render(request,"All_Users.html",{"msg":msg,"data":data})

def View_Amc(request):
    msg=""
    data=am.objects.all()
    return render(request,"View_Amc.html",{"msg":msg,"data":data})
def remove_usr(request):
    usr.objects.filter(User_id=request.GET["id"]).delete()
    response = redirect('/All_Users')
    return response

def complaints(request):
        msg=""
        today = date.today()
        #datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                c_date = request.POST["c_date"]
                #datau=stf.objects.get(Staff_logid=t2)
                msg="updated sucessfully"
                comp.objects.filter(Complaint_id=t1).update(allot_id=t2,deadline_date=c_date,assigned_date=today)
        data1=comp.objects.all()
        data2=stf.objects.all()
      
   
        return render(request, "Answer_Queries.html",{"msg":msg,"data":data1,"d":data2,'today':today})

def Alloted_works(request):
        msg=""
        #datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                #datau=stf.objects.get(Staff_logid=t2)
                msg="updated sucessfully"
                comp.objects.filter(Complaint_id=t1).update(Complaint_reply=t2)
        d=request.session['id']
        datau=stf.objects.get(Staff_logid=d)
        data1=comp.objects.filter(allot_id=datau).all()
        return render(request, "Alloted_works.html",{"msg":msg,"data":data1})
def Adminhome(request):
    return render(request,"Adminhome.html",{"msg":""})
def Staffhome(request):
    datau=stf.objects.get(Staff_logid=request.session["id"])
    return render(request,"Staffhome.html",{'datau':datau})

def Userhome(request):
    msg=request.GET.get("msg","")
    datau=usr.objects.get(Log_id=request.session["id"])
    today = date.today()
    cart=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).count()

    # data=mst.objects.filter(date=today).all()
    data=mst.objects.all()
    return render(request,"Userhome.html",{"msg":msg,"cart":cart,"data":data})
def proceed(request):
    msg=""
    datau=usr.objects.get(Log_id=request.session["id"])
    today = date.today()
    tot=request.GET["tot"]
    bl.objects.create(date=today,user=datau,total=tot,order_status="waiting")
    datab=bl.objects.last()
    dc=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).all()
    for d in dc:
        ol.objects.create(cart_id=d,billno=datab)

    crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).update(cart_status="approved")
    response =redirect("/Userhome?msg="+msg)

    return response
def myorder(request):
    msg=""
    datau=usr.objects.get(Log_id=request.session["id"])
    today = date.today()
    cart=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).count()
    data=bl.objects.filter(user=datau).all()
    return render(request,"myorder.html",{"msg":msg,"cart":cart,"data":data})
def myorderitem(request):
    msg=""
    datau=usr.objects.get(Log_id=request.session["id"])
    today = date.today()
    cart=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).count()
    datab=bl.objects.get(billno=request.GET["id"])
    total=datab.total
    data=ol.objects.filter(billno=request.GET["id"]).all()
    return render(request,"myorderitem.html",{"msg":msg,"cart":cart,"data":data,"total":total})
def myorder1(request):
    msg=""



    data=bl.objects.filter().all()
    return render(request,"myorder1.html",{"msg":msg,"data":data})
def myorder2(request):
    msg=""


    data=bl.objects.filter().all()
    return render(request,"myorder1.html",{"msg":msg,"data":data})


def updateorder(request):
    bl.objects.filter(billno=request.GET["id"]).update(order_status="delevered")
    response =redirect("/myorder1")

    return response
def myorderitem1(request):
    msg=""

    datab=bl.objects.get(billno=request.GET["id"])
    total=datab.total
    data=ol.objects.filter(billno=request.GET["id"]).all()
    return render(request,"myorderitem1.html",{"msg":msg,"data":data,"total":total})

def myorderitem2(request):
    msg=""

    datab=bl.objects.get(billno=request.GET["id"])
    total=datab.total
    data=ol.objects.filter(billno=request.GET["id"]).all()
    return render(request,"myorderitem1.html",{"msg":msg,"data":data,"total":total})

def remct(request):
    msg=""
    crt.objects.filter(cart_id=request.GET["id"]).delete()
    response =redirect("/mycart?msg="+msg)

    return response
def redct(request):
    datac=crt.objects.get(cart_id=request.GET["id"])
    stk=int(datac.pqty)
    msg=""
    if stk==1:
        msg="minimum puchase quantity is 1"
    else :
        nstk=stk-1
        crt.objects.filter(cart_id=request.GET["id"]).update(pqty=nstk)
        msg="Quantiy updated in cart"
    response =redirect("/mycart?msg="+msg)

    return response
def addct(request):
    datac=crt.objects.get(cart_id=request.GET["id"])
    stk=int(datac.pqty)
    avlstk=int(datac.stock_id.qty)
    pustk=0
    msg=""
    datap=crt.objects.filter(stock_id=datac.stock_id,cart_status="approved").all()
    for p in datap:
            pustk=pustk+int(p.pqty)
    balstk=avlstk-pustk
    if balstk > stk:
        nstk=stk+1
        crt.objects.filter(cart_id=request.GET["id"]).update(pqty=nstk)
        msg="Quantiy updated in cart"
    else:
        msg="Sorry!..Avilable stock is "+ str(balstk)

    response =redirect("/mycart?msg="+msg)

    return response
def mycart(request):
    msg=request.GET.get("msg","")
    datau=usr.objects.get(Log_id=request.session["id"])
    today = date.today()
    cart=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).count()
    data=crt.objects.filter(user=datau,cart_status="waiting",cart_date=today).all()
    total=0
    for d in data:
        m=int(d.menu_id.menu_price) * int(d.pqty)
        total=total+m
    return render(request,"mycart.html",{"msg":msg,"cart":cart,"data":data,"total":total})
def add_cart(request):
    msg=""
    datau=usr.objects.get(Log_id=request.session["id"])
    datas=mst.objects.get(stock_id=request.GET["id"])
    today = date.today()
    crt.objects.filter(stock_id=datas,user=datau,cart_status="waiting").exclude(cart_date=today).delete()
    crtc=crt.objects.filter(stock_id=datas,user=datau,cart_status="waiting",cart_date=today).count()
    if crtc > 0:
        datac = crt.objects.get(stock_id=datas,user=datau,cart_status="waiting",cart_date=today)
        stk=int(datac.pqty)
        avlstk=int(datas.qty)
        pustk=0
        datap=crt.objects.filter(stock_id=datas,cart_status="approved").all()
        for p in datap:
            pustk=pustk+int(p.pqty)
        balstk=avlstk-pustk
        if balstk > stk:
            nstk=stk+1
            crt.objects.filter(stock_id=datas,user=datau,cart_status="waiting",cart_date=today).update(pqty=nstk)
            msg="Quantiy updated in cart"
        else :
            msg="Sorry!..Avilable stock is "+ str(balstk)
    else:

        crt.objects.create(stock_id=datas,menu_id=datas.menu_id,user=datau,pqty="1",cart_status="waiting",cart_date=today)
        msg="Added to cart"

    response =redirect("/Userhome?msg="+msg)

    return response
def add_complaints(request):
      cart=2
      datax=usr.objects.get(Log_id=request.session["id"])
      data1=comp.objects.filter(User_id=datax).all()
      return render(request, "Add_complaints.html",{"data":data1,"cart":cart})
def Manage_complaints(request):
        msg=""
        cart=2
        #datay=log.objects.get(log_id=request.session["id"])
        datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                t3 = request.POST["t3"]
                t4 = request.POST["t4"]
                today = date.today()

               
                comp.objects.create(Complaint_subject=t1,Complaint_message=t2,Complaint_date=today,Complaint_reply="not yet Seen",User_id=datax,Complaint_product=t3,Complaint_priority=t4)
        data1=comp.objects.filter(User_id=datax).all()
        #.filter(User_id=datax)
        messages.add_message(request, messages.INFO, 'Complaints Posted successfully.')
        return redirect('add_complaints')
def apply_amc(request):
        msg=""
        cart=2
        #datay=log.objects.get(log_id=request.session["id"])
        datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                t3 = request.POST["t3"]
                t4 = request.POST["t4"]
                today = date.today()

                msg="posted sucessfully"
                am.objects.create(amc_from=t1,Description=t2,amc_to=t3,amc_amount=t4,User_id=datax,amc_status="Active")
        data1=am.objects.filter(User_id=datax).all()
        #.filter(User_id=datax)
        return render(request, "apply_amc.html",{"msg":msg,"data":data1,"cart":cart})

def Manage_Menutype(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        msg="posted sucessfully"
        typ.objects.create(type_name=t1)
    data=typ.objects.all()
    return render(request, "Add_type.html",{"msg":msg,"data":data})

def Manage_Menu(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.FILES["t4"]
        fs = FileSystemStorage()
        fnm=fs.save(t4.name, t4)
        dataty= typ.objects.get(type_id=t1)
        msg="posted sucessfully"
        mnu.objects.create(menu_type=dataty,menu_name=t2,menu_price=t3,menu_photo=t4)

    data=mnu.objects.all()
    data1=typ.objects.all()
    return render(request, "Add_menu.html",{"msg":msg,"data":data,"data1":data1})

def delete_type(request):
    typ.objects.filter(type_id=request.GET["id"]).delete()
    response = redirect('/Manage_Menutype')
    return response

def delete_menu(request):
    mnu.objects.filter(menu_id=request.GET["id"]).delete()
    response = redirect('/Manage_Menu')
    return response

def edit_menu(request):
    data1=typ.objects.all()
    data=mnu.objects.get(menu_id=request.GET["id"])
    return render(request, "edit_menu.html",{"data":data,"data1":data1})

def Update_Menu(request):
        menu_id=request.POST.get("menu_id")
        tbl=mnu.objects.get(menu_id=menu_id)
        if len(request.FILES) != 0:

            image=request.FILES['t4']
            split_tup = os.path.splitext(image.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,image)
            url1=obj.url(file)
            tbl.menu_photo=url1
        tbl.menu_name=request.POST.get("t2")
        tbl.menu_price=request.POST.get("t3")
        tbl.save()
        data=mnu.objects.all()
        data1=typ.objects.all()
        msg="Updated sucessfully"
        return render(request, "Add_menu.html",{"msg":msg,"data":data,"data1":data1})

def edit_type(request):

    data=typ.objects.get(type_id=request.GET["id"])
    return render(request, "edit_type.html",{"data":data})
def Update_Menutype(request):
        type_id=request.POST.get("type_id")
        tbl=typ.objects.get(type_id=type_id)
        tbl.type_name=request.POST.get("t1")
        tbl.save()
        data=typ.objects.all()
        msg="Updated sucessfully"
        return render(request, "Add_type.html",{"msg":msg,"data":data})





def getmenu(request):
    st="<option value=''>-select-</option>"
    data=mnu.objects.filter(menu_type=request.GET["id"]).all()
    for datas in data:
        st+="<option value='"+str(datas.menu_id)+"'>"+datas.menu_name+"</option>"

    return HttpResponse(st)
def getdt(request):
    st="0"
    data=mnu.objects.get(menu_id=request.GET["t2"])
    dat=request.GET["id"]
    dc=mst.objects.filter(date=dat,menu_id=data).count()
    if dc > 0:
        dr=mst.objects.get(date=dat,menu_id=data)
        st=dr.qty
    return HttpResponse(st)
def Manage_Stock(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.POST["t4"]
        data=mnu.objects.get(menu_id=t2)
        dc=mst.objects.filter(date=t3,menu_id=data).count()
        if dc > 0:
            mst.objects.filter(date=t3,menu_id=data).update(qty=t4)
            msg="stock updated"
        else:
            msg="stock Added"
            mst.objects.create(menu_id=data,qty=t4,date=t3)
    data1=typ.objects.all()
    data=mst.objects.all()
    return render(request, "Add_menustock.html",{"msg":msg,"data1":data1,"data":data})

def delete_stock(request):
    mst.objects.filter(stock_id=request.GET["id"]).delete()
    response = redirect('/Manage_Stock')
    return response

def getlist(request):
    st=""
    data=mst.objects.filter(date=request.GET["id"]).all()
    i=1
    for datas in data:
        st+='''<tr>
            <td>'''+ str(i) +'''</td>
            <td><img src="/media/'''+str(datas.menu_id.menu_photo)+'''" width="50px" height="50px"/></td>
            <td>'''+datas.menu_id.menu_type.type_name+'''</td>
            <td>'''+datas.menu_id.menu_name+'''</td>
            <td>'''+str(datas.menu_id.menu_price)+'''</td>
            <td>'''+datas.date+'''</td>
            <td>'''+str(datas.qty)+'''</td>

            <td><a class="btn-danger btn" href="delete_stock/?id='''+str(datas.stock_id)+'''">Remove</a></td>


            </tr>'''
        i+=1

    return HttpResponse(st)

def chat(request):

    id=request.session['id']
    data1=usr.objects.get(Log_id=id)
    return render(request, "chat.html",{'data':data1})
def chat_save(request):
    id=request.session['id']
    message=request.GET.get("message")
    data={}
    cht.objects.create(chat_message =message,chat_first_person_login_id=id,chat_second_person_login_id = 0,chat_user='User')
    data["success"]="Success"
    return JsonResponse(data)
    # tbl.login_id=id

def chat_display(request):
    id=request.session['id']
    cursor=connection.cursor()
    sql="select * from edpapp_chat where chat_user='User' and  (chat_first_person_login_id=0  and chat_second_person_login_id="+str(id)+")  or (chat_first_person_login_id="+str(id)+" and chat_second_person_login_id=0) order by chat_date asc "
    cursor.execute(sql)
    data=cursor.fetchall()
    str1=""
    for i in data:
        if i[3] == 0:
            user="Admin"
        else:
             user="Me"
        str1+="<div class='col-sm-3'><img style='margin:5px' width='20' height='20' src='static/assets/images/1.png'>"+str(user)+"</div><div class='col-sm-5'>"+str(i[1])+"</div> <div class='col-sm-4'>"+str(i[2].strftime("%Y-%m-%d %H:%M:%S"))+"</div><div style='clear:both; margin:15px'></div>"
    return HttpResponse(str1)
def chat_admin(request):
    data=usr.objects.all()
    return render(request,"admin_chat.html",{"data":data})
def chat_adm_user(request):
    log_id=request.GET["id"]
    data=usr.objects.get(Log_id=log_id)
    return render(request,"admin_chat_user.html",{"data":data})


def chat_display_adm(request):
    id=request.GET.get("logid")
    data1=usr.objects.get(Log_id=id)
    chat_user=data1.User_name
    cursor=connection.cursor()
    sql="select * from edpapp_chat where  chat_user='User' and  (chat_first_person_login_id=0  and chat_second_person_login_id="+str(id)+")  or (chat_first_person_login_id="+str(id)+" and chat_second_person_login_id=0) order by chat_date asc"
    cursor.execute(sql)
    data=cursor.fetchall()
    str1=""
    for i in data:
        if i[3] == 0:
            user="Admin"
        
        else:
             user=chat_user
        str1+="<div class='col-sm-3'><img style='margin:5px' width='20' height='20' src='static/assets/images/1.png'>"+str(user)+"</div><div class='col-sm-5'>"+str(i[1])+"</div> <div class='col-sm-4'>"+str(i[2].strftime("%Y-%m-%d %H:%M:%S"))+"</div><div style='clear:both; margin:15px'></div>"
    
    return HttpResponse(str1)
    
def chat_save_adm(request):
    id=request.GET.get("logid")
    message=request.GET.get("message")
    data={}
    cht.objects.create(chat_message =message,chat_first_person_login_id=0,chat_second_person_login_id = id,chat_user='User')
    data["success"]="Success"
    return JsonResponse(data)       
def chat_staff_admin(request):
    data=stf.objects.all()
    return render(request,"chat_staff_admin.html",{"data":data})
def chat_adm_staff(request):
    log_id=request.GET["id"]
    data=stf.objects.get(Staff_logid_id=log_id)
    return render(request,"admin_chat_staff.html",{"data":data})
def chat_save_adm_staff(request):
    id=request.GET.get("logid")
    message=request.GET.get("message")
    data={}
    cht.objects.create(chat_message =message,chat_first_person_login_id=0,chat_second_person_login_id = id,chat_user='Staff')
    data["success"]="Success"
def chat_display_adm_staff(request):
    id=request.GET.get("logid")
    data1=stf.objects.get(Staff_logid_id=id)
    chat_user=data1.Staff_name
    cursor=connection.cursor()
    sql="select * from edpapp_chat where  chat_user='Staff' and  (chat_first_person_login_id=0  and chat_second_person_login_id="+str(id)+")  or (chat_first_person_login_id="+str(id)+" and chat_second_person_login_id=0) order by chat_date asc"
    cursor.execute(sql)
    data=cursor.fetchall()
    str1=""
    for i in data:
        if i[3] == 0:
            user="Admin"
        
        else:
             user=chat_user
        str1+="<div class='col-sm-3'><img style='margin:5px' width='20' height='20' src='static/assets/images/1.png'>"+str(user)+"</div><div class='col-sm-5'>"+str(i[1])+"</div> <div class='col-sm-4'>"+str(i[2].strftime("%Y-%m-%d %H:%M:%S"))+"</div><div style='clear:both; margin:15px'></div>"
    
    return HttpResponse(str1)
def chat_staff(request):
    id=request.session['id']
    data1=stf.objects.get(Staff_logid_id=id)
    return render(request, "chat_staff.html",{'data':data1})
def chat_save_staff(request):
    id=request.session['id']
    message=request.GET.get("message")
    data={}
    cht.objects.create(chat_message =message,chat_first_person_login_id=id,chat_second_person_login_id = 0,chat_user='Staff')
    data["success"]="Success"
    return JsonResponse(data)
def chat_display_staff(request):
    id=request.session['id']
    cursor=connection.cursor()
    sql="select * from edpapp_chat where chat_user='Staff' and  (chat_first_person_login_id=0  and chat_second_person_login_id="+str(id)+")  or (chat_first_person_login_id="+str(id)+" and chat_second_person_login_id=0) order by chat_date asc "
    cursor.execute(sql)
    data=cursor.fetchall()
    str1=""
    for i in data:
        if i[3] == 0:
            user="Admin"
        else:
             user="Me"
        str1+="<div class='col-sm-3'><img style='margin:5px' width='20' height='20' src='static/assets/images/1.png'>"+str(user)+"</div><div class='col-sm-5'>"+str(i[1])+"</div> <div class='col-sm-4'>"+str(i[2].strftime("%Y-%m-%d %H:%M:%S"))+"</div><div style='clear:both; margin:15px'></div>"
    return HttpResponse(str1)
def complete_work(request,id):
     
    if (request.session.get('role', '')== "staff"):
        today = date.today()
        data=comp.objects.get(Complaint_id=id)
        data.status="Completed"
        data.completed_date=today
        data.save()
        messages.add_message(request, messages.INFO, 'Successfull')
        return redirect('Alloted_works')
    else:
      return redirect('login')
    

   
        
def employee_evaluation(request):
    if request.session.get('role', '') == "admin":
        staff_list = stf.objects.all()
        evaluations = []

        for staff in staff_list:
            complaints = comp.objects.filter(allot_id=staff)
            total_complaints = complaints.count()
            resolved_complaints = complaints.filter(status="Completed").count()

            resolution_rate = (Decimal(resolved_complaints) / Decimal(total_complaints) * Decimal(100)) if total_complaints > 0 else Decimal(0)
            satisfaction_score = Decimal(rate.objects.filter(Complaint_id__allot_id=staff).aggregate(Avg('rating'))['rating__avg'] or 0)

            on_time_completions = complaints.filter(completed_date__lte=F('deadline_date')).count()
            timeliness_score = (Decimal(on_time_completions) / Decimal(resolved_complaints) * Decimal(100)) if resolved_complaints > 0 else Decimal(0)

            quality_score = satisfaction_score * Decimal(20)  # Assuming a 5-star scale converted to a percentage

            eps = (resolution_rate * Decimal(0.3)) + (satisfaction_score * Decimal(0.2)) + (timeliness_score * Decimal(0.2)) + (quality_score * Decimal(0.3))

            evaluations.append({
                'staff': staff,
                'resolution_rate': round(resolution_rate, 2),
                'satisfaction_score': round(satisfaction_score, 2),
                'timeliness_score': round(timeliness_score, 2),
                'quality_score': round(quality_score, 2),
                'eps': round(eps, 2),
            })

        return render(request, 'evaluation.html', {'evaluations': evaluations})
    else:
     return redirect('login')
def evaluation_graph(request):
   
    if request.session.get('role', '') == "admin":
        staff_list = stf.objects.all()
        evaluations = []

        for staff in staff_list:
            complaints = comp.objects.filter(allot_id=staff)
            total_complaints = complaints.count()
            resolved_complaints = complaints.filter(status="Completed").count()

            resolution_rate = float((Decimal(resolved_complaints) / Decimal(total_complaints) * Decimal(100)) if total_complaints > 0 else Decimal(0))
            satisfaction_score = float(rate.objects.filter(Complaint_id__allot_id=staff).aggregate(Avg('rating'))['rating__avg'] or 0)

            on_time_completions = complaints.filter(completed_date__lte=F('deadline_date')).count()
            timeliness_score = float((Decimal(on_time_completions) / Decimal(resolved_complaints) * Decimal(100)) if resolved_complaints > 0 else Decimal(0))

            quality_score = float(satisfaction_score * 20)  # Convert satisfaction score to percentage

            # Convert Decimal constants to float before multiplying
            eps = (resolution_rate * 0.3) + (satisfaction_score * 0.2) + (timeliness_score * 0.2) + (quality_score * 0.3)

            evaluations.append({
                'staff_name': staff.Staff_name,  # Convert model object to string
                'resolution_rate': round(resolution_rate, 2),
                'satisfaction_score': round(satisfaction_score, 2),
                'timeliness_score': round(timeliness_score, 2),
                'quality_score': round(quality_score, 2),
                'eps': round(eps, 2),
            })

        # Convert evaluations list to JSON format
        evaluations_json = json.dumps(evaluations)

        return render(request, 'graph.html', {'evaluations': evaluations_json})
    else:
        return redirect('login')
def add_rating(request,id):
     
    if (request.session.get('role', '')== "user"):
  
         if request.method == "POST":
            complaint = get_object_or_404(comp, pk=id)
            rating_value = request.POST.get("rating")

            if rating_value:
                rating_value = float(rating_value)

                # Check if a rating already exists for this complaint
                rating, created = rate.objects.get_or_create(Complaint_id=complaint, defaults={'rating': rating_value})

                if not created:
                    rating.rating = rating_value  # Update the existing rating
                    rating.save()
                    messages.success(request, "Rating updated successfully!")
                else:
                    messages.success(request, "Rating added successfully!")

            else:
                messages.error(request, "Invalid rating value!")

         return redirect("add_complaints")  # Redirect to your complaints page
      
     
    else:
      return redirect('login')
    






def makedata_set(request):
    if request.session.get('role', '') != "admin":
        return redirect('login')

    # Define CSV file path
    file_path = os.path.join(settings.MEDIA_ROOT, 'Data/employee_dataset.csv')

    # Fetch staff data
    staff_list = stf.objects.all()
    evaluations = []

    for staff in staff_list:
        complaints = comp.objects.filter(allot_id=staff)
        total_complaints = complaints.count()
        resolved_complaints = complaints.filter(status="Completed").count()
        pending_tickets = total_complaints - resolved_complaints  # 🔹 Pending tickets calculation

        resolution_rate = (resolved_complaints / total_complaints * 100) if total_complaints > 0 else 0
        satisfaction_score = rate.objects.filter(Complaint_id__allot_id=staff).aggregate(Avg('rating'))['rating__avg'] or Decimal(0)
        on_time_completions = complaints.filter(completed_date__lte=F('deadline_date')).count()
        timeliness_score = (on_time_completions / resolved_complaints * 100) if resolved_complaints > 0 else 0
        quality_score = float(satisfaction_score) * 20  # Convert satisfaction score to percentage

        # EPS Calculation (Convert Decimal to float)
        eps = (
            float(resolution_rate) * 0.3 + 
            float(satisfaction_score) * 0.2 + 
            float(timeliness_score) * 0.2 + 
            float(quality_score) * 0.3
        )

        evaluations.append({
            'staff_id': staff.Staff_id,
            'staff_name': staff.Staff_name,
            'experience': staff.Staff_experience,
            'resolution_rate': round(resolution_rate, 2),
            'satisfaction_score': round(float(satisfaction_score), 2),
            'timeliness_score': round(timeliness_score, 2),
            'quality_score': round(quality_score, 2),
            'pending_tickets': pending_tickets,  # 🔹 Added pending tickets
            'eps': round(eps, 2),
        })

    # Define CSV headers
    headers = [
        "Employee_ID", "Name", "Experience", "Resolution_Rate", 
        "Satisfaction_Score", "Timeliness_Score", "Quality_Score", 
        "Pending_Tickets", "EPS"  # 🔹 Added Pending Tickets column
    ]

    # Write data to CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for eval in evaluations:
            writer.writerow([
                eval['staff_id'], eval['staff_name'], eval['experience'], 
                eval['resolution_rate'], eval['satisfaction_score'], 
                eval['timeliness_score'], eval['quality_score'], 
                eval['pending_tickets'], eval['eps']  # 🔹 Write Pending Tickets
            ])

    # Render dataset display page
    return render(request, 'dataset_display.html', {'evaluations': evaluations})

def train_data(request):
    # Ensure only admin can access
    if request.session.get('role', '') != "admin":
        return redirect('login')
    
    # Define file paths
    data_dir = os.path.join(settings.MEDIA_ROOT, "Data")
    file_path = os.path.join(data_dir, "employee_dataset.csv")
    model_path = os.path.join(data_dir, "task_allocation_model.pkl")
    scaler_path = os.path.join(data_dir, "scaler.pkl")
    report_path = os.path.join(data_dir, "classification_report.json")
    
    # Load Dataset
    df = pd.read_csv(file_path)
    
    # Define Features (X) and Target (y)
    X = df[['Experience', 'Resolution_Rate', 'Satisfaction_Score', 'Timeliness_Score', 'Quality_Score', 'Pending_Tickets', 'EPS']]
    y = df['Task_Assigned']
    
    # Handle Class Imbalance with SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    
    # Normalize Features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_resampled)
    
    # Split data into training & test sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_resampled, test_size=0.2, random_state=42)
    
    # Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions & Classification Report
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Rename "f1-score" to "f1_score"
    for key, value in report.items():
        if isinstance(value, dict) and "f1-score" in value:
            value["f1_score"] = value.pop("f1-score")

    # Rearrange report order: First class labels, then accuracy, then avg metrics
    ordered_report = {key: report[key] for key in sorted(report.keys()) if key not in ['accuracy', 'macro avg', 'weighted avg']}
    ordered_report["accuracy"] = report["accuracy"]
    ordered_report["macro avg"] = report["macro avg"]
    ordered_report["weighted avg"] = report["weighted avg"]

    # Save Report as JSON
    with open(report_path, 'w') as report_file:
        json.dump(ordered_report, report_file, indent=4)
    
    # Save Model & Scaler
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    with open(scaler_path, 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)
    
    return render(request, 'classification_report.html', {'report': ordered_report})



def get_recommendations(request, complaint_id):
    try:
        # Define paths for model and scaler
        data_dir = os.path.join(settings.MEDIA_ROOT, "Data")
        model_path = os.path.join(data_dir, "task_allocation_model.pkl")
        scaler_path = os.path.join(data_dir, "scaler.pkl")

        # Load model & scaler
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        with open(scaler_path, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        # Get all staff data
        staff_list = stf.objects.all()
        recommendations = []
        debug_logs = []  # Collect debugging steps

        for staff in staff_list:
            debug_logs.append(f"Processing Staff: {staff.Staff_name} (ID: {staff.Staff_id})")

            # Fetch complaints assigned to staff
            complaints = comp.objects.filter(allot_id=staff)
            total_complaints = complaints.count()
            resolved_complaints = complaints.filter(status="Completed").count()
            pending_tickets = total_complaints - resolved_complaints  

            debug_logs.append(f"Total Complaints: {total_complaints}, Resolved: {resolved_complaints}, Pending: {pending_tickets}")

            # Performance metrics
            resolution_rate = (resolved_complaints / total_complaints * 100) if total_complaints > 0 else 0
            satisfaction_score = rate.objects.filter(Complaint_id__allot_id=staff).aggregate(Avg('rating'))['rating__avg'] or Decimal(0)
            on_time_completions = complaints.filter(completed_date__lte=F('deadline_date')).count()
            timeliness_score = (on_time_completions / resolved_complaints * 100) if resolved_complaints > 0 else 0
            quality_score = float(satisfaction_score) * 20  

            debug_logs.append(f"Resolution Rate: {resolution_rate:.2f}%, Satisfaction Score: {satisfaction_score}, Timeliness Score: {timeliness_score:.2f}%, Quality Score: {quality_score}")

            # EPS Calculation (convert Decimal to float explicitly)
            eps = (
                float(resolution_rate) * 0.3 +
                float(satisfaction_score) * 0.2 +
                float(timeliness_score) * 0.2 +
                float(quality_score) * 0.3
            )

            debug_logs.append(f"EPS Score: {eps:.2f}")

            # Prepare feature vector & normalize
            feature_vector = np.array([[staff.Staff_experience, resolution_rate, float(satisfaction_score), timeliness_score, quality_score, pending_tickets, eps]])
            scaled_features = scaler.transform(feature_vector)

            # Predict task assignment suitability
            task_assigned = model.predict(scaled_features)[0]

            debug_logs.append(f"Predicted Task Suitability: {task_assigned}")

            recommendations.append({
                "Staff_id": staff.Staff_id,
                "Staff_name": staff.Staff_name,
                "recommended_task": int(task_assigned)  # Convert NumPy int64 to regular int
            })

        return JsonResponse({"employees": recommendations, "debug_logs": debug_logs}, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
