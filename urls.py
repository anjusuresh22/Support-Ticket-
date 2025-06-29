from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="index"),
    path('login/', views.login,name="login"),
    path('registration/', views.registration,name="registration"),
    path('index', views.index,name="index"),
    path('SignUp',views.SignUp,name="SignUp"),
    path('Adminhome',views.Adminhome,name="Adminhome"),
    path('Userhome',views.Userhome,name="Userhome"),
    path('Staffhome',views.Staffhome,name="Staffhome"),
    path('Logout',views.Logout,name="Logout"),
    path('Privacy',views.Privacy,name="Privacy"),
    path("Appoint_Staff",views.Appoint_Staff,name='Appoint_Staff'),
    path("List_Staff",views.List_Staff,name='List_Staff'),
    path("delete_staff",views.delete_staff,name='delete_staff'),
    path("complaints",views.complaints,name='complaints'),

    path("All_Users",views.All_Users,name='All_Users'),
    path("remove_usr",views.remove_usr,name='remove_usr'),
    path("Profile",views.Profile,name='Profile'),
 
    path('add_complaints',views.add_complaints,name="add_complaints"),
    path('Manage_complaints',views.Manage_complaints,name="Manage_complaints"),
    path('Manage_Menutype',views.Manage_Menutype,name="Manage_Menutype"),
    path('Manage_Menu',views.Manage_Menu,name="Manage_Menu"),
    path('Manage_Stock',views.Manage_Stock,name="Manage_Stock"),
    path('delete_type',views.delete_type,name="delete_type"),
    path('delete_menu',views.delete_menu,name="delete_menu"),
    path('getmenu',views.getmenu,name="getmenu"),
    path('getdt',views.getdt,name="getdt"),
    path('delete_stock',views.delete_stock,name="delete_stock"),
    path('getlist',views.getlist,name="getlist"),
    path('add_cart',views.add_cart,name="add_cart"),
    path('mycart',views.mycart,name="mycart"),
    path('apply_amc',views.apply_amc,name="apply_amc"),
    path('View_Amc',views.View_Amc,name="View_Amc"),
    path('Alloted_works',views.Alloted_works,name="Alloted_works"),



    path('remct',views.remct,name="remct"),
    path('redct',views.redct,name="redct"),
    path('addct',views.addct,name="addct"),
    path('proceed',views.proceed,name="proceed"),
    path('myorder',views.myorder,name="myorder"),
    path('myorderitem',views.myorderitem,name="myorderitem"),
    path('myorder1',views.myorder1,name="myorder1"),
    path('myorderitem1',views.myorderitem1,name="myorderitem1"),
    path('updateorder',views.updateorder,name="updateorder"),
    path('myorder2',views.myorder2,name="myorder2"),
    path('myorderitem2',views.myorderitem2,name="myorderitem2"),

    path('edit_menu',views.edit_menu,name="edit_menu"),
    path('Update_Menu',views.Update_Menu,name="Update_Menu"),
    path('edit_type',views.edit_type,name="edit_type"),
    path('Update_Menutype',views.Update_Menutype,name="Update_Menutype"),
    path('chat',views.chat,name="chat"),
    path('chat_save',views.chat_save,name="chat_save"),
    path('chat_display',views.chat_display,name="chat_display"),
    path('chat_admin',views.chat_admin,name="chat_admin"),
    path("chat_adm_user",views.chat_adm_user,name='chat_adm_user'),

    path('chat_display_adm',views.chat_display_adm,name="chat_display_adm"),
    path('chat_save_adm',views.chat_save_adm,name="chat_save_adm"),
  
    path('chat_staff_admin',views.chat_staff_admin,name="chat_staff_admin"),
    path("chat_adm_staff",views.chat_adm_staff,name='chat_adm_staff'),
    path('chat_save_adm_staff',views.chat_save_adm_staff,name="chat_save_adm_staff"),
    path('chat_display_adm_staff',views.chat_display_adm_staff,name="chat_display_adm_staff"),
    path('chat_staff',views.chat_staff,name="chat_staff"),
    path('chat_save_staff',views.chat_save_staff,name="chat_save_staff"),
    path('chat_display_staff',views.chat_display_staff,name="chat_display_staff"),

 path('complete_work/<int:id>',views.complete_work,name="complete_work"),
path('add_rating/<int:id>',views.add_rating,name="add_rating"),  

path('employee-evaluation',views.employee_evaluation,name="employee-evaluation"), 
  path('evaluation-graph',views.evaluation_graph,name="evaluation-graph"), 

path('makedata_set',views.makedata_set,name="makedata_set"),
path('train_data',views.train_data,name="train_data"),
 path('get_recommendations/<int:complaint_id>/', views.get_recommendations, name='get_recommendations'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
