# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def link_to_sites(apps, schema_editor):
    SiteSettings = apps.get_model('site', 'SiteSettings')
    Site = apps.get_model('sites', 'Site')

    for site in SiteSettings.objects.all():
        try:
            site.site = Site.objects.get(domain__iexact=site.domain)
        except:
            site.site = Site.objects.all().order_by('pk')[0]
        site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('site', '0005_auto_20170906_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='site',
            field=models.OneToOneField(default=0,
                                       on_delete=django.db.models.deletion.CASCADE,
                                       related_name='settings',
                                       to='sites.Site'),
            preserve_default=False,
        ),
        migrations.RunPython(link_to_sites),
        migrations.RemoveField(
            model_name='sitesettings',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='name',
        ),
    ]