from constructs.race import Race


def generate_name(race, gender, count=1):
    retter = []

    for i in range(0, count):
        if race == Race.Beholders:
            from people.races.dndBeholders import nameGen
            retter.append(nameGen(gender))
        if race == Race.Changelings:
            from people.races.dndChangelings import nameGen
            retter.append(nameGen(gender))
        if race == Race.DeepGnome:
            from people.races.dndDeepGnome import nameGen
            retter.append(nameGen(gender))
        if race == Race.Deva:
            from people.races.dndDevaNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Dragonborn:
            from people.races.dndDragonbornNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Drow:
            from people.races.dndDrowNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Dwarf:
            from people.races.dndDwarfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Eladrin:
            from people.races.dndEladrinNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Elf:
            from people.races.dndElfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Genasi:
            from people.races.dndGenasi import nameGen
            retter.append(nameGen(gender))
        if race == Race.Githzerai:
            from people.races.dndGithzeraiNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Gnoll:
            from people.races.dndGnollNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Gnome:
            from people.races.dndGnomeNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Goliath:
            from people.races.dndGoliathNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Hag:
            from people.races.dndHagNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Halfelf:
            from people.races.dndHalfelfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Halfling:
            from people.races.dndHalflingNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Human:
            from people.races.dndHumanNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Kenku:
            from people.races.dndKenkuNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Kobolds:
            from people.races.dndKobolds import nameGen
            retter.append(nameGen(gender))
        if race == Race.Lizardfolk:
            from people.races.dndLizardfolkNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.MindFlayers:
            from people.races.dndMindFlayers import nameGen
            retter.append(nameGen(gender))
        if race == Race.Minotaur:
            from people.races.dndMinotaurNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Orc:
            from people.races.dndOrcNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Orcs:
            from people.races.dndOrcs import nameGen
            retter.append(nameGen(gender))
        if race == Race.Shardmind:
            from people.races.dndShardmindNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Shifter:
            from people.races.dndShifterNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Tabaxi:
            from people.races.dndTabaxiNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Tiefling:
            from people.races.dndTieflingNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Triton:
            from people.races.dndTriton import nameGen
            retter.append(nameGen(gender))
        if race == Race.Warforged:
            from people.races.dndWarforged import nameGen
            retter.append(nameGen(gender))
        if race == Race.Wilden:
            from people.races.dndWildenNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.YuanTi:
            from people.races.dndYuanTi import nameGen
            retter.append(nameGen(gender))
        if race == Race.Aarakocra:
            from people.races.dndAarakocra import nameGen
            retter.append(nameGen(gender))
        if race == Race.Aasimar:
            from people.races.dndAasimar import nameGen
            retter.append(nameGen(gender))

    return retter
