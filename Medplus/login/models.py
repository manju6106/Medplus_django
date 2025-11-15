from django.db import models

class Register(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    DOB = models.DateField()
    phno = models.CharField(max_length=15)
    email = models.EmailField()
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Login(models.Model):
    username=models.CharField(primary_key=True)
    password=models.CharField(max_length=20)

class Medicine(models.Model):
    mid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    expiry = models.DateField()
    usage = models.TextField()
    dosage = models.TextField()
    image = models.ImageField(upload_to='meds/')


#
# class operator(models.Model):
#     opid=models.IntegerField(max_length=20,primary_key=True)
#     uname=models.CharField(max_length=20)
#     pwd=models.CharField(max_length=10)
#     g=models.CharField(max_length=10)
#     phno=models.IntegerField(max_length=10)
#
# class Bill(models.Model):
#     # mname = models.CharField(max_length=100)
#     mname = models.CharField(max_length=50, default='unknown')
#     date = models.DateField(auto_now_add=True)
#     amount = models.IntegerField()


class Operator(models.Model):
    opid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=10)
    g = models.CharField(max_length=10)
    phno = models.CharField(max_length=15)

class Bill(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    mname = models.CharField(max_length=50, default='unknown')
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"Bill {self.id} by {self.operator.uname}"



