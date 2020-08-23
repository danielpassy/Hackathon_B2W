# Generated by Django 3.1 on 2020-08-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AmePequenosNegocios', '0008_transaction_cashback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
