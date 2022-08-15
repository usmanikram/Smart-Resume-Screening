# Generated by Django 4.0.3 on 2022-08-15 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('completion_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('company_contact', models.CharField(max_length=200)),
                ('company_address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
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
        migrations.AddField(
            model_name='job',
            name='user_id',
            field=models.ForeignKey(limit_choices_to={'is_approved': True}, on_delete=django.db.models.deletion.CASCADE, to='base.users'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
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
