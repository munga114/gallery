# Generated by Django 3.1.2 on 2020-10-12 05:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('name', models.CharField(max_length=100)),
                ('CREATED_AT', models.DateTimeField(default=datetime.datetime.now)),
                ('UPDATED_AT', models.DateTimeField(default=datetime.datetime.now)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categories.category')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='locations.location')),
            ],
        ),
    ]
