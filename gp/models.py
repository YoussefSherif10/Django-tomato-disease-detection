from django.db import models

class Rec(models.Model):
    disease = models.CharField(max_length=100)
    avoid = models.TextField()
    bp = models.TextField()

    # Shows up in the admin list
    def __str__(self):
        return self.disease


class Imaage(models.Model):
    name= models.CharField(max_length=100)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)

