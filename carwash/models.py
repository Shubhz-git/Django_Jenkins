from django.db import models
from django.conf import settings

# Create your models here.

class Carwashbooking(models.Model):
    bookingId = models.CharField(max_length=15)
    packageType = models.CharField(max_length=100)
    carWashPoint = models.CharField(max_length=100, null=True)
    fullName = models.CharField(max_length=150, null=True)
    mobileNumber = models.CharField(max_length=15, null=True)
    washDate = models.DateField(null=True)
    washTime = models.TimeField(null=True)
    message = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50, null=True)
    adminRemark = models.CharField(max_length=300, null=True)
    paymentMode = models.CharField(max_length=100, null=True)
    txnNumber = models.CharField(max_length=50, null=True)
    postingDate = models.DateTimeField(auto_now_add=True)
    lastUpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.bookingId

class Enquiry(models.Model):
    FullName = models.CharField(max_length=150, null=True)
    EmailId = models.CharField(max_length=100, null=True)
    Contact = models.CharField(max_length=15, null=True)
    Subject = models.CharField(max_length=100, null=True)
    Description = models.CharField(max_length=300, null=True)
    PostingDate = models.DateField(null=True)
    Status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.EmailId

class Washingpoints(models.Model):
    washingPointName = models.CharField(max_length=200, null=True)
    washingPointAddress = models.CharField(max_length=250, null=True)
    contactNumber = models.CharField(max_length=15, null=True)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.washingPointName# Create your models here.
