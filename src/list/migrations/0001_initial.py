# Generated by Django 2.1.5 on 2020-08-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('due_date', models.DateTimeField()),
                ('done', models.BooleanField(null=True)),
            ],
        ),
    ]