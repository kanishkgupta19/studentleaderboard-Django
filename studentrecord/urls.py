from rest_framework import routers
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.apiInfo, name="api-overview"),
    path('students-records/view-all/', views.viewallrecords, name="view-all-records"),
    path('students-records/view/<str:rollno>', views.viewStudentrecord, name="view-single-record"),
    path('students-records/view/sortby/<str:field>', views.viewsortbystudentrecord, name="view-students-record-sortby"),
    path('students-records/create/', views.createnewrecord, name="create-new-record"),
    path('students-records/update/<int:pk>', views.updatestudentrecord, name="update-student-record"),
    path('students-records/delete/<int:pk>', views.deletestudentrecord, name="delete-student-record"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
