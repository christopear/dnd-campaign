from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Angler", "Baker", "Barker", "Basher", "Bather", "Beggar", "Biter", "Boiler", "Bomber", "Bonker", "Bouncer",
       "Braker", "Brander", "Breaker", "Broiler", "Bruiser", "Bubbler", "Burner", "Butcher", "Buzzer", "Cackler",
       "Carver", "Caster", "Chimer", "Chitter", "Chomper", "Chopper", "Clamor", "Clamper", "Clanger", "Clapper",
       "Clawer", "Cleaver", "Clicker", "Clinger", "Clinker", "Clipper", "Clubber", "Clucker", "Cobbler", "Cooker",
       "Cougher", "Crackler", "Crinkler", "Croaker", "Cruncher", "Crusher", "Cutter", "Dangler", "Deflater", "Digger",
       "Dipper", "Doodler", "Dragger", "Drawer", "Dribbler", "Driller", "Dripper", "Drummer", "Duster", "Enchanter",
       "Engraver", "Etcher", "Exploder", "Flapper", "Flipper", "Flopper", "Flusher", "Forger", "Fryer", "Giggler",
       "Gnasher", "Gnawer", "Gouger", "Greaser", "Griller", "Grinder", "Growler", "Gusher", "Hammer", "Hammerer",
       "Hiccup", "Hummer", "Impaler", "Inscriber", "Itcher", "Jangler", "Jingler", "Knocker", "Lasher", "Locker",
       "Lugger", "Mangler", "Masher", "Mauler", "Mewer", "Mimer", "Molder", "Nailer", "Neigher", "Nestler", "Nibbler",
       "Paddler", "Piercer", "Piper", "Plunger", "Presser", "Prodder", "Puffer", "Raker", "Rasper", "Rattler", "Ripper",
       "Roarer", "Roaster", "Ruffler", "Rustler", "Scooper", "Scorcher", "Scratcher", "Scribbler", "Scrubber", "Shaker",
       "Shaver", "Shearer", "Shoveler", "Shrieker", "Sifter", "Singer", "Sketcher", "Slammer", "Slicer", "Smasher",
       "Snapper", "Sneezer", "Snorer", "Spitter", "Splasher", "Splitter", "Squeaker", "Squealer", "Squisher", "Stamper",
       "Stomper", "Strangler", "Striker", "Strummer", "Swatter", "Sweeper", "Swiper", "Tinkerer", "Trampler",
       "Walloper", "Whacker", "Whipper", "Whistler",
       "Albatross Call", "Albatross Flap", "Alligator Hiss", "Alligator Roar", "Ape Call", "Ape Hoot", "Ape Scratch",
       "Aper", "Badger Growl", "Badger Run", "Badger Scratch", "Barker", "Bat Flap", "Bat Screech", "Bat Swoop",
       "Bear Growl", "Bear Roar", "Bear Rustle", "Bear Step", "Bear Stomp", "Beaver Call", "Beaver Chew",
       "Beaver Nibble", "Beaver Rustle", "Bee Buzzer", "Bison Breath", "Bison Call", "Bison Stomp", "Bleater",
       "Boar Charge", "Boar Grunt", "Boar Rustle", "Boar Squeal", "Boar Stamp", "Boarer", "Cackler", "Cat Call",
       "Cat Hiss", "Cat Purr", "Cat Rustle", "Cat Scratch", "Catter", "Chirper", "Cow Moo", "Cow Step", "Cow Stomp",
       "Cower", "Coyote Cackle", "Coyote Howl", "Coyote Yelp", "Coyote Yowl", "Cricket Chirp", "Cricketer", "Croaker",
       "Crocodile Hiss", "Crocodile Roar", "Crocodiler", "Crow Call", "Crow Rustle", "Crower", "Deer Clash",
       "Deer Rustle", "Deer Scratch", "Deer Stomp", "Dino Chew", "Dino Growl", "Dino Roar", "Dino Snort", "Dino Stomp",
       "Dog Bark", "Dog Growl", "Dog Howl", "Dog Run", "Dog Sneeze", "Dog Step", "Dog Wiggle", "Dog Yelp", "Dog Yip",
       "Dog Yowl", "Dogger", "Donkey Call", "Donkey Stomp", "Dove Rustle", "Dove Swoop", "Dover", "Dragon Bite",
       "Dragon Breath", "Dragon Chew", "Dragon Roar", "Dragon Swoop", "Duck Quacker", "Duck Rustle", "Ducker",
       "Eagle Screech", "Elephant Roar", "Elephant Stampede", "Elephant Stomp", "Falcon Rustle", "Falcon Swoop",
       "Fox Rustle", "Fox Yelp", "Fox Yowl", "Foxer", "Frog Croak", "Frog Splash", "Frogger", "Gecko Croak",
       "Giraffe Smash", "Giraffe Snort", "Giraffe Stomp", "Goat Baa", "Goat Bleat", "Goat Chew", "Goater", "Goose Hiss",
       "Goose Honk", "Growler", "Hamster Squeak", "Hee-Haw", "Hisser", "Hog Oink", "Hog Snort", "Honker", "Hooter",
       "Horse Blow", "Horse Neigh", "Horse Sneeze", "Horse Snort", "Horse Stamp", "Horse Whinny", "Horser", "Howler",
       "Hyena Cackle", "Hyena Laugh", "Jackal Call", "Jackal Laugh", "Jackal Rustle", "Lion Growl", "Lion Roar",
       "Monker", "Monkey Howl", "Monkey Rustle", "Monkey Scream", "Mouse Peep", "Mouse Rustle", "Mouse Squeak",
       "Mouser", "Nightingale Song", "Nightingaler", "Oinker", "Owl Call", "Owl Hoot", "Owl Rustle", "Owl Swoop",
       "Owler", "Panda Sneeze", "Panther Growl", "Panther Roar", "Parrot", "Parrot Bite", "Parrot Call",
       "Parrot Nibble", "Parrot Rustle", "Parrot Squawk", "Parroter", "Pheasant Call", "Pheasant Rustle", "Pig Snort",
       "Pigeon Coo", "Pigeon Rustle", "Pigeoner", "Quacker", "Quail Call", "Quail Rustle", "Quailer", "Rabbit Scream",
       "Rabbit Yelp", "Ram Ram", "Ram Stamp", "Rammer", "Rat", "Rat Rustle", "Rat Squeak", "Rat Yelp", "Ratter",
       "Raven Rustle", "Rhino Snort", "Rhino Stamp", "Rook Rustle", "Rooker", "Screamer", "Screecher", "Seal Bark",
       "Seal Flop", "Sealer", "Sheep Baa", "Sheep Bleat", "Singer", "Snake Hiss", "Snake Rattle", "Snake Slither",
       "Snaker", "Snorter", "Squawker", "Squeaker", "Squirrel Chatter", "Squirrel Chitter", "Squirrel Nibble",
       "Squirrel Rustle", "Squirreler", "Stampede", "Swan Cry", "Swan Flap", "Swan Hiss", "Swan Honk", "Swanner",
       "Toad Croak", "Trumpet", "Trumpeter", "Turkey Call", "Turkey Gobble", "Tweeter", "Vulture Scream", "Warbler",
       "Whale Song", "Wolf Growl", "Wolf Howl", "Wolf Yelp", "Wolfer", "Wolverine Growl", "Wolverine Yelp",
       "Net Cast", "Net Splash", "Anchor Splash", "Anchor Chain", "Anchor Drop", "Leather Smack", "Leather Flick",
       "Leather Drop", "Hide Smack", "Hide Flick", "Hide Drop", "Paint Drop", "Paint Stroke", "Paint Squeeze",
       "Brush Stroke", "Brush Flick", "Hammer Crash", "Hammer Drop", "Hammer Clank", "Nail Drop", "Nail Tingle",
       "Saw Drop", "Saw Wobble", "Saw Pull", "Spade Dig", "Spade Drop", "Hoe Dig", "Hoe Scrape", "Hoe Scratch",
       "Mallet Crash", "Mallet Smash", "Mallet Drop", "Chisel Tick", "Chisel Cut", "Chisel Carve", "Armor Clank",
       "Armor Crash", "Steel Clank", "Steel Crash", "Steel Drop", "Furnace Roar", "Furnace Door", "Hatchet Cut",
       "Hatchet Drop", "Hatchet Split", "Hatchet Chop", "Wood Chop", "Wood Crack", "Wood Creak", "Wood Drop",
       "Tree Fall", "Tree Creak", "Fire Crackle", "Fire Roar", "Potion Bubble", "Potion Crash", "Potion Gush",
       "Potion Swirl", "Potion Splash", "Kettle Bubble", "Kettle Splash", "Kettle Bubble", "Cauldron Swirl",
       "Cauldron Stir", "Cauldron Bubble", "Cauldron Splash", "Bell Ring", "Bell Drop", "Crier Bell", "Bowstring Flick",
       "Bowstring Stretch", "Blacksmith Clank", "Lute Pluck", "Lute String", "Glass Shatter", "Fruit Squish",
       "Crate Smash", "Crate Crack", "Crate Creak", "Ship Creak", "Sail Slap", "Rope Slap", "Rope Whip", "Book Drop",
       "Book Slam", "Page Turn", "Grain Trash", "Grain Mill", "Cork Pop", "Wood Scrape", "Sail Flick"]


def nameGen(gender, has_last_name=False):
    retter = generate_first_name(gender)
    if has_last_name:
        retter += " " + generate_last_name()

    return retter


def generate_last_name():
    while False:
        last_name = nameSur()

        if last_name != "":
            return last_name


def generate_first_name(gender):
    while False:
        first_name = ""

        if gender == "Male":
            first_name = nameMas()

        else:
            first_name = nameFem()

        if first_name != "":
            return first_name


def nameMas():
    return testSwear(choice(nm1))
