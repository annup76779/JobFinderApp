# Generated by Django 4.0.6 on 2022-12-02 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscrap', '0002_personalize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='name',
            new_name='skill',
        ),
    ]