import random
import story
from geopy import distance

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='some_database_name',
    user='some_user_name',
    password='some_password',
    autocommit=True
)


# FUNCTIONS

# select 30 airports for the game
def get_airports():
    sql = """SELECT iso_country, ident, name, type, latitude_deg, longitude_deg
FROM airport
WHERE continent = 'EU' 
AND type='large_airport'
ORDER by RAND()
LIMIT 30;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# get all goals
def get_goals():
    sql = "SELECT * FROM goal;"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# create new game
def create_game(start_money, p_range, cur_airport, p_name, a_ports):
    sql = "INSERT INTO game (money, player_range, location, screen_name) VALUES (%s, %s, %s, %s);"
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (start_money, p_range, cur_airport, p_name))
    g_id = cursor.lastrowid

    # add goals / loot boxes
    goals = get_goals()
    goal_list = []
    for goal in goals:
        for i in range(0, goal['probability'], 1):
            goal_list.append(goal['id'])

    # exclude starting airport
    g_ports = a_ports[1:].copy()
    random.shuffle(g_ports)

    for i, goal_id in enumerate(goal_list):
        sql = "INSERT INTO ports (game, airport, goal) VALUES (%s, %s, %s);"
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, (g_id, g_ports[i]['ident'], goal_id))

    return g_id


# get airport info
def get_airport_info(icao):
    sql = f'''SELECT iso_country, ident, name, latitude_deg, longitude_deg
                  FROM airport
                  WHERE ident = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


# check if airport has a goal
def check_goal(g_id, cur_airport):
    sql = f'''SELECT ports.id, goal, goal.id as goal_id, name, money 
    FROM ports 
    JOIN goal ON goal.id = ports.goal 
    WHERE game = %s 
    AND airport = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (g_id, cur_airport))
    result = cursor.fetchone()
    if result is None:
        return False
    return result


# calculate distance between two airports
def calculate_distance(current, target):
    start = get_airport_info(current)
    end = get_airport_info(target)
    return distance.distance((start['latitude_deg'], start['longitude_deg']),
                             (end['latitude_deg'], end['longitude_deg'])).km


# get airports in range
def airports_in_range(icao, a_ports, p_range):
    in_range = []
    for a_port in a_ports:
        dist = calculate_distance(icao, a_port['ident'])
        if dist <= p_range and not dist == 0:
            in_range.append(a_port)
    return in_range


# set loot box opened

# update location
def update_location(icao, p_range, u_money, g_id):
    sql = f'''UPDATE game SET location = %s, player_range = %s, money = %s WHERE id = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (icao, p_range, u_money, g_id))


# game starts
# ask to show the story
storyDialog = input('Do you want to read the background story? (Y/N): ')
if storyDialog == 'Y':
    # print wrapped string line by line
    for line in story.getStory():
        print(line)

# GAME SETTINGS
print('When you are ready to start, ')
player = input('type player name: ')
# boolean for game over and win
game_over = False
win = False

# start money = 1000
money = 1000
# start range in km = 2000
player_range = 2000

# score = 0
score = 0

# boolean for diamond found
diamond_found = False

# all airports
all_airports = get_airports()
# start_airport ident
start_airport = all_airports[0]['ident']

# current airport
current_airport = start_airport

# game id
game_id = create_game(money, player_range, start_airport, player, all_airports)

# GAME LOOP
while not game_over:
    # get current airport info
    airport = get_airport_info(current_airport)
    # show game status
    print(f'''You are at {airport['name']}.''')
    print(f'''You have {money:.0f}$ and {player_range:.0f}km of range.''')
    # pause
    input('\033[32mPress Enter to continue...\033[0m')
    # if airport has goal ask if player wants to open it
    # check goal type and add/subtract money accordingly
    goal = check_goal(game_id, current_airport)
    if goal:
        question = input(
            f'''Do you want to open lootbox for {"100$ or " if money > 100 else ""}{"50km range" if player_range > 50 else ""}? M = money, R = range, enter to skip: ''')
        if not question == '':
            if question == 'M':
                money -= 100
            elif question == 'R':
                player_range -= 50
            if goal['money'] > 0:
                money += goal['money']
                print(f'''Congratulations! You found {goal['name']}. That is worth {goal['money']}$.''')
                print(f'''You have now {money:.0f}$''')
            elif goal['money'] == 0:
                win = True
                print(f'''Congratulations! You found the diamond. Now go to start.''')
            else:
                money = 0
                print(f'''Oh no! You have been robbed. You lost all your money''')

    # pause
    input("\033[32mPress Enter to continue...\033[0m")

    # ask to buy fuel/range
    if money > 0:
        question2 = input('Do you want to by fuel? 1$ = 2km of range. Enter amount or press enter. ')
        if not question2 == '':
            question2 = float(question2)
            if question2 > money:
                print(f'''You don't have enough money.''')
            else:
                player_range += question2 * 2
                money -= question2
                print(f'''You have now {money:.0f}$ and {player_range:.0f}km of range''')
        # pause
        input("\033[32mPress Enter to continue...\033[0m")

    # if no range, game over
    # show airports in range. if none, game over
    airports = airports_in_range(current_airport, all_airports, player_range)
    print(f'''\033[34mThere are {len(airports)} airports in range: \033[0m''')
    if len(airports) == 0:
        print('You are out of range.')
        game_over = True
    else:
        print(f'''Airports: ''')
        for airport in airports:
            ap_distance = calculate_distance(current_airport, airport['ident'])
            print(f'''{airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f}km''')
        # ask for destination
        dest = input('Enter destination icao: ')
        selected_distance = calculate_distance(current_airport, dest)
        player_range -= selected_distance
        update_location(dest, player_range, money, game_id)
        current_airport = dest
        if player_range < 0:
            game_over = True
    # if diamond is found and player is at start, game is won
    if win and current_airport == start_airport:
        print(f'''You won! You have {money}$ and {player_range}km of range left.''')
        game_over = True


# if game is over loop stops
# show game result
print(f'''{'You won!' if win else 'You lost!'}''')
print(f'''You have {money:.0f}$''')
print(f'''Your range is {player_range:.0f}km''')