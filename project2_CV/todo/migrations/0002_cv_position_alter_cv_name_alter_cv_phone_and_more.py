# Generated by Django 4.0 on 2024-03-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='position',
            field=models.CharField(default='data', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='name',
            field=models.CharField(default='data', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cv',
            name='profile_image',
            field=models.ImageField(upload_to='profileimg'),
        ),
    ]
