# Generated by Django 4.1.3 on 2023-02-01 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('type_abonnement', models.CharField(max_length=255)),
                ('type_abonnee', models.CharField(max_length=255)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('numero_credit_carte', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='gestmuseeAPP\\static\\img\\data\\profile')),
            ],
        ),
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField()),
                ('date_deces', models.DateField(blank=True, null=True)),
                ('nationalite', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gestmuseeAPP\\static\\img\\data/artiste')),
            ],
        ),
        migrations.CreateModel(
            name='CalendrierMusee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('type_of_reservation', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('capacite', models.IntegerField()),
                ('est_valable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('personel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestmuseeAPP.personel')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type_of_reservation', models.CharField(max_length=255)),
                ('abonnee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestmuseeAPP.abonnee')),
            ],
        ),
        migrations.CreateModel(
            name='Oeuvre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('type_ouevre', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='gestmuseeAPP\\static\\img\\data\\oeuvre')),
                ('type_assurence', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestmuseeAPP.artiste')),
            ],
        ),
        migrations.CreateModel(
            name='Manifestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('theme', models.CharField(blank=True, max_length=50, null=True)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('image', models.ImageField(upload_to='gestmuseeAPP\\static\\img\\data\\manifestation')),
                ('notes', models.TextField(blank=True, null=True)),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestmuseeAPP.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('theme', models.CharField(blank=True, max_length=50, null=True)),
                ('Conferencier', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('duree', models.IntegerField(help_text='Durée en minutes', verbose_name='Durée de la conférence')),
                ('image', models.ImageField(upload_to='gestmuseeAPP\\static\\img\\data\\conference')),
                ('notes', models.TextField(blank=True, null=True)),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestmuseeAPP.salle')),
            ],
        ),
    ]
