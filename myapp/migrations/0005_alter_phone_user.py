# Generated by Django 4.1 on 2022-09-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_phone_phonenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone",
            name="user",
            field=models.CharField(max_length=10, verbose_name="user id"),
        ),
    ]
