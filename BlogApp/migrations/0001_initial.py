# Generated by Django 4.1 on 2024-06-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_content', models.TextField()),
                ('blog_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
