# Generated by Django 4.1.1 on 2022-09-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_releve_etat_releve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='nb_releve',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='releve',
            name='nb_comment_releve',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='releve',
            name='nb_tread_releve',
            field=models.IntegerField(blank=True),
        ),
    ]
