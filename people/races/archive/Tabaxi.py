from random import choice

from people.Person import Person
from tools.swearCheck import testSwear


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
			return testSwear("The " + name_component + " " + name_component2 + " Clan")

		elif i == 1:
			name_component = choice(self.nm1)
			return testSwear(name_component)

		elif i == 2:
			name_component = choice(self.nm2)
			name_component2 = choice(self.nm3)

			names = name_component + " " + name_component2 + " (" + name_component + ")"
			return testSwear(names)
		else:
			name_component = choice(self.nm2)
			name_component2 = choice(self.nm3)

			names = name_component + " " + name_component2 + " (" + name_component2 + ")"
		return testSwear(names)
