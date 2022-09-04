from django.shortcuts import render
from .models import Candidate
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

#=================== Frontend =========================
# Home
def home(request):
    return render(request, 'home.html')

# Candidate Registration
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successfully")
            return HttpResponseRedirect("/")
        else:
            return render(request, "register.html", {'form': form})
    else:
        form = CandidateForm()
        return render(request, "register.html", {'form': form})

#=================== backend =========================
# HR - Home Page
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    context = {'data_read': Candidate.objects.all()}
    return render(request, 'backend.html', context)

# Access candidates (Individual)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    return render(request, 'candidate.html', {'candidate': candidate})