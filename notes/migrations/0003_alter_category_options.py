# Generated by Django 4.0.4 on 2024-05-03 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_total_unique_words_note_total_words'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
