### account/admin.py

from django.contrib import admin
from account.models import Profile, Post, PostLikes, Comment, CommentLikes, Replay, ReplayLikes, Question, Status, QuestionVotes, Answer, AnswerVotes, Disease, Category, Therapy, ReplayTherapy

### Profile
class ProfileAdmin(admin.ModelAdmin):
    pass

### Post
class PostAdmin(admin.ModelAdmin):
    pass

class PostLikesAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class CommentLikesAdmin(admin.ModelAdmin):
    pass

class ReplayAdmin(admin.ModelAdmin):
    pass

class ReplayLikesAdmin(admin.ModelAdmin):
    pass

### Question
class QuestionAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

class QuestionVotesAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    pass

class AnswerVotesAdmin(admin.ModelAdmin):
    pass

### Disease
class DiseasenAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class TherapyAdmin(admin.ModelAdmin):
    pass

class ReplayTherapyAdmin(admin.ModelAdmin):
    pass

### Profile
admin.site.register(Profile, ProfileAdmin)

### Post
admin.site.register(Post, PostAdmin)
admin.site.register(PostLikes, PostLikesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentLikes, CommentLikesAdmin)
admin.site.register(Replay, ReplayAdmin)
admin.site.register(ReplayLikes, ReplayLikesAdmin)

### Question
admin.site.register(Question, QuestionAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(QuestionVotes, QuestionVotesAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerVotes, AnswerVotesAdmin)

### Disease
admin.site.register(Disease, DiseasenAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Therapy, TherapyAdmin)
admin.site.register(ReplayTherapy, ReplayTherapyAdmin)
