from django.db import models
import pickle
from django.contrib.auth.models import User
import tensorflow as tf



class Diseases(models.Model):
    name = models.CharField(max_length=20 )
    age=models.IntegerField(default=0)
    sex=models.IntegerField(default=0,choices={ ('1','male') , ('0','female')})
    cp=models.IntegerField(default=0)
    trestbps=models.IntegerField(default=0)
    chol=models.IntegerField(default=0)
    fbs=models.IntegerField(default=0)
    restecg=models.IntegerField(default=0)
    max_heart_rate=models.IntegerField(default=0)
    exercise_angina = models.IntegerField(default=0)
    oldpeak=models.FloatField(default=0)
    slope = models.IntegerField(default=0)
    target =models.IntegerField(null=True)


    def save(self,*args,**kwargs):
        model = tf.keras.models.load_model('./dl_model/ann')
        self.target = model.predict([[self.age,self.sex,self.cp,self.trestbps,self.chol,self.fbs,self.restecg,self.max_heart_rate,self.exercise_angina,self.oldpeak,self.slope]])
        
        print(self.target)
        if self.target >= 0.5:
            self.targt = 1
        else:
            self.target =0
            
        return super().save(*args , **kwargs)





class Doctors(models.Model):
    name=models.CharField('Doctor Name' ,max_length=100)
    image = models.ImageField(upload_to='doctors')
    spciality=models.CharField("Doctor Spaciality",max_length=100 , choices={
        ('heart','heart'),
        ('brain','brain'),
    })

    address =models.TextField()
    contact =models.CharField(max_length=13)
    desc=models.TextField("About Doctor")
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class Article(models.Model):
    title = models.CharField('Article Title', max_length=100)
    image=models.ImageField( upload_to = 'article/')
    desc=models.TextField('Article Description')
    publish_by =models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

