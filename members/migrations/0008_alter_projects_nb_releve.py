# Generated by Django 4.1.1 on 2022-09-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_projects_nb_releve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='nb_releve',
            field=models.IntegerField(null=True),
        ),
    ]
