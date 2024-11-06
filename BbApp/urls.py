from django.urls import path
from . import views
from django.contrib.auth import views as bb
urlpatterns = [
    path('',views.home,name="hm"),
    path('blgr/',views.bloodgroups,name="bg"),
    path('dodo/',views.donat,name="dd"),
    path('reqa/',views.requestss,name="rea"),
    path('regi/',views.register,name="reg"),
    path('abt/',views.about,name="ab"),
    path('lgn/',bb.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('lgot/',bb.LogoutView.as_view(template_name="html/logout.html"),name="lgt"),
    path('usrlist/',views.userlist,name="ul"),
    path('pfle/',views.profile,name="pf"),
    path('uppf/',views.updprofile,name="upf"),
    path('reqm/',views.requestmain,name="req"),
    path('upreq/<int:w>/',views.uprequest,name="ure"),
    path('dlereq/<int:p>/',views.reqdlt,name="dlr"),
    path('dona/',views.donatee,name="doo"),
    path('updon/<int:w>/',views.updonate,name="udn"),
    path('dledon/<int:p>/',views.dondlt,name="dldn"),
    path('chge/',views.chgepwd,name="cge"),
    path('deluser/<int:p>/',views.userdlt,name="du"),
]