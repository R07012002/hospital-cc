# Generated by Django 3.0.5 on 2021-05-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='admitDate',
            new_name='consultDate',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='symptoms',
            new_name='dateOfPregnancy',
        ),
        migrations.RenameField(
            model_name='patientdischargedetails',
            old_name='admitDate',
            new_name='consultDate',
        ),
        migrations.RenameField(
            model_name='patientdischargedetails',
            old_name='symptoms',
            new_name='dateOfPregnancy',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='daySpent',
        ),
        migrations.RemoveField(
            model_name='patientdischargedetails',
            name='roomCharge',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Maternity Unit ', 'Maternity Unit'), ('Birthing Unit', 'Birthing Unit'), ('General Care Nursery (GCN)', 'General Care Nursery (GCN)'), ('Special Care Nursery (SCN)', 'Special Care Nursery (SCN)'), ('Psychologist', 'Psychologist')], default='Maternity Unit', max_length=50),
        ),
    ]