# Generated by Django 4.1.7 on 2023-03-28 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exscursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_of_stay', models.CharField(choices=[('1_week', '1 Неделя'), ('2_week', '2 Неделя'), ('3_week', '3 Неделя')], max_length=100)),
                ('service', models.CharField(choices=[('all_inclusive', 'Все включено'), ('not_all_inclusive', 'Не все включено')], max_length=100)),
                ('people_count', models.IntegerField()),
                ('hotel', models.CharField(choices=[('3_stars', '3 Звезды'), ('4_stars', '4 Звезды'), ('5_stars', '5 Звезд')], max_length=100)),
                ('price', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('excursions', models.ManyToManyField(to='main.exscursion')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tour')),
            ],
        ),
    ]
