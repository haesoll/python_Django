from django.db import models

# Create your models here.


# (models.E004) 'id' can only be used as a field name if the field also sets 'primary_key=True'.
class MemberInfo(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    tel = models.EmailField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

# 글번호는 Django에서 자동으로 만들어짐
class Board(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Study(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)