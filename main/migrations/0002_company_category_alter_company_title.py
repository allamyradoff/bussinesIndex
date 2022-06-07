# Generated by Django 4.0.4 on 2022-06-06 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category'),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
