# Generated by Django 5.0.1 on 2024-01-10 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Post_Nom', models.CharField(max_length=50)),
                ('Prénom', models.CharField(max_length=50)),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.cursus')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='EnvoisTp',
            fields=[
                ('classe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usersapp.classe')),
                ('Séléctionner_Votre_travail', models.FileField(upload_to='')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.promotion')),
                ('vacation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersapp.vacation')),
            ],
            bases=('usersapp.classe',),
        ),
    ]
