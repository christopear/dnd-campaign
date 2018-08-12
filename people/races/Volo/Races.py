from people.Person import *


class Lizardfolk(Person):
	nm1 = ["", "", "", "", "", "b", "d", "g", "jh", "k", "l", "m", "n", "r", "s", "sh", "t", "tr", "th", "thr", "v"]
	nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e",
		   "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o",
		   "u", "aa", "ae", "ao", "au"]
	nm3 = ["ch", "d", "dr", "dh", "g", "gr", "gh", "gg", "l", "ll", "lt", "lth", "lr", "p", "r", "rg", "rht", "rk",
		   "rt",
		   "rd", "rth", "sh", "sk", "shr", "sh", "sl", "t", "th", "tr", "thr"]
	nm4 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o",
		   "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "a", "e", "i",
		   "o", "u", "ea", "ua", "ae", "ia", "aa", "ao"]
	nm5 = ["c", "g", "gr", "gn", "k", "kh", "kr", "r", "rr", "s", "ss", "sr", "st", "str", "t", "th", "tr"]
	nm6 = ["", "", "", "", "", "", "", "ch", "k", "n", "nd", "nk", "nt", "r", "rd", "rk", "rt", "rth", "s", "ss", "sh",
		   "sj", "sk", "t", "th", "v", "x"]

	def generate_masculine(self):
		i = choice(range(0, 3))
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm6)
		if i == 0:

			while name_component3 == name_component:
				name_component3 = choice(self.nm6)

			nMs = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm3)
			name_component5 = choice(self.nm4)
			while name_component4 == name_component or name_component4 == name_component3:
				name_component4 = choice(self.nm3)

			if i == 1:
				nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3
			else:
				name_component6 = choice(self.nm2)
				name_component7 = choice(self.nm5)
				while name_component7 == name_component4 or name_component7 == name_component3:
					name_component7 = choice(self.nm5)

				nMs = name_component + name_component2 + name_component4 + name_component6 + name_component7 + name_component5 + name_component3

		return nMs


class Kenku(SimplePerson):
	nm1 = ["Angler", "Baker", "Barker", "Basher", "Bather", "Beggar", "Biter", "Boiler", "Bomber", "Bonker", "Bouncer",
		   "Braker", "Brander", "Breaker", "Broiler", "Bruiser", "Bubbler", "Burner", "Butcher", "Buzzer", "Cackler",
		   "Carver", "Caster", "Chimer", "Chitter", "Chomper", "Chopper", "Clamor", "Clamper", "Clanger", "Clapper",
		   "Clawer", "Cleaver", "Clicker", "Clinger", "Clinker", "Clipper", "Clubber", "Clucker", "Cobbler", "Cooker",
		   "Cougher", "Crackler", "Crinkler", "Croaker", "Cruncher", "Crusher", "Cutter", "Dangler", "Deflater",
		   "Digger",
		   "Dipper", "Doodler", "Dragger", "Drawer", "Dribbler", "Driller", "Dripper", "Drummer", "Duster", "Enchanter",
		   "Engraver", "Etcher", "Exploder", "Flapper", "Flipper", "Flopper", "Flusher", "Forger", "Fryer", "Giggler",
		   "Gnasher", "Gnawer", "Gouger", "Greaser", "Griller", "Grinder", "Growler", "Gusher", "Hammer", "Hammerer",
		   "Hiccup", "Hummer", "Impaler", "Inscriber", "Itcher", "Jangler", "Jingler", "Knocker", "Lasher", "Locker",
		   "Lugger", "Mangler", "Masher", "Mauler", "Mewer", "Mimer", "Molder", "Nailer", "Neigher", "Nestler",
		   "Nibbler",
		   "Paddler", "Piercer", "Piper", "Plunger", "Presser", "Prodder", "Puffer", "Raker", "Rasper", "Rattler",
		   "Ripper",
		   "Roarer", "Roaster", "Ruffler", "Rustler", "Scooper", "Scorcher", "Scratcher", "Scribbler", "Scrubber",
		   "Shaker",
		   "Shaver", "Shearer", "Shoveler", "Shrieker", "Sifter", "Singer", "Sketcher", "Slammer", "Slicer", "Smasher",
		   "Snapper", "Sneezer", "Snorer", "Spitter", "Splasher", "Splitter", "Squeaker", "Squealer", "Squisher",
		   "Stamper",
		   "Stomper", "Strangler", "Striker", "Strummer", "Swatter", "Sweeper", "Swiper", "Tinkerer", "Trampler",
		   "Walloper", "Whacker", "Whipper", "Whistler",
		   "Albatross Call", "Albatross Flap", "Alligator Hiss", "Alligator Roar", "Ape Call", "Ape Hoot",
		   "Ape Scratch",
		   "Aper", "Badger Growl", "Badger Run", "Badger Scratch", "Barker", "Bat Flap", "Bat Screech", "Bat Swoop",
		   "Bear Growl", "Bear Roar", "Bear Rustle", "Bear Step", "Bear Stomp", "Beaver Call", "Beaver Chew",
		   "Beaver Nibble", "Beaver Rustle", "Bee Buzzer", "Bison Breath", "Bison Call", "Bison Stomp", "Bleater",
		   "Boar Charge", "Boar Grunt", "Boar Rustle", "Boar Squeal", "Boar Stamp", "Boarer", "Cackler", "Cat Call",
		   "Cat Hiss", "Cat Purr", "Cat Rustle", "Cat Scratch", "Catter", "Chirper", "Cow Moo", "Cow Step", "Cow Stomp",
		   "Cower", "Coyote Cackle", "Coyote Howl", "Coyote Yelp", "Coyote Yowl", "Cricket Chirp", "Cricketer",
		   "Croaker",
		   "Crocodile Hiss", "Crocodile Roar", "Crocodiler", "Crow Call", "Crow Rustle", "Crower", "Deer Clash",
		   "Deer Rustle", "Deer Scratch", "Deer Stomp", "Dino Chew", "Dino Growl", "Dino Roar", "Dino Snort",
		   "Dino Stomp",
		   "Dog Bark", "Dog Growl", "Dog Howl", "Dog Run", "Dog Sneeze", "Dog Step", "Dog Wiggle", "Dog Yelp",
		   "Dog Yip",
		   "Dog Yowl", "Dogger", "Donkey Call", "Donkey Stomp", "Dove Rustle", "Dove Swoop", "Dover", "Dragon Bite",
		   "Dragon Breath", "Dragon Chew", "Dragon Roar", "Dragon Swoop", "Duck Quacker", "Duck Rustle", "Ducker",
		   "Eagle Screech", "Elephant Roar", "Elephant Stampede", "Elephant Stomp", "Falcon Rustle", "Falcon Swoop",
		   "Fox Rustle", "Fox Yelp", "Fox Yowl", "Foxer", "Frog Croak", "Frog Splash", "Frogger", "Gecko Croak",
		   "Giraffe Smash", "Giraffe Snort", "Giraffe Stomp", "Goat Baa", "Goat Bleat", "Goat Chew", "Goater",
		   "Goose Hiss",
		   "Goose Honk", "Growler", "Hamster Squeak", "Hee-Haw", "Hisser", "Hog Oink", "Hog Snort", "Honker", "Hooter",
		   "Horse Blow", "Horse Neigh", "Horse Sneeze", "Horse Snort", "Horse Stamp", "Horse Whinny", "Horser",
		   "Howler",
		   "Hyena Cackle", "Hyena Laugh", "Jackal Call", "Jackal Laugh", "Jackal Rustle", "Lion Growl", "Lion Roar",
		   "Monker", "Monkey Howl", "Monkey Rustle", "Monkey Scream", "Mouse Peep", "Mouse Rustle", "Mouse Squeak",
		   "Mouser", "Nightingale Song", "Nightingaler", "Oinker", "Owl Call", "Owl Hoot", "Owl Rustle", "Owl Swoop",
		   "Owler", "Panda Sneeze", "Panther Growl", "Panther Roar", "Parrot", "Parrot Bite", "Parrot Call",
		   "Parrot Nibble", "Parrot Rustle", "Parrot Squawk", "Parroter", "Pheasant Call", "Pheasant Rustle",
		   "Pig Snort",
		   "Pigeon Coo", "Pigeon Rustle", "Pigeoner", "Quacker", "Quail Call", "Quail Rustle", "Quailer",
		   "Rabbit Scream",
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
		   "Cauldron Stir", "Cauldron Bubble", "Cauldron Splash", "Bell Ring", "Bell Drop", "Crier Bell",
		   "Bowstring Flick",
		   "Bowstring Stretch", "Blacksmith Clank", "Lute Pluck", "Lute String", "Glass Shatter", "Fruit Squish",
		   "Crate Smash", "Crate Crack", "Crate Creak", "Ship Creak", "Sail Slap", "Rope Slap", "Rope Whip",
		   "Book Drop",
		   "Book Slam", "Page Turn", "Grain Trash", "Grain Mill", "Cork Pop", "Wood Scrape", "Sail Flick"]


class Triton(Person):
	nm1 = ["c", "d", "dh", "j", "jh", "k", "kh", "m", "n", "r", "v", "z"]
	nm2 = ["a", "e", "i", "o", "u"]
	nm3 = ["d", "dd", "g", "gl", "hn", "hl", "hr", "l", "lg", "lm", "ld", "ln", "lz", "m", "mn", "mr", "n", "nn", "nd",
		   "nl", "nr", "nv", "r", "rl", "rn", "rv", "rz", "v", "vn", "z"]

	nm4 = ["", "", "", "", "", "", "", "", "b", "bh", "d", "dh", "f", "fl", "h", "l", "m", "n", "s", "sh", "vl", "w",
		   "wh",
		   "y"]
	nm5 = ["a", "e", "o", "u", "a", "e", "o", "u", "i"]
	nm6 = ["d", "dd", "dr", "gr", "gl", "hl", "hn", "l", "lr", "lt", "lth", "ml", "nl", "nth", "nr", "r", "rn", "rl",
		   "rr",
		   "s", "sh", "st", "sl", "sn", "t", "th", "tr", "thr", "tl", "thl"]
	nm7 = ["d", "h", "l", "m", "n", "r"]
	nm8 = ["e", "y", "y", "y", "y", "y", "y"]

	nm9 = ["", "", "", "b", "bh", "d", "dh", "j", "g", "l", "m", "n", "p", "r", "s", "v", "z"]
	nm10 = ["a", "u", "a", "u", "a", "u", "e", "o"]
	nm11 = ["b", "d", "g", "gh", "hl", "hn", "hm", "hr", "l", "n", "m", "r", "v"]
	nm12 = ["a", "o", "a", "o", "e", "u"]
	nm13 = ["d", "g", "l", "ll", "ln", "lm", "lv", "m", "mn", "n", "ns", "nz", "r", "rs", "s", "sn", "x", "z"]

	def generate_feminine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm4)
		name_component2 = choice(self.nm5)
		name_component3 = choice(self.nm6)
		name_component4 = choice(self.nm8)
		while name_component3 == name_component:
			name_component3 = choice(self.nm6)

		if i == 0:
			nFm = name_component + name_component2 + name_component3 + name_component4 + "n"
		else:
			name_component5 = choice(self.nm5)
			name_component6 = choice(self.nm7)
			while name_component6 == name_component3:
				name_component6 = choice(self.nm7)

			nFm = name_component + name_component2 + name_component3 + name_component5 + name_component6 + name_component4 + "n"

		return nFm

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		while name_component == name_component3:
			name_component3 = choice(self.nm3)

		name_component4 = choice(self.nm2)
		nMs = name_component + name_component2 + name_component3 + name_component4 + "s"
		return nMs


class Tabaxi(Person):
	nm1 = ["Afternoon Nap (Nap)", "Animal in the Woods (Woods)", "Answered Riddle (Riddle)", "Art of Shadows (Art)",
		   "Aura of Passion (Aura)", "Aurora of Winter (Aurora)", "Autumn Harvest (Autumn)", "Beats of a Heart (Beats)",
		   "Beauty of Summer (Summer)", "Beauty's Eye (Beauty)", "Belly of a Beast (Beast)", "Berry Bush (Bush)",
		   "Big Heart (Big)", "Bird Feather (Bird)", "Bite Marks (Bite)", "Blank Board (Board)",
		   "Blank Canvas (Canvas)",
		   "Blazing Fire (Blaze)", "Blossoms in Summer (Blossom)", "Branch of a River (River)",
		   "Breath of Fresh Air (Breath)", "Broken Chain (Chain)", "Bubble of a Cauldron (Bubble)",
		   "Burden of Chains (Chains)", "Burning Desire (Desire)", "Burning Fire (Fire)", "Bush in the Forest (Forest)",
		   "Bushy Branch (Branch)", "Busy Bee (Bee)", "Cadence of Water (Cadence)", "Cake of Chocolate (Cake)",
		   "Call of a Bird (Bird)", "Call of the Owl (Owl)", "Call to Action (Action)", "Candle in the Dark (Candle)",
		   "Cannon on Deck (Cannon)", "Carriage on the Road (Road)", "Clanking Bottle (Clank)",
		   "Cloaking Dagger (Dagger)",
		   "Cloud in the Sky (Sky)", "Coursing River (River)", "Cover of Clouds (Cover)", "Crescent Moon (Moon)",
		   "Dangling Button (Button)", "Dangling Lace (Lace)", "Daydream at Night (Dream)", "Dew on the Grass (Dew)",
		   "Dream of Days (Dream)", "Drifting Cloud (Cloud)", "Drifting Snowflake (Snowflake)", "Drop in a Pond (Drop)",
		   "Dust of Chalk (Dust)", "Dust on the Road (Dust)", "Eclipse of the Moon (Eclipse)",
		   "Edge of the World (Edge)",
		   "End of Winter (Winter)", "Endless Time (Time)", "Fall of Water (Water)", "Fallen Twig (Twig)",
		   "Fang of a Snake (Fang)", "Feather in the Wind (Feather)", "Fire in the Distance (Fire)",
		   "Fish in the River (River)", "Flame of Passion (Passion)", "Flame of the Spirit (Flame)",
		   "Flickering Fire (Fire)", "Flickering Flame (Flame)", "Flight of a Robin (Robin)",
		   "Flow of the River (Flow)",
		   "Flower in the Field (Flower)", "Flower of Ivory (Ivory)", "Forgotten Link (Link)",
		   "Four-Leaf Clover (Clover)",
		   "Fragrance of Spring (Spring)", "Friend of Foe (Friend)", "Gale of the Storm (Gale)",
		   "Game of Chance (Game)",
		   "Garden of Flowers (Flower)", "Gift of a Guest (Gift)", "Glow of the Sun (Sun)", "Grass of Spring (Grass)",
		   "Guest at Home (Guest)", "Guide of Life (Guide)", "Hawk Feather (Hawk)", "Hen of the Flock (Hen)",
		   "Hidden Depths (Depth)", "Hidden Treasure (Treasure)", "Hide of the Beast (Hide)", "High Noon (Noon)",
		   "Honey of Bees (Honey)", "Hot Flame (Flame)", "Hot as Fire (Fire)", "Ice in Summer (Ice)",
		   "Ice on the Lake (Ice)", "Ink on Skin (Ink)", "Jewel of the Mountain (Jewel)", "Kite in the Wind (Kite)",
		   "Leaf on the Water (Leaf)", "Leaping Frog (Frog)", "Light in the Morning (Light)",
		   "Lightning After Thunder (Lightning)", "Little Flower (Little)", "Lock on an Open Door (Lock)",
		   "Locket on a Heart (Locket)", "Looping Coil (Coil)", "Loose String (String)", "Luck of the Draw (Luck)",
		   "Marble in the Sky (Marble)", "Mark of Life (Mark)", "Melting of Snow (Snow)",
		   "Mirror's Reflection (Mirror)",
		   "Mist in the Morning (Mist)", "Mountain Boulder (Boulder)", "Needle in Hay (Needle)",
		   "Night of Dreams (Night)",
		   "Open Gates (Gate)", "Owl in the Morning (Owl)", "Page of a Book (Page)", "Paint on a Canvas (Paint)",
		   "Patch in the Forest (Patch)", "Paw of a Bear (Paw)", "Peak of Mountains (Peak)",
		   "Piece of the Puzzle (Piece)",
		   "Plume in the Wind (Plume)", "Plume of Smoke (Smoke)", "Poem of Summer (Poem)", "Print of a Boot (Boot)",
		   "Print of an Animal (Animal)", "Quill in the Grass (Quill)", "Rain in Summer (Rain)", "Rain of Fall (Rain)",
		   "Rainbow After Rain (Rainbow)", "Rays of the Sun (Ray)", "Remnants of History (Remnant)",
		   "Rhythm of Drums (Rhythm)", "Ringing of Bells (Bell)", "Rinkling Chains (Chains)", "Roar of a Bear (Roar)",
		   "Rope in a Knot (Knot)", "Rustling of a Deer (Deer)", "Sailing Ship (Ship)", "Sand of the Beach (Sand)",
		   "Sands of Time (Sand)", "Scarf in Summer (Scarf)", "Scratch on Wood (Scratch)", "Screech of Bats (Bat)",
		   "Sea of Opportunity (Sea)", "Second Chance (Chance)", "Serpent Scale (Scale)", "Shadow of a Star (Shadow)",
		   "Shadows in the Wind (Shadow)", "Sky Full of Stars (Sky)", "Sky of a Sunset (Sky)", "Sleight Hand (Hand)",
		   "Smooth as Silk (Silk)", "Snapping Branch (Snap)", "Snow of the Mountain (Snow)",
		   "Solstice of Summer (Solstice)", "Song of Paradise (Song)", "Sound of the Drum (Drum)",
		   "Spark of Life (Spark)",
		   "Sparkle of Light (Sparkle)", "Spell of Rain (Spell)", "Spots of a Leopard (Spot)",
		   "Spring Blossom (Spring)",
		   "Spring Winds (Spring)", "Star in the Morning (Star)", "Steady Rock (Rock)", "Stitch of Fabric (Stitch)",
		   "Stone in Water (Stone)", "Storm at Sea (Sea)", "Storm on the Horizon (Storm)", "Strength of Love (Love)",
		   "Stripes of a Tiger (Tiger)", "Stroke of a Brush (Brush)", "Summer Afternoon (Summer)",
		   "Sunshine at Night (Sunshine)", "Tale of Wonder (Tale)", "Taste of Fruit (Taste)", "Three Tree (Three)",
		   "Thrill of Life (Thrill)", "Thunder in the Morning (Thunder)", "Ticking Clock (Clock)",
		   "Tome of Secrets (Tome)",
		   "Top Card (Card)", "Trail in the Woods (Trail)", "Tree Blossom (Blossom)", "Tree in the Woods (Tree)",
		   "Tricking Treat (Trick)", "Two River (River)", "Unpulled Cart (Cart)", "Unread Book (Book)",
		   "Veil of Shadows (Veil)", "Veil of a Mask (Veil)", "Wave on the Shore (Wave)", "Windy Shore (Shore)",
		   "Wing of an Angel (Angel)", "Winter Breath (Winter)", "Wish Upon a Star (Wish)",
		   "Wonder of the World (Wonder)"]
	nm2 = ["Active", "Agile", "Amused", "Amusing", "Ancient", "Angelic", "Arctic", "Austere", "Bizarre", "Bold",
		   "Brash",
		   "Brave", "Bright", "Bronze", "Cheeky", "Clever", "Curious", "Defiant", "Dynamic", "Eager", "Elegant",
		   "Elite",
		   "Emerald", "Ethereal", "Faint", "Fine", "Five", "Flawless", "Four", "Fragile", "Fragrant", "Free", "Fresh",
		   "Gentle", "Gold", "Golden", "Grand", "Half", "Happy", "Hearty", "Hidden", "Humble", "Hushed", "Icy", "Jade",
		   "Jolly", "Kind", "Lazy", "Light", "Little", "Lone", "Lost", "Lucky", "Magic", "Mellow", "Merry", "Misty",
		   "Mystery", "Nimble", "Odd", "Opal", "Prime", "Proud", "Pure", "Quick", "Quiet", "Quirky", "Radiant", "Rare",
		   "Ruby", "Sapphire", "Secret", "Serene", "Seven", "Shady", "Silent", "Single", "Six", "Smooth", "Stout",
		   "Subtle",
		   "Sweet", "Swift", "Three", "Tranquil", "True", "Twin", "Two", "Velvet", "Vibrant", "Violet", "Wild"]
	nm3 = ["Animal", "Aspect", "Bat", "Beach", "Bear", "Beast", "Beauty", "Beetle", "Bell", "Berry", "Bird", "Bit",
		   "Bite",
		   "Block", "Board", "Boat", "Book", "Boot", "Bottle", "Brain", "Branch", "Breath", "Brush", "Bubble", "Bush",
		   "Button", "Cable", "Cake", "Candle", "Candy", "Cannon", "Canvas", "Card", "Carriage", "Cart", "Chain",
		   "Chains",
		   "Chalk", "Chance", "Child", "Clock", "Cloud", "Clover", "Coil", "Deer", "Device", "Dream", "Drop", "Dust",
		   "Edge", "Fang", "Feather", "Fire", "Fish", "Flame", "Flower", "Frog", "Game", "Garden", "Gate", "Gift",
		   "Glove",
		   "Grass", "Guest", "Guide", "Hen", "Hide", "Honey", "Ice", "Ink", "Jewel", "Kite", "Knot", "Lace", "Leaf",
		   "Light", "Lightning", "Link", "Lock", "Locket", "Love", "Luck", "Marble", "Mark", "Mask", "Mirror", "Needle",
		   "Night", "Owl", "Page", "Patch", "Path", "Peak", "Piece", "Plume", "Poem", "Quill", "Quilt", "Rain",
		   "Riddle",
		   "River", "Robin", "Rock", "Scale", "Scarf", "Scratch", "Sea", "Shadow", "Shoe", "Shore", "Silk", "Smoke",
		   "Snow",
		   "Snowflake", "Song", "Spark", "Sparkle", "Spell", "Star", "Stitch", "Stone", "Storm", "Straw", "Stream",
		   "String", "Stripe", "Tale", "Thing", "Thrill", "Thunder", "Timber", "Time", "Tome", "Trail", "Tree", "Trick",
		   "Veil", "Wave", "Wind", "Wing", "Wish", "Wonder"]

	nm4 = ["Abandoned", "Adamant", "Anchored", "Ancient", "Angelic", "Animated", "Arctic", "Ascending", "Awakening",
		   "Awoken", "Barren", "Basking", "Bellowing", "Binding", "Blank", "Bleak", "Blossoming", "Boundless", "Bright",
		   "Brisk", "Broken", "Bustling", "Changing", "Cherished", "Chilly", "Cleansing", "Clear", "Colorful",
		   "Covering",
		   "Crawling", "Dancing", "Dark", "Darkening", "Desired", "Distant", "Dreaming", "Dreary", "Dry", "Dual",
		   "Echoing",
		   "Elder", "Enchanted", "Enchanting", "Entangling", "Ethereal", "Evading", "Everlasting", "Exotic",
		   "Expanding",
		   "Fading", "Far", "Faraway", "Fertile", "Flawless", "Flickering", "Fragile", "Fragrant", "Free", "Gathering",
		   "Gentle", "Gleaming", "Glistening", "Graceful", "Grand", "Great", "Grieving", "Growing", "Healing",
		   "Heavenly",
		   "Hidden", "High", "Humble", "Hushed", "Infinite", "Lasting", "Light", "Little", "Living", "Lone", "Longing",
		   "Loving", "Lurking", "Lush", "Magical", "Meager", "Mellow", "Merging", "Mild", "Misty", "Mountain",
		   "Mumbling",
		   "Murky", "Murmuring", "Musing", "Noiseless", "Passing", "Pleasing", "Precious", "Protecting", "Prowling",
		   "Pure",
		   "Quiet", "Radiant", "Reflected", "Reflecting", "Reigning", "Rising", "Roaming", "Roaring", "Rumbling",
		   "Scented",
		   "Serene", "Shimmering", "Silent", "Sleepy", "Snoozing", "Snoring", "Soothing", "Stormy", "Surging",
		   "Thundering",
		   "Tired", "Trailing", "Tranquil", "Tumbling", "Twinkling", "Twirling", "Twisting", "Unraveling", "Velvet",
		   "Vibrant", "Wailing", "Wandering", "Watching", "Weeping", "Whispering", "Whistling", "Wild"]
	nm5 = ["Barrens", "Bayou", "Bluff", "Bluffs", "Bog", "Bogs", "Bush", "Cave", "Cavern", "Caverns", "Caves", "Cliff",
		   "Cliffs", "Coast", "Coasts", "Copse", "Crag", "Crags", "Creek", "Creeks", "Deluge", "Den", "Desert",
		   "Deserts",
		   "Dune", "Dunes", "Estuary", "Field", "Fields", "Fjord", "Fjords", "Forest", "Forests", "Glade", "Glades",
		   "Grotto", "Hail", "Island", "Islands", "Isle", "Isles", "Jungle", "Jungles", "Lagoon", "Lagoons", "Lake",
		   "Lakes", "Marsh", "Mesa", "Mist", "Mists", "Monsoon", "Morass", "Mountain", "Mountains", "Oasis", "Peak",
		   "Peaks", "Rain", "Rainforest", "Reservoir", "Ridge", "River", "Rivers", "Shore", "Shores", "Shower",
		   "Sierra",
		   "Slopes", "Storm", "Swamp", "Swamps", "Thicket", "Torrent", "Wild", "Wilderness", "Wilds", "Woodland",
		   "Woodlands", "Woods"]

	def generate_masculine(self):
		i = choice(range(0, 4))
		if i == 0:
			name_component = choice(self.nm4)
			name_component2 = choice(self.nm5)
			return "The " + name_component + " " + name_component2 + " Clan"

		elif i == 1:
			name_component = choice(self.nm1)
			return name_component

		elif i == 2:
			name_component = choice(self.nm2)
			name_component2 = choice(self.nm3)

			names = name_component + " " + name_component2 + " (" + name_component + ")"
			return names
		else:
			name_component = choice(self.nm2)
			name_component2 = choice(self.nm3)

			names = name_component + " " + name_component2 + " (" + name_component2 + ")"
		return names


class Goliath(Person):
	nmFF = ["Age", "Ane", "Gau", "Ge", "Ina", "Kau", "Ke", "Ki", "Kuo", "La", "Le", "Maa", "Man", "Mau", "Me", "Na",
			"Nal",
			"Ni", "One", "Ori", "Paa", "Pau", "Pe", "Tha", "The", "Thu", "Vaa", "Vau", "Ve", "Vu"]
	nmFL = ["gea", "geo", "gia", "gu", "kea", "keo", "ki", "kia", "kio", "la", "lai", "lane", "lea", "leo", "lo", "lu",
			"meo", "mi", "mia", "ne", "nea", "neo", "ni", "nia", "nu", "peo", "peu", "pu", "rea", "ri", "ria", "the",
			"thea", "thia", "thio", "thu", "vea", "vi", "via", "vu"]
	nmMF = ["Ag", "Apa", "Au", "Aug", "Eg", "Gau", "Gea", "Gha", "Ili", "Kana", "Kava", "Keo", "Khu", "La", "Ma", "Mau",
			"Mea", "Mo", "Na", "Neo", "Pa", "Pu", "Tha", "Thava", "Tho", "Va", "Vau", "Vega", "Vi", "Vo"]
	nmML = ["gak", "gal", "gan", "gath", "ghan", "gith", "glath", "gun", "kan", "kein", "khal", "kin", "kon", "lath",
			"lig",
			"lok", "mahg", "mahk", "mahl", "mak", "man", "mith", "mul", "nak", "nath", "nihl", "noth", "path", "phak",
			"thag", "thak", "tham", "thi", "thok", "veith", "vek", "vhal", "vhik", "vith", "voi"]
	nmMdF = ["Adept", "Bear", "Brave", "Bright", "Dawn", "Day", "Deer", "Dream", "Flint", "Fearless", "Flower", "Food",
			 "Fright", "Goat", "Hard", "Hide", "High", "Honest", "Horn", "Keen", "Lone", "Long", "Low", "Lumber",
			 "Master",
			 "Mind", "Mountain", "Night", "Rain", "River", "Rock", "Root", "Silent", "Sky", "Sly", "Smart", "Steady",
			 "Stone", "Storm", "Strong", "Swift", "Thread", "Thunder", "Tree", "Tribe", "True", "Truth", "Wander",
			 "Wild",
			 "Wise", "Wound"]
	nmMdL = ["aid", "bearer", "breaker", "caller", "carver", "chaser", "climber", "cook", "dream", "drifter", "eye",
			 "finder", "fist", "friend", "frightener", "guard", "hand", "hauler", "heart", "herder", "hunter", "jumper",
			 "killer", "lander", "leader", "leaper", "logger", "maker", "mender", "picker", "runner", "shot", "smasher",
			 "speaker", "stalker", "striker", "tanner", "twister", "vigor", "walker", "wanderer", "warrior", "watcher",
			 "weaver", "worker"]
	nmSF = ["Agu-Ul", "Agu-V", "Anakal", "Apuna-M", "Athun", "Egena-V", "Egum", "Elan", "Ganu-M", "Gathak", "Gean",
			"Inul",
			"Kalag", "Kaluk", "Katho-Ol", "Kolae-G", "Kolak", "Kulan", "Kulum", "Lakum", "Maluk", "Munak", "Muthal",
			"Nalak", "Nola-K", "Nugal", "Nulak", "Ogol", "Oveth", "Thenal", "Thul", "Thunuk", "Ugun", "Uthenu-K",
			"Vaimei-L", "Valu-N", "Vathun", "Veom", "Vuma-Th", "Vunak"]
	nmSL = ["aga", "ageane", "akane", "akanu", "akume", "alathi", "amino", "amune", "anathi", "atake", "athai",
			"athala",
			"atho", "avea", "avi", "avone", "eaku", "ekali", "elo", "iaga", "iago", "iala", "iano", "igala", "igane",
			"igano", "igo", "igone", "ileana", "ithino", "olake", "ugate", "ugoni", "ukane", "ukate", "ukena", "ulane",
			"upine", "utha", "uthea"]

	def generate_surname(self):
		name_component = choice(self.nmMdF)
		name_component2 = choice(self.nmMdL)
		name_component3 = choice(self.nmSF)
		name_component4 = choice(self.nmSL)
		return name_component + name_component2 + " " + name_component3 + name_component4

	def generate_feminine(self):
		name_component = choice(self.nmFF)
		name_component2 = choice(self.nmFL)
		nMs = name_component + name_component2
		return nMs

	def generate_masculine(self):
		name_component = choice(self.nmMF)
		name_component2 = choice(self.nmML)
		nMs = name_component + name_component2
		return nMs


class Aasimar(Person):
	nm1 = ["", "", "", "", "b", "br", "c", "cr", "h", "l", "m", "n", "p", "r", "t", "v", "w", "z"]
	nm2 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "au", "ai", "ea",
		   "ei"]
	nm3 = ["d", "dr", "g", "gg", "gr", "gw", "k", "kr", "kl", "l", "ld", "lg", "lw", "lr", "lt", "n", "nr", "nw", "nl",
		   "r",
		   "rn", "rr", "rw", "rl", "v", "vr", "w"]
	nm4 = ["a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "e", "a", "i", "e", "a", "i", "e", "o", "o", "u",
		   "u", "ee", "ia", "ie", "ai", "ei"]
	nm5 = ["d", "l", "m", "n", "t", "v"]
	nm6 = ["l", "m", "n", "nt", "r"]

	nm7 = ["", "", "", "", "", "br", "d", "dr", "h", "l", "m", "n", "ph", "r", "rh", "th", "v", "w", "z"]
	nm8 = ["a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "e", "e", "ia",
		   "io",
		   "ea", "eo"]
	nm9 = ["d", "j", "l", "ld", "ldr", "lv", "ll", "lt", "m", "mm", "mn", "n", "nr", "nv", "nl", "ndr", "nm", "r", "rd",
		   "rk", "rs", "s", "sr", "sl", "v"]
	nm10 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "ea",
			"ia",
			"ie"]
	nm11 = ["l", "m", "n", "r", "s", "z"]
	nm12 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "au", "ou", "oe"]
	nm13 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "h", "l", "m", "n", "r"]

	def generate_feminine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm7)
		name_component2 = choice(self.nm8)
		name_component3 = choice(self.nm9)
		name_component4 = choice(self.nm10)
		name_component5 = choice(self.nm13)
		if i == 0:
			while name_component3 == name_component or name_component3 == name_component5:
				name_component3 = choice(self.nm9)

			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			name_component6 = choice(self.nm11)
			name_component7 = choice(self.nm12)
			while name_component6 == name_component3 or name_component6 == name_component5:
				name_component6 = choice(self.nm11)

			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

		return nMs

	def generate_masculine(self):
		i = choice(range(0, 2))
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		name_component4 = choice(self.nm4)
		name_component5 = choice(self.nm6)
		if i == 0:
			while name_component3 == name_component or name_component3 == name_component5:
				name_component3 = choice(self.nm3)

			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component5
		else:
			name_component6 = choice(self.nm5)
			name_component7 = choice(self.nm4)
			while name_component6 == name_component3 or name_component6 == name_component5:
				name_component6 = choice(self.nm5)

			nMs = name_component + name_component2 + name_component3 + name_component4 + name_component6 + name_component7 + name_component5

		return nMs


class Aarakocra(Person):
	nm1 = ["", "", "", "", "", "c", "cl", "cr", "d", "g", "gr", "h", "k", "kh", "kl", "kr", "q", "qh", "ql", "qr", "r",
		   "rh", "s", "y", "z"]
	nm2 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e",
		   "i", "u", "a", "e", "i", "u", "ae", "aia", "ee", "oo", "ou", "ua", "uie"]
	nm3 = ["c", "cc", "k", "kk", "l", "ll", "q", "r", "rr"]
	nm4 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "aa", "ea", "ee", "ia", "ie"]
	nm5 = ["", "", "", "", "c", "ck", "d", "f", "g", "hk", "k", "l", "r", "rr", "rc", "rk", "rrk", "s", "ss"]

	def generate_masculine(self):
		i = choice(range(0, 2))

		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm5)

		if i == 0:
			while name_component == name_component3:
				name_component3 = choice(self.nm5)

			nMs = name_component + name_component2 + name_component3
		else:
			name_component4 = choice(self.nm3)
			name_component5 = choice(self.nm4)
			nMs = name_component + name_component2 + name_component4 + name_component5 + name_component3

		return nMs
