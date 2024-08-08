from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Survey(models.Model):
  title = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class Question(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.text

  def __str__(self):
    return self.text

class Choice(models.Model):
  question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.question.text}:{self.text}"

class Submission(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.PROTECT)
  answer = models.ManyToManyField(Choice)
  status = models.CharField(max_length=255)
  
  def __str__(self):
    return self.answer


############################################################################################################

class estadocasino(models.Model):
  estado = models.CharField(max_length=255)
  
  def __str__(self):
    return self.estado

class datoimp(models.Model):
  envia = models.ManyToManyField(Submission)
  importante = models.ForeignKey(Choice, on_delete=models.PROTECT)