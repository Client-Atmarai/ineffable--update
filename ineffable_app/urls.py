from django.urls import path,include
from ineffable_app import views

urlpatterns = [
    path('',views.home,name=""),
    path('about/',views.about,name="about"),
    path('notice/',views.notice,name="notice"),
    path('contact/',views.contact,name="contact"),
    path('index/',views.index,name="index"),
    path('hello/',views.hello),
    # path('logout_admin/',views.admin_logout,name="admin_logout"),
    # path('enq_form/',views.enq_form,name="enq_form"),
    # path('adduser/',views.adduser,name='adduser'),
    path('centre_login/',views.centre_login,name="centre_login"),
    # path('add_student/',views.add_student,name="add_student"),
    # path('student_status/',views.status_check,name="status_check"),
    # # path('admin_check_status/',views.admin_check_status,name="admin_check_status"), 
    path('courses/',views.courses,name="courses"),
    path('search/',views.search,name="search"),
    path('searchcentre/',views.searchcentre,name="searchcentre"),
    path('login_centre/',views.login_centre,name="login_centre"),
    path('centrelogin/',views.centrelogin,name="centrelogin"),
   
]

