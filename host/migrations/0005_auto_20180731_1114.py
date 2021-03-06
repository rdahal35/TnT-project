# Generated by Django 2.0.7 on 2018-07-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0004_listing_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='ical_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='platform',
            field=models.CharField(blank=True, choices=[('Airbnb', 'Airbnb'), ('Booking.com', 'Booking.com'), ('HomeAway', 'HomeAway'), ('VRBO', 'VRBO'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_image/'),
        ),
    ]
