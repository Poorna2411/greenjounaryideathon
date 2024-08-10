from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm
from .models import Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SubmissionForm, TeamMemberForm
from .models import Submission, TeamMember, Profile
from .forms import TeamRegistrationForm
from .models import TeamRegistration
from django.http import JsonResponse

# Predefined answers for basic questions
answers = {
    "hello": "Hello! How can I help you today?",
    "what is your name": "I am the Ideathon Bot.",
    "how can I register": "You can register by clicking the 'Register here' button on the navigation bar.",
    "what are the event dates": "The event dates are listed in the Schedule section.",
}

def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message').lower()
        response_message = answers.get(user_message, "Sorry, I didn't understand that.")
        return JsonResponse({'response': response_message})
    return JsonResponse({'response': 'Invalid request method.'})

def chatbot_page(request):
    return render(request, 'homepage/chatbot.html')




def register_team(request):
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.total_amount = registration.team_size * 30
            registration.save()
            request.session['registration_id'] = registration.id
            return redirect('complete_transaction')
    else:
        form = TeamRegistrationForm()
    return render(request, 'registration/register_team.html', {'form': form})

def complete_transaction(request):
    registration_id = request.session.get('registration_id')
    if not registration_id:
        return redirect('register_team')

    registration = TeamRegistration.objects.get(id=registration_id)

    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        if transaction_id:
            registration.transaction_id = transaction_id
            registration.save()
            return redirect('registration_success')

    return render(request, 'registration/complete_transaction.html', {'registration': registration})

def registration_success(request):
    return render(request, 'registration/registration_success.html')




@login_required
def submission(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    user_submission = Submission.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            if user_submission:
                user_submission.document = form.cleaned_data['document']
                user_submission.save()
            else:
                user_submission = form.save(commit=False)
                user_submission.user = request.user
                user_submission.save()

            team_member_names = request.POST.getlist('team_members')
            TeamMember.objects.filter(submission=user_submission).delete()  # Remove old team members
            for name in team_member_names:
                TeamMember.objects.create(submission=user_submission, name=name)

            return redirect('upload_c')
    else:
        form = SubmissionForm(instance=user_submission)
        team_member_forms = [TeamMemberForm() for _ in range(profile.team_size)]

    context = {
        'form': form,
        'team_member_forms': team_member_forms,
        'event_name': 'Your Event Name',
        'created': user_submission is not None
    }

    return render(request, 'homepage/submission.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  # Restrict superuser access to admin panel
                messages.error(request, 'Superusers cannot log in here. Please use the admin panel.')
            else:
                login(request, user)
                return redirect('submission')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'homepage/login.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_complete')
    else:
        form = ContactForm()

    return render(request, 'homepage/contact.html', {'form': form})

def contact_complete(request):
    return render(request, 'homepage/contact_complete.html')

def upload_c(request):
    return render(request, 'homepage/upload.html')


def home(request):
    return render(request, 'homepage/index.html')


def rules(request):
    return render(request, 'homepage/rules.html')

def about(request):
    event_name = "GreenJourney Ideathon"
    return render(request, 'homepage/about.html', {'event_name': event_name})


