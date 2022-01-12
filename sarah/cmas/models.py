from django.db import models

class Price(models.Model):
    price = models.CharField(max_length=3,unique=False)
    def __str__(self):
        return str(self.price)

class Food(models.Model):
    address = models.CharField(max_length=300)
    price = models.ForeignKey('Price',  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=400)
    foodtype = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class Entertainment(models.Model):
    IN_OUT = (
        ('Indoors', 'Indoors'),
        ('Outdoors', 'Outdoors'),
    )
    TIME_OFDAY = (
        ('Day', 'Daytime'),
        ('Night', 'Nightime'),
        ('both', 'Both'),
    )
    address = models.CharField(max_length=300)
    price = models.ForeignKey('Price',  on_delete=models.CASCADE)
    inout = models.CharField(max_length=20,choices=IN_OUT)
    name = models.CharField(max_length=200) 
    timeOfday = models.CharField(max_length=20,choices=TIME_OFDAY)
    description = models.CharField(max_length=1000) 
    link = models.CharField(max_length=400)
    
    
    def __str__(self):
        return self.name

class DC_facts(models.Model):
    facts = models.CharField(max_length=1000)
    num = models.IntegerField(default=0)
    
    def __str__(self):
        return self.facts
class BookStores(models.Model):
    address = models.CharField(max_length=300)
    price = models.ForeignKey('Price',  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000) 
    link = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
    

       
