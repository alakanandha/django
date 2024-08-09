from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('show',views.show,name='show'),
    path('departments',views.departments,name='departments'),
    path('doctor',views.doctor),
    path('booking',views.booking),
]