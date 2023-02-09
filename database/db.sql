create table punto(
    id_punto integer not null identity,
    coord_x integer not null,
    coord_y integer not null,
    constraint pk_punto primary key(id_punto)
);
create table recta(
    id_recta integer not null identity,
    punto_a integer not null,
    punto_b integer not null,
    constraint pk_recta primary key(id_recta),
    constraint fk_punto_recta_a foreign key(punto_a) references punto(id_punto),
    constraint fk_punto_recta_b foreign key(punto_b) references punto(id_punto)
);
create table circunferencia(
    id_circunferencia integer not null identity,
    centro integer not null,
    radio numeric(6, 2) not null,
    constraint pk_circunferencia primary key(id_circunferencia),
    constraint fk_punto_circ foreign key(centro) references punto(id_punto)
);
create table parabola(
    id_parabola integer not null identity,
    vertice integer not null,
    p numeric(6, 2) not null,
    eje_focal varchar(1) not null,
    constraint pk_parabola primary key(id_parabola),
    constraint fk_punto_parab foreign key(vertice) references punto(id_punto)
);
create table elipse(
    id_elipse integer not null identity,
    centro integer not null,
    a numeric(6, 2) not null,
    b numeric(6, 2) not null,
    eje_focal varchar(1) not null,
    constraint pk_elipse primary key(id_elipse),
    constraint fk_punto_elipse foreign key(centro) references punto(id_punto)
);
create table hiperbola(
    id_hiperbola integer not null identity,
    centro integer not null,
    a numeric(6, 2) not null,
    b numeric(6, 2) not null,
    eje_focal varchar(1) not null,
    constraint pk_hiperbola primary key(id_hiperbola),
    constraint fk_punto_hiperbola foreign key(centro) references punto(id_punto)
);
insert into punto(coord_x, coord_y)
values(-1, 3);
insert into punto(coord_x, coord_y)
values(-4, -1);
insert into punto(coord_x, coord_y)
values(0, 0);
insert into punto(coord_x, coord_y)
values(2, 5);
insert into punto(coord_x, coord_y)
values(2, -3);
insert into recta(punto_a, punto_b)
values(1, 4);
insert into recta(punto_a, punto_b)
values(2, 3);
insert into recta(punto_a, punto_b)
values(3, 4);
insert into recta(punto_a, punto_b)
values(5, 2);
insert into recta(punto_a, punto_b)
values(4, 5);
insert into parabola(vertice, p, eje_focal)
values(2, -3, 'x');
insert into parabola(vertice, p, eje_focal)
values(1, 4, 'y');
insert into parabola(vertice, p, eje_focal)
values(3, -5, 'y');
insert into parabola(vertice, p, eje_focal)
values(5, 6, 'x');
insert into circunferencia(centro, radio)
values(2, 3);
insert into circunferencia(centro, radio)
values(1, 4);
insert into circunferencia(centro, radio)
values(3, 5);
insert into circunferencia(centro, radio)
values(5, 6);
insert into elipse(centro, a, b, eje_focal)
values(1, 4, 3, 'x');
insert into elipse(centro, a, b, eje_focal)
values(2, 5, 4, 'y');
insert into elipse(centro, a, b, eje_focal)
values(3, 6, 4, 'y');
insert into elipse(centro, a, b, eje_focal)
values(4, 7, 5, 'x');
insert into elipse(centro, a, b, eje_focal)
values(3, 8, 6, 'x');
insert into hiperbola(centro, a, b, eje_focal)
values(1, 4, 3, 'y');
insert into hiperbola(centro, a, b, eje_focal)
values(2, 3, 5, 'x');
insert into hiperbola(centro, a, b, eje_focal)
values(3, 3, 4, 'x');
insert into hiperbola(centro, a, b, eje_focal)
values(4, 5, 4, 'y');
insert into hiperbola(centro, a, b, eje_focal)
values(3, 3, 6, 'y');
declare @points nvarchar(max)
set @points = (
        select p.id_punto,
            p.coord_x,
            p.coord_y
        from punto p
        where p.id_punto = 1 for json path
    )
select @points as points return
declare @lines nvarchar(max)
set @lines = (
        select r.id_recta as 'recta.id_recta',
            pa.id_punto as 'punto_a.id_punto',
            pa.coord_x as 'punto_a.coord_x',
            pa.coord_y as 'punto_a.coord_y',
            pb.id_punto 'punto_b.id_punto',
            pb.coord_x as 'punto_b.coord_x',
            pb.coord_y as 'punto_b.coord_y'
        from punto pa,
            recta r,
            punto pb
        where r.punto_a = pa.id_punto
            and r.punto_b = pb.id_punto for json path
    )
select @lines as lines return
declare @circunferences nvarchar(max)
set @circunferences = (
        select c.id_circunferencia as 'circunferencia.id_circunferencia',
            p.id_punto as 'centro.id_punto',
            p.coord_x as 'centro.coord_x',
            p.coord_y as 'centro.coord_y'
        from circunferencia c
            inner join punto p on c.centro = p.id_punto for json path
    )
select @circunferences as circunferences return
declare @elipses nvarchar(max)
set @elipses = (
        select e.id_elipse as 'elipse.id_elipse',
            e.a as 'elipse.a',
            e.b as 'elipse.b',
            e.eje_focal as 'elipse.eje_focal',
            p.id_punto as 'centro.id_punto',
            p.coord_x as 'centro.coord_x',
            p.coord_y as 'centro.coord_y'
        from elipse e
            inner join punto p on e.centro = p.id_punto for json path
    )
select @elipses as elipses return
declare @hiperbolas nvarchar(max)
set @hiperbolas = (
        select h.id_hiperbola as 'hiperbola.id_hiperbola',
            h.a as 'hiperbola.a',
            h.b as 'hiperbola.b',
            h.eje_focal as 'hiperbola.eje_focal',
            p.id_punto as 'centro.id_punto',
            p.coord_x as 'centro.coord_x',
            p.coord_y as 'centro.coord_y'
        from hiperbola h
            inner join punto p on h.centro = p.id_punto for json path
    )
select @hiperbolas as hiperbolas return
declare @parabolas nvarchar(max)
set @parabolas = (
        select p.id_parabola as 'parabola.id_parabola',
            p.p as 'parabola.p',
            p.eje_focal as 'parabola.eje_focal',
            v.id_punto as 'vertice.id_punto',
            v.coord_x as 'vertice.coord_x',
            v.coord_y as 'vertice.coord_y'
        from parabola p
            inner join punto v on p.vertice = v.id_punto for json path
    )
select @parabolas as parabolas return
select p.id_punto,
    p.coord_x,
    p.coord_y
from punto p
where p.id_punto = 40 for json path;
select r.id_recta as 'recta.id_recta',
    pa.id_punto as 'punto_a.id_punto',
    pa.coord_x as 'punto_a.coord_x',
    pa.coord_y as 'punto_a.coord_y',
    pb.id_punto 'punto_b.id_punto',
    pb.coord_x as 'punto_b.coord_x',
    pb.coord_y as 'punto_b.coord_y'
from punto pa,
    recta r,
    punto pb
where r.punto_a = pa.id_punto
    and r.punto_b = pb.id_punto
    and r.id_recta = 1 for json path;
select c.id_circunferencia as 'circunferencia.id_circunferencia',
    p.id_punto as 'centro.id_punto',
    p.coord_x as 'centro.coord_x',
    p.coord_y as 'centro.coord_y'
from circunferencia c
    inner join punto p on c.centro = p.id_punto
    and c.id_circunferencia = 1 for json path;
select e.id_elipse as 'elipse.id_elipse',
    e.a as 'elipse.a',
    e.b as 'elipse.b',
    e.eje_focal as 'elipse.eje_focal',
    p.id_punto as 'centro.id_punto',
    p.coord_x as 'centro.coord_x',
    p.coord_y as 'centro.coord_y'
from elipse e
    inner join punto p on e.centro = p.id_punto
    and e.id_elipse = 1 for json path;
select h.id_hiperbola as 'hiperbola.id_hiperbola',
    h.a as 'hiperbola.a',
    h.b as 'hiperbola.b',
    h.eje_focal as 'hiperbola.eje_focal',
    p.id_punto as 'centro.id_punto',
    p.coord_x as 'centro.coord_x',
    p.coord_y as 'centro.coord_y'
from hiperbola h
    inner join punto p on h.centro = p.id_punto
    and h.id_hiperbola = 1 for json path;
select p.id_parabola as 'parabola.id_parabola',
    p.p as 'parabola.p',
    p.eje_focal as 'parabola.eje_focal',
    v.id_punto as 'vertice.id_punto',
    v.coord_x as 'vertice.coord_x',
    v.coord_y as 'vertice.coord_y'
from parabola p
    inner join punto v on p.vertice = v.id_punto
    and p.id_parabola = 1 for json path;
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (23, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (11, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (23, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (8, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (7, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (24, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (1, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (19, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (5, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (7, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (25, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (3, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (21, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (9, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (17, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (11, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (21, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (24, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (9, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (17, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (3, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (1, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (1, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (20, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (7, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (15, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (21, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (6, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (19, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (5, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (5, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (21, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (25, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (9, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (11, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (25, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (12, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (19, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (17, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (25, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (23, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (4, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (17, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (14, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (13, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (23, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (19, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (16, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (9, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (24, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (5, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (24, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (17, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (18, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (10, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (20, 20.0, 'x');
insert into parabola (vertice, p, eje_focal)
values (2, 20.0, 'y');
insert into parabola (vertice, p, eje_focal)
values (20, 20.0, 'y');
insert into recta (punto_a, punto_b)
values (20, 20);
insert into recta (punto_a, punto_b)
values (18, 20);
insert into recta (punto_a, punto_b)
values (23, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (3, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (6, 20);
insert into recta (punto_a, punto_b)
values (8, 20);
insert into recta (punto_a, punto_b)
values (11, 20);
insert into recta (punto_a, punto_b)
values (21, 20);
insert into recta (punto_a, punto_b)
values (10, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (16, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (19, 20);
insert into recta (punto_a, punto_b)
values (20, 20);
insert into recta (punto_a, punto_b)
values (8, 20);
insert into recta (punto_a, punto_b)
values (23, 20);
insert into recta (punto_a, punto_b)
values (7, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (25, 20);
insert into recta (punto_a, punto_b)
values (18, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (9, 20);
insert into recta (punto_a, punto_b)
values (24, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (7, 20);
insert into recta (punto_a, punto_b)
values (25, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (24, 20);
insert into recta (punto_a, punto_b)
values (21, 20);
insert into recta (punto_a, punto_b)
values (3, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (9, 20);
insert into recta (punto_a, punto_b)
values (9, 20);
insert into recta (punto_a, punto_b)
values (1, 20);
insert into recta (punto_a, punto_b)
values (17, 20);
insert into recta (punto_a, punto_b)
values (3, 20);
insert into recta (punto_a, punto_b)
values (11, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (9, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (21, 20);
insert into recta (punto_a, punto_b)
values (10, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (7, 20);
insert into recta (punto_a, punto_b)
values (23, 20);
insert into recta (punto_a, punto_b)
values (11, 20);
insert into recta (punto_a, punto_b)
values (3, 20);
insert into recta (punto_a, punto_b)
values (1, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (1, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (6, 20);
insert into recta (punto_a, punto_b)
values (16, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (16, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (1, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (20, 20);
insert into recta (punto_a, punto_b)
values (22, 20);
insert into recta (punto_a, punto_b)
values (5, 20);
insert into recta (punto_a, punto_b)
values (17, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (11, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (19, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (14, 20);
insert into recta (punto_a, punto_b)
values (3, 20);
insert into recta (punto_a, punto_b)
values (25, 20);
insert into recta (punto_a, punto_b)
values (21, 20);
insert into recta (punto_a, punto_b)
values (1, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (20, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (23, 20);
insert into recta (punto_a, punto_b)
values (15, 20);
insert into recta (punto_a, punto_b)
values (12, 20);
insert into recta (punto_a, punto_b)
values (4, 20);
insert into recta (punto_a, punto_b)
values (13, 20);
insert into circunferencia (centro, radio)
values (9, 18.65);
insert into circunferencia (centro, radio)
values (9, 3.54);
insert into circunferencia (centro, radio)
values (5, 9.69);
insert into circunferencia (centro, radio)
values (1, 6.56);
insert into circunferencia (centro, radio)
values (7, 3.01);
insert into circunferencia (centro, radio)
values (15, 14.05);
insert into circunferencia (centro, radio)
values (8, 0.24);
insert into circunferencia (centro, radio)
values (13, 14.36);
insert into circunferencia (centro, radio)
values (14, 11.56);
insert into circunferencia (centro, radio)
values (2, 9.09);
insert into circunferencia (centro, radio)
values (22, 11.77);
insert into circunferencia (centro, radio)
values (9, 15.98);
insert into circunferencia (centro, radio)
values (1, 7.81);
insert into circunferencia (centro, radio)
values (11, 6.25);
insert into circunferencia (centro, radio)
values (8, 4.03);
insert into circunferencia (centro, radio)
values (23, 17.04);
insert into circunferencia (centro, radio)
values (3, 1.77);
insert into circunferencia (centro, radio)
values (21, 12.26);
insert into circunferencia (centro, radio)
values (23, 11.84);
insert into circunferencia (centro, radio)
values (25, 3.35);
insert into circunferencia (centro, radio)
values (17, 19.52);
insert into circunferencia (centro, radio)
values (1, 3.37);
insert into circunferencia (centro, radio)
values (19, 11.99);
insert into circunferencia (centro, radio)
values (1, 12.12);
insert into circunferencia (centro, radio)
values (19, 7.07);
insert into circunferencia (centro, radio)
values (24, 19.39);
insert into circunferencia (centro, radio)
values (14, 11.77);
insert into circunferencia (centro, radio)
values (18, 1.1);
insert into circunferencia (centro, radio)
values (11, 14.79);
insert into circunferencia (centro, radio)
values (15, 4.05);
insert into circunferencia (centro, radio)
values (9, 18.94);
insert into circunferencia (centro, radio)
values (15, 7.24);
insert into circunferencia (centro, radio)
values (11, 14.43);
insert into circunferencia (centro, radio)
values (9, 0.13);
insert into circunferencia (centro, radio)
values (8, 17.63);
insert into circunferencia (centro, radio)
values (24, 4.92);
insert into circunferencia (centro, radio)
values (8, 5.38);
insert into circunferencia (centro, radio)
values (24, 14.37);
insert into circunferencia (centro, radio)
values (4, 13.62);
insert into circunferencia (centro, radio)
values (13, 11.28);
insert into circunferencia (centro, radio)
values (23, 8.59);
insert into circunferencia (centro, radio)
values (12, 5.56);
insert into circunferencia (centro, radio)
values (18, 3.47);
insert into circunferencia (centro, radio)
values (13, 16.14);
insert into circunferencia (centro, radio)
values (18, 12.91);
insert into circunferencia (centro, radio)
values (24, 12.71);
insert into circunferencia (centro, radio)
values (18, 15.67);
insert into circunferencia (centro, radio)
values (2, 5.51);
insert into circunferencia (centro, radio)
values (8, 14.06);
insert into circunferencia (centro, radio)
values (19, 17.92);
insert into circunferencia (centro, radio)
values (9, 19.0);
insert into circunferencia (centro, radio)
values (12, 9.01);
insert into circunferencia (centro, radio)
values (25, 19.41);
insert into circunferencia (centro, radio)
values (4, 18.63);
insert into circunferencia (centro, radio)
values (7, 9.21);
insert into circunferencia (centro, radio)
values (18, 17.49);
insert into circunferencia (centro, radio)
values (16, 14.65);
insert into circunferencia (centro, radio)
values (15, 11.05);
insert into circunferencia (centro, radio)
values (20, 11.86);
insert into circunferencia (centro, radio)
values (12, 11.58);
insert into circunferencia (centro, radio)
values (23, 3.59);
insert into circunferencia (centro, radio)
values (22, 15.77);
insert into circunferencia (centro, radio)
values (23, 13.69);
insert into circunferencia (centro, radio)
values (1, 2.83);
insert into circunferencia (centro, radio)
values (12, 14.27);
insert into circunferencia (centro, radio)
values (25, 4.87);
insert into circunferencia (centro, radio)
values (1, 11.26);
insert into circunferencia (centro, radio)
values (25, 9.92);
insert into circunferencia (centro, radio)
values (21, 11.38);
insert into circunferencia (centro, radio)
values (1, 3.59);
insert into circunferencia (centro, radio)
values (24, 19.84);
insert into circunferencia (centro, radio)
values (6, 15.46);
insert into circunferencia (centro, radio)
values (3, 4.04);
insert into circunferencia (centro, radio)
values (17, 6.24);
insert into circunferencia (centro, radio)
values (12, 14.0);
insert into circunferencia (centro, radio)
values (4, 17.14);
insert into circunferencia (centro, radio)
values (16, 10.31);
insert into circunferencia (centro, radio)
values (12, 11.19);
insert into circunferencia (centro, radio)
values (2, 5.21);
insert into circunferencia (centro, radio)
values (16, 18.31);
insert into circunferencia (centro, radio)
values (9, 3.89);
insert into circunferencia (centro, radio)
values (13, 8.58);
insert into circunferencia (centro, radio)
values (23, 16.58);
insert into circunferencia (centro, radio)
values (2, 7.72);
insert into circunferencia (centro, radio)
values (24, 16.98);
insert into circunferencia (centro, radio)
values (15, 12.72);
insert into circunferencia (centro, radio)
values (1, 18.47);
insert into circunferencia (centro, radio)
values (25, 19.56);
insert into circunferencia (centro, radio)
values (12, 4.59);
insert into circunferencia (centro, radio)
values (6, 7.17);
insert into circunferencia (centro, radio)
values (11, 10.46);
insert into circunferencia (centro, radio)
values (23, 3.03);
insert into circunferencia (centro, radio)
values (2, 15.12);
insert into circunferencia (centro, radio)
values (17, 5.77);
insert into circunferencia (centro, radio)
values (14, 10.8);
insert into circunferencia (centro, radio)
values (14, 7.79);
insert into circunferencia (centro, radio)
values (18, 16.27);
insert into circunferencia (centro, radio)
values (6, 4.92);
insert into circunferencia (centro, radio)
values (8, 8.18);
insert into circunferencia (centro, radio)
values (19, 15.9);
insert into elipse (centro, a, b, eje_focal)
values (8, 22.93, 15.94, 'x');
insert into elipse (centro, a, b, eje_focal)
values (2, 24.18, 18.23, 'x');
insert into elipse (centro, a, b, eje_focal)
values (5, 24.47, 15.35, 'y');
insert into elipse (centro, a, b, eje_focal)
values (4, 21.93, 15.34, 'x');
insert into elipse (centro, a, b, eje_focal)
values (5, 23.58, 15.57, 'y');
insert into elipse (centro, a, b, eje_focal)
values (11, 23.14, 17.77, 'y');
insert into elipse (centro, a, b, eje_focal)
values (1, 22.68, 17.44, 'x');
insert into elipse (centro, a, b, eje_focal)
values (13, 24.28, 15.42, 'x');
insert into elipse (centro, a, b, eje_focal)
values (16, 23.41, 17.03, 'y');
insert into elipse (centro, a, b, eje_focal)
values (11, 23.73, 18.19, 'x');
insert into elipse (centro, a, b, eje_focal)
values (17, 22.46, 19.89, 'y');
insert into elipse (centro, a, b, eje_focal)
values (1, 21.29, 15.95, 'y');
insert into elipse (centro, a, b, eje_focal)
values (17, 22.89, 15.94, 'y');
insert into elipse (centro, a, b, eje_focal)
values (5, 24.66, 18.13, 'y');
insert into elipse (centro, a, b, eje_focal)
values (20, 24.57, 18.05, 'x');
insert into elipse (centro, a, b, eje_focal)
values (25, 24.89, 19.44, 'x');
insert into elipse (centro, a, b, eje_focal)
values (4, 22.25, 16.58, 'y');
insert into elipse (centro, a, b, eje_focal)
values (12, 24.48, 18.48, 'y');
insert into elipse (centro, a, b, eje_focal)
values (10, 23.64, 16.92, 'y');
insert into elipse (centro, a, b, eje_focal)
values (13, 23.06, 19.33, 'y');
insert into elipse (centro, a, b, eje_focal)
values (4, 22.59, 17.77, 'x');
insert into elipse (centro, a, b, eje_focal)
values (13, 21.6, 16.46, 'x');
insert into elipse (centro, a, b, eje_focal)
values (13, 21.83, 17.81, 'x');
insert into elipse (centro, a, b, eje_focal)
values (7, 24.34, 16.9, 'y');
insert into elipse (centro, a, b, eje_focal)
values (24, 21.3, 18.68, 'y');
insert into elipse (centro, a, b, eje_focal)
values (16, 23.61, 15.33, 'x');
insert into elipse (centro, a, b, eje_focal)
values (8, 21.78, 18.0, 'y');
insert into elipse (centro, a, b, eje_focal)
values (23, 23.06, 18.37, 'y');
insert into elipse (centro, a, b, eje_focal)
values (20, 23.27, 19.5, 'x');
insert into elipse (centro, a, b, eje_focal)
values (13, 24.6, 15.72, 'y');
insert into elipse (centro, a, b, eje_focal)
values (25, 24.52, 18.22, 'x');
insert into elipse (centro, a, b, eje_focal)
values (4, 21.01, 15.84, 'y');
insert into elipse (centro, a, b, eje_focal)
values (8, 23.76, 19.15, 'x');
insert into elipse (centro, a, b, eje_focal)
values (14, 24.18, 16.17, 'y');
insert into elipse (centro, a, b, eje_focal)
values (20, 23.6, 17.08, 'x');
insert into elipse (centro, a, b, eje_focal)
values (20, 22.12, 17.9, 'x');
insert into elipse (centro, a, b, eje_focal)
values (12, 22.34, 17.29, 'x');
insert into elipse (centro, a, b, eje_focal)
values (3, 23.36, 16.08, 'x');
insert into elipse (centro, a, b, eje_focal)
values (16, 23.91, 19.03, 'x');
insert into elipse (centro, a, b, eje_focal)
values (20, 24.29, 15.61, 'x');
insert into elipse (centro, a, b, eje_focal)
values (18, 23.15, 17.81, 'y');
insert into elipse (centro, a, b, eje_focal)
values (16, 23.88, 19.84, 'x');
insert into elipse (centro, a, b, eje_focal)
values (12, 23.91, 17.42, 'x');
insert into elipse (centro, a, b, eje_focal)
values (9, 22.75, 19.26, 'x');
insert into elipse (centro, a, b, eje_focal)
values (22, 23.77, 18.39, 'y');
insert into elipse (centro, a, b, eje_focal)
values (7, 24.61, 18.73, 'x');
insert into elipse (centro, a, b, eje_focal)
values (7, 24.47, 19.01, 'x');
insert into elipse (centro, a, b, eje_focal)
values (22, 22.77, 15.19, 'y');
insert into elipse (centro, a, b, eje_focal)
values (20, 23.95, 15.11, 'x');
insert into elipse (centro, a, b, eje_focal)
values (9, 22.42, 18.58, 'y');
insert into elipse (centro, a, b, eje_focal)
values (12, 21.9, 16.52, 'x');
insert into elipse (centro, a, b, eje_focal)
values (22, 23.19, 19.75, 'y');
insert into elipse (centro, a, b, eje_focal)
values (4, 24.23, 18.71, 'y');
insert into elipse (centro, a, b, eje_focal)
values (3, 23.61, 19.24, 'x');
insert into elipse (centro, a, b, eje_focal)
values (25, 21.54, 17.08, 'x');
insert into elipse (centro, a, b, eje_focal)
values (21, 23.56, 17.02, 'y');
insert into elipse (centro, a, b, eje_focal)
values (24, 23.06, 19.04, 'x');
insert into elipse (centro, a, b, eje_focal)
values (7, 23.0, 15.3, 'y');
insert into elipse (centro, a, b, eje_focal)
values (2, 22.55, 17.5, 'x');
insert into elipse (centro, a, b, eje_focal)
values (24, 24.25, 18.9, 'y');
insert into elipse (centro, a, b, eje_focal)
values (23, 24.06, 16.34, 'x');
insert into elipse (centro, a, b, eje_focal)
values (2, 23.77, 18.29, 'x');
insert into elipse (centro, a, b, eje_focal)
values (11, 22.86, 18.17, 'x');
insert into elipse (centro, a, b, eje_focal)
values (3, 21.52, 16.49, 'y');
insert into elipse (centro, a, b, eje_focal)
values (23, 24.91, 16.92, 'x');
insert into elipse (centro, a, b, eje_focal)
values (1, 23.16, 16.89, 'y');
insert into elipse (centro, a, b, eje_focal)
values (9, 24.07, 19.01, 'y');
insert into elipse (centro, a, b, eje_focal)
values (4, 24.27, 17.41, 'y');
insert into elipse (centro, a, b, eje_focal)
values (25, 22.01, 17.36, 'y');
insert into elipse (centro, a, b, eje_focal)
values (2, 23.4, 17.66, 'y');
insert into elipse (centro, a, b, eje_focal)
values (3, 21.07, 16.55, 'x');
insert into elipse (centro, a, b, eje_focal)
values (15, 23.6, 15.76, 'x');
insert into elipse (centro, a, b, eje_focal)
values (6, 21.75, 15.2, 'x');
insert into elipse (centro, a, b, eje_focal)
values (12, 21.47, 16.26, 'x');
insert into elipse (centro, a, b, eje_focal)
values (1, 22.51, 16.24, 'y');
insert into elipse (centro, a, b, eje_focal)
values (8, 21.93, 18.49, 'x');
insert into elipse (centro, a, b, eje_focal)
values (7, 24.3, 18.21, 'y');
insert into elipse (centro, a, b, eje_focal)
values (16, 21.07, 17.78, 'x');
insert into elipse (centro, a, b, eje_focal)
values (21, 21.06, 18.03, 'y');
insert into elipse (centro, a, b, eje_focal)
values (3, 23.41, 17.86, 'x');
insert into elipse (centro, a, b, eje_focal)
values (16, 24.24, 15.89, 'x');
insert into elipse (centro, a, b, eje_focal)
values (19, 23.31, 17.37, 'x');
insert into elipse (centro, a, b, eje_focal)
values (2, 23.76, 19.93, 'x');
insert into elipse (centro, a, b, eje_focal)
values (20, 22.94, 15.74, 'x');
insert into elipse (centro, a, b, eje_focal)
values (23, 21.94, 15.8, 'y');
insert into elipse (centro, a, b, eje_focal)
values (25, 21.97, 18.51, 'x');
insert into elipse (centro, a, b, eje_focal)
values (8, 22.09, 20.0, 'y');
insert into elipse (centro, a, b, eje_focal)
values (23, 22.26, 15.99, 'x');
insert into elipse (centro, a, b, eje_focal)
values (24, 23.09, 17.88, 'x');
insert into elipse (centro, a, b, eje_focal)
values (13, 21.79, 19.37, 'x');
insert into elipse (centro, a, b, eje_focal)
values (5, 23.54, 19.05, 'x');
insert into elipse (centro, a, b, eje_focal)
values (21, 22.39, 19.44, 'x');
insert into elipse (centro, a, b, eje_focal)
values (3, 24.67, 19.13, 'y');
insert into elipse (centro, a, b, eje_focal)
values (20, 22.51, 18.77, 'x');
insert into elipse (centro, a, b, eje_focal)
values (12, 24.12, 19.7, 'y');
insert into elipse (centro, a, b, eje_focal)
values (18, 24.47, 17.66, 'x');
insert into elipse (centro, a, b, eje_focal)
values (1, 22.7, 15.3, 'y');
insert into elipse (centro, a, b, eje_focal)
values (18, 21.81, 18.23, 'x');
insert into elipse (centro, a, b, eje_focal)
values (4, 22.42, 16.18, 'y');
insert into elipse (centro, a, b, eje_focal)
values (17, 22.32, 15.09, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (6, 21.42, 16.54, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (22, 23.23, 18.35, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (19, 21.71, 19.78, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (16, 22.25, 15.76, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (7, 23.58, 17.3, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (24, 22.66, 16.93, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 21.25, 15.21, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (8, 24.73, 18.66, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 21.56, 18.73, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (3, 21.7, 18.11, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 24.7, 15.78, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (13, 21.55, 18.84, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (10, 23.85, 16.98, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (18, 21.27, 17.66, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (7, 22.15, 18.72, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 21.18, 16.66, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 22.5, 16.63, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 24.02, 15.28, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (18, 22.68, 18.04, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 22.04, 18.06, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (14, 24.6, 17.81, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 24.68, 16.01, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 22.34, 16.1, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 22.07, 16.62, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (13, 23.4, 16.41, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 23.15, 15.01, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 21.53, 18.65, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (20, 22.98, 18.87, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 21.8, 17.29, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (19, 21.87, 17.9, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (8, 24.39, 19.42, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (18, 21.81, 16.4, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (17, 22.06, 18.62, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 23.23, 19.98, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (8, 22.17, 19.63, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 22.59, 15.19, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (8, 24.34, 16.44, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (21, 24.13, 18.78, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 21.79, 16.3, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 22.28, 18.73, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (24, 22.06, 16.39, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 22.26, 19.59, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (20, 24.48, 17.31, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (7, 23.34, 15.86, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 24.69, 16.09, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (25, 23.67, 19.39, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 24.1, 15.76, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (18, 21.09, 20.0, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (18, 21.15, 17.68, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (10, 23.21, 16.88, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (12, 24.95, 17.12, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 21.0, 15.82, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (21, 23.34, 17.85, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 21.81, 16.98, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 21.27, 15.0, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (24, 22.2, 19.5, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (13, 22.79, 16.57, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (25, 24.18, 17.2, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (17, 22.11, 17.9, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (5, 23.86, 15.49, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 24.07, 17.53, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 23.51, 15.67, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (17, 24.69, 19.23, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (23, 23.05, 18.43, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (21, 24.92, 16.06, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (7, 22.64, 18.49, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (6, 21.83, 19.66, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 24.54, 16.0, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (16, 22.47, 16.9, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (20, 23.81, 15.6, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 24.97, 15.88, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (14, 22.98, 17.6, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (4, 21.42, 15.85, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (20, 22.27, 19.94, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (23, 22.3, 18.5, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 22.74, 16.49, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 23.52, 17.56, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (5, 23.9, 19.2, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (3, 23.21, 17.95, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (17, 21.58, 16.09, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (22, 23.22, 18.64, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (12, 24.07, 19.41, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 24.56, 17.07, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (12, 23.6, 19.72, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (15, 23.99, 15.61, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (23, 22.06, 18.13, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (5, 21.18, 17.38, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (6, 21.76, 18.94, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (13, 21.03, 17.92, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 21.74, 15.55, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (9, 23.86, 18.54, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (13, 21.21, 19.16, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (11, 24.24, 18.43, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 22.69, 17.3, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (22, 24.23, 19.9, 'x');
insert into hiperbola (centro, a, b, eje_focal)
values (20, 24.24, 17.51, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (1, 24.23, 19.62, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (21, 24.35, 19.42, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (2, 23.89, 15.08, 'y');
insert into hiperbola (centro, a, b, eje_focal)
values (19, 21.09, 15.37, 'y');