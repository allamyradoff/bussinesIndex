# Generated by Django 4.0.4 on 2022-06-07 11:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_company_category_alter_company_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
