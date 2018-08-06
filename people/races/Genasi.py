from random import choice

from people.Person import Person


class Genasi(Person):
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

	def nameMas(self):
		return choice(Genasi.nm1)
