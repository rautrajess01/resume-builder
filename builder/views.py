from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume


@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user)
    return render(request, 'builder/list.html', {'resumes': resumes})
@login_required
def create_resume(request):
    form = ResumeForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        resume = form.save(commit=False)
        resume.user = request.user
        resume.save()
        return redirect('preview_resume', id=resume.id)
    return render(request, 'builder/form.html', {'form': form, 'title': 'Create New Resume', 'button_text': 'Preview'})

@login_required
def preview_resume(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)
    return render(request, 'builder/preview.html', {'resume': resume})


@login_required
def edit_resume(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)
    form = ResumeForm(request.POST or None, instance=resume)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('preview_resume', id=id)
    return render(request, 'builder/form.html', {'form': form, 'title': 'Edit Resume', 'button_text': 'Update Resume'})

def delete_resume(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)
    resume.delete()
    return redirect('resume_list')
