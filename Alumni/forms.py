from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import datetime


class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email?'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserInfoBasicsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(UserInfoBasicsForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    name = forms.CharField(max_length=150, required=False)
    age = forms.IntegerField()
    profile_pic = forms.ImageField(required=False)
    branch = forms.CharField(max_length=150, required=False)
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=False)

    class Meta:
        model = UserInfoBasic
        fields = ('user', 'name', 'age', 'profile_pic', 'branch', 'batch')


class UserInfoBasicsUpdateForm(forms.ModelForm):
    BRANCH = (
        ('Computer Science', 'Computer Science'),
        ('Electrical', 'Electrical'),
        ('Mechanical', 'Mechanical'),
        ('Electronics', 'Electronics'),
    )

    name = forms.CharField(max_length=150, required=False)
    age = forms.IntegerField()
    profile_pic = forms.ImageField(required=False)
    branch = forms.CharField(max_length=150, required=True, widget=forms.Select(choices=BRANCH))
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=True)

    class Meta:
        model = UserInfoBasic
        fields = ('name', 'age', 'profile_pic', 'branch', 'batch')


class UserLinkInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(UserLinkInfoForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    school = forms.CharField(max_length=150, required=False)
    fav_part_of_college = forms.CharField(max_length=150, required=False)
    fav_part_of_canteen = forms.CharField(max_length=150, required=False)
    insta = forms.CharField(max_length=150, required=False)
    blog_link = forms.CharField(max_length=150, required=False)

    class Meta:
        model = UserLinkInfo
        fields = ('user', 'school', 'fav_part_of_college', 'fav_part_of_canteen', 'insta', 'blog_link',)


class UserLinkInfoUpdateForm(forms.ModelForm):
    fav_col = (
        ('Canteen', 'Canteen'),
        ('Tapri', 'Nanu Kirana'),
        ('Terrace stairs', 'Terrace Stairs'),
        ('Hostel', 'Hostel'),
    )
    fav_canteen = (
        ('Samosa', 'Samosa'),
        ('Chai', 'Chai'),
        ('Fried Rice', 'Fried Rice'),
        ('Tanhai', 'Tanhai'),
    )

    school = forms.CharField(max_length=150, required=False)
    fav_part_of_college = forms.CharField(max_length=150, required=False, widget=forms.Select(choices=fav_col))
    fav_food_of_canteen = forms.CharField(max_length=150, required=False, widget=forms.Select(choices=fav_canteen))
    insta = forms.CharField(max_length=150, required=False)
    blog_link = forms.CharField(max_length=150, required=False)

    class Meta:
        model = UserLinkInfo
        fields = ('school', 'fav_part_of_college', 'fav_food_of_canteen', 'insta', 'blog_link',)


class ThoughtCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(ThoughtCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    thought = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Thought ...', 'rows': 5}),
                              max_length=499,
                              label="Thought", required=True)

    class Meta:
        model = ThoughtsByUser
        fields = ['user', 'thought', ]


class ThoughtUpdateForm(forms.ModelForm):
    user = forms.CharField(disabled=True)
    thought = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Thought ...', 'rows': 5}),
                              max_length=499,
                              label="Thought", required=True)

    class Meta:
        model = ThoughtsByUser
        fields = ['user', 'thought', ]


class DateInput(forms.DateInput):
    input_type = 'date'


class JobCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(JobCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    TYPE = (
        ('Internship', 'Internship'),
        ('Job', 'Job'),
    )

    user = forms.ModelChoiceField(queryset=None, initial=0)
    company_name = forms.CharField(max_length=150, required=True)
    position = forms.CharField(max_length=150, required=True)
    started_from = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}), required=True)
    ended_on = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Leave blank if still working!'}),
                               required=False)
    type = forms.CharField(max_length=150, required=True, widget=forms.Select(choices=TYPE))
    role = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Role ...', 'rows': 5}),
                           max_length=499,
                           label="Role", required=True)

    class Meta:
        model = Job
        fields = ['user', 'company_name', 'position', 'type', 'started_from', 'ended_on', 'role', ]


class JobUpdateForm(forms.ModelForm):
    TYPE = (
        ('Internship', 'Internship'),
        ('Job', 'Job'),
    )

    company_name = forms.CharField(max_length=150, required=True)
    position = forms.CharField(max_length=150, required=True)
    started_from = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}), required=True)
    ended_on = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Leave blank if still working!'}),
                               required=False)
    type = forms.CharField(max_length=150, required=True, widget=forms.Select(choices=TYPE))
    role = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Role ...', 'rows': 5}),
                           max_length=499,
                           label="Role", required=True)

    class Meta:
        model = Job
        fields = ['company_name', 'position', 'type', 'started_from', 'ended_on', 'role', ]


class SkillsCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(SkillsCreateForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    LEVEL = (
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Elite', 'Elite'),
    )

    user = forms.ModelChoiceField(queryset=None, initial=0)
    skill_name = forms.CharField(max_length=150, required=True)
    learnt_from = forms.CharField(max_length=150, required=True)
    level = forms.CharField(max_length=150, required=True, widget=forms.Select(choices=LEVEL))

    class Meta:
        model = Skills
        fields = ['user', 'skill_name', 'learnt_from', 'level', ]


class SkillsUpdateForm(forms.ModelForm):
    LEVEL = (
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Elite', 'Elite'),
    )
    skill_name = forms.CharField(max_length=150, required=True)
    learnt_from = forms.CharField(max_length=150, required=True)
    level = forms.CharField(max_length=150, required=True, widget=forms.Select(choices=LEVEL))

    class Meta:
        model = Skills
        fields = ['skill_name', 'learnt_from', 'level', ]

