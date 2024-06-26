# Generated by Django 5.0.3 on 2024-04-23 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_system', '0005_classregister_marks_delete_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management_system.classregister')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management_system.payment')),
            ],
        ),
    ]
