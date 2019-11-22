from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template import loader
from .forms import ProfileForm, RequestForm, OfferForm
from .models import Profile, requests, offer, SignUp
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
import datetime

def BaseView(request):
    template = loader.get_template('rideshare/base.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='../../')
def IndexView(request):
    template = loader.get_template('rideshare/index.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='../../')
def CalendarView(request):
    suggest = offer.objects.all().filter(depart_date__gte= datetime.date.today()).order_by('depart_date' ,'depart_time')
    x = SignUp.objects.all().filter(user=request.user)
    context = {
        'user': request.user,
        'posts': suggest,
        'signups' : x
    }
    return render(request, 'rideshare/calendar.html', context)

@login_required(login_url='../../')
def FeedView(request):
    suggest = requests.objects.all().filter(depart_date__gte= datetime.date.today()).order_by('depart_date' ,'depart_time')
    context = {
        'user': request.user,
        'posts': suggest,
    }
    return render(request, 'rideshare/feed.html', context)


@login_required(login_url='../../')
def SearchReqResultsView(request):
    start = request.GET.get('start');
    end = request.GET.get('end');
    suggest = requests.objects.all().filter(start_location__icontains=start).filter(end_location__icontains=end).order_by('depart_date' ,'depart_time')
    context = {
        'user': request.user,
        'posts': suggest
    }
    return render(request, 'rideshare/feed.html', context)

@login_required(login_url='../../')
def SearchOffResultsView(request):
    start = request.GET.get('start');
    end = request.GET.get('end');
    suggest = offer.objects.all().filter(start_location__icontains=start).filter(end_location__icontains=end).order_by('depart_date' ,'depart_time')
    context = {
        'user': request.user,
        'posts': suggest
    }
    return render(request, 'rideshare/calendar.html', context)

@login_required(login_url='../../')
def FeedSpecifics(request, requests_id):
    suggest = get_object_or_404(requests, pk=requests_id)
    profs = Profile.objects.all()
    requested_by_profile = profs[0]
    for i in profs:
        if i.User == suggest.author:
            requested_by_profile = i
    context = {
        'posts': suggest,
        'authed': requested_by_profile
    }
    return render(request, 'rideshare/more_request_info.html', context)

@login_required(login_url='../../')
def CalSpecifics(request, offer_id):
    suggest = get_object_or_404(offer, pk=offer_id)
    x = SignUp.objects.all().filter(offer=suggest)
    y = suggest.seats - len(x)
    suggest.seats_open = y
    suggest.save()
    profs = Profile.objects.all().filter(User=suggest.author)[0]
    print(profs)
    context = {
        'posts': suggest,
        'authed': profs,
        'signups' : x,
    }
    return render(request, 'rideshare/more_offer_info.html', context)

@login_required(login_url='../../')
def ProfSpecifics(request, Profile_id):
    suggest = get_object_or_404(Profile, pk=Profile_id)
    offs = offer.objects.all().filter(author=suggest.User)
    reqs = requests.objects.all().filter(author=suggest.User)
    signups = SignUp.objects.all().filter(user=suggest.User)
    context = {
        'authed': suggest,
        'pesto': offs,
        'pasta': reqs,
        'signups': signups
    }
    return render(request, 'rideshare/view_others_profile.html', context)

@login_required(login_url='../../')
def del_post(request, key):
    post = requests.objects.get(pk=key)
    post.delete()
    return render(request, 'del_done.html')

@login_required(login_url='../../')
def NewProfileView(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        prof = form.save(commit=False)
        prof.User = request.user
        form.save()
        form = ProfileForm()
        return CalendarView(request)
    context = {
        'form': form
    }
    return render(request, "rideshare/new_profile.html", context )

@login_required(login_url='../../')
def edit_post(request, key):
    post = requests.objects.get(pk=key)
    if post.author == request.user:
        if request.method == 'POST':
            form = RequestForm(request.POST, instance=post)
            if form.is_valid():
                prof = form.save(commit=False)
                prof.author = request.user
                form.save()
                return FeedView(request)
        else:
            form = RequestForm(instance=post)
        context = {
            'form': form
        }
        return render(request, "rideshare/request_form.html", context )
    return FeedView(request)

@login_required(login_url='../../')
def delete_post(request, key):
    post = requests.objects.get(pk=key)
    if post.author == request.user:
        post.delete()
    return FeedView(request)

@login_required(login_url='../../')
def edit_offer(request, key):
    post = offer.objects.get(pk=key)
    x = len(SignUp.objects.all().filter(offer=post))
    if post.author == request.user:
        if request.method == 'POST':
            form = OfferForm(request.POST, instance=post)
            if form.is_valid():
                prof = form.save(commit=False)
                prof.author = request.user
                prof.seats_open = prof.seats - x
                form.save()
                return CalendarView(request)
        else:
            form = OfferForm(instance=post)
        context = {
            'form': form
        }
        return render(request, "rideshare/offer_form.html", context )
    return CalendarView(request)

@login_required(login_url='../../')
def delete_offer(request, key):
    post = offer.objects.get(pk=key)
    if post.author == request.user:
        post.delete()
    return CalendarView(request)

@login_required(login_url='../../')
def EditProfileView(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return ProfileDetailsView(request)
    else:
        form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, "rideshare/edit_profile.html", context )

@login_required(login_url='../../')
def RequestView(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        prof = form.save(commit=False)
        prof.author = request.user
        form.save()
        form = RequestForm()
        return FeedView(request)
    context = {
        'form': form
    }
    return render(request, "rideshare/request_form.html", context )

@login_required(login_url='../../')
def OfferView(request):
    form = OfferForm(request.POST or None)
    if form.is_valid():
        prof = form.save(commit=False)
        prof.author = request.user
        prof.seats_open = prof.seats
        form.save()
        form = RequestForm()
        return CalendarView(request)
    return render(request, "rideshare/offer_form.html", {'form' : form} )

@login_required(login_url='../../')
def SignUpOffer(request, key):
    post = offer.objects.get(pk=key)
    x = SignUp.objects.all().filter(offer=post)
    y = SignUp.objects.all().filter(offer=post, user=request.user)
    if len(y) > 0 or request.user == post.author:
        return CalSpecifics(request, key)
    if len(x) < post.seats:
        SignUp.objects.create(user=request.user, offer=post)
    return CalSpecifics(request, key)

@login_required(login_url='../../')
def delete_signup(request, key):
    sig = SignUp.objects.get(pk=key)
    sig.delete()
    return CalSpecifics(request, sig.offer_id)


def LoginView(request):
    template = loader.get_template('rideshare/login.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='../../')
def ProfileDetailsView(request):
    template = loader.get_template('rideshare/profile.html')
    suggest = requests.objects.all().filter(author=request.user, depart_date__gte= datetime.date.today()).order_by('depart_date','depart_time')
    offs = offer.objects.all().filter(author=request.user, depart_date__gte= datetime.date.today()).order_by('depart_date' ,'depart_time')
    signups = SignUp.objects.all().filter(user=request.user)
    context = {
        'pasta': suggest,
        'pesto': offs,
        'signups' : signups
    }
    return render(request, 'rideshare/profile.html', context)

@login_required(login_url='../../')
def logout_view(request):
    logout(request)
    template = loader.get_template('rideshare/login.html')
    return HttpResponse(template.render({}, request))

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
