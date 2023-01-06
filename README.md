# software-1-project-example
Game inspired by the infamous Afrikan Tähti.

This game uses the airport table from the database course. In addition you need the following tables:
```sql
create table game
(
    id           int auto_increment
        primary key,
    money        int(8)      null,
    location     varchar(10) null,
    screen_name  varchar(40) null,
    player_range int         null,
    constraint game_ibfk_1
        foreign key (location) references airport (ident)
)
    charset = latin1;

create index location
    on game (location);
```
```sql
create table goal
(
    id          int         not null
        primary key,
    name        varchar(40) null,
    money       int         null,
    probability int         null
)
    charset = latin1;

insert into goal (id, name, money, probability)
values  (1, 'TOPAZ', 300, 4),
        (2, 'EMERALD', 600, 3),
        (3, 'RUBY', 1000, 2),
        (4, 'DIAMOND', 0, 1),
        (5, 'BANDIT', -1, 3);
```
```sql
create table ports
(
    id      int auto_increment
        primary key,
    game    int                  null,
    airport varchar(11)          not null,
    goal    int                  null,
    opened  tinyint(1) default 0 null
);
```