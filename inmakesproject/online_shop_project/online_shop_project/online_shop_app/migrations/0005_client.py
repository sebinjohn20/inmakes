# Generated by Django 4.2.7 on 2023-11-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_app', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
