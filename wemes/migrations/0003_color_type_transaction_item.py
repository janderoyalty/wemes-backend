# Generated by Django 4.0.6 on 2022-08-01 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wemes', '0002_user_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop_off', models.DateField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_admin', to='wemes.user')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='wemes.user')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drop_off', models.DateField(blank=True)),
                ('due_date', models.DateField(blank=True)),
                ('is_shoe', models.BooleanField(default=True)),
                ('follow_up', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wemes.color')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='wemes.transaction')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wemes.type')),
            ],
        ),
    ]
