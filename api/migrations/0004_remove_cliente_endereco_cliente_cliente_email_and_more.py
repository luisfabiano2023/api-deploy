# Generated by Django 5.0.6 on 2024-06-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cliente_cpf_alter_cliente_contato_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco_cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='email', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
