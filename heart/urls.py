from django.urls import path
from . import views
urlpatterns=[
    path('',views.index , name="index"),
    path('cardio/',views.cardio ,name='cardio'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view , name='logout_view'),
    path('signup/',views.SignUp,name='SignUp'),
    path('contact/',views.contact_view,name="contact"),
    path('cooming_soon/',views.commingsoon,name="cooming_soon"),
    path('prediction/',views.prediction_view,name="prediction"),
    # path('p/',views.PatientView.as_view(),name='p'),
    path('patient_report/<int:pk>/',views.patient_report,name='patient_report'),
    path('article/' ,views.ListArticles.as_view(),name="article"),
    path('article_detail/<int:pk>' ,views.DetailArticle.as_view(),name="detail_article"),
    path('doctors/',views.DoctorsList.as_view(),name="doctors"),
    path('doctors_detail/<int:pk>',views.DoctorsDetail.as_view(),name="doctors_detail")
]