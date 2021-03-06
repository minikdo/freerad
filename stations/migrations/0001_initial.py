# Generated by Django 2.2.5 on 2019-09-10 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Radgroupcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.TextField()),
                ('attribute', models.TextField()),
                ('op', models.CharField(max_length=2)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'radgroupcheck',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nasname', models.TextField()),
                ('shortname', models.TextField()),
                ('type', models.TextField()),
                ('ports', models.IntegerField(blank=True, null=True)),
                ('secret', models.TextField()),
                ('server', models.TextField(blank=True, null=True)),
                ('community', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nas',
            },
        ),
        migrations.CreateModel(
            name='Radacct',
            fields=[
                ('radacctid', models.BigAutoField(primary_key=True, serialize=False)),
                ('acctsessionid', models.TextField()),
                ('acctuniqueid', models.TextField(unique=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('realm', models.TextField(blank=True, null=True)),
                ('nasipaddress', models.GenericIPAddressField()),
                ('nasportid', models.TextField(blank=True, null=True)),
                ('nasporttype', models.TextField(blank=True, null=True)),
                ('acctstarttime', models.DateTimeField(blank=True, null=True)),
                ('acctupdatetime', models.DateTimeField(blank=True, null=True)),
                ('acctstoptime', models.DateTimeField(blank=True, null=True)),
                ('acctinterval', models.BigIntegerField(blank=True, null=True)),
                ('acctsessiontime', models.BigIntegerField(blank=True, null=True)),
                ('acctauthentic', models.TextField(blank=True, null=True)),
                ('connectinfo_start', models.TextField(blank=True, null=True)),
                ('connectinfo_stop', models.TextField(blank=True, null=True)),
                ('acctinputoctets', models.BigIntegerField(blank=True, null=True)),
                ('acctoutputoctets', models.BigIntegerField(blank=True, null=True)),
                ('calledstationid', models.TextField(blank=True, null=True)),
                ('callingstationid', models.TextField(blank=True, null=True)),
                ('acctterminatecause', models.TextField(blank=True, null=True)),
                ('servicetype', models.TextField(blank=True, null=True)),
                ('framedprotocol', models.TextField(blank=True, null=True)),
                ('framedipaddress', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'db_table': 'radacct',
            },
        ),
        migrations.CreateModel(
            name='Radgroupreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.TextField()),
                ('attribute', models.TextField()),
                ('op', models.CharField(max_length=2)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'radgroupreply',
            },
        ),
        migrations.CreateModel(
            name='Radpostauth',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('pass_field', models.TextField(blank=True, db_column='pass', null=True)),
                ('reply', models.TextField(blank=True, null=True)),
                ('calledstationid', models.TextField(blank=True, null=True)),
                ('callingstationid', models.TextField(blank=True, null=True)),
                ('authdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'radpostauth',
            },
        ),
        migrations.CreateModel(
            name='Radreply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('attribute', models.TextField()),
                ('op', models.CharField(max_length=2)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'radreply',
            },
        ),
        migrations.CreateModel(
            name='Radusergroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('groupname', models.TextField()),
                ('priority', models.IntegerField()),
            ],
            options={
                'db_table': 'radusergroup',
            },
        ),
        migrations.CreateModel(
            name='Radcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=64)),
                ('attribute', models.CharField(choices=[('NT-Password', 'hashed'), ('Cleartext-Password', 'cleartext')], max_length=64)),
                ('op', models.CharField(max_length=2)),
                ('value', models.CharField(max_length=253)),
                ('mac', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'radcheck',
            },
        ),
    ]
