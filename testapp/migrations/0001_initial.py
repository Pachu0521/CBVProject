# Generated by Django 4.0.5 on 2024-01-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=15)),
                ('sid', models.IntegerField()),
                ('smarks', models.FloatField()),
            ],
        ),
    ]