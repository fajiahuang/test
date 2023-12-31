# Generated by Django 2.0.5 on 2018-07-30 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('remark', models.TextField(null=True)),
                ('installPath', models.TextField(null=True)),
                ('driverPath', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Browser',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('pageId', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('remark', models.TextField(null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('by', models.CharField(max_length=20)),
                ('locator', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'element',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=20)),
                ('host', models.TextField()),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Environment',
            },
        ),
        migrations.CreateModel(
            name='EnvironmentLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginId', models.IntegerField()),
                ('environmentId', models.IntegerField()),
                ('parameter', models.TextField()),
            ],
            options={
                'db_table': 'EnvironmentLogin',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('type', models.IntegerField(default=2)),
                ('package', models.CharField(max_length=200, null=True)),
                ('clazz', models.CharField(max_length=50, null=True)),
                ('method', models.CharField(max_length=50, null=True)),
                ('params', models.TextField(null=True)),
                ('steps', models.TextField(null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'keyword',
            },
        ),
        migrations.CreateModel(
            name='LoginConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('remark', models.TextField(null=True)),
                ('checkType', models.TextField(default='')),
                ('checkValue', models.TextField(default='')),
                ('steps', models.TextField()),
                ('params', models.TextField()),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('remark', models.TextField(null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'page',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('remark', models.TextField(null=True)),
                ('creator', models.IntegerField()),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('taskId', models.IntegerField(default=0, null=True)),
                ('projectId', models.IntegerField()),
                ('testcaseId', models.IntegerField()),
                ('browsers', models.TextField(null=True)),
                ('beforeLogin', models.TextField(null=True)),
                ('environments', models.TextField(null=True)),
                ('status', models.IntegerField(default=10)),
                ('parameter', models.TextField()),
                ('steps', models.TextField()),
                ('checkType', models.TextField()),
                ('checkValue', models.TextField()),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Result',
            },
        ),
        migrations.CreateModel(
            name='SplitResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environmentId', models.IntegerField(null=True)),
                ('browserId', models.IntegerField(null=True)),
                ('resultId', models.IntegerField()),
                ('loginStatus', models.IntegerField(default=0)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('startTime', models.DateTimeField(null=True)),
                ('finishTime', models.DateTimeField(null=True)),
                ('parameter', models.TextField()),
                ('expect', models.BooleanField()),
                ('status', models.IntegerField(default=10)),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'SplitResult',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testcases', models.TextField()),
                ('browsers', models.TextField(null=True)),
                ('status', models.IntegerField(default=1, null=True)),
                ('timing', models.IntegerField(default=1)),
                ('remark', models.TextField(null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Task',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('level', models.IntegerField(default=1)),
                ('beforeLogin', models.TextField(null=True)),
                ('steps', models.TextField()),
                ('parameter', models.TextField()),
                ('checkType', models.TextField()),
                ('checkValue', models.TextField()),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'testcase',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=10, null=True)),
                ('group', models.IntegerField(default=1, null=True)),
                ('email', models.TextField(null=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
