# software-1-project-example
Game inspired by the infamous Afrikan Tähti.

### Story
John was an adventurous traveler, who had always wanted to explore the world. One day, he decided he was going to take on the ultimate challenge and try to find the elusive and mysterious diamond of the sky. 

John set off on his journey, traveling to the first airport on his list. When he arrived, he was greeted with a message on the airport's display board that said "Welcome to X Airport! You have X$ and Xkm of range left." 

John was determined to find the diamond, and he knew he would need money and range to do so. He decided to try his luck and opened a lootbox at the airport. Much to his surprise, he won a great reward- money! He was ecstatic and now had the funds to continue on his journey.

With his newfound wealth, John was able to continue on his journey, but he had to be careful with his money and range. He was able to purchase fuel at each airport, and he eventually made it to the airport where the diamond was rumored to be. 

Much to his surprise, when he arrived, he saw the diamond shining in the sunlight. He had finally found the diamond!

John was elated, but he knew he had to be careful as he made his way back to the starting airport. He had heard rumors that robbers were prowling around the airports, hoping to steal money and valuable items. As he made his way back, he was careful to not fall victim to any of their schemes. 

When he finally arrived back at the starting airport, he was relieved to find that he still had the diamond and all the money he had won along the way. He had won the challenge! 

John was overjoyed with his success and the money he had won. He had finally found the diamond of the sky and was able to keep all of his hard-earned money. He was a true success story!

### Database

This game uses the airport table from the database course.

1. Create a new database 'demogame': `CREATE DATABASE demogame;`
2. Switch to that database: `USE demogame;`
3. Import the same `lp.sql` as you did earlier in the database course: `source path/to/lp.sql`
4. Keep `airport` and `contry` tables, remove others: 
   - `SET FOREIGN_KEY_CHECKS = 0;`
   - `DROP TABLE game;`
   - `DROP TABLE goal;`
   - `DROP TABLE goal_reached;`
   - `SET FOREIGN_KEY_CHECKS = 1;`
     - `CASCADE` is needed, because _game_ and _goal_ tables have constraints (relations to other tables)
5. Create the following tables:
    ```sql
    create table game
    (
        id           int auto_increment
            primary key,
        money        int(8)      null,
        location     varchar(10) null,
        screen_name  varchar(40) null,
        player_range int         null
    )
        charset = latin1;
   
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
6. Check that you have the necessary tables: `SHOW TABLES;`
   - The result should be like this:
   ```text
    +----------------+
    | Tables_in_test |
    +----------------+
    | airport        |
    | country        |
    | game           |
    | goal           |
    | ports          |
    +----------------+
   ```
