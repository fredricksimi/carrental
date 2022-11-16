# Generated by Django 4.1.3 on 2022-11-14 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name_plural': 'Brands'},
        ),
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default-banner.jpg', upload_to='media_pics/')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vehicle')),
            ],
        ),
    ]