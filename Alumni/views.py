from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy


def login_excluded(redirect_to):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


def home(request):
    batch = Batch.objects.all()
    return render(request, "home.html", {'batch': batch})


@login_excluded(home)
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_info = UserInfoBasic()
            user_info.user = form.cleaned_data.get("username")
            user_info.save()
            user_link = UserLinkInfo()
            user_link.user = form.cleaned_data.get("username")
            user_link.save()
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, "registration/signup.html", {'form': form})


class UserInFoBasicsView(LoginRequiredMixin, generic.CreateView):
    model = UserInfoBasic
    form_class = UserInfoBasicsForm
    template_name = "user_basics_info.html"

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(UserInFoBasicsView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserInfoBasicsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = UserInfoBasic
    template_name = "user_info_update_form.html"
    form_class = UserInfoBasicsUpdateForm
    success_url = '../myprofile'

    def get_context_data(self, **kwargs):
        context = super(UserInfoBasicsUpdateView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class UserLinkInfoView(LoginRequiredMixin, generic.CreateView):
    model = UserLinkInfo
    form_class = UserLinkInfoForm
    template_name = "user_link_create.html"

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(UserLinkInfoView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserLinkInfoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = UserLinkInfo
    template_name = "user_link_update.html"
    form_class = UserLinkInfoUpdateForm
    success_url = '../myprofile'

    def get_context_data(self, **kwargs):
        context = super(UserLinkInfoUpdateView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = UserInfoBasic
    template_name = "myprofile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.all().filter(user=self.request.user)[0]
        context['user_link'] = UserLinkInfo.objects.all().filter(user=self.request.user)[0]
        context['user_thoughts'] = ThoughtsByUser.objects.all().filter(user=self.request.user)
        context['user_jobs'] = Job.objects.all().filter(user=self.request.user)
        context['user_skills'] = Skills.objects.all().filter(user=self.request.user)
        return context


@login_required
def verify(request):
    if request.method == 'POST':
        if request.POST.get('enroll') and request.POST.get('number'):
            form = Verification()
            form.user = request.user
            form.enroll_no = request.POST.get('enroll')
            form.mobile = request.POST.get('number')
            form.save()
            return redirect('home')
    else:
        form = Verification()
    return render(request, "verify_create.html")


@login_required
def batch_details(request, batch_name):
    batch = get_object_or_404(Batch, batch_name=batch_name)
    user_info = UserInfoBasic.objects.all().filter(batch=batch)
    return render(request, "batch_details.html", {'batch': batch, 'user_info': user_info})


@login_required
def student_detail(request, user):
    student = UserInfoBasic.objects.filter(user=user)
    student_username = user
    user_links = UserLinkInfo.objects.filter(user=user)
    user_thoughts = ThoughtsByUser.objects.filter(user=user)
    user_jobs = Job.objects.filter(user=user)
    user_skills = Skills.objects.filter(user=user)
    return render(request, 'student_details.html',
                  {'student': student, 'user_links': user_links, 'user_thoughts': user_thoughts,
                   'user_jobs': user_jobs, 'user_skills': user_skills, 'student_username': student_username})


class ThoughtsByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = ThoughtsByUser
    form_class = ThoughtCreateForm
    template_name = 'Addthought.html'
    success_url = '../myprofile'

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(ThoughtsByUserCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ThoughtByUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ThoughtsByUser
    form_class = ThoughtUpdateForm
    template_name = 'Updatethought.html'
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(ThoughtByUserUpdateView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class ThoughtByUserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ThoughtsByUser
    template_name = "deleteThought.html"
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(ThoughtByUserDeleteView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class JobCreateView(LoginRequiredMixin, generic.CreateView):
    model = Job
    form_class = JobCreateForm
    template_name = 'addJob.html'
    success_url = '../myprofile'

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(JobCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class JobUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Job
    form_class = JobUpdateForm
    template_name = 'updateJob.html'
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class JobDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Job
    template_name = "deleteJob.html"
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(JobDeleteView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class SkillsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Skills
    form_class = SkillsCreateForm
    template_name = 'addSkill.html'
    success_url = '../myprofile'

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(SkillsCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SkillsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Skills
    form_class = SkillsUpdateForm
    template_name = 'updateSkill.html'
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(SkillsUpdateView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


class SkillsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Skills
    template_name = "deleteSkill.html"
    success_url = '../../myprofile'

    def get_context_data(self, **kwargs):
        context = super(SkillsDeleteView, self).get_context_data(**kwargs)
        context['user_info'] = UserInfoBasic.objects.get(user=self.request.user)
        return context


def notes(request):
    return render(request, "notes.html")


class InsightsListView(generic.ListView):
    model = Insights
    template_name = "insights.html"

    def get_context_data(self, **kwargs):
        context = super(InsightsListView, self).get_context_data(**kwargs)
        context['insights'] = Insights.objects.all()
        return context
