# Generated by Django 3.1 on 2020-08-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmePequenosNegocios', '0010_auto_20200823_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='random', max_length=100),
            preserve_default=False,
        ),
    ]
