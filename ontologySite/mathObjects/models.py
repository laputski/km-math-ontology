from django.db import models

class Theorem(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    proof = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title

class Definition(models.Model):
    theorem = models.ForeignKey(Theorem)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title 