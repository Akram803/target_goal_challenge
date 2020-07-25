from django.urls import path
from .views import HomeView, this_week

app_name = "ta_go_cha"
urlpatterns = [
    path( "", HomeView , name="home"),
    path( "this-week/", this_week , name="home"),
    
    

]
