# Generated by Django 4.0.3 on 2022-06-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0005_diseases_name_alter_diseases_cp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='spciality',
            field=models.CharField(choices=[('brain', 'brain'), ('heart', 'heart')], max_length=100, verbose_name='Doctor Spaciality'),
        ),
    ]
