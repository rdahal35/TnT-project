# Generated by Django 2.0.7 on 2018-07-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='description',
            new_name='availability',
        ),
        migrations.AddField(
            model_name='listing',
            name='Title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='bath',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='bed_room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='cancelations',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='guests',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='house_rules',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='price_per_night',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
