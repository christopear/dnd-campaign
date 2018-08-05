from random import choice

from people.names.swearCheck import testSwear

nm1 = ["Acrid", "Ancient", "Angry", "Antique", "Antsy", "Arrogant", "Auntie", "Babbling", "Baggy", "Batty", "Bawdy",
       "Bickering", "Biting", "Bitter", "Bizarre", "Black", "Blaring", "Blathering", "Bony", "Bumbling", "Bumpy",
       "Cackling", "Cheeky", "Chittering", "Chuckling", "Cold", "Cooking", "Coughing", "Crabby", "Crackling", "Crafty",
       "Craven", "Crazy", "Crinkling", "Croaking", "Crooked", "Cruel", "Crumbling", "Delirious", "Demonic", "Depraved",
       "Deranged", "Despicable", "Disfigured", "Dismal", "Dread", "Dreaming", "Drooling", "Dusty", "Erratic", "Feeble",
       "Feisty", "Filthy", "Flaky", "Frail", "Frantic", "Gabby", "Giddy", "Giggling", "Gloomy", "Glum", "Granny",
       "Gray", "Greasy", "Greedy", "Grouchy", "Grubby", "Haunting", "Heckling", "Humming", "Hungry", "Icky", "Jaded",
       "Jolly", "Knobby", "Knotty", "Laughing", "Lone", "Lonely", "Lurking", "Mad", "Moldy", "Murky", "Muttering",
       "Nosy", "Nutty", "Old", "Outlandish", "Pale", "Paltry", "Pesky", "Putrid", "Ragged", "Raggedy", "Rambling",
       "Rickety", "Rotten", "Salty", "Sassy", "Screeching", "Shabby", "Shady", "Shaggy", "Shaky", "Shoddy", "Shrieking",
       "Silent", "Silver", "Singing", "Skinny", "Sleeping", "Slumbering", "Smelly", "Snappy", "Snickering", "Snoopy",
       "Stinking", "Stumbling", "Twitching", "Vicious", "Volatile", "Weary", "Whistling", "Wicked", "Wild", "Wretched",
       "Wrinkling"]
nm2 = ["Ada", "Addie", "Adeline", "Agnes", "Alberta", "Alice", "Alicia", "Allie", "Alma", "Alta", "Amanda", "Amelia",
       "Amy", "Andrea", "Angela", "Anita", "Ann", "Anna", "Anne", "Annette", "Annie", "Antoinette", "April", "Arlene",
       "Audrey", "Barbara", "Beatrice", "Becky", "Belinda", "Bernice", "Bertha", "Bessie", "Beth", "Bette", "Bettie",
       "Betty", "Beulah", "Beverly", "Billie", "Blanche", "Bobbie", "Bonnie", "Brenda", "Carla", "Carmen", "Carol",
       "Carole", "Caroline", "Carolyn", "Carrie", "Catherine", "Cathy", "Cecelia", "Celia", "Charlene", "Charlotte",
       "Cheryl", "Christina", "Christine", "Cindy", "Claire", "Clara", "Claudia", "Cleo", "Colleen", "Connie",
       "Constance", "Cora", "Crystal", "Cynthia", "Daisy", "Dana", "Darlene", "Dawn", "Deanna", "Debbie", "Deborah",
       "Debra", "Della", "Delores", "Denise", "Diana", "Diane", "Dianne", "Dolores", "Donna", "Dora", "Doreen", "Doris",
       "Dorothea", "Dorothy", "Edith", "Edna", "Effie", "Eileen", "Elaine", "Eleanor", "Eliza", "Elizabeth", "Ella",
       "Ellen", "Eloise", "Elsie", "Elva", "Emily", "Emma", "Erma", "Essie", "Estella", "Estelle", "Esther", "Ethel",
       "Etta", "Eula", "Eunice", "Eva", "Evelyn", "Fannie", "Faye", "Felicia", "Fern", "Flora", "Florence", "Flossie",
       "Frances", "Freda", "Frieda", "Gail", "Gayle", "Geneva", "Genevieve", "Georgia", "Geraldine", "Gertrude", "Gina",
       "Gladys", "Glenda", "Gloria", "Goldie", "Grace", "Gwendolyn", "Hannah", "Harriet", "Hattie", "Hazel", "Heather",
       "Heidi", "Helen", "Henrietta", "Hilda", "Holly", "Ida", "Imogene", "Ina", "Inez", "Irene", "Irma", "Isabel",
       "Isabelle", "Iva", "Jackie", "Jacqueline", "Jamie", "Jan", "Jane", "Janet", "Janice", "Janie", "Janis", "Jean",
       "Jeanette", "Jeanne", "Jeannette", "Jennie", "Jennifer", "Jessie", "Jill", "Jo", "Joan", "Joann", "Joanne",
       "Jodi", "Jody", "Johnnie", "Josephine", "Joy", "Joyce", "Juanita", "Judith", "Judy", "Julia", "Julie", "June",
       "Karen", "Karla", "Katherine", "Kathleen", "Kathryn", "Kathy", "Katie", "Kay", "Kelly", "Kim", "Kimberly",
       "Kristen", "Kristin", "Kristine", "Laura", "Laurie", "Laverne", "Lela", "Lena", "Leola", "Leona", "Leslie",
       "Lila", "Lillian", "Lillie", "Linda", "Lisa", "Lizzie", "Lois", "Lola", "Lorene", "Loretta", "Lori", "Lorraine",
       "Lottie", "Louise", "Lucile", "Lucille", "Lucy", "Luella", "Lula", "Lydia", "Lynda", "Lynn", "Lynne", "Mabel",
       "Mable", "Madeline", "Mae", "Maggie", "Mamie", "Marcella", "Marcia", "Margaret", "Margie", "Marguerite", "Maria",
       "Marian", "Marianne", "Marie", "Marilyn", "Marion", "Marjorie", "Marlene", "Marsha", "Martha", "Mary", "Maryann",
       "Matilda", "Mattie", "Maude", "Maureen", "Maxine", "May", "Melanie", "Melinda", "Melissa", "Melody", "Michele",
       "Michelle", "Mildred", "Minnie", "Miriam", "Mollie", "Monica", "Muriel", "Myrna", "Myrtle", "Nancy", "Nannie",
       "Naomi", "Natalie", "Nell", "Nellie", "Nettie", "Nicole", "Nina", "Nora", "Norma", "Ola", "Olga", "Olive",
       "Ollie", "Opal", "Ora", "Pam", "Pamela", "Pat", "Patricia", "Patsy", "Patti", "Patty", "Paula", "Paulette",
       "Pauline", "Pearl", "Peggy", "Penny", "Phyllis", "Priscilla", "Rachel", "Ramona", "Rebecca", "Regina", "Renee",
       "Rhonda", "Rita", "Roberta", "Robin", "Rosa", "Rosalie", "Rose", "Rosemarie", "Rosemary", "Rosie", "Roxanne",
       "Ruby", "Ruth", "Sadie", "Sallie", "Sally", "Sandra", "Sandy", "Sara", "Sarah", "Shannon", "Shari", "Sharon",
       "Sheila", "Shelia", "Shelley", "Shelly", "Sheri", "Sherri", "Sherry", "Sheryl", "Shirley", "Sonya", "Sophia",
       "Sophie", "Stacey", "Stacy", "Stella", "Stephanie", "Sue", "Susan", "Susie", "Suzanne", "Sylvia", "Tamara",
       "Tami", "Tammie", "Tammy", "Tanya", "Teresa", "Terri", "Terry", "Thelma", "Theresa", "Tina", "Toni", "Tonya",
       "Tracey", "Traci", "Tracy", "Valerie", "Vanessa", "Velma", "Vera", "Verna", "Veronica", "Vicki", "Vickie",
       "Vicky", "Victoria", "Viola", "Violet", "Virgie", "Virginia", "Vivian", "Wanda", "Wendy", "Willie", "Wilma",
       "Winifred", "Yolanda", "Yvette", "Yvonne"]
nm3 = ["Beast", "Beetle", "Bitter", "Blind", "Blood", "Bog", "Bone", "Boulder", "Branch", "Chain", "Chalk", "Chicken",
       "Clot", "Cold", "Creep", "Critter", "Crypt", "Dark", "Dead", "Devil", "Dirt", "Doll", "Dreck", "Dust", "Fang",
       "Filth", "Fire", "Flame", "Flesh", "Fowl", "Frog", "Gnat", "Grave", "Grease", "Green", "Grim", "Grime",
       "Gristle", "Gunk", "Horn", "Ink", "Knuckle", "Lard", "Light", "Marble", "Marsh", "Meat", "Mire", "Moon", "Mouse",
       "Muck", "Mud", "Nerve", "Night", "Ooze", "Pest", "Pig", "Powder", "Quill", "Rat", "Raw", "Red", "Rock", "Rodent",
       "Root", "Rubble", "Salt", "Scale", "Scrap", "Silt", "Slime", "Slop", "Smoke", "Snail", "Snake", "Soil", "Soot",
       "Spider", "Spite", "Spot", "Sprig", "Stew", "Stitch", "Stone", "Swamp", "Tallow", "Tear", "Thatch", "Titch",
       "Toad", "Toe", "Twig", "Twist", "Vein", "Vermin", "Waste", "Wax", "Web", "Wood", "Wrinkle"]
nm4 = ["chewer", "wart", "teeth", "gums", "bones", "wallow", "tooth", "willow", "stealer", "mouth", "wiggle", "back",
       "bend", "bite", "biter", "bone", "breath", "cheek", "cheeks", "chin", "cough", "cougher", "counter", "cracker",
       "finger", "fingers", "foot", "feet", "growth", "hand", "hands", "heart", "hide", "hook", "joint", "joints",
       "knee", "knees", "leg", "legs", "mask", "mind", "mouth", "body", "sister", "face", "babbler", "baker", "belcher",
       "boggle", "bristle", "cackle", "carver", "cleaver", "cobble", "coddler", "crackle", "cradle", "cradler",
       "crinkle", "croaker", "dabble", "dangler", "dipper", "dribble", "dribbler", "fiddle", "fidget", "giggle",
       "giggler", "goggle", "jangle", "jiggle", "jumbler", "lurker", "meddler", "mingle", "mingler", "mumbler",
       "mutterer", "nibbler", "nuzzle", "paddle", "paddler", "prattler", "rambler", "ramble", "rattle", "rattler",
       "rumbler", "scrambler", "scratcher", "shifter", "shuffler", "sifter", "singer", "skewer", "soother", "spitter",
       "startler", "startle", "squirmer", "stumbler", "stumble", "surge", "switcher", "tangler", "tickler", "tinkerer",
       "toppler", "trampler", "tremble", "trembler", "trick", "trickle", "tumbler", "twitch", "twitcher", "waddle",
       "waggle", "whistle", "whistler", "whittle", "wiggle", "wrangle", "wrangler"]


def nameGen(gender, has_last_name=True):
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


def nameSur():
    name_component3 = choice(nm3)
    name_component4 = choice(nm4)
    return testSwear(name_component3 + name_component4)


def nameFem():
    name_component = choice(nm1)
    name_component2 = choice(nm2)

    return testSwear(name_component + " " + name_component2)
