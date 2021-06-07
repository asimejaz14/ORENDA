# Generated by Django 3.2.4 on 2021-06-03 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cnic',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employee.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to='employee/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]