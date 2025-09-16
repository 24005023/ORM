from django.db import models 
from django.contrib import admin
class Cars_DB (models.Model):
     Car_name=models.CharField(max_length=20)
     reg_no=models.IntegerField (primary_key=True)
     fuel_type=models.CharField(max_length=20)
     engine_model=models.CharField(max_length=20)
     insurance_no=models.IntegerField()
class Cars_DBAdmin(admin.ModelAdmin):
     list_display=["Car_name","reg_no","fuel_type","engine_model","insurance_no"]

