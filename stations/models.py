# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


ATTRIBUTES = (
    ('NT-Password', 'hashed'),
    ('Cleartext-Password', 'cleartext'),
)


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified``
    and ``created_by`` fields.
    """

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(User,
                                   on_delete=models.SET_NULL,
                                   null=True)

    class Meta:
        abstract = True


class Nas(models.Model):
    nasname = models.TextField()
    shortname = models.TextField()
    type = models.TextField()
    ports = models.IntegerField(blank=True, null=True)
    secret = models.TextField()
    server = models.TextField(blank=True, null=True)
    community = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nas'


class Radacct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.TextField()
    acctuniqueid = models.TextField(unique=True)
    username = models.TextField(blank=True, null=True)
    realm = models.TextField(blank=True, null=True)
    nasipaddress = models.GenericIPAddressField()
    nasportid = models.TextField(blank=True, null=True)
    nasporttype = models.TextField(blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctupdatetime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctinterval = models.BigIntegerField(blank=True, null=True)
    acctsessiontime = models.BigIntegerField(blank=True, null=True)
    acctauthentic = models.TextField(blank=True, null=True)
    connectinfo_start = models.TextField(blank=True, null=True)
    connectinfo_stop = models.TextField(blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.TextField(blank=True, null=True)
    callingstationid = models.TextField(blank=True, null=True)
    acctterminatecause = models.TextField(blank=True, null=True)
    servicetype = models.TextField(blank=True, null=True)
    framedprotocol = models.TextField(blank=True, null=True)
    framedipaddress = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radacct'


class Radcheck(TimeStampedModel):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64, choices=ATTRIBUTES)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)
    mac = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'radcheck'

    def save(self, *args, **kwargs):
        # format mac address for freeradius style
        self.mac = str(self.mac).upper().replace(':', '-')

        # default operator
        self.op = ':='

        if self.attribute == 'NT-Password':
            import hashlib
            self.value = hashlib.new('md4', self.value.encode('utf-16le'))\
                                .hexdigest()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('stations:index')

    def __str__(self):
        return self.username


class Radgroupcheck(models.Model):
    groupname = models.TextField()
    attribute = models.TextField()
    op = models.CharField(max_length=2)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'radgroupcheck'


class Radgroupreply(models.Model):
    groupname = models.TextField()
    attribute = models.TextField()
    op = models.CharField(max_length=2)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'radgroupreply'


class Radpostauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    reply = models.TextField(blank=True, null=True)
    calledstationid = models.TextField(blank=True, null=True)
    callingstationid = models.TextField(blank=True, null=True)
    authdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radpostauth'


class Radreply(models.Model):
    username = models.TextField()
    attribute = models.TextField()
    op = models.CharField(max_length=2)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'radreply'


class Radusergroup(models.Model):
    username = models.TextField()
    groupname = models.TextField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radusergroup'
