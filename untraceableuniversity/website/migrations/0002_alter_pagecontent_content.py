# Generated by Django 4.2.2 on 2023-08-18 07:23

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]
