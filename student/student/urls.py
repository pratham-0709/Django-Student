"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.student_list),
    path('student_update/',views.student_list_by_id),
    path('stud_details/',views.stud_details1),
    path('stud_details1/<int:prn>',views.stud_details_update),
    path('marks/',views.sub_marks_detail),
    path('marks/<int:prn>/<str:sub>',views.sub_marks_update),
    path('All_details/<int:prn>',views.all_details),
    path('All_details1/<int:prn>',views.all_details_usingRelation)
    
]
