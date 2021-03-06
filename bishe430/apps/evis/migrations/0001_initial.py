# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 08:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='devCompChEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='元素名称')),
                ('content', models.FloatField(default=0, verbose_name='元素含量')),
                ('offset', models.FloatField(default=0, verbose_name='元素偏差值')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
        ),
        migrations.CreateModel(
            name='devCompEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseID', models.CharField(max_length=10, verbose_name='案件编号')),
                ('evidenceID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('eviState', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证状态')),
                ('eviMake', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证制备方法')),
                ('eviDraw', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证提取方法')),
                ('eviAnalyse', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证分析方法')),
                ('analyseCondition', models.CharField(blank=True, max_length=30, null=True, verbose_name='分析条件')),
                ('picUrl', models.ImageField(blank=True, null=True, upload_to='devCompEvi/', verbose_name='装置物证外观图片路径')),
                ('picDescrip', models.CharField(blank=True, max_length=100, null=True, verbose_name='图片描述')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员')),
            ],
        ),
        migrations.CreateModel(
            name='devCompEviFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectDevice', models.CharField(blank=True, max_length=30, null=True, verbose_name='检测设备名称及型号')),
                ('detectMrfs', models.CharField(blank=True, max_length=20, null=True, verbose_name='仪器厂家')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('detectType', models.IntegerField(choices=[(1, 'FTIF'), (2, 'Raman'), (3, 'XRD'), (4, 'XRF'), (5, 'GC-MS')], verbose_name='检测数据类型')),
                ('docType', models.IntegerField(blank=True, choices=[(1, 'txt'), (2, 'excel'), (3, 'PDF')], null=True, verbose_name='录入文档格式')),
                ('docUrl', models.FileField(blank=True, null=True, upload_to='devCompEviFile/', verbose_name='录入文档路径')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('devCompEvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.devCompEvi', verbose_name='对应的物证')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员')),
            ],
        ),
        migrations.CreateModel(
            name='devCompEviPeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peakStart', models.FloatField(default=0, verbose_name='起点')),
                ('peakEnd', models.FloatField(default=0, verbose_name='终点')),
                ('peakHeight', models.FloatField(default=0, verbose_name='峰高')),
                ('peakArea', models.FloatField(default=0, verbose_name='峰面积')),
                ('devCompEviFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.devCompEviFile', verbose_name='对应的物证文件')),
            ],
        ),
        migrations.CreateModel(
            name='devShapeEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCircuit', models.BooleanField(default=False, verbose_name='是否是电路板')),
                ('eviID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('originalUrl', models.ImageField(blank=True, null=True, upload_to='devShapeEviOriginal/', verbose_name='原始图像文件路径')),
                ('originalResolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='原始图像采集分辨率')),
                ('nomUrl', models.ImageField(blank=True, null=True, upload_to='devShapeEviNom/', verbose_name='归一化图像文件路径')),
                ('nomResolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='归一化图像分辨率')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员')),
            ],
        ),
        migrations.CreateModel(
            name='exploChEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='元素名称')),
                ('content', models.FloatField(default=0, verbose_name='元素含量')),
                ('offset', models.FloatField(default=0, verbose_name='元素偏差值')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
        ),
        migrations.CreateModel(
            name='exploEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseID', models.CharField(max_length=10, verbose_name='案件编号')),
                ('evidenceID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('eviState', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证状态')),
                ('eviMake', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证制备方法')),
                ('eviDraw', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证提取方法')),
                ('eviAnalyse', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证分析方法')),
                ('analyseCondition', models.CharField(blank=True, max_length=30, null=True, verbose_name='分析条件')),
                ('picUrl', models.ImageField(blank=True, null=True, upload_to='exploEvi/', verbose_name='炸药物证外观图片路径')),
                ('picDescrip', models.CharField(blank=True, max_length=100, null=True, verbose_name='图片描述')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员')),
            ],
        ),
        migrations.CreateModel(
            name='exploEviFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectDevice', models.CharField(blank=True, max_length=30, null=True, verbose_name='检测设备名称及型号')),
                ('detectMrfs', models.CharField(blank=True, max_length=20, null=True, verbose_name='仪器厂家')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('detectType', models.IntegerField(choices=[(1, 'FTIF'), (2, 'Raman'), (3, 'XRD'), (4, 'XRF'), (5, 'GC-MS')], verbose_name='检测数据类型')),
                ('docType', models.IntegerField(blank=True, choices=[(1, 'txt'), (2, 'excel'), (3, 'PDF')], null=True, verbose_name='录入文档格式')),
                ('docUrl', models.FileField(blank=True, null=True, upload_to='exploEviFile/', verbose_name='录入文档路径')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
                ('exploEvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.exploEvi', verbose_name='对应的物证')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员')),
            ],
        ),
        migrations.CreateModel(
            name='exploEviPeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peakStart', models.FloatField(default=0, verbose_name='起点')),
                ('peakEnd', models.FloatField(default=0, verbose_name='终点')),
                ('peakHeight', models.FloatField(default=0, verbose_name='峰高')),
                ('peakArea', models.FloatField(default=0, verbose_name='峰面积')),
                ('exploEviFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.exploEviFile', verbose_name='对应的物证文件')),
            ],
        ),
        migrations.AddField(
            model_name='explochevi',
            name='exploEvi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.exploEvi', verbose_name='对应的物证'),
        ),
        migrations.AddField(
            model_name='devcompchevi',
            name='devCompEvi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evis.devCompEvi', verbose_name='对应的物证'),
        ),
    ]
