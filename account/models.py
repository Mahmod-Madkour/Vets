### account/models.py

from django.db import models
from django.contrib.auth.models import User

####################################################################################################
### Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    about = models.TextField(max_length=1000, null=True)
    photo = models.ImageField(default="Profile/Profile-default.png", upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

####################################################################################################
### Post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1000, null=True)
    post_likes_count = models.PositiveIntegerField(default=0, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"

class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500, null=True)
    comment_likes_count = models.PositiveIntegerField(default=0, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"

class CommentLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"
       
class Replay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500, null=True)
    replay_likes_count = models.PositiveIntegerField(default=0, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"

class ReplayLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    replay = models.ForeignKey(Replay, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"

####################################################################################################
### Question
class Question(models.Model):
    STATUS = (
        ('Not Answered', 'Not Answered'),
        ('Answered', 'Answered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, unique=True, null=True)
    body = models.TextField(max_length=1000, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    question_votes_count = models.PositiveIntegerField(default=0, null=True)
    #status = models.ForeignKey("Status", on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=200, default="Not Answered", choices=STATUS, null=True)

    def __str__(self):
        return f"{self.title}"

### Question Votes
class QuestionVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"

### Answer
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1000, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    answer_votes_count = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.question}"

### Answer Votes
class AnswerVotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"
    
####################################################################################################
### Disease
class Disease(models.Model):
    CATEGORY = (
        ('Fungal Disease', 'Fungal Disease'),
        ('Protozoal Disease', 'Protozoal Disease'),
        ('Bacterial Disease', 'Bacterial Disease'),
        ('Parasitic Disease', 'Parasitic Disease'),
        ('Viral Disease', 'Viral Disease'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='disease/', blank=True, null=True)
    body = models.TextField(max_length=1000, null=True)
    #category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"
    
### Therapy
class Therapy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1000, null=True)
    photo = models.ImageField(upload_to='therapy/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"

### Replay Therapy
class ReplayTherapy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)
    therapy = models.ForeignKey(Therapy, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.body}"
