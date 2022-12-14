# Generated by Django 4.1.1 on 2022-09-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_projects_nb_releve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releve',
            name='id_members',
        ),
        migrations.RemoveField(
            model_name='releve',
            name='id_project',
        ),
        migrations.AddField(
            model_name='releve',
            name='id_members',
            field=models.ManyToManyField(to='members.members'),
        ),
        migrations.AddField(
            model_name='releve',
            name='id_project',
            field=models.ManyToManyField(to='members.projects'),
        ),
    ]
