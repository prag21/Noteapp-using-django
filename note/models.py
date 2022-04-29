from django.db import models
import datetime
class Customer(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    def get1(self):
        if Customer.objects.filter(username=self.username):
            return True
        else:
            return False

    def get2(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    def get3(email,password):
        try:
            return Customer.objects.get(email=email,password=password)
        except:
            return False
   
class Todo(models.Model):
    status_choices=[('C','COMPLETED'),('P','PENDING')]
    priority_choices=[('1','1️⃣'),('2','2️⃣'),('3','3️⃣'),('4','4️⃣'),('5️⃣','PENDING'),('6️⃣','PENDING'),('7️⃣','PENDING'),('8️⃣','PENDING'),('9️⃣','PENDING'),('🔟','PENDING')]
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    date=models.DateField(default=datetime.datetime.today)
    priority=models.CharField(max_length=2, choices=status_choices)
    status=models.CharField(max_length=2, choices=status_choices)
    def get5(user):
        return Todo.objects.filter(user=user)
    def get6(id1):
        return Todo.objects.get(id=id1)

    
       
