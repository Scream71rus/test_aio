
create schema aio;

create table if not exists aio.customer(
    id serial primary key,
    login text not null,
    password text not null,
    created timestamp not null default now()
);
