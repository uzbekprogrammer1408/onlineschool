# Generated by Django 4.0.2 on 2022-02-13 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fanlar',
            },
        ),
        migrations.CreateModel(
            name='Sinflar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinf', models.IntegerField(unique=True)),
                ('sinf_text', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Sinf',
                'verbose_name_plural': 'Sinflar',
            },
        ),
        migrations.CreateModel(
            name='Mavzular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.fanlar')),
            ],
            options={
                'verbose_name': 'Mavzu',
                'verbose_name_plural': 'Mavzular',
            },
        ),
        migrations.AddField(
            model_name='fanlar',
            name='sinf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.sinflar'),
        ),
    ]
