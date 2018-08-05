from constructs.race import Race


def generate_name(race, gender, count=1):
    retter = []

    for i in range(0, count):
        if race == Race.Beholders:
            from people.names.dndBeholders import nameGen
            retter.append(nameGen(gender))
        if race == Race.Changelings:
            from people.names.dndChangelings import nameGen
            retter.append(nameGen(gender))
        if race == Race.DeepGnome:
            from people.names.dndDeepGnome import nameGen
            retter.append(nameGen(gender))
        if race == Race.Deva:
            from people.names.dndDevaNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Dragonborn:
            from people.names.dndDragonbornNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Drow:
            from people.names.dndDrowNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Dwarf:
            from people.names.dndDwarfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Eladrin:
            from people.names.dndEladrinNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Elf:
            from people.names.dndElfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Genasi:
            from people.names.dndGenasi import nameGen
            retter.append(nameGen(gender))
        if race == Race.Githzerai:
            from people.names.dndGithzeraiNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Gnoll:
            from people.names.dndGnollNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Gnome:
            from people.names.dndGnomeNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Goliath:
            from people.names.dndGoliathNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Hag:
            from people.names.dndHagNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Halfelf:
            from people.names.dndHalfelfNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Halfling:
            from people.names.dndHalflingNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Human:
            from people.names.dndHumanNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Kenku:
            from people.names.dndKenkuNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Kobolds:
            from people.names.dndKobolds import nameGen
            retter.append(nameGen(gender))
        if race == Race.Lizardfolk:
            from people.names.dndLizardfolkNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.MindFlayers:
            from people.names.dndMindFlayers import nameGen
            retter.append(nameGen(gender))
        if race == Race.Minotaur:
            from people.names.dndMinotaurNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Orc:
            from people.names.dndOrcNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Orcs:
            from people.names.dndOrcs import nameGen
            retter.append(nameGen(gender))
        if race == Race.Shardmind:
            from people.names.dndShardmindNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Shifter:
            from people.names.dndShifterNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Tabaxi:
            from people.names.dndTabaxiNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Tiefling:
            from people.names.dndTieflingNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.Triton:
            from people.names.dndTriton import nameGen
            retter.append(nameGen(gender))
        if race == Race.Warforged:
            from people.names.dndWarforged import nameGen
            retter.append(nameGen(gender))
        if race == Race.Wilden:
            from people.names.dndWildenNames import nameGen
            retter.append(nameGen(gender))
        if race == Race.YuanTi:
            from people.names.dndYuanTi import nameGen
            retter.append(nameGen(gender))
        if race == Race.Aarakocra:
            from people.names.dndAarakocra import nameGen
            retter.append(nameGen(gender))
        if race == Race.Aasimar:
            from people.names.dndAasimar import nameGen
            retter.append(nameGen(gender))

    return retter
