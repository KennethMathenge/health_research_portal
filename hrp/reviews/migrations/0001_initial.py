# Generated by Django 2.2.9 on 2020-02-11 11:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('researches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researches.Research')),
            ],
        ),
    ]
