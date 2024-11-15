# Generated by Django 5.1.2 on 2024-11-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_participant_attempted_quiz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_login_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
