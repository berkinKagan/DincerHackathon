# Generated by Django 4.2.5 on 2023-09-10 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_warehouse_normalimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='normalImage',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='segmentedImage',
        ),
    ]
