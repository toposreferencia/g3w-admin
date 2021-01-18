# Generated by Django 2.2.16 on 2021-01-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0060_auto_20210104_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qgisauth',
            name='id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='QgisAuth ID'),
        ),
        migrations.AlterField(
            model_name='qgisauth',
            name='method',
            field=models.CharField(default='Basic', max_length=32, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='qgisauth',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='qgisauth',
            name='uri',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='URI (unused)'),
        ),
        migrations.AlterField(
            model_name='qgisauth',
            name='version',
            field=models.IntegerField(default=2, editable=False, verbose_name='Version'),
        ),
    ]