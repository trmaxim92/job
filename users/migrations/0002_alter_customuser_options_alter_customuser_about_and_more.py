# Generated by Django 4.2 on 2025-06-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_employer',
            field=models.BooleanField(default=False, verbose_name='Работодатель'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_worker',
            field=models.BooleanField(default=False, verbose_name='Соискатель'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics/', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rating',
            field=models.FloatField(default=0.0, verbose_name='Рейтинг'),
        ),
    ]
