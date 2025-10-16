from django.urls import path
from lumapp import views
urlpatterns=[path('add_course/',views.add_course,name='add_course'),
             path('save_course/',views.save_course,name='save_course'),
             path('display_course/',views.display_course,name='display_course'),
             path('edit_course/<int:c_id>',views.edit_course,name='edit_course'),
             path('update_course/<int:c_id>',views.update_course,name='update_course'),
             path('delete_course/<int:c_id>',views.delete_course,name='delete_course'),
             path('add_employee/',views.add_employee,name='add_employee'),
             path('save_employee/',views.save_employee,name='save_employee'),
             path('display_employee/',views.display_employee,name='display_employee'),
             path('edit_employee/<int:e_id>',views.edit_employee,name='edit_employee'),
             path('update_employee/<int:e_id>',views.update_employee,name='update_employee'),
             path('delete_employee/<int:e_id>',views.delete_employee,name='delete_employee'),
             path('add_student',views.add_student,name='add_student')]