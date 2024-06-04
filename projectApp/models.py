from django.db import models

# Create your models here.

class projectModel(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.IntegerField(default=00)

    class Meta:
        db_table = 'project_Data'