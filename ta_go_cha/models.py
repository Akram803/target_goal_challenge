from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Target(models.Model):

    user = models.ForeignKey( User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100, )
    slug = models.SlugField(unique=True)
    st_date = models.DateField(auto_now=False, auto_now_add=True) 
    periority = models.IntegerField(default=0)    
    
    class Meta:
        verbose_name = ("target")
        verbose_name_plural = ("target")
        ordering = ["periority"]
        unique_together = [  
            ["user" ,"name"],
            ["user" , 'periority'],
          ]

    def __str__(self):
        return self.name        

    def get_absolute_url(self):
        return reverse("ta_go_cha:sub-targets-list", kwargs={"name": self.slug})

def pre_save_target_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_target_receiver,Target)


class Goal(models.Model):

    user = models.ForeignKey( User , on_delete=models.CASCADE)
    target = models.ForeignKey("ta_go_cha.Target", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    st_date = models.DateField(auto_now=False, auto_now_add=True)
    periority = models.IntegerField(default=0)
    n_units = models.IntegerField(default=0)
    

    class Meta:
        verbose_name = ("goal")
        verbose_name_plural = ("goal")
        unique_together = [  ["user", "target", "name"],
                             ["user", "target", "periority"] ]
        ordering = ["periority"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Sub_Targets_detail", kwargs={"pk": self.pk})


class Challenge(models.Model):

    user = models.ForeignKey( User , on_delete=models.CASCADE)
    target = models.ForeignKey("ta_go_cha.Target", on_delete=models.DO_NOTHING)
    goal = models.ForeignKey("ta_go_cha.Goal", on_delete=models.CASCADE)
    n = models.IntegerField()
    what = models.CharField(max_length=50)

    PERIOD_CHOICES = ( 
                        ("d", "day"), 
                        ("w", "weak"), 
                        ("m", "month"),
                        ) 
    per = models.CharField( 
        max_length = 1, 
        choices = PERIOD_CHOICES, 
        ) 
        
    st_date = models.DateField(auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = ("challenge")
        verbose_name_plural = ("challenge")

    def __str__(self):
        return str(self.goal.name +": "+ str(self.n) +" " +self.what+ " per " + self.per)

    def get_absolute_url(self):
        return reverse("Goals_detail", kwargs={"pk": self.pk})


class ChallengeLogs(models.Model):

    user = models.ForeignKey( User , on_delete=models.CASCADE)
    target = models.ForeignKey("ta_go_cha.Target", on_delete=models.DO_NOTHING)
    goal = models.ForeignKey("ta_go_cha.Goal", on_delete=models.DO_NOTHING)
    challenge = models.ForeignKey("ta_go_cha.Challenge", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.TimeField(auto_now=False, auto_now_add=True)
    count = models.IntegerField()

    class Meta:
        verbose_name = ("challengelogs")
        verbose_name_plural = ("challengelogs")

    def __str__(self):
        return self.goal.__str__()

    def get_absolute_url(self):
        return reverse("goallogs_detail", kwargs={"pk": self.pk})


