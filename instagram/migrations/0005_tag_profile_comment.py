# Generated by Django 4.0.5 on 2022-06-13 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0004_remove_comment_blog_remove_comment_parent_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='blogs/profile', verbose_name='Image file')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('bio', models.TextField(max_length=255, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.post')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]