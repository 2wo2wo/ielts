# Generated by Django 4.0.5 on 2022-06-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_summarycompletion_part_givenkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentencePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=255, null=True)),
                ('belong_text', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sentence_completions', to='api.matchingheadingcollection')),
            ],
        ),
    ]
