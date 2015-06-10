from django.db import models


class Requisite(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    payee_code = models.CharField(max_length=10, null=False, blank=False)
    bank_code = models.CharField(max_length=6, null=False, blank=False)
    account = models.CharField(max_length=20, null=False, blank=False)


class Parameter(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    requisite = models.ForeignKey(Requisite)


class Payment(models.Model):
    sender_name = models.CharField(max_length=50, null=False, blank=False)
    sender_address = models.CharField(max_length=100, null=False, blank=False)
    payee_name = models.CharField(max_length=50, null=False, blank=False)
    payee_code = models.CharField(max_length=10, null=False, blank=False)
    bank_code = models.CharField(max_length=6, null=False, blank=False)
    account = models.CharField(max_length=20, null=False, blank=False)
    amount = models.DecimalField()
    remark = models.CharField(max_length=160, null=False, blank=True)


class PaymentParameter(models.Model):
    value = models.CharField(max_length=200, null=False, blank=False)
    parameter = models.ForeignKey(Parameter)
    payment = models.ForeignKey(Payment)
