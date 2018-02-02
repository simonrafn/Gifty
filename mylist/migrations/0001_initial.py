# Generated by Django 2.0.1 on 2018-02-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=1000, null=True)),
                ('price', models.CharField(max_length=20)),
                ('is_removed', models.BooleanField(default=False)),
            ],
        ),
    ]
