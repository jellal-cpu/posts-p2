# Generated by Django 5.1 on 2024-08-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255, verbose_name='Tiêu đề')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Posts',
                'verbose_name_plural': 'Posts',
                'db_table': 'posts',
                'ordering': ('-created_at',),
            },
        ),
    ]
