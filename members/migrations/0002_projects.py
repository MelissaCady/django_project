# Generated by Django 4.1.1 on 2022-09-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=255)),
                ('date_project', models.DateField()),
                ('nb_releve', models.IntegerField()),
                ('url_site', models.TextField()),
            ],
        ),
    ]
