from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import Note
from .forms import NoteForm

@login_required
def note_list(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    notes = Note.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'form': form, 'notes': notes})


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/note_edit.html'
    success_url = reverse_lazy('note_list')

    def test_func(self):
        return self.get_object().owner == self.request.user  # only owner can edit


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')

    def test_func(self):
        return self.get_object().owner == self.request.user  # only owner can delete