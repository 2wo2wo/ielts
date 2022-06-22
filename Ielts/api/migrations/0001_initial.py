# Generated by Django 4.0.5 on 2022-06-18 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatchingHeadingCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='MatchingHeadingText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('head_letter', models.CharField(max_length=1)),
                ('belong_to_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.matchingheadingcollection')),
            ],
        ),
        migrations.CreateModel(
            name='MatchingHeadingChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_choice', models.CharField(max_length=255)),
                ('belong_tomatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.matchingheadingcollection')),
            ],
        ),
    ]