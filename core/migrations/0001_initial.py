# Generated by Django 3.0.6 on 2020-05-31 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
