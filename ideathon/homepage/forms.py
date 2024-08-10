# homepage/forms.py

from django import forms
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm
from .models import Submission, TeamMember
from .models import TeamRegistration

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = TeamRegistration
        fields = ['student_name', 'email', 'phone_number', 'roll_number', 'college_name', 'team_size', 'team_member_names']
        
    def clean(self):
        cleaned_data = super().clean()
        team_size = cleaned_data.get("team_size")
        if team_size and team_size <= 0:
            self.add_error('team_size', 'Number of team members must be at least 1')
        return cleaned_data





class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['document']

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name']



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']




