### account/models.py

from django.db import models
from django.contrib.auth.models import User

####################################################################################################
### Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=1000, null=True)
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

####################################################################################################
### Post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    post_likes_count = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"

class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    comment_likes_count = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"

class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
       
class Replay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    replay_likes_count = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"

class ReplayLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    replay = models.ForeignKey(Replay, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

####################################################################################################
### Question
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    question_votes_count = models.PositiveIntegerField(default=0)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

### Question Status
class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

### Question Votes
class QuestionVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"

### Answer
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    answer_votes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.question}"

### Answer Votes
class AnswerVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"
    
####################################################################################################
### Disease
class Disease(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='disease/', blank=True, null=True)
    body = models.TextField(max_length=1000)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"
    
### Disease Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    
### Therapy
class Therapy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='therapy/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"

### Replay Therapy
class ReplayTherapy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"

