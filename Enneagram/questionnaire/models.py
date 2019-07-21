from django.db import models

# Create your models here.


class Question(models.Model):
    qid = models.IntegerField(primary_key=True)
    qcontent = models.CharField(max_length=200)
    qclass = models.IntegerField()

    def __str__(self):
        return self.qcontent

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ccontent = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ccontent