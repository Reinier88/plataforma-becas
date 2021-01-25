# Generated by Django 3.1.4 on 2021-01-25 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("becas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AverageGradeRanges",
            fields=[
                (
                    "average_grade_range_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "average_grade_range",
                    models.CharField(max_length=30, verbose_name="Promedio general"),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="FamilyMembersRange",
            fields=[
                (
                    "family_members_range_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "family_members_range",
                    models.CharField(
                        max_length=50,
                        verbose_name="Número de integrantes de la familia",
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="FamilyMonthlyIncome",
            fields=[
                (
                    "family_monthly_income_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "family_monthly_income",
                    models.CharField(
                        max_length=50, verbose_name="Ingreso familiar mensual"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="HomeCeil",
            fields=[
                ("home_ceil_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "home_ceil",
                    models.CharField(
                        max_length=50, verbose_name="Tipo de techo de la vivienda"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="HomeFloor",
            fields=[
                ("home_floor_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "home_floor",
                    models.CharField(
                        max_length=50, verbose_name="Tipo de piso de la vivienda"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="HomePersons",
            fields=[
                (
                    "home_persons_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "home_persons",
                    models.CharField(
                        max_length=50, verbose_name="Número de personas por habitación"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="HomeType",
            fields=[
                ("home_type_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "home_type",
                    models.CharField(max_length=50, verbose_name="Tipo de vivienda"),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="HomeWalls",
            fields=[
                ("home_walls_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "home_walls",
                    models.CharField(
                        max_length=50, verbose_name="Tipo de muros de la vivienda"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="MaritalStatus",
            fields=[
                (
                    "marital_status_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "marital_status",
                    models.CharField(max_length=50, verbose_name="Estado Civil"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParentsEducationLevel",
            fields=[
                (
                    "parent_education_level_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "parent_education_level",
                    models.CharField(
                        max_length=50, verbose_name="Nivel educativo del padre/madre"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="PovertyRange",
            fields=[
                ("poverty_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "poverty",
                    models.CharField(
                        max_length=30, verbose_name="Rango de pobreza de su colonia"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="ProviderPerks",
            fields=[
                (
                    "provider_perks_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "provider_perks",
                    models.CharField(
                        max_length=50,
                        verbose_name="Principal proveedor con prestaciones",
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="ServiceElectricity",
            fields=[
                (
                    "service_electricity_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "service_electricity",
                    models.CharField(max_length=50, verbose_name="Electricidad"),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="ServiceGas",
            fields=[
                ("service_gas_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "service_gas",
                    models.CharField(
                        max_length=50, verbose_name="Combustible para cocinar"
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="ServiceSewer",
            fields=[
                (
                    "service_sewer_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "service_sewer",
                    models.CharField(max_length=50, verbose_name="Drenaje"),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="ServiceWater",
            fields=[
                (
                    "service_water_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "service_water",
                    models.CharField(max_length=50, verbose_name="Agua potable"),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="SocialSecurity",
            fields=[
                (
                    "social_security_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "social_security",
                    models.CharField(
                        max_length=50,
                        verbose_name="Afiliación a servicios de salud y seguridad social",
                    ),
                ),
                ("value", models.IntegerField(verbose_name="Puntuación")),
            ],
        ),
        migrations.CreateModel(
            name="SocioEconomicStudy",
            fields=[
                (
                    "username",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="auth.user",
                    ),
                ),
                (
                    "dad_occupation",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Ocupación del padre ",
                    ),
                ),
                (
                    "dad_income",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Ingresos mensuales del padre ",
                    ),
                ),
                (
                    "mom_occupation",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Ocupación de la madre ",
                    ),
                ),
                (
                    "mom_income",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Ingresos mensuales de la madre ",
                    ),
                ),
                (
                    "son_occupation",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Ocupación del hijo ",
                    ),
                ),
                (
                    "son_income",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Ingresos mensuales del hijo ",
                    ),
                ),
                (
                    "candidate_occupation",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Ocupación del candidato ",
                    ),
                ),
                (
                    "candidate_income",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Ingresos mensuales del candidato ",
                    ),
                ),
                (
                    "other_occupation",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Ocupación del candidato ",
                    ),
                ),
                (
                    "other_income",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Ingresos mensuales del candidato ",
                    ),
                ),
                (
                    "exp_food",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados en comida ",
                    ),
                ),
                (
                    "exp_rent",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados en renta/hipoteca ",
                    ),
                ),
                (
                    "exp_water",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados en  el  servicio de agua",
                    ),
                ),
                (
                    "exp_energy",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados en el servicio de electricidad",
                    ),
                ),
                (
                    "exp_leisure",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a la diversión ",
                    ),
                ),
                (
                    "exp_transport",
                    models.FloatField(
                        verbose_name="Gastos mensuales aproximados dedicados al transporte"
                    ),
                ),
                (
                    "exp_education",
                    models.FloatField(
                        verbose_name="Gastos mensuales aproximados dedicados a la educación"
                    ),
                ),
                (
                    "exp_telecom",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a servicios de telefonía, cable e internet",
                    ),
                ),
                (
                    "exp_medic",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a gastos médicos",
                    ),
                ),
                (
                    "exp_gas",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a gas y energía",
                    ),
                ),
                (
                    "exp_vestido",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a vestido",
                    ),
                ),
                (
                    "exp_loans",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a créditos e intereses",
                    ),
                ),
                (
                    "exp_gasolina",
                    models.FloatField(
                        blank=True,
                        null=True,
                        verbose_name="Gastos mensuales aproximados dedicados a gasolina",
                    ),
                ),
                (
                    "exp_otros",
                    models.FloatField(
                        blank=True, null=True, verbose_name="Otros gastos "
                    ),
                ),
                (
                    "employment_benefits",
                    models.CharField(
                        choices=[
                            ("0", "Ninguna prestación"),
                            (
                                "1",
                                "Servicio médico, sistema de ahorro para retiro, incapacidad laboral con goce de sueldo",
                            ),
                        ],
                        max_length=100,
                        verbose_name="Principal proveedor en el hogar económicamente activo, asalariado con todas y cada una de las siguientes prestaciones laborales:",
                    ),
                ),
                (
                    "section4_obs",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Observaciones"
                    ),
                ),
                (
                    "punct_section4",
                    models.IntegerField(
                        verbose_name="puntuación total obtenida en el apartado "
                    ),
                ),
                (
                    "home_type",
                    models.CharField(
                        choices=[
                            ("0", "Prestada"),
                            ("1", "Rentada"),
                            ("2", "La están pagando"),
                            ("3", "Propia"),
                        ],
                        max_length=100,
                        verbose_name="La casa que habita la familia es:",
                    ),
                ),
                (
                    "floor_type",
                    models.CharField(
                        choices=[
                            ("0", "Firme de cemento, tierra"),
                            (
                                "1",
                                "Con recubrimiento (laminado, vitropiso, mosaico, madera)",
                            ),
                        ],
                        max_length=100,
                        verbose_name="el piso  de su vivienda es:",
                    ),
                ),
                (
                    "ceiling_type",
                    models.CharField(
                        choices=[
                            ("0", "Prestada"),
                            ("1", "Rentada"),
                            ("2", "La están pagando"),
                            ("3", "Propia"),
                        ],
                        max_length=100,
                        verbose_name="El techo de su vivienda es:",
                    ),
                ),
                (
                    "walls_tipe",
                    models.CharField(
                        choices=[
                            ("0", "Adobe"),
                            ("1", "Piedra"),
                            ("2", "Madera"),
                            ("3", "Block"),
                            ("4", "Tabique o ladrillo"),
                        ],
                        max_length=100,
                        verbose_name="Los muros de su vivienda son de:",
                    ),
                ),
                (
                    "room_persons",
                    models.CharField(
                        choices=[
                            ("0", "Número  de personas por cuarto mayor a 2.5"),
                            ("1", "Número  de personas por cuarto menor a 2.5"),
                        ],
                        max_length=100,
                        verbose_name="Número de personas por cuarto:",
                    ),
                ),
                (
                    "water_service",
                    models.CharField(
                        choices=[("0", "Si"), ("1", "No")],
                        max_length=100,
                        verbose_name="¿ Su casa cuenta con servicio de agua entubada dentro de la vivienda o fuera de la vivienda, pero dentro del terreno ?:",
                    ),
                ),
                (
                    "drain_service",
                    models.CharField(
                        choices=[("0", "Si"), ("1", "No")],
                        max_length=100,
                        verbose_name="¿ Su casa cuenta con servicio de drenaje conectado a una red pública o a una fora séptica ?:",
                    ),
                ),
                (
                    "elect_service",
                    models.CharField(
                        choices=[("0", "Si"), ("1", "No")],
                        max_length=100,
                        verbose_name="¿ Su casa cuenta con servicio de electricidad obtenido del servicio público, de panel solar o de otra fuente, planta paticular?:",
                    ),
                ),
                (
                    "fuel_service",
                    models.CharField(
                        choices=[("0", "Si"), ("1", "No")],
                        max_length=100,
                        verbose_name="¿ Su casa cuenta con servicio de drenaje conectado a una red pública o a una fora séptica ?:",
                    ),
                ),
                (
                    "veracity",
                    models.BooleanField(
                        blank=True,
                        null=True,
                        verbose_name=" ¿ Confirma que toda la informacion proporcionada es verídica ?",
                    ),
                ),
                (
                    "total_punct",
                    models.IntegerField(
                        verbose_name="puntuación total obtenida en  el ESE "
                    ),
                ),
                (
                    "porcent_punct",
                    models.IntegerField(
                        verbose_name="nivel de vulnerabilidad o pobreza obtenido  en  el Estudio Socio Económico (Porciento) "
                    ),
                ),
                (
                    "poverty_level",
                    models.IntegerField(
                        verbose_name="nivel de vulnerabilidad o pobreza obtenido  en  el Estudio Socio Económico (Puntos)"
                    ),
                ),
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "average_grade_range",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.averagegraderanges",
                        verbose_name="Promedio general",
                    ),
                ),
                (
                    "education_level_father",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education_level_father",
                        to="becas.parentseducationlevel",
                        verbose_name="Escolaridad del padre",
                    ),
                ),
                (
                    "education_level_mother",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education_level_mother",
                        to="becas.parentseducationlevel",
                        verbose_name="Escolaridad de la madre",
                    ),
                ),
                (
                    "education_level_partner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education_level_partner",
                        to="becas.parentseducationlevel",
                        verbose_name="Escolaridad de la esposa(o)",
                    ),
                ),
                (
                    "family_members",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.familymembersrange",
                        verbose_name="Número de integrantes de la familia",
                    ),
                ),
                (
                    "family_monthly_income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.familymonthlyincome",
                        verbose_name="Ingreso familiar mensual",
                    ),
                ),
                (
                    "home_ceil",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.homeceil",
                        verbose_name="Tipo de techo de la vivienda",
                    ),
                ),
                (
                    "home_floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.homefloor",
                        verbose_name="Tipo de piso de la vivienda",
                    ),
                ),
                (
                    "home_persons",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.homepersons",
                        verbose_name="Número de personas por habitación",
                    ),
                ),
                (
                    "home_walls",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.homewalls",
                        verbose_name="Tipo de muros de la vivienda",
                    ),
                ),
                (
                    "marital_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.maritalstatus",
                        verbose_name="Estado civil",
                    ),
                ),
                (
                    "poverty_range",
                    models.ForeignKey(
                        help_text="Puedes consultar la clasificación de tu colonia en el siguiente vínculo: https://www.coneval.org.mx/Medicion/IRS/Paginas/Rezago_social_AGEB_2010.aspx\n Te recordamos que proporcionar información falsa o imprecisa descalificará tu solicitud.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.povertyrange",
                        verbose_name="Rango de pobreza de su colonia",
                    ),
                ),
                (
                    "provider_perks",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.providerperks",
                        verbose_name="Principal proveedor en el hogar cuenta con prestaciones",
                    ),
                ),
                (
                    "service_electricity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.serviceelectricity",
                        verbose_name="Electricidad",
                    ),
                ),
                (
                    "service_gas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.servicegas",
                        verbose_name="Coombustible para cocinar",
                    ),
                ),
                (
                    "service_sewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.servicesewer",
                        verbose_name="Drenaje",
                    ),
                ),
                (
                    "service_water",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.servicewater",
                        verbose_name="Agua potable",
                    ),
                ),
                (
                    "social_security",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="becas.socialsecurity",
                        verbose_name="Afiliación a servicios de salud y seguridad social",
                    ),
                ),
            ],
        ),
    ]
