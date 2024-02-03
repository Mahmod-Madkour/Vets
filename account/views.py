### account/view.py

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import LoginForm, RegisterForm, UserProfileForm, ProfileEditForm, UpdatePasswordForm, PostForm, CommentForm, ReplayForm, UpdateForm, QuestionForm, AnswerForm, UpdateQuestionForm, DiseaseForm, TherapyForm
from .models import User, Profile, Post, PostLikes, Comment, CommentLikes, Replay, ReplayLikes, Question, QuestionVotes, Answer, AnswerVotes, Status, Disease, Category, Therapy, ReplayTherapy


####################################################################################################
####################################################################################################
# Sign Up
def sign_up(request):
    if request.method == 'GET':
        user_form = RegisterForm()
        profile_form = UserProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'auth/register.html', context)
    
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            return redirect('login')
        else:
            context = {
            'user_form': user_form,
            'profile_form': profile_form
            }
            return render(request, 'auth/register.html', context)

# Sign In
def sign_in(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('post_home')
            else:
                # If authentication fails or form is invalid, display error message
                messages.error(request, 'Username or Password is incorrect !')
        
    return render(request, 'auth/login.html', {'form': form})

# Profile
@login_required
def user_profile(request):
    profile = Profile.objects.filter(user= request.user).first()
    context = {
        'profile': profile,
        }
    return render(request, 'profile/profile.html', context=context)

# Profile For Everyone
@login_required
def user_profile_everyone(request, pk_user):
    profile = Profile.objects.filter(user= pk_user).first()
    context = {
        'profile': profile,
        }
    return render(request, 'profile/profile_everyone.html', context=context)

# Update Profile
@login_required
def profile_update(request):
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
        
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile_update.html', context=context)

# Update Password
@login_required
def update_password(request):
    user = request.user
    password_form = UpdatePasswordForm(user)

    if request.method == 'POST':
        password_form = UpdatePasswordForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            UpdatePasswordForm(request, user)
            update_session_auth_hash(request, user)  # Important for security
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below !')

    context = {
        'password_form': password_form,
    }
    return render(request, 'profile/update_password.html', context=context)

# Sign Out
@login_required
def sign_out(request):
    logout(request)
    return redirect('login')

####################################################################################################
####################################################################################################
### Post Page
def post_home(request):
    user = request.user

    if request.method == "GET":
        posts = Post.objects.all().order_by("-created_on")

        # Calculate the count of comments for each post
        post_comments_count = {}
        for post in posts:
            count = Comment.objects.filter(post_id=post.id).count()
            post_comments_count[post.id] = count

        # Retrieve data from the database
        data = PostLikes.objects.all()
        likes = {}
        for item in data:
            likes[item.post_id] = item.user_id

        context = {
            'likes': likes,
            'user': user,
            'posts': posts,
            'post_comments_count': post_comments_count,
        }
        return render(request, "post/home.html", context)

### Create a New Post
def create_post(request):
    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Post(
                body= post_form.cleaned_data["body"],
                user= request.user,
            )
            post.save()
            return redirect('post_home')
    
    context = {
        "post_form": post_form,
    }
    return render(request, "post/post_create.html", context)

### Like of Post
def like_post(request, pk_post):
    post = Post.objects.filter(pk=pk_post).first()

    # Check if the user has already liked the post
    if PostLikes.objects.filter(user=request.user, post=post).exists():
        # Unlike the post
        PostLikes.objects.filter(user=request.user, post=post).delete()
        post.post_likes_count -= 1
    else:
        # Like the post
        PostLikes.objects.create(user=request.user, post=post)
        post.post_likes_count += 1
    post.save()
    
    return redirect(reverse('post_home'))

# Ask New Question
def ask_question(request):
    question_form = QuestionForm()
    status = Status.objects.first()

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = Question(
                title= question_form.cleaned_data["title"],
                body= question_form.cleaned_data["body"],
                user= request.user,
                status= status ,
            )
            question.save()
            return redirect(reverse('question_home'))
    context = {
        "question_form": question_form,
    }
    return render(request, "question/ask_question.html", context)
### Update Post
def update_post(request, pk_post):
    post = Post.objects.get(pk=pk_post)
    
    update_form = UpdateForm(instance=post)
    if request.method == "POST":
        update_form = UpdateForm(request.POST, instance=post)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse('post_home'))
    context = {
        'post': post,
        "update_form": update_form,
    }
    return render(request, 'post/update_post.html', context)

### Delete Post
def delete_post(request, pk_post):
    post = Post.objects.filter(pk=pk_post)

    if request.method == 'POST' and post:
        post.delete()
        return redirect(reverse('post_home'))

    if request.method == 'GET' and post:
        return render(request, 'post/delete_post.html')
    
    if request.method == 'GET' and not post:
        return redirect(reverse('post_home'))
    
### Detail Of Post & Add Comment
def post_detail(request, pk_post):
    user = request.user
    post = Post.objects.get(pk=pk_post)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                body= comment_form.cleaned_data["body"],
                post= post,
                user= request.user,
            )
            comment.save()
            return redirect('post_detail', pk_post=pk_post)
    comments = Comment.objects.filter(post=post).order_by("-created_on")
    counts = Comment.objects.filter(post=post).count()

    # Calculate the count of replaies for each comment
    comment_replaies_count = {}
    for comment in comments:
        count = Replay.objects.filter(comment_id=comment.id).count()
        comment_replaies_count[comment.id] = count

    context = {
        'user': user,
        "post": post,
        "comments": comments,
        "counts": counts,
        'comment_replaies_count': comment_replaies_count,
        "comment_form": comment_form,
    }
    return render(request, "post/detail_post.html", context)

### Like of Comment
def like_comment(request, pk_post, pk_comment):
    comment = Comment.objects.get(pk=pk_comment)

    # Check if the user has already liked the post
    if CommentLikes.objects.filter(user=request.user, comment=comment).exists():
        # Unlike the post
        CommentLikes.objects.filter(user=request.user, comment=comment).delete()
        comment.comment_likes_count -= 1
    else:
        # Like the post
        CommentLikes.objects.create(user=request.user, comment=comment)
        comment.comment_likes_count += 1
    comment.save()
    
    return redirect(reverse('post_detail', kwargs={'pk_post': pk_post}))

### Update Comment
def update_comment(request, pk_post, pk_comment):
    comment = Comment.objects.get(pk=pk_comment)
    
    update_form = UpdateForm(instance=comment)
    if request.method == "POST":
        update_form = UpdateForm(request.POST, instance=comment)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse('post_detail', kwargs={'pk_post': pk_post}))
    context = {
        'comment': comment,
        "update_form": update_form,
    }
    return render(request, 'post/update_comment.html', context)

### Delete Comment
def delete_comment(request, pk_post, pk_comment):
    comment = Comment.objects.filter(pk=pk_comment)

    if request.method == 'POST' and comment:
        comment.delete()
        return redirect(reverse('post_detail', kwargs={'pk_post': pk_post}))
    
    if request.method == 'GET' and comment:
        return  render(request, 'post/delete_comment.html')

    if request.method == 'GET' and not comment:
        return redirect(reverse('post_home', kwargs={}))

### Detail Of Comment & Add Replay
def comment_detail(request, pk_post, pk_comment):
    user = request.user
    post = Post.objects.get(pk=pk_post)
    comment = Comment.objects.get(pk=pk_comment)
    replay_form = ReplayForm()

    if request.method == "POST":
        replay_form = ReplayForm(request.POST)
        if replay_form.is_valid():
            replay = Replay(
                body= replay_form.cleaned_data["body"],
                post=post,
                comment= comment,
                user= request.user,
            )
            replay.save()
            return HttpResponseRedirect(request.path_info)
    replies = Replay.objects.filter(comment=comment).order_by("-created_on")
    counts = Replay.objects.filter(comment=comment).count()

    context = {
        'user': user,
        'post': post,
        "comment": comment,
        "replies": replies,
        "counts": counts,
        "replay_form": replay_form,
    }
    return render(request, "post/detail_comment.html", context)

### Like of Replay
def like_replay(request, pk_post, pk_comment, pk_replay):
    replay = Replay.objects.get(pk=pk_replay)

    # Check if the user has already liked the post
    if ReplayLikes.objects.filter(user=request.user, replay=replay).exists():
        # Unlike the post
        ReplayLikes.objects.filter(user=request.user, replay=replay).delete()
        replay.replay_likes_count -= 1
    else:
        # Like the post
        ReplayLikes.objects.create(user=request.user, replay=replay)
        replay.replay_likes_count += 1
    replay.save()
    
    return redirect(reverse('comment_detail', kwargs={'pk_post': pk_post, 'pk_comment': pk_comment}))

### Update Replay
def update_replay(request, pk_post, pk_comment, pk_replay):
    replay = Replay.objects.get(pk=pk_replay)
    
    update_form = UpdateForm(instance=replay)
    if request.method == "POST":
        update_form = UpdateForm(request.POST, instance=replay)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse('comment_detail', kwargs={'pk_post': pk_post, 'pk_comment': pk_comment}))
    context = {
        'replay': replay,
        "update_form": update_form,
    }
    return render(request, 'post/update_replay.html', context)

### Delete Replay
def delete_replay(request, pk_post, pk_comment, pk_replay):
    replay = Replay.objects.filter(pk=pk_replay)

    if request.method == 'POST' and replay:
        replay.delete()
        return redirect(reverse('comment_detail', kwargs={'pk_post': pk_post, 'pk_comment': pk_comment}))
    if request.method == 'GET' and replay:
        return  render(request, 'post/delete_replay.html')

    if request.method == 'GET' and not replay:
        return redirect(reverse('post_detail', kwargs={'pk_post': pk_post}))

####################################################################################################
####################################################################################################
# All Questions
def question_home(request):
    questions = Question.objects.all().order_by("-created_on")
    
    # Calculate the count of answers for each question
    question_answers_count = {}
    for question in questions:
        count = Answer.objects.filter(question_id=question.id).count()
        question_answers_count[question.id] = count

    context = {
        "questions": questions,
        'question_answers_count': question_answers_count,
    }
    return render(request, "question/question.html", context)

# Ask New Question
def ask_question(request):
    question_form = QuestionForm()
    status = Status.objects.first()

    if request.method == "POST":
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = Question(
                title= question_form.cleaned_data["title"],
                body= question_form.cleaned_data["body"],
                user= request.user,
                status= status ,
            )
            question.save()
            return redirect(reverse('question_home'))
    context = {
        "question_form": question_form,
    }
    return render(request, "question/ask_question.html", context)

# All Questions Same Status
def status_question(request, pk_status):
    status = Status.objects.get(pk=pk_status)
    questions = Question.objects.filter(status=status).order_by("-created_on")

    # Calculate the count of answers for each question
    question_answers_count = {}
    for question in questions:
        count = Answer.objects.filter(question_id=question.id).count()
        question_answers_count[question.id] = count

    context = {
        "questions": questions,
        'question_answers_count': question_answers_count,
    }
    return render(request, "question/status.html", context)

# All Detail of One Question
# Add New Answer & Vote Question & Display All Answers
def detail_question(request, pk_question):
    question = Question.objects.get(pk=pk_question)
    answers = Answer.objects.filter(question=question).order_by("-created_on")
    counts = Answer.objects.filter(question=question).count()

    if request.method == "GET":
        # Answer Form
        answer_form = AnswerForm()

        context = {
        'question': question,
        'answers': answers,
        'counts': counts,
        'answer_form': answer_form,
        }
        return render(request, "question/detail_question.html", context)

    # Add New Answer
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = Answer(
                body= answer_form.cleaned_data["body"],
                question= question,
                user= request.user,
            )
            answer.save()
            return HttpResponseRedirect(request.path_info)

    # Vote Question
    if request.method == "POST":
        # Check if the user has already voted 
        if QuestionVotes.objects.filter(user=request.user, question=question).exists():
            # Un Vote
            QuestionVotes.objects.filter(user=request.user, question=question).delete()
            question.question_votes_count -= 1
        else:
            # Vote
            QuestionVotes.objects.create(user=request.user, question=question)
            question.question_votes_count += 1
        question.save()
        return HttpResponseRedirect(request.path_info)

### Update Question
def update_question(request, pk_question):
    question = Question.objects.get(pk=pk_question)

    if request.method == "GET":
        update_form = UpdateQuestionForm(instance=question)
        context = {
            'question': question,
            "update_form": update_form,
        }
        return render(request, 'question/update_question.html', context)

    if request.method == "POST":
        updete_form = UpdateQuestionForm(request.POST, instance=question)
        if updete_form.is_valid():
            updete_form.save()
            return redirect(reverse('detail_question', kwargs={'pk_question': pk_question}))

### Delete Question
def delete_question(request, pk_question):
    question = Question.objects.filter(pk=pk_question)

    if request.method == 'GET' and question:
        return render(request, 'question/delete_question.html')

    if request.method == 'GET' and not question:
        return redirect(reverse('question_home'))

    if request.method == 'POST' and question:
        question.delete()
        return redirect(reverse('question_home'))
    
### Delete Answer
def delete_answer(request, pk_question, pk_answer):
    answer = Answer.objects.filter(pk=pk_answer)

    if request.method == 'GET' and answer:
        return render(request, 'question/delete_answer.html')
    
    if request.method == 'GET' and not answer:
        return redirect(reverse('question_home'))
    
    if request.method == 'POST' and answer:
        answer.delete()
        return redirect(reverse('detail_question', kwargs={'pk_question': pk_question }))

# Vote Answer
def vote_answer(request, pk_question, pk_answer):
    question = Question.objects.get(pk=pk_question)
    answer = Answer.objects.get(pk=pk_answer)
    
    # Check if the user has already voted 
    if AnswerVotes.objects.filter(user= request.user, answer=answer).exists():
        # Un Vote
        AnswerVotes.objects.filter(user= request.user, answer=answer).delete()
        answer.answer_votes_count -= 1
    else:
        # Vote
        AnswerVotes.objects.create(user= request.user, answer=answer)
        answer.answer_votes_count += 1
    answer.save()
    return redirect(reverse('detail_question', kwargs={'pk_question': pk_question }))

####################################################################################################
####################################################################################################
# All Diseases
def disease_home(request):
    diseases = Disease.objects.all().order_by("-created_on")

    context = {
        "diseases": diseases,
    }
    return render(request, "disease/disease.html", context)

# All Diseases Same Category
def category_disease(request, pk_category):
    category = Category.objects.filter(pk=pk_category).first()
    diseases = Disease.objects.filter(category=category).order_by("-created_on")

    context = {
        "diseases": diseases,
    }
    return render(request, "disease/category.html", context)

# Add New Disease
def add_disease(request):
    disease_form = DiseaseForm()

    if request.method == "POST":
        disease_form = DiseaseForm(request.POST, request.FILES)
        if disease_form.is_valid():
            disease = disease_form.save(commit=False)
            disease.user = request.user
            disease.save()
            return redirect(reverse('disease_home'))
        else:
            messages.error(request, 'Please correct the error below.')
    context = {
        "disease_form": disease_form,
    }
    return render(request, "disease/add_disease.html", context)

# All Detail of One Disease
# Add New Answer & Vote Question & Display All Therapy
def detail_disease(request, pk_disease):
    disease = Disease.objects.get(pk=pk_disease)
    therapies = Therapy.objects.filter(disease=disease).order_by("-created_on")
    counts = Therapy.objects.filter(disease=disease).count()

    if request.method == "GET":
        # Answer Form
        therapy_form = TherapyForm()

        context = {
        'disease': disease,
        'therapies': therapies,
        'counts': counts,
        'therapy_form': therapy_form,
        }
        return render(request, "disease/detail_disease.html", context)

    # Add New Therapy
    if request.method == "POST":
        therapy_form = TherapyForm(request.POST, request.FILES)
        if therapy_form.is_valid():
            therapy = therapy_form.save(commit=False)
            therapy.disease = disease
            therapy.user = request.user
            therapy.save()
            return HttpResponseRedirect(request.path_info)

### Delete Question
def delete_disease(request, pk_disease):
    disease = Disease.objects.filter(pk=pk_disease)

    if request.method == 'GET' and disease:
        return render(request, 'disease/delete_disease.html')

    if request.method == 'GET' and not disease:
        return redirect(reverse('disease_home'))

    if request.method == 'POST' and disease:
        disease.delete()
        return redirect(reverse('disease_home'))
    
### Delete Therapy
def delete_therapy(request, pk_disease, pk_therapy):
    therapy = Therapy.objects.filter(pk=pk_therapy)

    if request.method == 'GET' and therapy:
        return render(request, 'disease/delete_therapy.html')

    if request.method == 'GET' and not therapy:
        return redirect(reverse('detail_disease', kwargs={'pk_disease': pk_disease }))

    if request.method == 'POST' and therapy:
        therapy.delete()
        return redirect(reverse('detail_disease', kwargs={'pk_disease': pk_disease }))
    
### Delete Therapy Repaly
def delete_therapy_replay(request, pk_disease, pk_therapy, pk_replay):
    replay = ReplayTherapy.objects.filter(pk=pk_replay)

    if request.method == 'GET' and replay:
        return render(request, 'disease/delete_replay.html')

    if request.method == 'GET' and not replay:
        return redirect(reverse('detail_therapy', kwargs={'pk_disease': pk_disease, 'pk_therapy': pk_therapy}))

    if request.method == 'POST' and replay:
        replay.delete()
        return redirect(reverse('detail_therapy', kwargs={'pk_disease': pk_disease, 'pk_therapy': pk_therapy}))

### Detail Therapy
def detail_therapy(request, pk_disease, pk_therapy):
    user = request.user
    disease = Disease.objects.get(pk=pk_disease)
    therapy = Therapy.objects.get(pk=pk_therapy)
    replay_form = ReplayForm()

    if request.method == "POST":
        replay_form = ReplayForm(request.POST)
        if replay_form.is_valid():
            replay = ReplayTherapy(
                body= replay_form.cleaned_data["body"],
                disease= disease,
                therapy= therapy,
                user= user,
            )
            replay.save()
            return HttpResponseRedirect(request.path_info)
    replies = ReplayTherapy.objects.filter(therapy=therapy).order_by("-created_on")
    counts = ReplayTherapy.objects.filter(therapy=therapy).count()

    context = {
        'user': user,
        'disease': disease,
        "therapy": therapy,
        "replies": replies,
        "counts": counts,
        "replay_form": replay_form,
    }
    return render(request, "disease/detail_therapy.html", context)

####################################################################################################
####################################################################################################
### Profile Post Page
def profile_posts(request):
    user = request.user
    profile = Profile.objects.filter(user= request.user).first()
    posts = Post.objects.filter(user=user).all().order_by("-created_on")
    found = 0

    if posts:
        found = found + 1
        # Calculate the count of comments for each post
        post_comments_count = {}
        for post in posts:
            count = Comment.objects.filter(post_id=post.id).count()
            post_comments_count[post.id] = count

        # Retrieve data from the database
        data = PostLikes.objects.all()
        likes = {}
        for item in data:
            likes[item.post_id] = item.user_id

        context = {
            'profile': profile,
            'found': found,
            'likes': likes,
            'user': user,
            'posts': posts,
            'post_comments_count': post_comments_count,
        }
        return render(request, "profile/profile_posts.html", context)
    else:
        context = {
            'profile': profile,
            'found': found,
            'user': user,
        }
        return render(request, "profile/profile_posts.html", context)


### Profile Question Page
def profile_questions(request):
    user = request.user
    profile = Profile.objects.filter(user= request.user).first()
    questions = Question.objects.filter(user=user).all().order_by("-created_on")
    found = 0

    if questions:
        found = found + 1
        # Calculate the count of answers for each question
        question_answers_count = {}
        for question in questions:
            count = Answer.objects.filter(question_id=question.id).count()
            question_answers_count[question.id] = count

        context = {
            'found': found,
            'profile': profile,
            "questions": questions,
            'question_answers_count': question_answers_count,
        }
    else:
        context = {
            'found': found,
            'profile': profile,
            'user': user,
            }
    return render(request, "profile/profile_questions.html", context)
    
### Profile Diseases Page
def profile_diseases(request):
    user = request.user
    profile = Profile.objects.filter(user= request.user).first()
    diseases = Disease.objects.filter(user=user).all().order_by("-created_on")
    found = 0

    if diseases:
        found = found + 1
        context = {
            'found': found,
            'profile': profile,
            "diseases": diseases,
        }
    else:
        context = {
            'found': found,
            'profile': profile,
        }
    return render(request, "profile/profile_diseases.html", context)

####################################################################################################
####################################################################################################
