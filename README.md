# software-1-project-example
Game inspired by the infamous Afrikan Tähti.

#### Watch the videos:
[![Watch the videos](https://i.ytimg.com/vi/AVAs9eFomD8/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhBIFUoZTAP&rs=AOn4CLCT0c5w686gZCkuXoLKE4GQnl4lHw)](https://youtube.com/playlist?list=PLKenVLUxjmH9AyGZUeNDs8RinDVLQIQXY)

### Story

You are an adventurous traveler, who has always wanted to explore the world. One day, you decide you are going to take on the ultimate challenge and try to find the elusive and mysterious diamond of the sky.

You set off on your journey, traveling to the first airport on your list. When you arrived, you were greeted with a message on the airport's display board that said "Welcome to X Airport! You have X$ and Xkm of range left." 

You were determined to find the diamond, and you knew you would need money and range to do so. You decided to try your luck and opened a lootbox at the airport. Much to your surprise, you won a great reward- money! You were ecstatic and now had the funds to continue on your journey.

With your newfound wealth, you were able to continue on your journey, but you had to be careful with your money and range. You were able to purchase fuel at each airport, and you eventually made it to the airport where the diamond was rumored to be. 

Much to your surprise, when you arrived, you saw the diamond shining in the sunlight. You had finally found the diamond!

You were elated, but you knew you had to be careful as you made your way back to the starting airport. You had heard rumors that robbers were prowling around the airports, hoping to steal money and valuable items. As you made your way back, you were careful to not fall victim to any of their schemes. 

When you finally arrived back at the starting airport, you were relieved to find that you still had the diamond and all the money you had won along the way. You had won the challenge! 

You were overjoyed with your success and the money you had won. You had finally found the diamond of the sky and was able to keep all of your hard-earned money. You were a true success story!
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
