# Generated by Django 3.1.6 on 2021-03-23 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duoclieu', '0011_auto_20210323_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='HinhAnhLv5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level5')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level4')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level3')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level2')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level1')),
            ],
        ),
        migrations.CreateModel(
            name='HinhAnhLv0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hinh', models.ImageField(upload_to='giaotrinh')),
                ('ten_hinh', models.CharField(max_length=200)),
                ('level_0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='duoclieu.level0')),
            ],
        ),
    ]
