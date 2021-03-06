# Generated by Django 3.1.6 on 2021-03-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duoclieu', '0005_auto_20210320_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duoclieu',
            name='slug',
            field=models.SlugField(blank=True, help_text='Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/duoclieu/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là tên khoa học của dược liệu.', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hothucvat',
            name='gioi_thieu_chung',
            field=models.TextField(blank=True, help_text='Nếu không có gì để viết vào có thể để trống.', max_length=1000, null=True, verbose_name='giới thiện chung'),
        ),
        migrations.AlterField(
            model_name='hothucvat',
            name='slug',
            field=models.SlugField(help_text='Thông tin này sẽ hiển thị tại địa chỉ web, ví dụ: www.home/ho-thuc-vat/XXXXX, nếu không nhập dữ liệu chương trình sẽ mặc định XXXXX là họ dược liệu.', null=True, unique=True),
        ),
    ]
