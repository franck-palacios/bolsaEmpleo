# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agencias(models.Model):
    agenciaid = models.AutoField(db_column='AgenciaID', primary_key=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='CuentaID')  # Field name made lowercase.
    agenombre = models.CharField(db_column='AgeNombre', unique=True, max_length=100)  # Field name made lowercase.
    agecorreo = models.CharField(db_column='AgeCorreo', unique=True, max_length=50)  # Field name made lowercase.
    agetelefono = models.CharField(db_column='AgeTelefono', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agencias'

    def __str__(self):
        return self.agenombre


class Areas(models.Model):
    areaid = models.AutoField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    areanombre = models.CharField(db_column='AreaNombre', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'

    def __str__(self):
        return self.areanombre


class Aspirantes(models.Model):
    aspiranteid = models.AutoField(db_column='AspiranteID', primary_key=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='CuentaID')  # Field name made lowercase.
    lugarid = models.ForeignKey('Lugares', models.DO_NOTHING, db_column='LugarID')  # Field name made lowercase.
    aspinombres = models.CharField(db_column='AspiNombres', max_length=50)  # Field name made lowercase.
    aspiapellidos = models.CharField(db_column='AspiApellidos', max_length=50)  # Field name made lowercase.
    aspigenero = models.CharField(db_column='AspiGenero', max_length=1)  # Field name made lowercase.
    aspinacionalidad = models.CharField(db_column='AspiNacionalidad', max_length=30)  # Field name made lowercase.
    aspinacimiento = models.DateField(db_column='AspiNacimiento')  # Field name made lowercase.
    aspicorreo = models.CharField(db_column='AspiCorreo', unique=True, max_length=50)  # Field name made lowercase.
    aspidui = models.CharField(db_column='AspiDui', max_length=9, blank=True, null=True)  # Field name made lowercase.
    aspipasaporte = models.CharField(db_column='AspiPasaporte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aspinit = models.CharField(db_column='AspiNit', max_length=14)  # Field name made lowercase.
    aspinup = models.CharField(db_column='AspiNup', max_length=12)  # Field name made lowercase.
    aspitelefono = models.CharField(db_column='AspiTelefono', max_length=8)  # Field name made lowercase.
    aspipaso = models.IntegerField(db_column='AspiPaso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aspirantes'

    def __str__(self):
        return self.aspinombres


class Aspirantesconocimientos(models.Model):
    aspiranteconocimientoid = models.AutoField(db_column='AspiranteConocimientoID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    conocimientoid = models.ForeignKey('Conocimientos', models.DO_NOTHING, db_column='ConocimientoID')  # Field name made lowercase.
    aconofecha = models.DateField(db_column='AConoFecha')  # Field name made lowercase.
    aconootorgado = models.CharField(db_column='AConoOtorgado', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspirantesConocimientos'

    def __str__(self):
        return self.aspiranteconocimientoid


class Aspiranteshabilidades(models.Model):
    aspirantehabilidadid = models.AutoField(db_column='AspiranteHabilidadID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    habilidadid = models.ForeignKey('Habilidades', models.DO_NOTHING, db_column='HabilidadID')  # Field name made lowercase.
    nivelid = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NivelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspirantesHabilidades'
        unique_together = (('aspiranteid', 'habilidadid'),)

    def __str__(self):
        return self.aspirantehabilidadid


class Aspirantesidiomas(models.Model):
    aspiranteidiomaid = models.AutoField(db_column='AspiranteIdiomaID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    idiomaid = models.ForeignKey('Idiomas', models.DO_NOTHING, db_column='IdiomaID')  # Field name made lowercase.
    nivelconverid = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NivelConverID')  # Field name made lowercase.
    nivelescuid = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NivelEscuID', related_name='idioma2')  # Field name made lowercase.
    nivelescriid = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NivelEscriID', related_name='nivel3')  # Field name made lowercase.
    nivellectuid = models.ForeignKey('Niveles', models.DO_NOTHING, db_column='NivelLectuID', related_name='nivel2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspirantesIdiomas'
        unique_together = (('aspiranteid', 'idiomaid'),)

    def __str__(self):
        return self.aspiranteidiomaid


class Candidatos(models.Model):
    candidatoid = models.AutoField(db_column='CandidatoID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    ofertaid = models.ForeignKey('Ofertas', models.DO_NOTHING, db_column='OfertaID')  # Field name made lowercase.
    candiactivo = models.IntegerField(db_column='CandiActivo')  # Field name made lowercase.
    candiprioridad = models.IntegerField(db_column='CandiPrioridad')  # Field name made lowercase.
    candiseleccionado = models.IntegerField(db_column='CandiSeleccionado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidatos'
        unique_together = (('aspiranteid', 'ofertaid'),)

    def __str__(self):
        return self.candidatoid


class Conocimientos(models.Model):
    conocimientoid = models.AutoField(db_column='ConocimientoID', primary_key=True)  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    conocimientotipoid = models.ForeignKey('Conocimientostipos', models.DO_NOTHING, db_column='ConocimientoTipoID')  # Field name made lowercase.
    cononombre = models.CharField(db_column='ConoNombre', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Conocimientos'
        unique_together = (('areaid', 'conocimientotipoid', 'cononombre'),)

    def __str__(self):
        return self.cononombre


class Conocimientostipos(models.Model):
    conocimientotipoid = models.AutoField(db_column='ConocimientoTipoID', primary_key=True)  # Field name made lowercase.
    conocimientotipo = models.CharField(db_column='ConocimientoTipo', unique=True, max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConocimientosTipos'

    def __str__(self):
        return self.conocimientotipo

class Delegaciones(models.Model):
    delegacionid = models.AutoField(db_column='DelegacionID', primary_key=True)  # Field name made lowercase.
    agenciaid = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='AgenciaID')  # Field name made lowercase.
    ofertaid = models.ForeignKey('Ofertas', models.DO_NOTHING, db_column='OfertaID', unique=True)  # Field name made lowercase.
    deletipo = models.CharField(db_column='DeleTipo', max_length=1)  # Field name made lowercase.
    delefechafin = models.DateField(db_column='DeleFechaFin')  # Field name made lowercase.
    deleestado = models.CharField(db_column='DeleEstado', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Delegaciones'

    def __str__(self):
        return self.delegacionid


class Empresas(models.Model):
    empresaid = models.AutoField(db_column='EmpresaID', primary_key=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='CuentaID')  # Field name made lowercase.
    emprenombre = models.CharField(db_column='EmpreNombre', unique=True, max_length=50)  # Field name made lowercase.
    emprecorreo = models.CharField(db_column='EmpreCorreo', unique=True, max_length=50)  # Field name made lowercase.
    empretelefono = models.CharField(db_column='EmpreTelefono', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'

    def __str__(self):
        return self.emprenombre


class Escritos(models.Model):
    escritoid = models.AutoField(db_column='EscritoID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    escritotipoid = models.ForeignKey('Escritostipos', models.DO_NOTHING, db_column='EscritoTipoID')  # Field name made lowercase.
    escrinombre = models.CharField(db_column='EscriNombre', max_length=70)  # Field name made lowercase.
    escrilugar = models.CharField(db_column='EscriLugar', max_length=70)  # Field name made lowercase.
    escrifecha = models.DateField(db_column='EscriFecha')  # Field name made lowercase.
    escrireferencia = models.TextField(db_column='EscriReferencia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Escritos'

    def __str__(self):
        return self.escrinombre


class Escritostipos(models.Model):
    escritotipoid = models.AutoField(db_column='EscritoTipoID', primary_key=True)  # Field name made lowercase.
    escritipo = models.CharField(db_column='EscriTipo', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscritosTipos'

    def __str__(self):
        return self.escritipo


class Evaluaciones(models.Model):
    evaluacionid = models.AutoField(db_column='EvaluacionID', primary_key=True)  # Field name made lowercase.
    candidatoid = models.ForeignKey(Candidatos, models.DO_NOTHING, db_column='CandidatoID')  # Field name made lowercase.
    examenid = models.ForeignKey('Examenes', models.DO_NOTHING, db_column='ExamenID')  # Field name made lowercase.
    evapuntos = models.IntegerField(db_column='EvaPuntos')  # Field name made lowercase.
    evaobtenidos = models.IntegerField(db_column='EvaObtenidos')  # Field name made lowercase.
    evafecha = models.DateField(db_column='EvaFecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Evaluaciones'

    def __str__(self):
        return self.evaluacionid


class Evaluacionesrespuestas(models.Model):
    evaluacionrespuestaid = models.AutoField(db_column='EvaluacionRespuestaID', primary_key=True)  # Field name made lowercase.
    evaluacionid = models.ForeignKey(Evaluaciones, models.DO_NOTHING, db_column='EvaluacionID')  # Field name made lowercase.
    evarespuntos = models.IntegerField(db_column='EvaResPuntos')  # Field name made lowercase.
    evaresenunciado = models.CharField(db_column='EvaResEnunciado', max_length=250)  # Field name made lowercase.
    evaresrespuesta = models.CharField(db_column='EvaResRespuesta', max_length=250)  # Field name made lowercase.
    evaresseleccionado = models.CharField(db_column='EvaResSeleccionado', max_length=250)  # Field name made lowercase.
    evaresacertado = models.IntegerField(db_column='EvaResAcertado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EvaluacionesRespuestas'

    def __str__(self):
        return self.evaluacionrespuestaid


class Examenes(models.Model):
    examenid = models.AutoField(db_column='ExamenID', primary_key=True)  # Field name made lowercase.
    agenciaid = models.ForeignKey(Agencias, models.DO_NOTHING, db_column='AgenciaID', blank=True, null=True)  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='EmpresaID', blank=True, null=True)  # Field name made lowercase.
    exanombre = models.CharField(db_column='ExaNombre', max_length=50)  # Field name made lowercase.
    exaduracion = models.IntegerField(db_column='ExaDuracion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Examenes'
        unique_together = (('agenciaid', 'empresaid', 'exanombre'),)

    def __str__(self):
        return self.exanombre


class Experiencias(models.Model):
    experienciaid = models.AutoField(db_column='ExperienciaID', primary_key=True)  # Field name made lowercase.
    puestoid = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='PuestoID')  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    expeperiodocant = models.IntegerField(db_column='ExpePeriodoCant')  # Field name made lowercase.
    expeperiodouni = models.CharField(db_column='ExpePeriodoUni', max_length=1)  # Field name made lowercase.
    expeorganizacion = models.CharField(db_column='ExpeOrganizacion', max_length=70)  # Field name made lowercase.
    expecontacto = models.CharField(db_column='ExpeContacto', max_length=100)  # Field name made lowercase.
    expetelefono = models.CharField(db_column='ExpeTelefono', max_length=8, blank=True, null=True)  # Field name made lowercase.
    expecorreo = models.CharField(db_column='ExpeCorreo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Experiencias'

    def __str__(self):
        return self.experienciaid


class Funciones(models.Model):
    funcionid = models.AutoField(db_column='FuncionID', primary_key=True)  # Field name made lowercase.
    experienciaid = models.ForeignKey(Experiencias, models.DO_NOTHING, db_column='ExperienciaID')  # Field name made lowercase.
    funcion = models.CharField(db_column='Funcion', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Funciones'

    def __str__(self):
        return self.funcion


class Habilidades(models.Model):
    habilidadid = models.AutoField(db_column='HabilidadID', primary_key=True)  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    habinombre = models.CharField(db_column='HabiNombre', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Habilidades'
        unique_together = (('areaid', 'habinombre'),)

    def __str__(self):
        return self.habinombre


class Idiomas(models.Model):
    idiomaid = models.AutoField(db_column='IdiomaID', primary_key=True)  # Field name made lowercase.
    idinombre = models.CharField(db_column='IdiNombre', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Idiomas'

    def __str__(self):
        return self.idinombre


class Logros(models.Model):
    logroid = models.AutoField(db_column='LogroID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    logronombre = models.CharField(db_column='LogroNombre', max_length=70)  # Field name made lowercase.
    logrootorga = models.CharField(db_column='LogroOtorga', max_length=50)  # Field name made lowercase.
    logrofecha = models.DateField(db_column='LogroFecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logros'

    def __str__(self):
        return self.logronombre


class Lugares(models.Model):
    lugarid = models.AutoField(db_column='LugarID', primary_key=True)  # Field name made lowercase.
    lugarpadreid = models.ForeignKey('self', models.DO_NOTHING, db_column='LugarPadreID', blank=True, null=True)  # Field name made lowercase.
    lugarnombre = models.CharField(db_column='LugarNombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugares'
        unique_together = (('lugarpadreid', 'lugarnombre'),)

    def __str__(self):
        return self.lugarnombre


class Mensajes(models.Model):
    mensajeid = models.AutoField(db_column='MensajeID', primary_key=True)  # Field name made lowercase.
    cuentaid = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='CuentaID', blank=True, null=True)  # Field name made lowercase.
    mentitulo = models.CharField(db_column='MenTitulo', max_length=100)  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=250)  # Field name made lowercase.
    menfecha = models.DateTimeField(db_column='MenFecha')  # Field name made lowercase.
    menleido = models.IntegerField(db_column='MenLeido')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mensajes'

    def __str__(self):
        return self.mentitulo


class Niveles(models.Model):
    nivelid = models.AutoField(db_column='NivelID', primary_key=True)  # Field name made lowercase.
    nivelnombre = models.CharField(db_column='NivelNombre', unique=True, max_length=30)  # Field name made lowercase.
    nivelpeso = models.IntegerField(db_column='NivelPeso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Niveles'

    def __str__(self):
        return self.nivelnombre


class Ofertas(models.Model):
    ofertaid = models.AutoField(db_column='OfertaID', primary_key=True)  # Field name made lowercase.
    plazaid = models.ForeignKey('Plazas', models.DO_NOTHING, db_column='PlazaID')  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='EmpresaID')  # Field name made lowercase.
    ofeinicio = models.DateField(db_column='OfeInicio')  # Field name made lowercase.
    ofecantidad = models.IntegerField(db_column='OfeCantidad')  # Field name made lowercase.
    ofetipo = models.CharField(db_column='OfeTipo', max_length=20)  # Field name made lowercase.
    ofefinreclutamiento = models.DateField(db_column='OfeFinReclutamiento')  # Field name made lowercase.
    ofedelegada = models.IntegerField(db_column='OfeDelegada')  # Field name made lowercase.
    ofeestado = models.CharField(db_column='OfeEstado', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ofertas'

    def __str__(self):
        return self.ofetipo


class Participaciones(models.Model):
    participacionid = models.AutoField(db_column='ParticipacionID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    partinombre = models.CharField(db_column='PartiNombre', max_length=70)  # Field name made lowercase.
    partilugar = models.CharField(db_column='PartiLugar', max_length=70)  # Field name made lowercase.
    partianfitrion = models.CharField(db_column='PartiAnfitrion', max_length=50)  # Field name made lowercase.
    partifecha = models.DateField(db_column='PartiFecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Participaciones'

    def __str__(self):
        return self.partinombre


class Perfiles(models.Model):
    perfilid = models.AutoField(db_column='PerfilID', primary_key=True)  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='EmpresaID')  # Field name made lowercase.
    pernombre = models.CharField(db_column='PerNombre', max_length=50)  # Field name made lowercase.
    peredad = models.IntegerField(db_column='PerEdad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Perfiles'
        unique_together = (('empresaid', 'pernombre'),)

    def __str__(self):
        return self.pernombre


class Perfilesareas(models.Model):
    perfilareaid = models.AutoField(db_column='PerfilAreaID', primary_key=True)  # Field name made lowercase.
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID')  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    conocimientotipoid = models.ForeignKey(Conocimientostipos, models.DO_NOTHING, db_column='ConocimientoTipoID', blank=True, null=True)  # Field name made lowercase.
    pareaperiodocant = models.IntegerField(db_column='PAreaPeriodoCant', blank=True, null=True)  # Field name made lowercase.
    pareaperiodouni = models.CharField(db_column='PAreaPeriodoUni', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesAreas'
        unique_together = (('perfilid', 'areaid'),)

    def __str__(self):
        return self.perfilareaid


class Perfilesconocimientos(models.Model):
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID', primary_key=True)  # Field name made lowercase.
    conocimientoid = models.ForeignKey(Conocimientos, models.DO_NOTHING, db_column='ConocimientoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesConocimientos'
        unique_together = (('perfilid', 'conocimientoid'),)

    def __str__(self):
        return self.perfilid


class Perfileshabilidades(models.Model):
    perfilhabilidadid = models.AutoField(db_column='PerfilHabilidadID', primary_key=True)  # Field name made lowercase.
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID')  # Field name made lowercase.
    habilidadid = models.ForeignKey(Habilidades, models.DO_NOTHING, db_column='HabilidadID')  # Field name made lowercase.
    nivelid = models.ForeignKey(Niveles, models.DO_NOTHING, db_column='NivelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesHabilidades'
        unique_together = (('perfilid', 'habilidadid'),)

    def __str__(self):
        return self.perfilhabilidadid


class Perfilesidiomas(models.Model):
    perfilidiomaid = models.AutoField(db_column='PerfilIdiomaID', primary_key=True)  # Field name made lowercase.
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID')  # Field name made lowercase.
    idiomaid = models.ForeignKey(Idiomas, models.DO_NOTHING, db_column='IdiomaID')  # Field name made lowercase.
    nivelid = models.ForeignKey(Niveles, models.DO_NOTHING, db_column='NivelID')  # Field name made lowercase.
    piditipo = models.CharField(db_column='PIdiTipo', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesIdiomas'

    def __str__(self):
        return self.perfilidiomaid


class Perfileslugares(models.Model):
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID', primary_key=True)  # Field name made lowercase.
    lugarid = models.ForeignKey(Lugares, models.DO_NOTHING, db_column='LugarID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesLugares'
        unique_together = (('perfilid', 'lugarid'),)

    def __str__(self):
        return self.perfilid


class Perfilespuestos(models.Model):
    perfilpuestoid = models.AutoField(db_column='PerfilPuestoID', primary_key=True)  # Field name made lowercase.
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID')  # Field name made lowercase.
    puestoid = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='PuestoID')  # Field name made lowercase.
    ppuesperiodocant = models.IntegerField(db_column='PPuesPeriodoCant')  # Field name made lowercase.
    ppuesperiodouni = models.CharField(db_column='PPuesPeriodoUni', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PerfilesPuestos'
        unique_together = (('perfilid', 'puestoid'),)

    def __str__(self):
        return self.perfilpuestoid


class Plazas(models.Model):
    plazaid = models.AutoField(db_column='PlazaID', primary_key=True)  # Field name made lowercase.
    empresaid = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='EmpresaID')  # Field name made lowercase.
    perfilid = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='PerfilID')  # Field name made lowercase.
    puestoid = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='PuestoID')  # Field name made lowercase.
    lugarid = models.ForeignKey(Lugares, models.DO_NOTHING, db_column='LugarID')  # Field name made lowercase.
    plasalariomin = models.IntegerField(db_column='PlaSalarioMin')  # Field name made lowercase.
    plasalariomax = models.IntegerField(db_column='PlaSalarioMax')  # Field name made lowercase.
    pladescripcion = models.CharField(db_column='PlaDescripcion', max_length=150)  # Field name made lowercase.
    platipo = models.CharField(db_column='PlaTipo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plazas'

    def __str__(self):
        return self.platipo


class Preguntas(models.Model):
    preguntaid = models.AutoField(db_column='PreguntaID', primary_key=True)  # Field name made lowercase.
    examenid = models.ForeignKey(Examenes, models.DO_NOTHING, db_column='ExamenID')  # Field name made lowercase.
    prepuntos = models.IntegerField(db_column='PrePuntos')  # Field name made lowercase.
    preenunciado = models.CharField(db_column='PreEnunciado', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preguntas'

    def __str__(self):
        return self.preenunciado


class Puestos(models.Model):
    puestoid = models.AutoField(db_column='PuestoID', primary_key=True)  # Field name made lowercase.
    areaid = models.ForeignKey(Areas, models.DO_NOTHING, db_column='AreaID')  # Field name made lowercase.
    puesnombre = models.CharField(db_column='PuesNombre', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Puestos'
        unique_together = (('areaid', 'puesnombre'),)

    def __str__(self):
        return self.puesnombre


class Recomendaciones(models.Model):
    recomendacionid = models.AutoField(db_column='RecomendacionID', primary_key=True)  # Field name made lowercase.
    aspiranteid = models.ForeignKey(Aspirantes, models.DO_NOTHING, db_column='AspiranteID')  # Field name made lowercase.
    reconombre = models.CharField(db_column='RecoNombre', max_length=100)  # Field name made lowercase.
    recotelefono = models.CharField(db_column='RecoTelefono', max_length=8)  # Field name made lowercase.
    recocorreo = models.CharField(db_column='RecoCorreo', max_length=50)  # Field name made lowercase.
    recotipo = models.CharField(db_column='RecoTipo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recomendaciones'

    def __str__(self):
        return self.reconombre


class Respuestas(models.Model):
    respuestaid = models.AutoField(db_column='RespuestaID', primary_key=True)  # Field name made lowercase.
    preguntaid = models.ForeignKey(Preguntas, models.DO_NOTHING, db_column='PreguntaID')  # Field name made lowercase.
    resenunciado = models.CharField(db_column='ResEnunciado', max_length=250)  # Field name made lowercase.
    rescorrecta = models.IntegerField(db_column='ResCorrecta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Respuestas'

    def __str__(self):
        return self.resenunciado


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
