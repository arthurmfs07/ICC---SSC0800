from enum import IntEnum


class Types(IntEnum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    NORMAL = 3
    ELECTRIC = 4


class Pokemon:
    _name = ''
    _main_type = Types.NORMAL

    def __init__(self, level, hp, attack, defense):
        self._defense = defense
        self._hp = hp
        self._attack_power = attack
        self._level = level

    def attack(self, enemy):
        print(self._name, 'attacks with a', self._attack_power, 'power', self._main_type.name, 'move!')
        enemy.take_damage(self._attack_power, self._main_type)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        self._hp -= damage
        self._print_damage(damage)

    def _print_damage(self, damage):
        print(self._name, 'took', damage, 'damage!')
        print(self._name, 'now has', self._hp, 'hp left.')

    @classmethod
    def get_name(cls):
        return cls._name


class Squirtle(Pokemon):
    _name = 'Squirtle'
    _main_type = Types.WATER

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.WATER or attack_type == Types.FIRE:
            damage *= 0.5
        elif attack_type == Types.GRASS:
            damage *= 2
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Charmander(Pokemon):
    _name = 'Charmander'
    _main_type = Types.FIRE

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.WATER:
            damage *= 2
        elif attack_type == Types.GRASS or attack_type == Types.FIRE:
            damage *= 0.5
        elif attack_type == Types.ELECTRIC:
            damage *= 1
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Bulbasaur(Pokemon):
    _name = 'Bulbasaur'
    _main_type = Types.GRASS

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.WATER:
            damage *= 0.5
        elif attack_type == Types.FIRE or attack_type == Types.GRASS:
            damage *= 1
        elif attack_type == Types.ELECTRIC:
            damage = 1
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Pikachu(Pokemon):
    _name = 'Pikachu'
    _main_type = Types.ELECTRIC

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.WATER:
            damage *= 0.5
        elif attack_type == Types.GRASS:
            damage *= 1
        elif attack_type == Types.ELECTRIC:
            damage *= 0.5
        elif attack_type == Types.FIRE:
            damage *= 1
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


def start_battle(pokemon_a, pokemon_b):
    pokemon_a.attack(pokemon_b)
    pokemon_b.attack(pokemon_a)


def read_pokemon_data():
    name = input().strip()
    attributes = list(map(int, input().split()))
    return name, attributes


def get_pokemon(name, attributes):
    if name == Charmander.get_name():
        return Charmander(*attributes)
    elif name == Squirtle.get_name():
        return Squirtle(*attributes)
    elif name == Bulbasaur.get_name():
        return Bulbasaur(*attributes)
    elif name == Pikachu.get_name():
        return Pikachu(*attributes)


def create_pokemon():
    name, attributes = read_pokemon_data()
    return get_pokemon(name, attributes)


def main():
    pokemons = []
    for _ in range(2):
        pokemon = create_pokemon()
        if pokemon:
            pokemons.append(pokemon)

    if len(pokemons) == 2:
        start_battle(pokemons[0], pokemons[1])


if __name__ == '__main__':
    main()



