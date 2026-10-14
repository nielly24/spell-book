from django.db import models

class Flower(models.Model):
    flower_name = models.CharField(max_length=100)
    price = models.IntegerField()

class Payment(models.Model):
    price = models.ForeignKey(Flower, on_delete=models.CASCADE, db_column='price_id')
    total_amount = models.IntegerField()

class ArrangementType(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    mode_of_payment = models.CharField(max_length=100)
    arrangement = models.ForeignKey(ArrangementType, on_delete=models.CASCADE)