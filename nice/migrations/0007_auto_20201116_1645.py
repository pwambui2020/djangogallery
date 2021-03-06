# Generated by Django 3.1.3 on 2020-11-16 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nice', '0006_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nice.category'),
        ),
        migrations.AlterField(
            model_name='images',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nice.location'),
        ),
    ]
