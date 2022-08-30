import argparse
import sys
import csv

# Monster:
# - ID (3-digit string ID)
# - Types (set of strings, e.g., {"Water", "Fire"})
# - Weaknesses (set of strings)
# - Evolution (list of string IDs)
class Monster:
    def __init__(self, ID, name, types, weaknesses, evolution):
        self.ID = ID
        self.name = name
        self.types = types
        self.weaknesses = weaknesses
        self.evolution = evolution

    def __str__(self):
        return self.ID

# Monster Registry:
# - Monsters (dictionary of monsters indexed by their ID)
class MonsterRegistry:
    def __init__(self, monsters):
        self.monsters = monsters

    '''
    Initialize a monster registry from a CSV file.
    '''
    @staticmethod
    def createMonsterRegistry(filename):
        monstersByID = {}

        with open(filename, mode='r') as data:
            reader = csv.reader(data)
            header = next(reader)
            header = {val: idx for idx, val in enumerate(header)}

            for row in reader:
                ID = row[header['ID']]

                name = row[header['Name']]

                types = row[header['Types']]
                types = set([] if len(types) == 0 else types.split(','))

                weaknesses = row[header['Weaknesses']]
                weaknesses = set([] if len(weaknesses) == 0 else weaknesses.split(','))

                evolution = row[header['Evolution']]
                evolution = [] if len(evolution) == 0 else evolution.split(',')
                evolution.sort()

                monster = Monster(ID, name, types, weaknesses, evolution)
                monstersByID[ID] = monster

        monsterRegistry = MonsterRegistry(monstersByID)
        return monsterRegistry

    '''
    Get a monster from the registry by case-insensitive name.
    '''
    def findMonster(self, monsterName):
        monsterName = monsterName.lower()
        for monster in self.monsters.values():
            if monster.name.lower() == monsterName:
                return monster
        return None

    '''
    Get all the possible evolution paths for a given monster using depth-first search.
    '''
    def evolutionPaths(self, monster):
        paths = []
        if monster is None:
            return paths

        def helper(monster, path):
            if len(monster.evolution) == 0:
                paths.append(path)
                return
            
            for ID in monster.evolution:
                pathClone = path.copy()
                m = self.monsters[ID]
                pathClone.append(m.name)
                helper(m, pathClone)
            return

        helper(monster, [monster.name])
        return paths

    '''
    Print the following information about a monster:
    - ID
    - Monsters it's strong against
    - Monsters it's weak against
    - All evolution paths
    '''
    def printMonster(self, monster):
        if monster is None:
            return

        print('ID:')
        print(f'    {monster}')

        strongAgainst = []
        weakAgainst = []
        for m in self.monsters.values():
            if not(m.weaknesses.isdisjoint(monster.types)):
                strongAgainst.append((m.ID, m.name))

            if not(m.types.isdisjoint(monster.weaknesses)):
                weakAgainst.append((m.ID, m.name))
    
        print('Strong against:')
        if len(strongAgainst) == 0:
            print('    None')
        else:
            strongAgainst.sort(key=lambda x:x[0])

            for i in range(len(strongAgainst)):
                print(f'    {strongAgainst[i][1]}')

        print('Weak against:')
        if len(weakAgainst) == 0:
            print('    None')
        else:
            weakAgainst.sort(key=lambda x:x[0])

            for i in range(len(weakAgainst)):
                print(f'    {weakAgainst[i][1]}')

        paths = self.evolutionPaths(monster)
        print('Evolution:')
        for p in paths:
            print(f'    {" > ".join(p)}')


def main():
    parser = argparse.ArgumentParser(description='Print a Monster registry report.')
    parser.add_argument('filename')
    parser.add_argument('monsterName')

    args = parser.parse_args(sys.argv[1:])
    monsterRegistry = MonsterRegistry.createMonsterRegistry(args.filename)

    monster = monsterRegistry.findMonster(args.monsterName)
    monsterRegistry.printMonster(monster)


main()
