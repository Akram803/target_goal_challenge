from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .forms import TargetForm
import datetime
from django.utils import timezone


from .models import( 
                    Target,
                    Goal,
                    Challenge,
                    ChallengeLogs,
                    ) 


class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        if request.user.is_authenticated:
            targets = Target.objects.filter(user=request.user,)

        print(  Common.weak_range()  )

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
    
    def get_context_data(self, **kwargs):

        targets = Target.objects.filter(user=self.request.user.id)

        return {
            "targets": targets,
        }




# class TargetListView(View):
#     template_name = "target-list.html"

#     def get(self, request, *args, **kwargs):
#         t = Targets.objects.filter(user=request.user,)

#         print(  Common.weak_range()  )

#         return render(request, self.template_name, {"targets":t})

#     def post(self, request, *args, **kwargs):
#         return HttpResponse('POST request!')

class TargetCreateView(View):
    template_name = "target-create.html"

    def get(self, request, *args, **kwargs):
        form = TargetForm()
        return render(request, self.template_name, {"form":form})

    def post(self, request, *args, **kwargs):
        form = TargetForm(request.POST)
        if form.is_valid:
            T = form.save(commit=False)
            T.user = request.user
            T.save()
            redirect(T.get_absolute_url())
        return HttpResponse('POST request!')

class SubTargetLitView(View):
    def get(self, request, *args, **kwargs):
        main_target= get_object_or_404(Target, user=request.user, slug=self.kwargs.get("name"))
        sub_targets = Goal.objects.filter(user=request.user, main_Target=main_target)
        print(main_target)
        print(sub_targets)
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')






class Common:

    __instance = None


    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Common.__instance == None:
            Common()
        return Common.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Common.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Common.__instance = self
    @staticmethod 
    def weak_range():
        the_day = datetime.date.today()
        dirst_week_day = (the_day.isoweekday() + 2) % 7 

        # The start of the week
        start = the_day - datetime.timedelta(days=dirst_week_day-1)
        # The start of the week
        end = the_day + datetime.timedelta(days=(7-dirst_week_day))
        return (str(start), str(end))


    















def this_week(req):
    context = {
        
        "days":["sat","sun","mon","tus","wed","thr","fri"],
        "goals":[
            {
                "name":"prayer",
                "values":[4,4,3.5,5,5,4,5]
            },{
                "name":"English",
                "values":[1,0,1,1,0,0,1]
            },{
                "name":"problem solving",
                "values":[1,1,2,1,0,0,1]
            },       
        ]
        }
    return render(req,"this-week.html",context)