from django.urls import path
from .views import HomeView, this_week , goals

app_name = "ta_go_cha"
urlpatterns = [
    path( "", HomeView , name="home"),
    path( "goals/", goals , name="goals"),
    path( "this-week/", this_week , name="this-week"),
    
    

]
 