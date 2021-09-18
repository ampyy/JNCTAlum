from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

BRANCH = (
    ('Computer Science', 'Computer Science'),
    ('Electrical', 'Electrical'),
    ('Mechanical', 'Mechanical'),
    ('Electronics', 'Electronics'),
)

LEVEL = (
    ('Basic', 'Basic'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Elite', 'Elite'),
)

TYPE = (
    ('Internship', 'Internship'),
    ('Job', 'Job'),
)


class Batch(models.Model):
    batch_name = models.CharField(max_length=150)

    def __str__(self):
        return self.batch_name

    def get_absolute_url(self):
        return reverse('batch_details', args=[str(self.batch_name)])


class Verification(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    enroll_no = models.CharField(max_length=150, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user


class UserInfoBasic(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="images/", blank=True, null=True)
    branch = models.CharField(max_length=50, choices=BRANCH, null=True, blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('student_details', args=[str(self.user)])


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


class UserLinkInfo(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    school = models.CharField(max_length=150, blank=True, null=True)
    fav_part_of_college = models.CharField(max_length=50, choices=fav_col, null=True, blank=True)
    fav_food_of_canteen = models.CharField(max_length=50, choices=fav_canteen, null=True, blank=True)
    insta = models.CharField(max_length=1000, blank=True, null=True)
    blog_link = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user


class ThoughtsByUser(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    thought = models.CharField(max_length=500, blank=False, null=False)
    posted_time = models.DateTimeField(default=datetime.datetime.now())


class Job(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    company_name = models.CharField(max_length=150, blank=False, null=False)
    position = models.CharField(max_length=150, blank=False, null=False)
    type = models.CharField(max_length=50, choices=TYPE, null=False, blank=False)
    started_from = models.CharField(max_length=150, blank=False, null=False)
    ended_on = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=500, blank=False, null=False)


class Skills(models.Model):
    user = models.CharField(max_length=150, blank=False, null=False)
    skill_name = models.CharField(max_length=150, blank=False, null=False)
    learnt_from = models.CharField(max_length=150, blank=False, null=False)
    level = models.CharField(max_length=50, choices=LEVEL, null=False, blank=False)


class Insights(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField()
    caption = models.CharField(max_length=500, blank=False, null=False)
    posted_time = models.DateTimeField(default=datetime.datetime.now())
