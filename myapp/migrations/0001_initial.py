# Generated by Django 3.2.18 on 2023-02-24 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('seconds', models.IntegerField()),
            ],
            options={
                'db_table': 'music',
            },
        ),
    ]
