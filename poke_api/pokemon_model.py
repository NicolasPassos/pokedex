class Pokemon:
    def __init__(self,abilities,base_experience,forms,game_indices,height,held_items,id,is_default,location_area_encounters,moves,name,order,past_abilities,past_types,species,sprites,stats,types,weight):
        self.abilities = abilities
        self.base_experience = base_experience
        self.forms = forms
        self.game_indices = game_indices
        self.height = height
        self.held_items = held_items
        self.id = id
        self.is_default = is_default
        self.location_area_encounters = location_area_encounters
        self.moves = moves
        self.name = name
        self.order = order
        self.past_abilities = past_abilities
        self.past_types = past_types
        self.species = species
        self.sprites = sprites
        self.stats = stats
        self.types = types
        self.weight = weight

class PokemonWidget:
    def __init__(self, name, photo, types, id):
        self.name = name
        self.photo = photo
        self.types = types
        self.id = id