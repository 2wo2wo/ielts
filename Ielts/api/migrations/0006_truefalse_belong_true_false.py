# Generated by Django 4.0.5 on 2022-06-20 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_truefalse'),
    ]

    operations = [
        migrations.AddField(
            model_name='truefalse',
            name='belong_true_false',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='true_false', to='api.matchingheadingcollection'),
        ),
    ]
