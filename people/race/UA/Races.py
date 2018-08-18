from random import choice

from people.race.Race import StandardRace, Race, SimpleRace


class Changeling(Race):
	nm1 = ["", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"]
	nm2 = ["a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai",
		   "oo", "ou"]
	nm3 = ["c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"]

	def generate_masculine(self):
		name_component = choice(self.nm1)
		name_component2 = choice(self.nm2)
		name_component3 = choice(self.nm3)
		while name_component == name_component3:
			name_component3 = choice(self.nm3)

		nMs = name_component + name_component2 + name_component3
		return nMs

	def race_check(self):
		pass


class Genasi(SimpleRace):
	nm1 = ["Ablaze", "Alight", "Ardor", "Ardour", "Arson", "Ash", "Austral", "Bake", "Beacon", "Blaze", "Blight",
		   "Boil", "Bonfire", "Brand", "Broil", "Burn", "Calcine", "Candle", "Cauterize", "Char", "Charcoal",
		   "Cinder",
		   "Coal", "Combust", "Conflagration", "Cremate", "Crisp", "Dante", "Dantean", "Ember", "Enkindle",
		   "Explosion",
		   "Fervor", "Fever", "Fiery", "Flame", "Flare", "Flash", "Flicker", "Flux", "Forge", "Frizzle", "Fry",
		   "Fuego",
		   "Fuel", "Fume", "Furnace", "Glare", "Gleam", "Glint", "Glow", "Grill", "Heat", "Hell", "Hellfire", "Hot",
		   "Igneous", "Ignite", "Ignition", "Incendiary", "Incinerate", "Infernal", "Inferno", "Kiln", "Kindle",
		   "Lantern", "Lava", "Light", "Lit", "Magma", "Melt", "Nether", "Oven", "Parch", "Phoenix", "Piping",
		   "Pyre",
		   "Pyro", "Roast", "Scald", "Scorch", "Scoria", "Sear", "Seethe", "Shine", "Singe", "Sizzle", "Smoke",
		   "Smolder", "Soot", "Spark", "Sultry", "Sun", "Swelter", "Thermal", "Thermo", "Tinder", "Toast", "Torch",
		   "Torrid", "Volcano", "Warmth", "Wildfire", "Wither",
		   "Agua", "Aqua", "Azure", "Basin", "Bath", "Bathe", "Beck", "Bore", "Branch", "Brine", "Brook", "Cleanse",
		   "Course", "Creek", "Current", "Dabble", "Damp", "Deluge", "Dew", "Dewdrop", "Douse", "Downpour", "Drain",
		   "Drench", "Drift", "Drip", "Drizzle", "Drop", "Droplet", "Drown", "Eagre", "Estuary", "Expanse", "Flood",
		   "Flow", "Flux", "Fog", "Fountain", "Geyser", "Gush", "Hose", "Hydra", "Hydrogen", "Influx", "Jet",
		   "Lagoon",
		   "Lake", "Lakelet", "Liquid", "Mere", "Mist", "Monsoon", "Neptune", "Ocean", "Paddle", "Plash", "Plunge",
		   "Pond", "Pool", "Precip", "Puddle", "Quagmire", "Rain", "Rill", "Rinse", "Ripple", "River", "Rivulet",
		   "Run",
		   "Runnel", "Rush", "Sea", "Seiche", "Shower", "Soak", "Spatter", "Splash", "Spout", "Spring", "Sprinkle",
		   "Storm", "Stream", "Streamlet", "Surf", "Surge", "Swish", "Tear", "Teardrop", "Tempest", "Tidal", "Tide",
		   "Torrent", "Tributary", "Tsunami", "Typhoon", "Vapor", "Wash", "Wave", "Well", "Wet",
		   "Adamant", "Agate", "Alabaster", "Amethyst", "Azurite", "Basalt", "Bedrock", "Block", "Boulder", "Brick",
		   "Callous", "Citrine", "Clay", "Cliff", "Cobble", "Cobblestone", "Crag", "Crystal", "Dense", "Diamond",
		   "Emerald", "Flint", "Fossil", "Fossilstone", "Garnet", "Gem", "Geo", "Geode", "Granite", "Gravel",
		   "Grime",
		   "Ground", "Hill", "Hunk", "Ingot", "Jade", "Jewel", "Lapis", "Lazuli", "Limestone", "Lodge", "Lump",
		   "Malachite", "Marble", "Marmoreal", "Mason", "Masonry", "Mineral", "Monolith", "Moonstone", "Mountain",
		   "Nugget", "Obsidian", "Onyx", "Opal", "Ore", "Pebble", "Pellet", "Peridot", "Precious", "Quarry",
		   "Quartz",
		   "Quartzite", "Rock", "Rocky", "Rough", "Rubble", "Ruby", "Rugged", "Sand", "Sandstone", "Sapphire",
		   "Sediment", "Shelf", "Slab", "Slate", "Soapstone", "Solid", "Spinel", "Stone", "Stony", "Sturdy", "Terra",
		   "Tile", "Topaz", "Travertine", "Turf", "Umber", "Wedge", "Zircon", "Aerate", "Aerial", "Air", "Ascend",
		   "Atmosphere", "Aura", "Aviate", "Azure", "Blast", "Blow", "Breath",
		   "Breeze", "Celeste", "Celestial", "Chinook", "Cruise", "Current", "Cyclone", "Draft", "Drift", "Eddy",
		   "Empyrean", "Fan", "Float", "Flow", "Flurry", "Flute", "Flutter", "Fly", "Funnel", "Gale", "Gasp",
		   "Glide",
		   "Gust", "Heave", "Heaven", "Hiss", "Hover", "Hurricane", "Lift", "Mistral", "Murmur", "Oxygen", "Ozone",
		   "Pipe", "Pneumatic", "Puff", "Rise", "Sail", "Shriek", "Sigh", "Sky", "Soar", "Squall", "Storm",
		   "Stratosphere", "Surge", "Tempest", "Tornado", "Troposphere", "Tumult", "Turbine", "Turbulence",
		   "Twister",
		   "Vent", "Waft", "Wheeze", "Whiff", "Whirl", "Whirlwind", "Whisk", "Whistle", "Wind", "Wing", "Zephyr"]

	def race_check(self):
		pass


class Warforged(SimpleRace):
	nm1 = ["Abider", "Achiever", "Actor", "Adapter", "Adviser", "Aegis", "Agent", "Animal", "Apparatus", "Armament",
		   "Artist", "Audience", "Author", "Awakener", "Basher", "Bastion", "Battler", "Bear", "Beast", "Beauty",
		   "Beetle",
		   "Bender", "Binder", "Blade", "Book", "Booster", "Boot", "Bouncer", "Brain", "Brander", "Brawler", "Breaker",
		   "Bringer", "Browser", "Bruiser", "Buffet", "Bug", "Builder", "Bulwark", "Calmer", "Candle", "Cannon",
		   "Carer",
		   "Carriage", "Carrier", "Cart", "Carver", "Case", "Caster", "Catcher", "Chain", "Chains", "Challenger",
		   "Champion", "Chaperon", "Charger", "Chaser", "Chopper", "Claymore", "Cleaver", "Climber", "Clock", "Club",
		   "Clubber", "Coil", "Commander", "Controller", "Cook", "Counter", "Creator", "Creature", "Creese", "Crew",
		   "Croaker", "Crow", "Crumbler", "Crusher", "Curator", "Curtana", "Custodian", "Cutlas", "Cutlass", "Cutter",
		   "Dagger", "Data", "Dealer", "Decipherer", "Defender", "Definer", "Delver", "Designer", "Destroyer",
		   "Diagnoser",
		   "Director", "Dirk", "Diver", "Doctor", "Dozer", "Dreamer", "Drifter", "Driver", "Drone", "Echo", "Edge",
		   "Enchanter", "Epee", "Eraser", "Estoc", "Etcher", "Examiner", "Expert", "Falchion", "Familiar", "Fighter",
		   "Figure", "Fire", "Five", "Flail", "Flame", "Fluke", "Foil", "Follower", "Forger", "Four", "Friend",
		   "Fumbler",
		   "Gasher", "Gauger", "Ghost", "Giant", "Gift", "Glaive", "Glancer", "Griller", "Grunter", "Guardian", "Guest",
		   "Guide", "Hacker", "Hammer", "Handler", "Heart", "Help", "Hook", "Horn", "Host", "Hummer", "Hunter", "Image",
		   "Inspector", "Iron", "Judge", "Junior", "Jury", "Katana", "Kid", "Killer", "Knife", "Knocker", "Kris",
		   "Launcher", "Leaper", "Lifter", "Lock", "Locket", "Lurker", "Mace", "Machine", "Mark", "Marker", "Mask",
		   "Masker", "Mauler", "Melter", "Menace", "Mentor", "Merger", "Metal", "Mime", "Mistake", "Model", "Molder",
		   "Murderer", "Nameless", "Needle", "Nemo", "Novice", "Nurse", "Observer", "Officer", "Ogler", "One",
		   "Ornament",
		   "Painter", "Passenger", "Patient", "Patriot", "Pierce", "Pilot", "Pious", "Player", "Porter", "Preacher",
		   "Pretender", "Prize", "Probe", "Protector", "Prowler", "Punisher", "Query", "Ravager", "Reader", "Reckoner",
		   "Relic", "Render", "Rescuer", "Responder", "Reviewer", "Rider", "Rune", "Saber", "Sabre", "Safeguard",
		   "Salvager", "Saviour", "Scimitar", "Scorcher", "Scratcher", "Scrubber", "Searcher", "Security", "Seeker",
		   "Senior", "Senser", "Sentinel", "Sentry", "Servant", "Shaper", "Shepherd", "Shield", "Shielder", "Shredder",
		   "Slasher", "Slicer", "Smasher", "Smiter", "Snooper", "Spark", "Sparkle", "Special", "Spirit", "Sprinter",
		   "Sprite", "Squasher", "Stalker", "Status", "Steel", "Steeple", "Stick", "Sticks", "Stitcher", "Striker",
		   "Student", "Stumbler", "Subject", "Suit", "Sunderer", "Supporter", "Surveyor", "Sword", "Tackler", "Taunter",
		   "Teacher", "Teaser", "Tempter", "Tester", "Thief", "Thinker", "Three", "Thunder", "Tinkerer", "Titan",
		   "Toad",
		   "Toledo", "Tutor", "Twister", "Two", "Undoer", "Unit", "Unmaker", "Unsung", "Vessel", "Victor", "Visitor",
		   "Voice", "Walker", "Ward", "Warden", "Watcher", "Whisperer", "Wielder", "Winker", "Winner", "Wonderer",
		   "Wrestler", "Zealot", "Zero"]

	def race_check(self):
		pass


class Shifter(SimpleRace):
	nm1 = ["Acor", "Almond", "Ash", "Astro", "Badger", "Barb", "Basalt", "Basil", "Beast", "Birch", "Blast", "Blaze",
		   "Bluff", "Bog", "Boulder", "Bramble", "Breach", "Briar", "Brock", "Brook", "Burst", "Canyon", "Char",
		   "Chasm",
		   "Cinder", "Claw", "Cliff", "Cloud", "Coal", "Cobalt", "Cobble", "Comet", "Cosmo", "Crag", "Crater", "Dash",
		   "Drake", "Drift", "Dune", "Dusk", "Dust", "Echo", "Fang", "Flame", "Flare", "Flax", "Flint", "Flood", "Foam",
		   "Fog", "Forest", "Fox", "Frost", "Frostbite", "Fume", "Fury", "Gale", "Glare", "Gorge", "Grime", "Grit",
		   "Grove", "Gulch", "Gust", "Kindle", "Light", "Lumber", "Magma", "Mahogany", "Marsh", "Mercury", "Midnight",
		   "Mire", "Moss", "Mountain", "Nebula", "Newt", "Nightfall", "Nightshade", "Nimbus", "North", "Nova", "Nyx",
		   "Oak", "Ocean", "Onyx", "Pitch", "Pyre", "Pyro", "Quicksilver", "Ravine", "Ridge", "Rift", "River", "Rock",
		   "Rubble", "Scar", "Shrub", "Silver", "Smoke", "Soot", "Spark", "Spike", "Spine", "Steam", "Steel", "Stone",
		   "Storm", "Surge", "Talon", "Thicket", "Thistle", "Thorn", "Thunder", "Tide", "Tiger", "Timber", "Tinder",
		   "Tor", "Torrent", "Vapor", "Vermin", "Vine", "Void", "Wave", "Willow", "Wolf", "Woods",

		   "Abyss", "Almond", "Amber", "Amethyst", "Anemone", "Aqua", "Aurora", "Autumn", "Birch", "Bloom", "Blossom",
		   "Breeze", "Briar", "Brook", "Canyon", "Chestnut", "Cloud", "Coral", "Coyote", "Crest", "Cricket", "Crystal",
		   "Dawn", "Dew", "Dewdrop", "Diamond", "Elm", "Ember", "Emerald", "Evening", "Feather", "Fern", "Flare",
		   "Floe",
		   "Flora", "Floret", "Flow", "Fluff", "Galaxy", "Gem", "Hail", "Harley", "Haze", "Hazel", "Horizon", "Ice",
		   "Indigo", "Iris", "Isle", "Ivy", "Jade", "Jasmine", "Juniper", "Karma", "Lake", "Lavender", "Leaf", "Lily",
		   "Luna", "Magenta", "Maple", "Marigold", "Meadow", "Midnight", "Mist", "Moon", "Moss", "Nebula", "Nutmeg",
		   "Ocean", "Olive", "Opal", "Orchid", "Pearl", "Petal", "Pine", "Pinecone", "Plume", "Poison", "Pyro", "Quill",
		   "Rain", "Raven", "Rill", "River", "Robin", "Rose", "Rosemary", "Ruby", "Saffron", "Sage", "Sapphire",
		   "Scarlet", "Shade", "Silver", "Sky", "Snow", "Snowflake", "Spring", "Star", "Stardust", "Sugar", "Summer",
		   "Sun", "Sunrise", "Sunset", "Sunshine", "Swill", "Thistle", "Tidal", "Tiger", "Tinder", "Topaz", "Twig",
		   "Twilight", "Urchin", "Vapor", "Violet", "Whirl", "Willow", "Wind", "Wing", "Winter"]

	def race_check(self):
		pass


class Gith(StandardRace):
	nm1 = ["Am", "Ar", "Ara", "Aza", "Bar", "Bra", "Bru", "Da", "Dar", "Dor", "Dra", "Dro", "Du", "Fa", "Far", "Fer",
		   "Gra",
		   "Gran", "Gre", "Gro", "Gru", "Hu", "Ka", "Kar", "Kha", "Kra", "Kro", "Ma", "Mu", "Na", "Nar", "Nu", "Ra",
		   "Ran",
		   "Rin", "Ru", "Sha", "Shra", "Sra", "Zra"]
	nm2 = ["d", "dak", "gh", "k", "kahr", "kar", "khar", "kk", "lag", "llak", "mag", "mak", "nag", "rag", "rak", "ram",
		   "rath", "rek", "rg", "rm", "rth", "ruk", "th", "tig", "zag", "zak", "zar", "zeg", "zirg", "zth"]
	nm3 = ["Ad", "Alm", "Arw", "Ash", "Dah", "Dhar", "Dolm", "Dran", "Ell", "Erzh", "Esz", "Ezh", "Grel", "Halm", "Han",
		   "Harn", "Heln", "Ihr", "Iln", "Imm", "Iz", "Kan", "Kharm", "Khaz", "Krez", "Laz", "Lez", "Lhash", "Magd",
		   "Marm",
		   "Nagr", "Nah", "Nalm", "Rasz", "Rez", "Sham", "Sharm", "Shund", "Um", "Uw"]
	nm4 = ["a", "ah", "aka", "al", "arah", "arin", "aya", "ayah", "eah", "eka", "el", "ela", "elna", "elya", "elzal",
		   "ena",
		   "enah", "era", "erah", "eya", "ihn", "ila", "ilzin", "in", "ina", "ira", "iza", "mina", "ya", "yara"]

	def race_check(self):
		pass


class Minotaur(Race):
	nmFF = ["Aam", "Ane", "Are", "Ase", "Duu", "Em", "Enti", "Este", "Fen", "Hene", "Hes", "Hila", "Hine", "Ias", "Ire",
			"Ki", "Kia", "Kuo", "Laan", "Line", "Loo", "Muu", "Nan", "Nea", "Neo", "Noo", "Nuo", "Oen", "Oes", "Raas",
			"Ras", "Sees", "Seo", "Sina", "Tee", "Tes", "Tia", "Tina", "Uova", "Weo"]
	nmFL = ["dra", "fin", "kane", "kea", "la", "las", "len", "lin", "lo", "mas", "me", "mi", "min", "na", "nan", "nas",
			"nim", "nu", "pen", "pe", "ra", "ren", "res", "rin", "ris", "ru", "sen", "sia", "ta", "ter", "tin", "tra",
			"tred", "tri", "trin", "tris", "ven", "vena", "vera", "vin"]
	nmMF = ["Ar", "Are", "Aste", "Bjor", "Car", "Cod", "Da", "Djar", "Djun", "Doen", "Dor", "Dur", "Foos", "Gar", "Goe",
			"Gra", "Gran", "Gun", "Hun", "Ja", "Jar", "Kar", "Kin", "Kir", "Koo", "Koor", "Krum", "Kur", "Man", "Min",
			"Mir", "Noo", "Pod", "Rak", "Te", "Toon", "Trak", "Tur", "Zam", "Zun"]
	nmML = ["ban", "baran", "bur", "dak", "daran", "dor", "fajar", "faruk", "furan", "gajan", "garak", "gur", "jar",
			"kan",
			"kar", "karat", "kun", "kurat", "kus", "manuk", "maruk", "nark", "narun", "paran", "raduk", "rak", "rakar",
			"ranak", "rapak", "ras", "rat", "rios", "ron", "rus", "rut", "tagar", "taruk", "toron", "turok", "tus"]
	nmSF = ["Agile", "Bear", "Bold", "Boulder", "Brave", "Bright", "Fearless", "Fist", "Glory", "Goblin", "Great",
			"Heavy",
			"Honor", "Iron", "Jagged", "Keen", "Nimble", "Orc", "Rock", "Rugged", "Sharp", "Silent", "Single", "Steady",
			"Steel", "Stone", "Storm", "Stout", "Strong", "Swift", "Thick", "Thunder", "Tough", "Truth", "Valiant",
			"Vigil",
			"Wolf"]
	nmSL = ["bane", "body", "eye", "fighter", "fist", "fury", "hand", "heart", "hide", "hoof", "horn", "horns",
			"hunter",
			"leader", "mind", "pelt", "roar", "runner", "skin", "skull", "slash", "slayer", "speaker", "step",
			"striker",
			"vigor", "walker", "warrior"]

	def race_check(self):
		pass

	def generate_surname(self):
		name_component = choice(self.nmSF)
		name_component2 = choice(self.nmSL)
		return name_component + name_component2

	def generate_feminine(self):
		name_component = choice(self.nmFF)
		name_component2 = choice(self.nmFL)
		nMs = name_component + name_component2

		return nMs

	def generate_masculine(self):
		i = choice(range(0, 2))
		if i == 0:
			name_component = choice(self.nmFF)
			name_component2 = choice(self.nmFL)
			nMs = name_component + name_component2
		else:
			name_component = choice(self.nmMF)
			name_component2 = choice(self.nmML)
			nMs = name_component + name_component2

		return nMs
