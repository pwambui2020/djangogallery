# Generated by Django 3.1.3 on 2020-11-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['image']},
        ),
    ]
