# Generated by Django 4.0.5 on 2022-06-21 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_tablecompletion_tablepart_tablechoices'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='uploads/')),
                ('belong_flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flow_charts', to='api.matchingheadingcollection')),
            ],
        ),
        migrations.CreateModel(
            name='FlowChartAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=128, verbose_name='answer')),
                ('belong_flow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flow_answers', to='api.flowchart')),
            ],
        ),
    ]
