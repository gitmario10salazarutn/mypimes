create table multa (
    mult_idmulta INT NOT NULL IDENTITY(1, 1),
    mult_nombre varchar(100),
    mult_valor varchar(100),
    primary key (mult_idmulta)
);
create table alicuota (
    aliact_id INT NOT NULL IDENTITY(1, 1),
    mult_idmulta integer,
    aliact_fechaactualizacion date,
    aliact_valoranterior numeric(8, 2),
    aliact_valoractual numeric(8, 2),
    primary key (aliact_id),
    foreign key (mult_idmulta) references multa (mult_idmulta)
);
create unique index alicuota_pk on alicuota (aliact_id asc);
create index fk_mult_alicuota_fk on alicuota (mult_idmulta asc);
create table alicuota_actualizada (
    aliact_id INT NOT NULL IDENTITY(1, 1),
    alic_idalicuota integer,
    alic_valor numeric(8, 2),
    alic_fecha date,
    primary key (aliact_id),
    foreign key (aliact_id) references alicuota (aliact_id)
);
create unique index alicuota_actualizada_pk on alicuota_actualizada (aliact_id asc);
create table rol_usuario (
    rol_idrol INT NOT NULL IDENTITY(1, 1),
    rol_nombrerol varchar(50) NOT NULL,
    prefiho varchar(4) NOT NULL,
    primary key (rol_idrol)
);
create table persona (
    pers_persona varchar(25) not null,
    pers_email varchar(50),
    pers_nombres varchar(50),
    pers_apellidos varchar(50),
    pers_telefono varchar(15),
    pers_direccion varchar(50),
    primary key (pers_persona)
);
create table user_usuario (
    user_idusuario varchar(25) not null,
    rol_idrol integer,
    pers_persona varchar(25),
    user_password varchar(200),
    user_estado smallint,
    user_fecha date,
    primary key (user_idusuario),
    foreign key (rol_idrol) references rol_usuario (rol_idrol),
    foreign key (pers_persona) references persona (pers_persona)
);
create table condomino (
    cond_idcondomino INT NOT NULL IDENTITY(1, 1),
    user_idusuario varchar(25),
    primary key (cond_idcondomino),
    foreign key (user_idusuario) references user_usuario (user_idusuario)
);
create unique index condomino_pk on condomino (cond_idcondomino asc);
create index fk_user_condomino_fk on condomino (user_idusuario asc);
create table tesorero (
    tes_idtesorero INT NOT NULL IDENTITY(1, 1),
    user_idusuario varchar(25),
    primary key (tes_idtesorero),
    foreign key (user_idusuario) references user_usuario (user_idusuario)
);
create table egresos (
    egre_id INT NOT NULL IDENTITY(1, 1),
    tes_idtesorero integer,
    egre_descripcion varchar(200),
    egre_subtotal numeric(8, 2),
    egre_iva numeric(8, 2),
    egre_total numeric(8, 2),
    egre_fecha date,
    egre_numero varchar(20),
    primary key (egre_id),
    foreign key (tes_idtesorero) references tesorero (tes_idtesorero)
);
create table detalle_egresos (
    detegre_id INT NOT NULL IDENTITY(1, 1),
    egre_id integer,
    detegre_numerofactura varchar(20),
    detegre_valorfactura numeric(8, 2),
    deteegre_documento varchar(200),
    detegre_subtotal numeric(8, 2),
    detegre_iva numeric(8, 2),
    detegre_total numeric(8, 2),
    detegre_fecha date,
    primary key (detegre_id),
    foreign key (egre_id) references egresos (egre_id)
);
create unique index detalle_egresos_pk on detalle_egresos (detegre_id asc);
create index fk_egresos_detegre_fk on detalle_egresos (egre_id asc);
create table pago_alicuota (
    pagali_id INT NOT NULL IDENTITY(1, 1),
    tes_idtesorero integer,
    cond_idcondomino integer,
    pagali_fecha date,
    pagali_numero varchar(10),
    pagali_subtotal numeric(8, 2),
    pagali_iva numeric(8, 2),
    pagali_total numeric(8, 2),
    primary key (pagali_id),
    foreign key (tes_idtesorero) references tesorero (tes_idtesorero),
    foreign key (cond_idcondomino) references condomino (cond_idcondomino)
);
create table detalle_pago (
    detpag_id INT NOT NULL IDENTITY(1, 1),
    pagali_id integer,
    aliact_id integer,
    detpag_subtotal numeric(8, 2),
    detpag_iva numeric(8, 2),
    detpag_total numeric(8, 2),
    detpag_fecha numeric(8, 2),
    detpag_multa numeric(8, 2),
    primary key (detpag_id),
    foreign key (pagali_id) references pago_alicuota (pagali_id),
    foreign key (aliact_id) references alicuota_actualizada (aliact_id)
);
create unique index detalle_pago_pk on detalle_pago (detpag_id asc);
create index fk_pagali_detpago_fk on detalle_pago (pagali_id asc);
create index fk_aliact_detpago_fk on detalle_pago (aliact_id asc);
create table tipo_servicios (
    tipserv_id INT NOT NULL IDENTITY(1, 1),
    tipserv_nombre varchar(50),
    primary key (tipserv_id)
);
create table servicios (
    serv_idservicios INT NOT NULL IDENTITY(1, 1),
    tipserv_id integer,
    serv_nombreservicio varchar(100),
    serv_descripcion varchar(100),
    serv_valor numeric(8, 2),
    serv_iva numeric(8, 2),
    serv_cantidad integer,
    primary key (serv_idservicios),
    foreign key (tipserv_id) references tipo_servicios (tipserv_id)
);
create table reservaciones (
    resv_idreservacion INT NOT NULL IDENTITY(1, 1),
    serv_idservicios integer,
    resv_fecha date,
    resv_descripcion varchar(200),
    primary key (resv_idreservacion),
    foreign key (serv_idservicios) references servicios (serv_idservicios)
);
create table secretario (
    sec_idsecretario INT NOT NULL IDENTITY(1, 1),
    user_idusuario varchar(25),
    primary key (sec_idsecretario),
    foreign key (user_idusuario) references user_usuario (user_idusuario)
);
create table detalle_reserveciones (
    detres_iddetalle INT NOT NULL IDENTITY(1, 1),
    resv_idreservacion integer,
    sec_idsecretario integer,
    cond_idcondomino integer,
    detres_subtotal numeric(8, 2),
    detres_iva numeric(8, 2),
    detres_total numeric(8, 2),
    detres_cantidad integer,
    detres_horainicio time,
    detres_horafin time,
    detres_fecha date,
    primary key (detres_iddetalle),
    foreign key (resv_idreservacion) references reservaciones (resv_idreservacion),
    foreign key (sec_idsecretario) references secretario (sec_idsecretario),
    foreign key (cond_idcondomino) references condomino (cond_idcondomino)
);
create unique index detalle_reserveciones_pk on detalle_reserveciones (detres_iddetalle asc);
create index fk_reserv_detreserv_fk on detalle_reserveciones (resv_idreservacion asc);
create index fk_secr_detreserv_fk on detalle_reserveciones (sec_idsecretario asc);
create index fk_cond_detresv_fk on detalle_reserveciones (cond_idcondomino asc);
create table tipo_documento (
    tipdoc_id INT NOT NULL IDENTITY(1, 1),
    tipdoc_nombre varchar(50),
    primary key (tipdoc_id)
);
create table documentos (
    doc_iddocumento INT NOT NULL IDENTITY(1, 1),
    tipdoc_id integer,
    sec_idsecretario integer,
    doc_descripcion varchar(200),
    doc_documento varbinary(max),
    doc_entidad varchar(100),
    doc_recibido integer,
    primary key (doc_iddocumento),
    foreign key (tipdoc_id) references tipo_documento (tipdoc_id),
    foreign key (sec_idsecretario) references secretario (sec_idsecretario)
);
create unique index documentos_pk on documentos (doc_iddocumento asc);
create index fk_tipdoc_docs_fk on documentos (tipdoc_id asc);
create index fk_secre_documentos_fk on documentos (sec_idsecretario asc);
create unique index egresos_pk on egresos (egre_id asc);
create index fk_tes_egresos_fk on egresos (tes_idtesorero asc);
create table estado_documentos (
    estdoc_id INT NOT NULL IDENTITY(1, 1),
    doc_iddocumento integer,
    aprobado_presidente smallint,
    aprobado_entidad smallint,
    fecha_aprovadopresidente date,
    fecha_aprobadoentidad date,
    primary key (estdoc_id),
    foreign key (doc_iddocumento) references documentos (doc_iddocumento)
);
create unique index estado_documentos_pk on estado_documentos (estdoc_id asc);
create index fk_docs_estdocs_fk on estado_documentos (doc_iddocumento asc);
create unique index multa_pk on multa (mult_idmulta asc);
create unique index pago_alicuota_pk on pago_alicuota (pagali_id asc);
create index fk_tes_pagalic_fk on pago_alicuota (tes_idtesorero asc);
create index fk_cond_pagali_fk on pago_alicuota (cond_idcondomino asc);
create unique index persona_pk on persona (pers_persona asc);
create table presidente (
    pres_idpresidente INT NOT NULL IDENTITY(1, 1),
    user_idusuario varchar(25),
    primary key (pres_idpresidente),
    foreign key (user_idusuario) references user_usuario (user_idusuario)
);
create unique index fk_pres_presidente_pk on presidente (pres_idpresidente asc);
create index fk_user_pres_fk on presidente (user_idusuario asc);
create unique index reservaciones_pk on reservaciones (resv_idreservacion asc);
create index fk_serv_reservaciones_fk on reservaciones (serv_idservicios asc);
create table reunion (
    reun_idreunion INT NOT NULL IDENTITY(1, 1),
    pres_idpresidente integer,
    mult_idmulta integer,
    reun_fecha date,
    reun_hora time,
    reun_descripcion varchar(200),
    reun_quorum varchar(200),
    reun_estado smallint,
    primary key (reun_idreunion),
    foreign key (pres_idpresidente) references presidente (pres_idpresidente),
    foreign key (mult_idmulta) references multa (mult_idmulta)
);
create unique index reunion_pk on reunion (reun_idreunion asc);
create index fk_pres_reunion_fk on reunion (pres_idpresidente asc);
create unique index rol_usuario_pk on rol_usuario (rol_idrol asc);
create unique index secretario_pk on secretario (sec_idsecretario asc);
create index relationship_4_fk on secretario (user_idusuario asc);
create unique index servicios_pk on servicios (serv_idservicios asc);
create index fk_tipserv_servicios_fk on servicios (tipserv_id asc);
create unique index tesorero_pk on tesorero (tes_idtesorero asc);
create index fk_user_tesorero_fk on tesorero (user_idusuario asc);
create unique index tipo_documento_pk on tipo_documento (tipdoc_id asc);
create unique index tipo_servicios_pk on tipo_servicios (tipserv_id asc);
create unique index user_usuario_pk on user_usuario (user_idusuario asc);
create index fk_rus_user_fk on user_usuario (rol_idrol asc);
create index fk_per_user_fk on user_usuario (pers_persona asc);
go create view get_usuarios as
select r.rol_idrol,
    r.rol_nombrerol,
    p.pers_persona,
    p.pers_email,
    p.pers_nombres,
    p.pers_apellidos,
    p.pers_telefono,
    p.pers_direccion,
    u.user_idusuario,
    u.user_estado,
    u.user_fecha,
    u.user_password
from user_usuario u,
    rol_usuario r,
    persona p
where u.rol_idrol = r.rol_idrol
    and u.pers_persona = p.pers_persona;
-- 
select *
from multa;
-- Update
update multa
set mult_nombre = 'Retraso a reunion Extraordinarias',
    mult_valor = 17.85
where mult_idmulta = 1;
-- Insert
insert into multa(mult_nombre, mult_valor)
values('Retraso en pago de alicuota mensual', 12.25);
select *
from alicuota;
-- Insert
insert into alicuota(
        mult_idmulta,
        ali_fecha_actualizacion,
        ali_valor_anterior,
        ali_valor_actual
    )
values(1, '02/02/2023', 10, 13);
insert into alicuota(
        mult_idmulta,
        ali_fecha_actualizacion,
        ali_valor_anterior,
        ali_valor_actual
    )
values(2, '02/02/2023', 12, 14);
insert into alicuota(
        mult_idmulta,
        ali_fecha_actualizacion,
        ali_valor_anterior,
        ali_valor_actual
    )
values(1, '02/02/2023', 13, 15);
select *
from alicuota_actualizada;
-- Insert
insert into alicuota_actualizada(alic_idalicuota, alic_valor, alic_fecha)
values(1, 10, '03/02/2023');
insert into alicuota_actualizada(alic_idalicuota, alic_valor, alic_fecha)
values(2, 12, '01/03/2023');
insert into alicuota_actualizada(alic_idalicuota, alic_valor, alic_fecha)
values(3, 13, '02/05/2023');
-- GET (Select)
select ac.alic_id,
    a.ali_idalicuota,
    m.mult_idmulta,
    m.mult_nombre,
    m.mult_valor,
    a.ali_fecha_actualizacion,
    a.ali_valor_anterior,
    a.ali_valor_actual,
    ac.alic_valor,
    ac.alic_fecha
from multa m,
    alicuota a,
    alicuota_actualizada ac
where m.mult_idmulta = a.mult_idmulta
    and a.ali_idalicuota = ac.alic_idalicuota;
-- Create view
create view get_alicuotas as
select ac.alic_id,
    a.ali_idalicuota,
    m.mult_idmulta,
    m.mult_nombre,
    m.mult_valor,
    a.ali_fecha_actualizacion,
    a.ali_valor_anterior,
    a.ali_valor_actual,
    ac.alic_valor,
    ac.alic_fecha
from multa m,
    alicuota a,
    alicuota_actualizada ac
where m.mult_idmulta = a.mult_idmulta
    and a.ali_idalicuota = ac.alic_idalicuota;
-- SELECT
select *
from get_alicuotas;
-- Modify table reunion
alter table reunion
add secretario varchar(25) not null;
alter table reunion
alter column secretario int not null;
ALTER TABLE reunion
ADD CONSTRAINT fk_sec_reu FOREIGN KEY (secretario) REFERENCES secretario (sec_idsecretario) ON DELETE CASCADE ON UPDATE CASCADE;