from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

import re


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name} {self.color}"


class Author(AbstractUser):

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("notes:author-detail", kwargs={"pk": self.pk})


class Note(models.Model):
    text = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        Author,
        related_name="authors",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    total_words = models.IntegerField(blank=True, null=True)
    total_unique_words = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-last_updated"]

    def save(self, *args, **kwargs):

        self.find_all_words()
        super().save(*args, **kwargs)

    def find_all_words(self):

        words = re.findall(r"[a-zA-Z][a-zA-Z']*|[\d.]+", self.text)
        self.total_words = len(words)

        unique_words = set(words)
        self.total_unique_words = len(unique_words)
