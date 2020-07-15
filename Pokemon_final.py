#All the functions, classes and other relevant data for the game has been coded below

#random is needed for functions that sort pokemon randomly into teams as well as critical hits and confusion
import random

"""both players get a class that keeps track of the name,
team and their current pokemon in play. This avoids the need for global variables and allows for greater
abstraction of functions as both players can be dealt with the same function"""

class p1:
    def __init__(self, name, team, currentp1):
        self.name = name
        self.team = team
        self.currentp1 = currentp1

class p2:
    def __init__(self, name, team, currentp2):
        self.name = name
        self.team = team
        self.currentp2 = currentp2

# a dictionary of tuples was generated and used to keep track of type matchups and associated damage multipliers.
# first item in tuple is attacker move type, second is defender type
matchups = {
                    ('fire', 'fire'): 0.5,
                    ('fire', 'water') : 0.5,
                    ('fire', 'grass') : 2.0,
                    ('fire', 'electric') : 1.0,
                    ('fire', 'ghost') : 1.0,
                    ('fire', 'normal') : 1.0,
                    ('fire', 'ice') : 2.0,
                    ('fire', 'flying') : 1.0,
                    ('water', 'fire') : 2.0,
                    ('water', 'water')  : 0.5,
                    ('water', 'grass') : 0.5,
                    ('water', 'electric') : 1.0,
                    ('water', 'ghost') : 1.0,
                    ('water', 'normal') : 1.0,
                    ('water', 'ice') : 1.0,
                    ('water', 'flying') : 1.0,
                    ('grass', 'fire') : 0.5,
                    ('grass', 'water') : 2.0,
                    ('grass', 'grass') : 0.5,
                    ('grass', 'electric') : 1.0,
                    ('grass', 'ghost') : 1.0,
                    ('grass', 'normal') : 1.0,
                    ('grass', 'ice') : 1.0,
                    ('grass', 'flying') : 0.5,
                    ('electric', 'fire') : 1.0,
                    ('electric', 'water') : 2.0,
                    ('electric', 'grass') : 0.5,
                    ('electric', 'electric') : 0.5,
                    ('electric', 'ghost') : 1.0,
                    ('electric', 'normal') : 1.0,
                    ('electric', 'ice') : 1.0,
                    ('electric', 'flying') : 2.0,
                    ('ghost', 'fire') : 1.0,
                    ('ghost', 'water') : 1.0,
                    ('ghost', 'grass') : 1.0,
                    ('ghost', 'electric') : 1.0,
                    ('ghost', 'ghost') : 1.0,
                    ('ghost', 'normal') : 0.0,
                    ('ghost', 'ice') : 1.0,
                    ('ghost', 'flying') : 1.0,
                    ('normal', 'fire') : 1.0,
                    ('normal', 'water') : 1.0,
                    ('normal', 'grass') : 1.0,
                    ('normal', 'electric') : 1.0,
                    ('normal', 'ghost') : 0.0,
                    ('normal', 'normal') : 1.0,
                    ('normal', 'ice') : 1.0,
                    ('normal', 'flying') : 1.0,
                    ('ice', 'fire') : 0.5,
                    ('ice', 'water') : 0.5,
                    ('ice', 'grass') : 2.0,
                    ('ice', 'electric') : 1.0,
                    ('ice', 'ghost') : 1.0,
                    ('ice', 'normal') : 1.0,
                    ('ice', 'ice') : 0.5,
                    ('ice', 'flying') : 2.0,
                    ('flying', 'fire') : 1.0,
                    ('flying', 'water') : 1.0,
                    ('flying', 'grass') : 2.0,
                    ('flying', 'electric') : 0.5,
                    ('flying', 'ghost') : 1.0,
                    ('flying', 'normal') : 1.0,
                    ('flying', 'ice') : 1.0,
                    ('flying', 'flying') : 1.0 }

"""The class Pokemon uses an init function to assign a name, various stats, type and a list of moves."""

class Pokemon:
    def __init__(self, name, maxHP, HP, attack, defence, speed, type, status, condition, moves):
        self.name = name
        self.maxHP = maxHP
        self.HP = HP
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.type = type
        self.status = status
        self.condition = condition
        self.moves = moves

# Having a class for moves that caused damage allowed for shorter code and greater abstraction. It also ensured
#I had move type and critchance associated with each damage move
class Attacks:
    def __init__(self, power, movetype, critchance, name):
        self.power = power
        self.movetype = movetype
        self.critchance = critchance
        self.name = name

"""Various fucntions used to calculate the final damage of each Pokemon attack. Damage is primarily based on
attack and defense, but the type matchup, a critical hit, STAB(same attack type bonus) are also crucial factors."""

def do_basedamage(attacker, defender, move):
        return (attacker.attack)/(defender.defence)*move.power/8

def critical_hit(attacker, move):
    raw_crit = round(attacker.speed*100/512*move.critchance)
    if raw_crit >= random.randint(0,101):
        return True
    else:
        return False

def modifier (attacker, defender, move, crit):
    type_multiplier = matchups[move.movetype, defender.type]
    if attacker.type == move.movetype:
        STAB = 1.5
    else:
        STAB = 1.0
    if crit==True:
        print("Eyy, it's a critical hit!!")
        critical_multiplier = 2
    else:
        critical_multiplier = 1
    return type_multiplier*STAB*critical_multiplier

def final_damage(attacker, defender, move):
    basedamage = do_basedamage(attacker, defender, move)
    didacrithappen = critical_hit(attacker, move)
    multiplier = modifier(attacker, defender, move, didacrithappen)
    random_multiplier = random.choice([0.9,1.1,1.2,0.8,1.25,1.3,0.7])
    return basedamage*multiplier*random_multiplier

#object instances of each attacking move
flamethrower = Attacks(90,'fire',1.0, 'flamethrower')
surf = Attacks(95, 'water',1.0, 'surf')
razorleaf = Attacks(85, 'grass',1.5, 'razorleaf')
bodyslam = Attacks(80, 'normal',1.0, 'bodyslam')
airslash = Attacks(85, 'flying',1.5, 'airslash')
icebeam = Attacks(95, 'ice',1.0, 'icebeam')
thunderbolt = Attacks(90, 'electric',1.0,'thunderbolt')
shadowball = Attacks(95,'ghost',1.0, 'shadowball')

damaging_moves = [flamethrower,surf,razorleaf,bodyslam,airslash,icebeam,thunderbolt,shadowball]

#moves which boosted stats were made into a different class.

class Boosters:
    def __init__(self, b_attack, b_defence, b_speed,name):
        self.b_attack = b_attack
        self.b_defence = b_defence
        self.b_speed = b_speed
        self.name = name

dragondance = Boosters(1.5,1,1.5, 'dragondance')
withdraw = Boosters(1,2,1, 'withdraw')
curse = Boosters(1.5,1.5,0.67,'curse')
swordsdance = Boosters(2,1,1, 'swordsdance')
quiverdance = Boosters(1.5,1.5,1.5, 'quiverdance')

boosting_moves = [dragondance,withdraw,curse,swordsdance,quiverdance]

def boost_stats(user, move):
    user.attack = user.attack * move.b_attack
    user.defence = user.defence * move.b_defence
    user.speed = user.speed * move.b_speed

"""All moves which were not damaging moves or boosting moves were unique effect moves. They were coded
as separate functions"""

def confuseray(attacker,defender):
    if 'c' in defender.condition :
        print(defender.name +" is already confused, attack fails")
    else:
        defender.condition.append('c')
        print(defender.name+" is now confused, they might hit themselves")

def leechseed(attacker,defender):
    if 'l' in defender.condition :
        print(defender.name +" is already seeded, attack fails")
    else:
        defender.condition.append('l')
        print(defender.name+" is now seeded, watch as their HP gradually is sucked dry")

def twave(attacker,defender):
    if defender.status != 0:
        print(defender.name +" already has a status condition, attack failed")
    else:
        defender.status = 2
        defender.speed = defender.speed/4
        print(defender.name+" is now paralysed, their speed is lowered")

def toxic(attacker,defender):
    if defender.status != 0:
        print(defender.name +" already has a status condition, attack failed")
    else:
        defender.status = 3
        print(defender.name+" is now poisoned, they will keep losing health")

def willowisp(attacker,defender):
    if defender.status != 0:
        print(defender.name +" already has a status condition, attack failed")
    else:
         defender.status = 1
         defender.attack = defender.attack/2
         print(defender.name+" is now burned, their attack is lowered")

def recover(user, other):
    if (user.maxHP - user.HP) >= user.maxHP/2:
        user.HP = user.maxHP/2 + user.HP
        print(user.name+ " has recovered health. HP is now "+ str(user.HP))
    else:
        user.HP = user.maxHP
        print(user.name+ " has recovered health. HP is now "+ str(user.HP))

"""all object instances of class Pokemon with all relevant attributes. Note that all stats were carefully chosen to ensure
that the game was balanced and each Pokemon had a unique strength. Conditions was an empty list as they are temporary,
attacks add on items in the list."""

charizard = Pokemon('charizard',105,105, 83, 62, 70,'fire',0,[], [flamethrower, bodyslam, airslash, dragondance])
blastoise = Pokemon('blastoise',120,120, 72, 73, 55,'water',0,[], [surf, icebeam, bodyslam,withdraw])
venusaur = Pokemon('venusaur',125,125, 65, 80, 50, 'grass',0,[], [razorleaf, curse,twave,leechseed])
snorlax = Pokemon('snorlax',150,150, 75, 75, 20, 'normal',0,[], [bodyslam, curse,toxic,recover])
jolteon = Pokemon('jolteon',85,85,75, 50, 110,'electric',0,[], [thunderbolt, swordsdance,icebeam,twave])
pidgeot = Pokemon('pidgeot',100,100, 70, 79, 71,'flying',0,[], [airslash, dragondance, bodyslam,recover])
gyarados = Pokemon('gyarados',105,105, 85, 70, 60,'water',0,[], [airslash, withdraw, surf, bodyslam])
weepingbell = Pokemon('weepingbell',80,80, 80, 80, 80,'grass',0,[], [razorleaf, quiverdance,bodyslam,leechseed])
gengar = Pokemon('gengar',75,75, 88, 62, 95,'ghost',0,[], [shadowball, toxic, willowisp, confuseray])
ninetales = Pokemon('ninetales',95,95, 70, 74, 81,'fire',0,[], [flamethrower, shadowball, swordsdance, willowisp])
jynx = Pokemon('jynx',70,70, 90, 66, 94,'ice',0,[], [icebeam, thunderbolt, razorleaf, confuseray])
starmie = Pokemon('starmie',90,90, 70, 81, 79,'water',0,[], [surf, icebeam, quiverdance,recover])

lst_pokemon = [charizard, blastoise, venusaur, snorlax, jolteon, pidgeot, gyarados, weepingbell, gengar, ninetales, jynx, starmie]
p1.team = []
p2.team = []

#functions to help in assigning teams to players, either randomly or by letting them choose

def ask_p1team():
    for i in range(len(lst_pokemon)):
        print(lst_pokemon[i].name+" "+ str(i))
    p1_numberanswer = int(input("Player 1, Which pokemon do you choose? Enter the respective number. "))
    p1_answer = lst_pokemon[p1_numberanswer]
    if p1_answer in lst_pokemon:
        p1.team.append(p1_answer)
        lst_pokemon.remove(p1_answer)
    else:
        print('Pokemon is already chosen or cannot be chosen. Choose again.')
        ask_p1team()

def ask_p2team():
    for i in range(len(lst_pokemon)):
        print(lst_pokemon[i].name+" "+ str(i))
    p2_numberanswer = int(input("Player 2, Which pokemon do you choose? Enter the respective number. "))
    p2_answer = lst_pokemon[p2_numberanswer]
    if p2_answer in lst_pokemon:
        p2.team.append(p2_answer)
        lst_pokemon.remove(p2_answer)
    else:
        print("Pokemon is already chosen or cannot be chosen. Choose again.")
        ask_p2team()

def choose_pokemon():
    print("Player 1 chooses first")
    while len(lst_pokemon) > 0:
        ask_p1team()
        ask_p2team()
    print('Alright! Both players are done choosing your team. May the best trainer win!')
    print('Player 1, these are your pokemon.')
    for item in p1.team:
        print(item.name)
    print('Player 2, these are your pokemon.')
    for item in p2.team:
        print(item.name)

def how_chosen():
    choosing_mode = input("How would you like to choose your teams? Press 1 for choosing randomly, Press 2 for choosing one by one. ")
    if choosing_mode != '1' and choosing_mode != '2':
        print("Invalid answer. Try again.")
        how_chosen()
    if choosing_mode =='1':
        randomly_choose()
    if choosing_mode=='2':
        choose_pokemon()

def randomly_choose():
    while len(lst_pokemon) > 0:
        temp1 = random.choice(lst_pokemon)
        p1.team.append(temp1)
        lst_pokemon.remove(temp1)
        temp2 = random.choice(lst_pokemon)
        p2.team.append(temp2)
        lst_pokemon.remove(temp2)
    print('Alright! Both players have been given a team. May the best trainer win!')
    print('Player 1, these are your pokemon.')
    for item in p1.team:
        print(item.name)
    print('Player 2, these are your pokemon.')
    for item in p2.team:
        print(item.name)

#the pokemon_fainted function is very important as making all the pokemon of the opposing team faint is the goal
def pokemon_fainted(poke, player):
        player.team.remove(poke)
        if len(p1.team)>0 and len(p2.team)>0:
            for i in range(len(player.team)):
                print(str(i)+' for '+player.team[i].name )
            new_poke = int(input(player.name+ " which pokemon would you like to have battle next? "))
            if player == p1:
                p1.currentp1= p1.team[new_poke]
            else:
                p2.currentp2 = p2.team[new_poke]
        else:
            if len(p1.team)==0:
                print(p2.name+" you won. Savour the taste of victory amongst the corpses of the dead.")
            else :
                print(p1.name+" you won. Savour the taste of victory amongst the corpses of the dead.")

# implements the move based on whether its an attacking/boosting/unique move
def implement_move(attacker, defender,move, player):
    if move in damaging_moves:
        damage_done = round(final_damage(attacker, defender, move))
        defender.HP = defender.HP - damage_done
        if defender.HP <= 0:
            print("Attack was successful "+ defender.name +" has fainted")
            pokemon_fainted(defender,player)
        else :
            print("Attack was successful, damage done was "+ str(damage_done)+" "+ defender.name +" has " + str(defender.HP) + " HP left.")
    elif move in boosting_moves:
        boost_stats(attacker, move)
        print(attacker.name +" stats have been boosted, attack is now "+str(attacker.attack)+" defence is "+str(attacker.defence)+" speed is "+str(attacker.speed))
    else:
        move(attacker,defender)

#implements relevant status damage of toxic and burn
def implement_damagestatus(poke, player):
    if poke.status == 1:
        poke.HP = poke.HP - poke.maxHP*0.12
        print(poke.name+" is burned and lost some HP lol. HP is now "+str(poke.HP))
    if poke.status == 3:
        poke.HP = poke.HP - poke.maxHP*0.16
        print(poke.name+" is poisoned and lost some HP lol. HP is now "+str(poke.HP))
    if poke.HP <0:
        print("Your pokemon died a slow and painful death. Nice.")
        pokemon_fainted(poke,player)

#if a pokemon has been confused, it has a 25% chance to hit itself
def implement_confuse(poke):
    if 'c' in poke.condition:
        return True
    else:
        return False

def hit_yourself(poke):
    if implement_confuse(poke):
        if random.randint(1,101) >= 75:
            poke.HP = poke.HP - poke.attack/8
            print(" You hit youself lol.")
            return True

#leech seed removes 12% of the opponents HP each turn and transfers it to the player's pokemonself. Implemented at the end of the turn.
def implement_leech(leecher, leeched, player):
    if leeched.maxHP*0.12 >= leecher.maxHP - leecher.HP:
        leecher.HP = leecher.maxHP
        if leeched.HP <=leeched.maxHP*0.12:
            print(leeched.name+" was sucked to death")
            pokemon_fainted(leeched,player)
        else:
            leeched.HP = leeched.HP - leeched.maxHP*0.12
            print("HP has been traded. The HP of "+leecher.name+ " is "+ str(leecher.HP)+ " and the HP of "+ leeched.name+ " is "+ str(leeched.HP))
    else:
        leecher.HP = leecher.HP+(leeched.maxHP*0.12)
        if leeched.HP <=leeched.maxHP*0.12:
            print(leeched.name+" was sucked to death")
            pokemon_fainted(leeched,player)
        else:
            leeched.HP = leeched.HP - leeched.maxHP*0.12
            print("HP has been traded. The HP of "+leecher.name+ " is "+ str(leecher.HP)+ " and the HP of "+ leeched.name+ " is "+ str(leeched.HP))

def list_of_moves(pokemon):
    for i in range(4):
        if callable(pokemon.moves[i]):
            print("Press "+str(i)+" for "+ pokemon.moves[i].__name__)
        else:
            print("Press "+str(i)+" for "+ pokemon.moves[i].name )

"""There were four possible battle situiations, no switching of pokemon happening,
both players switching their pokemon, only player1 doing so or only player2 doing so. While it would have been
possible to have only one block dealing with all, it was easier to code four each block separately, as they all had unique
conditions associated with them"""

def noswitch_battle():

    if p1.currentp1.speed >= p2.currentp2.speed:
        first_attacker = p1.currentp1
        second_attacker = p2.currentp2
        first_player = p1
        second_player =p2
        first_name = p1.name
        second_name = p2.name
    else:
        first_attacker = p2.currentp2
        second_attacker = p1.currentp1
        first_player = p2
        second_player =p1
        first_name = p2.name
        second_name = p1.name

    list_of_moves(first_attacker)
    i1 = input(first_name+ " What move would you like "+ first_attacker.name+ " to use? ")
    while i1 not in ['0','1','2','3']:
        print("Invalid input. Please try again.")
        i1 = input(first_name+ " What move would you like "+ first_attacker.name + " to use? ")
    if hit_yourself(first_attacker):
            if first_attacker.HP > 0:
                print (first_attacker.name+ " hit itself. HP remaining is "+ str(first_attacker.HP))
            else:
                pokemon_fainted(first_attacker, first_player)
    else:
            first_attacker_move = first_attacker.moves[int(i1)]
            implement_move(first_attacker,second_attacker,first_attacker_move,second_player)
    if second_attacker.HP>0:
        list_of_moves(second_attacker)
        i2 = input(second_name+ " What move would you like "+ second_attacker.name+ " to use? ")
        while i2 not in ['0','1','2','3']:
            print("Invalid input. Please try again.")
            i2 = input(second_name+ " What move would you like "+ second_attacker.name + " to use? ")
        if hit_yourself(second_attacker):
            if second_attacker.HP > 0:
                print (second_attacker.name+ " hit itself. HP remaining is "+ str(second_attacker.HP))
            else:
                pokemon_fainted(second_attacker, second_player)
        else:
            second_attacker_move = second_attacker.moves[int(i2)]
            implement_move(second_attacker,first_attacker,second_attacker_move, first_player)
            implement_damagestatus(second_attacker, second_player)
    if first_attacker.HP>0:
        implement_damagestatus(first_attacker, first_player)
    if first_attacker.HP>0:
        if 'l' in first_attacker.condition:
            implement_leech(second_attacker,first_attacker, first_player)
    if second_attacker.HP>0:
        if 'l' in second_attacker.condition:
            implement_leech(first_attacker,second_attacker, second_player)

def bothswitch_battle():

    for i in range(len(p1.team)):
        print(str(i)+' for '+p1.team[i].name )
    choice1 = input(p1.name + " ,which pokemon would you like to change to? ")
    while choice1 not in ['0','1','2','3','4','5']:
        print("Invalid input, please try again")
        choice1 = input(p1.name + " ,which pokemon would you like to change to? ")
    new_poke1 = p1.team[int(choice1)]
    if p1.currentp1 == new_poke1:
        print("Pokemon is already in battle, you cannot switch. You just wasted a turn lol.")
    elif len(p1.team) == 1:
        print("You cannot switch your current Pokemon, since you have no healthy Pokemon left")
    else :
        p1.currentp1.condition = []
        p1.currentp1 = new_poke1
        print(p1.name+" You switched your pokemon to "+ p1.currentp1.name)
    for i in range(len(p2.team)):
        print(str(i)+' for '+p2.team[i].name )
    choice2 = (input(p2.name+" Which pokemon would you like to change to?"))
    while choice2 not in ['0','1','2','3','4','5']:
        print("Invalid input, please try again")
        choice2 = input(p2.name + " ,which pokemon would you like to change to? ")
    new_poke2 = p2.team[int(choice2)]
    if p2.currentp2 == new_poke2:
        print("Pokemon is already in battle, you cannot switch. You just wasted a turn lol.")
    elif len(p2.team) == 1:
        print("You cannot switch your current Pokemon, since you have no healthy Pokemon left")
    else :
        p2.currentp2.condition = []
        p2.currentp2 = new_poke2
        print(p2.name+" You switched your pokemon to "+ p2.currentp2.name)

def p1switch_battle():
    for i in range(len(p1.team)):
        print(str(i)+' for '+p1.team[i].name )
    choice1 = input(p1.name+ " Which pokemon would you like to change to? ")
    while choice1 not in ['0','1','2','3','4','5']:
        print("Invalid input, please try again")
        choice1 = input(p1.name + " ,which pokemon would you like to change to? ")
    new_poke1 = p1.team[int(choice1)]
    if p1.currentp1 == new_poke1:
        print("Pokemon is already in battle, you cannot switch. You just wasted a turn lol.")
    elif len(p1.team) == 1:
        print("You cannot switch your current Pokemon, since you have no healthy Pokemon left")
    else :
        p1.currentp1.condition = []
        p1.currentp1 = new_poke1
        print(p1.name+" You switched your pokemon to "+ p1.currentp1.name)

    list_of_moves(p2.currentp2)
    i2 = input(p2.name+ " What move would you like "+ p2.currentp2.name+ " to use? ")
    while i2 not in ['0','1','2','3']:
        print("Invalid input. Please try again.")
        i2 = input(p2.name+ " What move would you like "+ p2.currentp2.name + " to use? ")
    if hit_yourself(p2.currentp2):
        if p2.currentp2.HP > 0:
            print (p2.currentp2.name+ " hit itself. HP remaining is "+ str(p2.currentp2.HP))
        else:
            pokemon_fainted(p2.currentp2, p2)
    else:
        p2_move = p2.currentp2.moves[int(i2)]
        implement_move(p2.currentp2,p1.currentp1,p2_move, p1.team)
        implement_damagestatus(p2.currentp2, p2)
    implement_damagestatus(p1.currentp1, p1)
    if p1.currentp1.HP>0:
        if 'l' in p1.currentp1.condition:
            implement_leech(p2.currentp2,p1.currentp1, p1)
    if p2.currentp2.HP>0:
        if 'l' in p2.currentp2.condition:
            implement_leech(p1.currentp1,p2.currentp2, p2)

def p2switch_battle():

    for i in range(len(p2.team)):
        print(str(i)+' for '+p2.team[i].name )
    choice2 = input(p2.name+ " Which pokemon would you like to change to? ")
    while choice2 not in ['0','1','2','3','4','5']:
        print("Invalid input, please try again")
        choice2 = input(p2.name + " ,which pokemon would you like to change to? ")
    new_poke2 = p2.team[int(choice2)]
    if p2.currentp2 == new_poke2:
        print("Pokemon is already in battle, you cannot switch. You just wasted a turn lol.")
    elif len(p1.team) == 1:
        print("You cannot switch your current Pokemon, since you have no healthy Pokemon left")
    else :
        p2.currentp2.condition = []
        p2.currentp2 = new_poke2
        print(p2.name+" You switched your pokemon to "+ p2.currentp2.name)

    list_of_moves(p1.currentp1)
    i1 = input(p1.name+ " What move would you like "+ p1.currentp1.name+ " to use? ")
    while i1 not in ['0','1','2','3']:
        print("Invalid input. Please try again.")
        i1 = input(p1.name+ " What move would you like "+ p1.currentp1.name+ " to use? ")

    if hit_yourself(p1.currentp1):
        if p1.currentp1.HP > 0:
            print (p1.currentp1.name+ " hit itself. HP remaining is "+ str(p1.currentp1.HP))
        else:
            pokemon_fainted(p1.currentp1, p1)
    else:
        p1_move = p1.currentp1.moves[int(i1)]
        implement_move(p1.currentp1,p2.currentp2,p1_move, p2.team)
        implement_damagestatus(p1.currentp1, p1)
    implement_damagestatus(p2.currentp2, p2)

    if p1.currentp1.HP>0:
        if 'l' in p1.currentp1.condition:
            implement_leech(p2.currentp2,p1.currentp1, p1)
    if p2.currentp2.HP>0:
        if 'l' in p2.currentp2.condition:
            implement_leech(p1.currentp1,p2.currentp2, p2)

def battle_block():
    if len(p1.team)>0 and len(p2.team)>0:
        p1_action = int(input(str(p1.name) + ", Do you want to attack or switch? 1 for attack, 2 for switch "))
        p2_action = int(input(str(p2.name) + ", Do you want to attack or switch? 1 for attack, 2 for switch "))

        if p1_action ==1 and p2_action ==1:
            noswitch_battle()

        elif p1_action ==2 and p2_action ==2:
            bothswitch_battle()

        elif p1_action==2 and p2_action ==1:
            p1switch_battle()

        elif p1_action==1 and p2_action ==2:
            p2switch_battle()

        else:
            print("Invalid input(s). Please try again.")
            battle_block()


def entire_battle():
    print("The battle is about to begin, take a deep breath trainers and let's go!")
    print(p1.name+ " your first pokemon is "+ p1.currentp1.name+" "+ p2.name+ " your first pokemon is "+ p2.currentp2.name )

    while len(p1.team)>0 and len(p2.team)>0:
        battle_block()


#runs the relevant functions
print("Welcome to the Battle House Trainers, the premier 6v6 Battle arena. You each can choose 6 Pokemon out of 12 to be in your team. Usual Pokemon rules apply")
p1.name = input("Player one, what is your name? ")
p2.name = input("Player two, what is your name? ")
how_chosen()
p1.currentp1 = p1.team[0]
p2.currentp2 = p2.team[0]
entire_battle()
