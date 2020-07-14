from django.contrib import admin
from .models import ( 
                Target,
                Goal,
                Challenge,
                Challenge,
                ChallengeLogs
                )   

# Register your models here.
@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'st_date' )
    list_filter = ('name', 'st_date' )
#   fields = [('availability', 'quantity')]

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("name", 'target', 'periority', 'st_date' )
    list_filter = ("name", 'target', 'periority', 'st_date' )
#   fields = [('availability', 'quantity')]

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        'goal',
        'n',
        'what',
        'per',
        'st_date',
        )
    list_filter = ('goal', 'per', 'st_date' )
#   fields = [('availability', 'quantity')]


@admin.register(ChallengeLogs)
class ChallengeLogsAdmin(admin.ModelAdmin):
    list_display = (
        'goal',
        'count',
        'date',
        'time',
        )
    list_filter = ('goal', 'date', 'time' )
#   fields = [('availability', 'quantity')]











