# Generated by Django 4.2.4 on 2025-01-17 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_organization_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(to='website.tag'),
        ),
        migrations.AddField(
            model_name='people',
            name='tags',
            field=models.ManyToManyField(to='website.tag'),
        ),
    ]
