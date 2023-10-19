DROP table IF EXISTS timetable;
DROP table IF EXISTS teacher;
DROP table IF EXISTS subject;


 CREATE TABLE subject(
    id bigserial not null,
    name varchar(100) not null,
    primary key (id)
);

CREATE TABLE  teacher(
    id bigserial not null,
    full_name varchar(40) not null,
    fk_id_subject integer not null,
    primary key (id),
    FOREIGN key (fk_id_subject) references subject (id)
);

CREATE TABLE timetable(
    id integer not null,
    day text not null,
    fk_id_teacher integer not null,
    view text not null,
    room text not null,
    start_time text not null,
    primary key (id),
    foreign key (fk_id_teacher) references teacher (id)
);

insert into subject values(1, '<Нет пары>');
insert into subject values(2, 'Игровые виды спорта');
insert into subject values(3, 'Основы DevOps');
insert into subject values(4, 'Проектный практикум');
insert into subject values(5, 'Высшая математика');
insert into subject values(6, 'Физика');
insert into subject values(7, 'История');
insert into subject values(8, 'Математические основы баз данных');
insert into subject values(9, 'Иностранный язык');
insert into subject values(10, 'Введение в информационные технологии');

insert into teacher values(1, '', 1);
insert into teacher values(2, 'Волохова С.В.', 2);
insert into teacher values(3, 'Липатов В.Н.', 3);
insert into teacher values(4, 'Потапченко Т.Д.', 4);
insert into teacher values(5, 'Воронова Е.В.', 9);
insert into teacher values(6, 'Шаймарданова Л.К.', 5);
insert into teacher values(7, 'Вальковский С.Н.', 6);
insert into teacher values(8, 'Скляр Л.Н.', 7);
insert into teacher values(9, 'Городничев М.Г', 3);
insert into teacher values(10, 'Фурлетов Ю.М.', 10);
insert into teacher values(11, 'Полищук Ю.В.', 8);
insert into teacher values(12, 'Тимошина М.И.', 6);
insert into teacher values(13, 'Изотова А.А.', 8);
insert into teacher values(14, 'Дегтярев В.Ф.', 6);

insert into timetable values(1, 'Понедельник', 1, '', '', '09:30-11:05');
insert into timetable values(2, 'Понедельник', 1, '', '', '11:20-12:55');
insert into timetable values(3, 'Понедельник', 10, 'Лаб. занятие', 'в А-Л-203', '13:10-14:45');
insert into timetable values(4, 'Понедельник', 2, 'Практика', 'в А-С/Зал', '15:25-17:00');
insert into timetable values(5, 'Понедельник', 1, '', '', '17:15-18:50');
insert into timetable values(6, 'Вторник', 1, '', '', '09:30-11:05');
insert into timetable values(7, 'Вторник', 10, 'Практика', 'в А-Л-206', '11:20-12:55');
insert into timetable values(8, 'Вторник', 3, 'Лаб. занятие', 'в А-ВЦ-302', '13:10-14:45');
insert into timetable values(9, 'Вторник', 4, 'Практика', 'в А-Л-205', '15:25-17:00');
insert into timetable values(10, 'Вторник', 2, 'Практика', 'в А-С/Зал', '17:15-18:50');
insert into timetable values(11, 'Среда', 5, 'Практика', 'в Н-314', '09:30-11:05');
insert into timetable values(12, 'Среда', 6, 'Практика', 'в Н-301', '11:20-12:55');
insert into timetable values(13, 'Среда', 6, 'Лекция', 'в Н-514', '13:10-14:45');
insert into timetable values(14, 'Среда', 7, 'Лекция', 'в Н-226', '15:25-17:00');
insert into timetable values(15, 'Среда', 1, '', '', '17:15-18:50');
insert into timetable values(16, 'Четверг', 1, '', '', '09:30-11:05');
insert into timetable values(17, 'Четверг', 1, '', '', '11:20-12:55');
insert into timetable values(18, 'Четверг', 1, '', '', '13:10-14:45');
insert into timetable values(19, 'Четверг', 1, '', '', '15:25-17:00');
insert into timetable values(20, 'Четверг', 1, '', '', '17:15-18:50');
insert into timetable values(21, 'Пятница', 8, 'Лекция', 'в Н-227', '09:30-11:05');
insert into timetable values(22, 'Пятница', 11, 'Лекция', 'в Н-535', '11:20-12:55');
insert into timetable values(23, 'Пятница', 12, 'Лаб. занятие', 'в Н-340', '13:10-14:45');
insert into timetable values(24, 'Пятница', 8, 'Практика', 'в Н-318', '15:25-17:00');
insert into timetable values(25, 'Пятница', 13, 'Лаб. занятие', 'в Н-131', '17:15-18:50');
insert into timetable values(26, 'Суббота', 1, '', '', '09:30-11:05');
insert into timetable values(27, 'Суббота', 1, '', '', '11:20-12:55');
insert into timetable values(28, 'Суббота', 1, '', '', '13:10-14:45');
insert into timetable values(29, 'Суббота', 1, '', '', '15:25-17:00');
insert into timetable values(30, 'Суббота', 1, '', '', '17:15-18:50');
insert into timetable values(31, 'Понедельник', 1, '', '', '09:30-11:05');
insert into timetable values(32, 'Понедельник', 6, 'Лекция', 'в Н-514', '11:20-12:55');
insert into timetable values(33, 'Понедельник', 5, 'Практика', 'в Н-324', '13:10-14:45');
insert into timetable values(34, 'Понедельник', 8, 'Практика', 'в Н-318', '15:25-17:00');
insert into timetable values(35, 'Понедельник', 6, 'Практика', 'в Н-301', '17:15-18:50');
insert into timetable values(36, 'Вторник', 1, '', '', '09:30-11:05');
insert into timetable values(37, 'Вторник', 1, '', '', '11:20-12:55');
insert into timetable values(38, 'Вторник', 1, '', '', '13:10-14:45');
insert into timetable values(39, 'Вторник', 1, '', '', '15:25-17:00');
insert into timetable values(40, 'Вторник', 1, '', '', '17:15-18:50');
insert into timetable values(41, 'Среда', 1, '', '', '09:30-11:05');
insert into timetable values(42, 'Среда', 2, 'Практика', 'в А-С/Зал', '11:20-12:55');
insert into timetable values(43, 'Среда', 9, 'Лекция', 'в А-414', '13:10-14:45');
insert into timetable values(44, 'Среда', 1, '', '', '15:25-17:00');
insert into timetable values(45, 'Среда', 1, '', '', '17:15-18:50');
insert into timetable values(46, 'Четверг', 1, '', '', '09:30-11:05');
insert into timetable values(47, 'Четверг', 14, 'Практика', 'в Н-332б', '11:20-12:55');
insert into timetable values(48, 'Четверг', 11, 'Практика', 'в Н-404', '13:10-14:45');
insert into timetable values(49, 'Четверг', 1, '', '', '15:25-17:00');
insert into timetable values(50, 'Четверг', 1, '', '', '17:15-18:50');
insert into timetable values(51, 'Пятница', 3, 'Лаб. занятие', 'в А-ВЦ-302', '09:30-11:05');
insert into timetable values(52, 'Пятница', 10, 'Лаб. занятие', 'в А-Л-207', '11:20-12:55');
insert into timetable values(53, 'Пятница', 2, 'Практика', 'в А-С/Зал', '13:10-14:45');
insert into timetable values(54, 'Пятница', 1, '', '', '15:25-17:00');
insert into timetable values(55, 'Пятница', 1, '', '', '17:15-18:50');
insert into timetable values(56, 'Суббота', 1, '', '', '09:30-11:05');
insert into timetable values(57, 'Суббота', 1, '', '', '11:20-12:55');
insert into timetable values(58, 'Суббота', 1, '', '', '13:10-14:45');
insert into timetable values(59, 'Суббота', 1, '', '', '15:25-17:00');
insert into timetable values(60, 'Суббота', 1, '', '', '17:15-18:50');




CREATE OR REPLACE FUNCTION delete_subject()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM timetable WHERE fk_id_teacher IN (SELECT id FROM teacher WHERE fk_id_subject = OLD.id);
    DELETE FROM teacher WHERE fk_id_subject = OLD.id;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_delete_subject
BEFORE DELETE ON subject
FOR EACH ROW EXECUTE FUNCTION delete_subject();




CREATE OR REPLACE FUNCTION delete_timetable()
RETURNS TRIGGER AS $$
BEGIN
    DELETE FROM timetable WHERE fk_id_teacher = OLD.id;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_delete_timetable
BEFORE DELETE ON teacher
FOR EACH ROW EXECUTE FUNCTION delete_timetable();



