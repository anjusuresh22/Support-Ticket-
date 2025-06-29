from django.db import models
from datetime import datetime

# Create your models here.
class login(models.Model):
    log_id = models.AutoField(primary_key=True)
    username = models.CharField("username", max_length=100)
    password = models.CharField("password", max_length=100)
    role = models.CharField("role", max_length=100)
#log_id,username,password,role

class Staff(models.Model):
   Staff_id= models.AutoField(primary_key=True)
   Staff_name= models.CharField("Name",max_length=100)
   Staff_address = models.CharField("Staff_address", max_length=500)
   Staff_email = models.EmailField("Staff_email", max_length=200)
   Staff_phone=models.CharField("Staff_phone",max_length=100)
   Staff_qualification = models.CharField("Staff_qualification", max_length=200)
   Staff_designation = models.CharField("Staff_designation", max_length=100)
   Staff_experience = models.CharField("Staff_experience", max_length=100)
   Staff_photo = models.FileField("Staff_photo", max_length=1000,upload_to='images/')
   Staff_status=models.CharField("Staff_status",max_length=50,default="")
   Staff_logid=models.ForeignKey(login, on_delete=models.CASCADE, null=True)
#Staff_id,Staff_name,Staff_address,Staff_email,Staff_phone,Staff_qualification, Staff_designation,Staff_experience,Staff_photo,Staff_status,Staff_logid


class User(models.Model):
    User_id= models.AutoField(primary_key=True)
    User_name=models.CharField("uname", max_length=200)
    User_address=models.CharField("address", max_length=200)
    User_email=models.CharField("email", max_length=100)
    User_phone=models.CharField("phone", max_length=100)
    User_alt_No=models.CharField("altno", max_length=200)
    User_status=models.CharField("status", max_length=200)
    Log_id=models.ForeignKey(login, on_delete=models.CASCADE, null=True)
#User_id,User_name,User_address,User_email,User_phone,User_alt_No,Log_id,User_status

class Complaint(models.Model):
    Complaint_id= models.AutoField(primary_key=True)
    Complaint_subject= models.CharField("subject", max_length=100)
    Complaint_message= models.CharField("message", max_length=500)
    Complaint_date= models.CharField("date", max_length=100)
    Complaint_reply= models.CharField("replay", max_length=500)
    User_id =models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Complaint_priority= models.CharField("priority", max_length=100, null=True)
    Complaint_product= models.CharField("productdetails", max_length=100, null=True)
    allot_id =models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="Pending",null=True)
    assigned_date = models.DateField(null=True, blank=True)
    deadline_date = models.DateField(null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)

#Complaint_id,Complaint_subject,Complaint_message,Complaint_, null=Truedate,Complaint_reply,User_id


class menutype(models.Model):
    type_id= models.AutoField(primary_key=True)
    type_name = models.CharField("type_name", max_length=100)
#type_id,type_name

class menu(models.Model):
    menu_id= models.AutoField(primary_key=True)
    menu_name = models.CharField("menu_name", max_length=100)
    menu_price = models.CharField("menu_price", max_length=100)
    menu_type =models.ForeignKey(menutype, on_delete=models.CASCADE, null=True)
    menu_photo = models.FileField("menu_photo", max_length=1000,upload_to='images/')
#menu_id,menu_name,menu_price,menu_type,menu_photo
class menustock(models.Model):
    stock_id= models.AutoField(primary_key=True)
    menu_id=models.ForeignKey(menu, on_delete=models.CASCADE, null=True)
    qty = models.CharField("qty", max_length=100)
    date = models.CharField("date", max_length=100)
#stock_id,menu_id,qty,date

class cart(models.Model):
    cart_id= models.AutoField(primary_key=True)
    stock_id=models.ForeignKey(menustock, on_delete=models.CASCADE, null=True)
    menu_id=models.ForeignKey(menu, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pqty = models.CharField("pqty", max_length=100)
    cart_date=models.CharField("date", max_length=100)
    cart_status = models.CharField("cart_status", max_length=100)
#cart_id,stock_id,menu_id,user,pqty,cart_status
class bill(models.Model):
    billno= models.AutoField(primary_key=True)
    date=models.CharField("date", max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total=models.CharField("date", max_length=100)
    order_status = models.CharField("order_status", max_length=100)
#billno,date,user,total,order_status
class orderlist(models.Model):
    orderno= models.AutoField(primary_key=True)
    cart_id=models.ForeignKey(cart, on_delete=models.CASCADE, null=True)
    billno=models.ForeignKey(bill, on_delete=models.CASCADE, null=True)
    
#orderno,cart_id,billno

class Amc(models.Model):
    amc_id= models.AutoField(primary_key=True)
    amc_from= models.CharField("date", max_length=100)
    Description= models.CharField("message", max_length=500)
    amc_to= models.CharField("date", max_length=100)
    amc_amount= models.CharField("replay", max_length=500)
    User_id =models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amc_status= models.CharField("priority", max_length=100)
  
class chat(models.Model):
    chat_id= models.AutoField(primary_key=True)
    chat_message = models.CharField(max_length=150)
    chat_date=models.DateTimeField(default=datetime.now, blank=True)
    chat_first_person_login_id = models.IntegerField()
    chat_second_person_login_id = models.IntegerField()
    chat_user = models.CharField(max_length=50)


class rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    Complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)