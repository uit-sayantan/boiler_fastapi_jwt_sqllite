drop table if exists audit;
create table audit (
    id integer primary key autoincrement,
    user_id integer not null,
    action text not null,
    object text not null,
    timestamp datetime default current_timestamp,
    foreign key (user_id) references users(user_id)
);

drop table if exists roles;
create table roles (
    role_id integer primary key autoincrement,
    role_name text not null unique
);

drop table if exists users;
create table users (
    user_id integer primary key autoincrement,
    user_name text not null unique,
    password text not null,
    role_id integer not null,
    foreign key (role_id) references roles(role_id)
);

drop view if exists user_details_v;
create view user_details_v as
select u.user_id, u.user_name, r.role_id, r.role_name
from users u
join roles r on u.role_id = r.role_id
;

insert into roles (role_name) values ('admin');
insert into roles (role_name) values ('user');