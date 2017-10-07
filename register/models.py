from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class StudentDetails(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	hallticketnumber = models.IntegerField(default=160114733000)
	branch = (
    		('CSE','Computer Science & Engineering'),
    		('IT','Information Technology'),
    		('ECE','Electrical & Electronics Engineering')
    	)
	branchname = models.CharField(max_length=3, choices=branch)
	section = models.IntegerField()
#class StudentDetails(models.Model):
    #author = models.ForeignKey('auth.User')
#    firstname = models.CharField(max_length=30)
#    lastname = models.CharField(max_length=30)
#    date_of_join = models.DateTimeField(default=timezone.now)
    
    #text = models.TextField()
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    #published_date = models.DateTimeField(
    #        blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    #def __str__(self):
    #    return self.title