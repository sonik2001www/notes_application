from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse

from notes.forms import CategoryForm, NoteForm, NoteFilterForm
from notes.models import Category, Note, Author


class CategoryListView(generic.ListView):
    model = Category
    context_object_name = "category_list"
    template_name = "notes/category_list.html"
    paginate_by = 7


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("notes:note-create")


class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("notes:category-list")


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy("notes:category-list")


class NoteListView(generic.ListView):
    model = Note
    paginate_by = 7
    template_name = "notes/note_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().select_related("category", "author")
        category = self.request.GET.get("category")
        active = self.request.GET.get("active")
        sorted_by = self.request.GET.get("sorted_by")

        if category:
            queryset = queryset.filter(category__id=category)

        if active == "on":
            queryset = queryset.filter(active=False)
        else:
            queryset = queryset.filter(active=True)

        if sorted_by:
            if sorted_by == "total_words":
                queryset = queryset.order_by("total_words")
            elif sorted_by == "unique_words":
                queryset = queryset.order_by("total_unique_words")
            else:
                queryset = queryset.order_by(sorted_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NoteFilterForm(self.request.GET)
        return context


class NoteCreateView(generic.CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes:note-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class NoteUpdateView(generic.UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes:note-list")


class NoteDeleteView(generic.DeleteView):
    model = Note
    success_url = reverse_lazy("notes:note-list")


class AuthorDetailView(generic.DetailView):
    model = Author


def archive_note(request, pk):
    note = Note.objects.get(pk=pk)
    note.active = False
    note.save()
    return JsonResponse({"success": True})


def unarchive_note(request, pk):
    note = Note.objects.get(pk=pk)
    note.active = True
    note.save()
    return JsonResponse({"success": True})
