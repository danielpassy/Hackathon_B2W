# Generated by Django 3.1 on 2020-08-22 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AmePequenosNegocios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgSend', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msgReceive', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
