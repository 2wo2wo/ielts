# Generated by Django 4.0.5 on 2022-06-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_truefalse_belong_true_false'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParagraphMatching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, null=True)),
                ('answer', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]
