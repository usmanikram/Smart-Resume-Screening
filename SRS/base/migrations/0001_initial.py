# Generated by Django 4.0.3 on 2022-08-23 10:40

import base.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('designation', models.CharField(max_length=200, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('company_contact', models.CharField(max_length=200, null=True)),
                ('company_address', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'UserModel',
            },
            managers=[
                ('objects', base.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(limit_choices_to={'is_approved': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='uploads/resume/')),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.job')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.job')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=1)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.job')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('issued_by', models.CharField(max_length=200)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.job'),
        ),
    ]