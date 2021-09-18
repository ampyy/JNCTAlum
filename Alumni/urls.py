from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup", views.signup, name="signup"),
    path("batch_details/<str:batch_name>", views.batch_details, name="batch_details"),
    path("batch_details/student_details/<str:user>", views.student_detail, name='student_details'),
    path("user_info_update/<int:pk>", views.UserInfoBasicsUpdateView.as_view(), name="update_info"),
    path("myprofile", views.ProfileView.as_view(), name="myprofile"),

    path("verify_update", views.verify, name='verify_update'),
    path("link_update/<int:pk>", views.UserLinkInfoUpdateView.as_view(), name='user_link_update'),
    path("myprofile/addthought", views.ThoughtsByUserCreateView.as_view(), name='addthought'),
    path("myprofile/updatethought/<int:pk>", views.ThoughtByUserUpdateView.as_view(), name='updatethought'),
    path("myprofile/deletethought/<int:pk>", views.ThoughtByUserDeleteView.as_view(), name='deletethought'),
    path("myprofile/addinternshipjob", views.JobCreateView.as_view(), name='addjob'),
    path("myprofile/updateinternshiporjob/<int:pk>", views.JobUpdateView.as_view(), name='updatejob'),
    path("myprrofile/deleteinternshiporjob/<int:pk>", views.JobDeleteView.as_view(), name='deletejob'),
    path("myprofile/addskill", views.SkillsCreateView.as_view(), name='addskill'),
    path("myprofile/updateskill/<int:pk>", views.SkillsUpdateView.as_view(), name='updateskill'),
    path("myprofile/deleteskill/<int:pk>", views.SkillsDeleteView.as_view(), name='deleteskill'),
    path("notes", views.notes, name='notes'),
    path("insights",views.InsightsListView.as_view(), name='insights'),
    path("myprrofile/deleteinternshiporjob/<int:pk>", views.JobDeleteView.as_view(), name='deletejob'),

]
