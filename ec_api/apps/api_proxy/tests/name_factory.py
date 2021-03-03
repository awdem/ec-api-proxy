import random

org_prefixes = {
    "Aberdeen",
    "Ayr",
    "Bedford",
    "Berk",
    "Buckingham",
    "Cambridge",
    "Carmarthen",
    "Che",
    "Clackmannan",
    "Denbigh",
    "Derby",
    "Dunbarton",
    "Flint",
    "Gloucester",
    "Hamp",
    "Hereford",
    "Hertford",
    "Huntingdon",
    "Lanark",
    "Lanca",
    "Leicester",
    "Lincoln",
    "Monmouth",
    "Northampton",
    "Nottingham",
    "Oxford",
    "Pembroke",
    "Renfrew",
    "Richmond",
    "Shrop",
    "Stafford",
    "Warwick",
    "Wilt",
    "Worcester",
    "York",
    "Aller",
    "Calder",
    "Roch",
    "Rossen",
    "Rye",
    "Ash",
    "Chester",
    "En",
    "Hat",
    "Lich",
    "Mans",
    "Shef",
    "Wake",
    "Ban",
    "Basil",
    "Croy",
    "Hilling",
    "Mal",
    "Swin",
    "Basing",
    "Birming",
    "Chelten",
    "Dagen",
    "Dur",
    "Fare",
    "Ful",
    "Graves",
    "Hors",
    "Lewis",
    "New",
    "Notting",
    "Old",
    "Rother",
    "Walt",
    "Woking",
    "Wrex",
    "Bed",
    "Bos",
    "Tam",
    "Wands",
    "Ash",
    "Bed",
    "Brad",
    "Chelms",
    "Dart",
    "Guild",
    "Ox",
    "Roch",
    "Sal",
    "Staf",
    "Tel",
    "Traf",
    "Uttles",
    "Wat",
    "Brent",
    "Charn",
    "Sher",
    "Aberdeen",
    "Ayr",
    "Bedford",
    "Berk",
    "Buckingham",
    "Cambridge",
    "Carmarthen",
    "Che",
    "Clackmannan",
    "Denbigh",
    "Derby",
    "Dunbarton",
    "Flint",
    "Gloucester",
    "Hamp",
    "Hereford",
    "Hertford",
    "Huntingdon",
    "Lanark",
    "Lanca",
    "Leicester",
    "Lincoln",
    "Monmouth",
    "Northampton",
    "Nottingham",
    "Oxford",
    "Pembroke",
    "Renfrew",
    "Richmond",
    "Shrop",
    "Stafford",
    "Warwick",
    "Wilt",
    "Worcester",
    "York",
    "Aller",
    "Calder",
    "Roch",
    "Rossen",
    "Rye",
    "Ash",
    "Chester",
    "En",
    "Hat",
    "Lich",
    "Mans",
    "Shef",
    "Wake",
    "Ban",
    "Basil",
    "Croy",
    "Hilling",
    "Mal",
    "Swin",
    "Basing",
    "Birming",
    "Chelten",
    "Dagen",
    "Dur",
    "Fare",
    "Ful",
    "Graves",
    "Hors",
    "Lewis",
    "New",
    "Notting",
    "Old",
    "Rother",
    "Walt",
    "Woking",
    "Wrex",
    "Bed",
    "Bos",
    "Tam",
    "Wands",
    "Ash",
    "Bed",
    "Brad",
    "Chelms",
    "Dart",
    "Guild",
    "Ox",
    "Roch",
    "Sal",
    "Staf",
    "Tel",
    "Traf",
    "Uttles",
    "Wat",
    "Brent",
    "Charn",
    "Sher",
}

ward_prefixes = {
    "Saws",
    "Woodset",
    "Cocker",
    "Stubbing",
    "Hubbers",
    "Westle",
    "Bar",
    "Over",
    "Beck",
    "Brix",
    "Eger",
    "Winter",
    "Whit",
    "Hunder",
    "Pic",
    "Al",
    "Doning",
    "Lin",
    "Ecking",
    "Chester",
    "Thurcas",
    "Ol",
    "Haggers",
    "Dithering",
    "Clop",
    "Whip",
    "Walling",
    "Letters",
    "Chopping",
    "Sis",
    "Stough",
    "Galmp",
    "Irthing",
    "Totting",
    "Salving",
    "Woods",
    "Ash",
    "Whis",
    "Neils",
    "Stur",
    "Colling",
    "Hunstan",
    "Bour",
    "Upper",
    "Aming",
    "Poul",
    "Willi",
    "Thurs",
    "Clut",
    "Riming",
    "Williams",
    "Essing",
    "Ribs",
    "Chedding",
    "Pren",
    "Pax",
    "Ribble",
    "Het",
    "Clough",
    "Bly",
    "Ay",
    "Terring",
    "Albrigh",
    "Galmp",
    "Sinning",
    "Lat",
    "Hillmor",
    "Alper",
    "Heading",
    "Bel",
    "Rusting",
    "Kings",
    "Alder",
    "Wheel",
    "Ac",
    "Alfre",
    "Ship",
    "Rals",
    "Scamp",
    "Staver",
    "Broning",
    "Calling",
    "Mister",
    "Cudding",
    "Aller",
    "Sprat",
    "Yap",
    "Kir",
    "Thurmas",
    "Faring",
    "Shurding",
    "Rep",
    "Longben",
    "Quin",
    "Bear",
    "Kinner",
    "Mos",
    "Pinx",
    "Kingsteign",
    "Stret",
    "Godin",
    "Nap",
    "Dip",
    "Gret",
    "Funting",
    "Bray",
    "Moul",
    "Cheving",
    "Wat",
    "Win",
    "Wigs",
    "Hat",
    "Til",
    "Haring",
    "Bux",
    "Ramp",
    "Sprows",
    "Wincan",
    "Frys",
    "Tuck",
    "Tup",
    "Wilming",
    "Cof",
    "Wollas",
    "Offing",
    "Cron",
    "Thurl",
    "Ather",
    "Swin",
    "Arling",
    "Crof",
    "Pel",
    "Tidding",
    "Paul",
    "Torring",
    "Dedding",
    "Nether",
    "Haux",
    "Gir",
    "Dinning",
    "Pember",
    "Woolas",
    "Scot",
    "Dray",
    "Per",
    "Es",
    "Kenning",
    "Doding",
    "Hol",
    "Craig",
    "Bebing",
    "Cressing",
    "War",
    "Murs",
    "Mil",
    "Gars",
    "Lyming",
    "Disting",
    "Tes",
    "Carl",
    "Pur",
    "Ashing",
    "Pendle",
    "Ea",
    "Tanker",
    "Kes",
    "Conis",
    "Duddings",
    "New",
    "Gower",
    "Longthorn",
    "Strat",
    "El",
    "Bromp",
    "Nymp",
    "Bret",
    "Dals",
    "Ashbur",
    "Little",
    "Whitting",
    "Westmes",
    "Cathering",
    "Hundle",
    "Abing",
    "Mal",
    "Crop",
    "Clin",
    "Coyl",
    "Taw",
    "Imping",
    "Todding",
    "Can",
    "Castle",
    "Badmin",
    "Gosber",
    "Lay",
    "Adling",
    "Wistas",
    "Wadding",
    "Uddings",
    "Clif",
    "Hecking",
    "Watling",
    "Chil",
    "Brother",
    "Clay",
    "Ley",
    "Skel",
    "Harling",
    "Chels",
    "Hin",
    "Urms",
    "Shel",
    "Leckhamp",
    "Eas",
    "Alfris",
    "Kensing",
    "Ormis",
    "Storring",
    "Brot",
    "Bishopsteign",
    "Bur",
    "Chir",
    "Rough",
    "Lemyng",
    "Etting",
    "Steven",
    "Stan",
    "Flix",
    "Tayn",
    "Cadox",
    "Mol",
    "Bec",
    "Whatling",
    "Milver",
    "Tadding",
    "Nes",
    "Pres",
    "Hop",
    "Littlehamp",
    "Chels",
    "Roys",
    "Tibber",
    "Yat",
    "Kinwar",
    "Thoro",
    "Tolling",
    "Har",
    "Johns",
    "Aylbur",
    "Wal",
    "Mor",
    "Thur",
    "Eccles",
    "Wel",
    "Alves",
    "Brough",
    "Stil",
    "Longstan",
    "Den",
    "Shil",
    "Tat",
    "Weigh",
    "Wot",
    "Pether",
    "Astley-Sut",
    "Harles",
    "Lilling",
    "Wyber",
    "Alvas",
    "Plunging",
    "Shilling",
    "Hamp",
    "Chittlehamp",
    "Coly",
    "Hay",
    "Northaller",
    "Harring",
    "Fenstan",
    "Cadding",
    "Cheri",
    "Breas",
    "Kimp",
    "Hamil",
    "Wough",
    "Werring",
    "Washing",
    "Sker",
    "Morris",
    "Mar",
    "Co",
    "Bamp",
    "My",
    "Riving",
    "Clac",
    "Darting",
    "Trumping",
    "Cromp",
    "Longhough",
    "Farling",
    "Woolaving",
    "Stevens",
    "Canning",
    "Wooddit",
    "Hilper",
    "Darling",
    "Fil",
    "Walber",
    "Welling",
    "Hather",
    "Stock",
    "Shers",
    "Edder",
    "Bru",
    "Balder",
    "Sels",
    "Gorles",
    "Charl",
    "Monks",
    "Sax",
    "Silver",
    "Wes",
    "Barlas",
    "Bedhamp",
    "Eux",
    "Hul",
    "Wimbling",
    "Leming",
    "Staugh",
    "Knut",
    "Mars",
    "Ox",
    "Knigh",
    "Edwal",
    "Glasshough",
    "Norman",
    "Hunting",
    "Wee",
    "Calver",
    "Shars",
    "Thurstas",
    "Mur",
    "Littlehemps",
    "Burs",
    "Kipping",
    "Fox",
    "Hamble",
    "Hove",
    "Wis",
    "Hal",
    "Lydding",
    "Wolstan",
    "Wolver",
    "Wenning",
    "Comber",
    "Sut",
    "Kine",
    "Newing",
    "Leigh",
    "Barns",
    "Ket",
    "Bough",
    "Dit",
    "Gilmer",
    "Chorl",
    "Brixing",
    "Gor",
    "Whar",
    "Briming",
    "Caun",
    "Fen",
    "Bit",
    "Assing",
    "Erding",
    "Rudbax",
    "Bishop",
    "Bris",
    "For",
    "Durring",
    "Hut",
    "Brigh",
    "Ander",
    "Hes",
    "Nunea",
    "Thros",
    "Sea",
    "Cor",
    "Surbi",
    "Wig",
    "Hun",
    "Wool",
    "Normans",
    "Mel",
    "Thorn",
    "Itching",
    "Adding",
    "Graf",
    "Nor",
    "Pux",
    "Working",
    "Haches",
    "Rowbar",
    "Feni",
    "Shirenew",
    "Livings",
    "Oul",
    "Homer",
    "Wink",
    "Clenchwar",
    "Dun",
    "Cleckhea",
    "Ships",
    "Hough",
    "Harving",
    "Codding",
    "Waver",
    "Brymp",
    "Norbi",
    "Tedding",
    "Duns",
    "Baillies",
    "Edgbas",
    "Comp",
    "Freming",
    "Thraps",
    "Leaming",
    "Ben",
    "Bier",
    "As",
    "Ex",
    "Alphing",
    "Cheddle",
    "Monk",
    "Frin",
    "Drewsteign",
    "Tokyng",
    "Hemling",
    "Leis",
    "Hogh",
    "Wools",
    "Cay",
    "Cal",
    "Grassing",
    "Dumbar",
    "Frat",
    "Augh",
    "Ough",
    "Easing",
    "Tros",
    "Bicking",
    "Carle",
    "Donning",
    "Dus",
    "Tythering",
    "Keding",
    "Dal",
    "Eving",
    "Rilling",
    "Wring",
    "Peckle",
    "Woolsing",
    "Kirkbur",
    "Edmon",
    "Cat",
    "Bolling",
    "Elling",
    "Shettles",
    "Tarle",
    "Alling",
    "Boning",
    "Credi",
    "Honi",
    "Brough",
    "Wybos",
    "Pot",
    "Barring",
    "Caster",
    "Bishops",
    "Mit",
    "Robroys",
    "Grindle",
    "Toller",
    "Quain",
    "Beigh",
    "Ken",
    "Mulbar",
    "Lo",
    "Rish",
    "Golding",
    "Cassing",
    "Pleasing",
    "Offer",
    "Wy",
    "Woot",
    "Oller",
    "Packing",
    "Hor",
    "Ruish",
    "Molling",
    "Stilling",
    "Gay",
    "Kimbol",
    "Apple",
    "Bemer",
    "Somer",
    "Congle",
    "Brat",
    "Hac",
    "Sheving",
    "Ever",
    "Swilling",
    "To",
    "Wiggin",
    "Hesling",
    "Newing",
    "Bac",
    "Yealmp",
    "Shaving",
    "Cubbing",
    "Hil",
    "Nec",
    "Wrox",
    "Or",
    "Roy",
    "Stanning",
    "King",
    "Pil",
    "Duckling",
    "Caws",
    "Brans",
    "Len",
    "Halber",
    "Minchinhamp",
    "Rat",
    "Parkes",
    "Penning",
    "Shepper",
    "Twer",
    "Lang",
    "Par",
    "Withing",
    "Chellas",
    "Bil",
    "Rusking",
    "Wedding",
    "Hackle",
    "Wit",
    "Sacris",
    "Chrys",
    "Osbas",
    "Arles",
    "Gun",
    "Frizing",
    "Holling",
    "Scor",
    "Middle",
    "Garsing",
    "Hea",
    "Wrighting",
    "Orping",
    "Claugh",
    "Hasling",
    "Wil",
    "Up",
    "Bramp",
    "Rudding",
    "Framp",
    "Blatching",
    "Aldermas",
    "Boul",
    "Bulking",
    "Grims",
    "Mux",
}

org_suffixes = {
    "shire",
    "dale",
    "field",
    "stead",
    "don",
    "stoke",
    "ham",
    "worth",
    "ford",
    "wood",
}

ward_suffixes = {
    "ton",
    "bridge",
    "dale",
    "ham",
}

ward_extra = {
    "Common",
    "North",
    "South",
    "East",
    "West",
    "Inner",
    "Outer",
}


def get_sample(data):
    return random.sample(data, 1)[0]


def make_ward_name(add_extra_name=True):
    pre = get_sample(ward_prefixes)
    suf = get_sample(ward_suffixes)
    name = "".join((pre, suf))

    # extras
    rand = random.randrange(1, 100)
    if rand > 0 and rand < 20:
        name = f"{name} {get_sample(ward_extra)}"

    if rand > 30 and rand < 35:
        name = f"{name}/{make_ward_name(add_extra_name=False)}"

    if rand > 35 and rand < 37:
        name = f"{name}-with-{make_ward_name(add_extra_name=False)}"

    if add_extra_name:
        if rand > 20 and rand < 30:
            name = f"{name} & {make_ward_name(add_extra_name=False)}"

    return name


def make_org_name():
    pre = get_sample(org_prefixes)
    suf = get_sample(org_suffixes)
    name = "".join((pre, suf))
    return name


if __name__ == "__main__":
    for i in range(20):
        print(make_org_name(), make_ward_name())
