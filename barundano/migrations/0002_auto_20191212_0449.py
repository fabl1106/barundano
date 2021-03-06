# Generated by Django 2.0.13 on 2019-12-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barundano', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='eat_together',
            field=models.SmallIntegerField(blank=True, choices=[(1, '혼자'), (2, '함께')], null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='feeling',
            field=models.SmallIntegerField(blank=True, choices=[(1, '좋아요'), (2, '괜찮아요'), (3, '별로에')], null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='food_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '아침식사'), (2, '점심식사'), (3, '저녁식사')], null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='real_meal_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='suggest_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
