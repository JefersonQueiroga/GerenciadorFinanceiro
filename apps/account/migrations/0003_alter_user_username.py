# Generated by Django 4.1.4 on 2022-12-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_telefone_user_phone_user_city_user_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
