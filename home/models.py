from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()


class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/about', blank=True, null=True)


class OurValue(models.Model):
    title= models.CharField(max_length=100)
    body= models.TextField()
    image= models.ImageField(upload_to='images/our-value', blank=True, null=True)
    def __str__(self):
        return self.title

class WorkStatus(models.Model):
    number= models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'WorkStatuses'


class Feature(models.Model):
    title= models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Feature2(models.Model):
    title= models.CharField(max_length=80)
    body= models.TextField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Features2'

class Service(models.Model):
    title= models.CharField(max_length=80)
    body= models.TextField()

    def __str__(self):
        return f'{self.title} - {self.id}'

class Price(models.Model):
    plan= models.CharField(max_length=50)
    price= models.IntegerField(default=0)

    plan_part1= models.CharField(max_length=50)
    plan_part2= models.CharField(max_length=50, null=True, blank=True)
    plan_part3= models.CharField(max_length=50, null=True, blank=True)
    plan_part4= models.CharField(max_length=50, null=True, blank=True)
    plan_part5= models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.plan

class Frequently(models.Model):
    title= models.CharField(max_length=150)
    body= models.TextField()

    class Meta:
        verbose_name_plural = 'Frequentlies'

    def __str__(self):
        return self.title


class Team(models.Model):
    image= models.ImageField(upload_to='images/team', null=True, blank=True)
    name= models.CharField(max_length=100)
    job_title= models.CharField(max_length=65)
    body= models.TextField()

    instagram= models.URLField(unique=True, null= True, blank=True)
    telegram= models.URLField(unique=True, null= True, blank=True)
    x = models.URLField(unique=True, null= True, blank=True)


    def __str__(self):
        return f'{self.name} - {self.job_title}'

class Contact(models.Model):
    name= models.CharField(max_length=80)
    email= models.EmailField()
    subject= models.CharField(max_length=100)
    body= models.TextField()



    def __str__(self):
        return f'{self.name} - {self.subject}'



class ContactUs(models.Model):
    address= models.TextField()
    phoneNumber1= models.CharField(max_length=11)
    phoneNumber2= models.CharField(max_length=11)
    email= models.EmailField()
    open_d_w= models.CharField(max_length=100)
    open_h= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'ContactUs'
