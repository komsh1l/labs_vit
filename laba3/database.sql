create table main(
    id integer not null,
    kafedra varchar not null,
    dekanat varchar not null,
    primary key (id)
);

create table student_group(
    id integer not null,
    name_group varchar not null,
    id_main bigint not null,
    primary key (id),
    foreign key (id_main) references main(id)
);

create table student(
    id serial primary key not null,
    name varchar not null,
    passport varchar(10) not null,
    id_student_group bigint references student_group(id) not null
);

insert into main values(1, 'прикладной искусственный интелект', 'ИТ');
insert into main values(2, 'системное программирование', 'ИТ');

insert into student_group values(1, 'БПИ2201', 1);
insert into student_group values(2, 'БПИ2202', 1);
insert into student_group values(3, 'БСП2205', 2);
insert into student_group values(4, 'БСП2206', 2);

insert into student values(1, 'Владислав Яковлевич Булавинцев', '9999267804', 2);
insert into student values(2, 'Елена Ивановна Шитпухина', '6911234583', 3);
insert into student values(3, 'Аркадий Андреевич Зварыкин', '2831970690', 4);
insert into student values(4, 'Геннадий Фёдорович Ратанов', '2600985192', 1);
insert into student values(5, 'Ева Федоровна Иршанкова', '3619818392', 2);
insert into student values(6, 'Василий Алексеевич Кандеев', '8080431039', 3);
insert into student values(7, 'Алла Петровна Минасуева', '2657079787', 4);
insert into student values(8, 'Надежда Андреевна Рахманина', '1070070469', 1);
insert into student values(9, 'Алена Евгеньевна Люкурина', '7928802848', 2);
insert into student values(10, 'Мария Василевна Залотина', '5045014150', 3);
insert into student values(11, 'Катерина Романовна Мощевитина', '8000559264', 4);
insert into student values(12, 'Ирина Сергеевна Кобытяева', '6225124187', 1);
insert into student values(13, 'Станислав Адамович Савухин', '7902063831', 2);
insert into student values(14, 'Георгий Тимофеевич Савчуков', '6942825317', 3);
insert into student values(15, 'Анастасия Максимовна Эйвазова', '7448727388', 4);
insert into student values(16, 'Евгения Романовна Шайбалова', '8842520123', 1);
insert into student values(17, 'Максим Юриевич Филилеев', '3891979933', 2);
insert into student values(18, 'Николай Вадимович Прудовский', '7841891926', 3);
insert into student values(19, 'Виктория Вадимовна Ратегова', '4961027052', 4);
insert into student values(20, 'Антон Василиевич Пучкин', '5563277008', 1);
