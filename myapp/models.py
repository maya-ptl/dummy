from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# class Mymodel(models.Model):
#   name = models.CharField(max_length=90)


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
  profile_image = models.FileField(upload_to ="media/",null=True,blank=True)
  username = models.CharField(max_length=50,unique=True,default='')
  bio = models.CharField(max_length=200)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  hobby = models.CharField(max_length=100)
  # age = models.IntegerField()




class Post(models.Model):
  user_name = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=255, blank=True)
  pic = models.FileField(upload_to="media/")
  date_posted = models.DateTimeField(default=timezone.now)
	

  def get_absolute_url(self):
		 return reverse('post-detail', kwargs={'pk': self.pk})
  





class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	write_comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)
  
 


class Comment_Like(models.Model):
  comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
 

# class Reply_on_Commnet(models.Model):
#   commetn = models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='reply')



class Like(models.Model):
	user = models.OneToOneField(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
	


# class Share(models.Model):
#   post = models.ForeignKey(Post,on_delete=models.CASCADE)
#   user = models.ForeignKey(Post,on_delete=models.CASCADE)


class Photo(models.Model):
  post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='photo')
  # user=



# class FreindList(models.Model):
#   user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
#   freind = models.ForeignKey(User,on_delete=models.CASCADE,related_name='freind') 




