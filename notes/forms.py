from django import forms

from notes.models import Category, Note


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "color": forms.HiddenInput(attrs={"id": "id_color"}),
        }


class NoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(NoteForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(NoteForm, self).save(commit=False)
        if self.request and self.request.user.is_authenticated:
            instance.author = self.request.user
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Note
        fields = ["category", "text", "active"]


class NoteFilterForm(forms.ModelForm):
    SORTED_CHOICES = [
        ("last_updated", "Data Update (Newest First)"),
        ("-last_updated", "Data Update (Oldest First)"),
        ("created", "Data Create (Newest First)"),
        ("-created", "Data Create (Oldest First)"),
        ("total_words", "Total Words"),
        ("unique_words", "Unique Words"),
    ]

    active = forms.BooleanField(label="Archived", required=False)
    sorted_by = forms.ChoiceField(
        label="Sorted", choices=SORTED_CHOICES, required=False
    )

    class Meta:
        model = Note
        fields = ["category", "active", "sorted_by"]
