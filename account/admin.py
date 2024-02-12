### account/admin.py

from django.contrib import admin
from account.models import *

### Profile
admin.site.register(Profile)

### Post
admin.site.register(Post)
admin.site.register(PostLikes)
admin.site.register(Comment)
admin.site.register(CommentLikes)
admin.site.register(Replay)
admin.site.register(ReplayLikes)

### Question
admin.site.register(Question)
admin.site.register(QuestionVotes)
admin.site.register(Answer)
admin.site.register(AnswerVotes)

### Disease
admin.site.register(Disease)
admin.site.register(Therapy)
admin.site.register(ReplayTherapy)
