# Story data for the Sunday 22 November 2026 front page.
# Every headline story below was checked against a live source that reports it
# as news of Sunday 22 November 2026 (UTC) -- it happened, or was first
# reported, on that day in some time zone. Stories whose events belong to an
# earlier day live in LEFT_OUT with their real dates, however tempting they
# were as headlines.
#
# tag: CONFIRMED = an actor's own dated announcement/report of the day.
#      REPORTED = carried as today's news by the named outlets on 22 Nov.

DATE_LINE = "SUNDAY 22 NOVEMBER 2026"

LEADS = [
    {
        "kicker": "UKRAINE WAR · OVERNIGHT",
        "headline": "RUSSIA UNLEASHES 400 DRONES AND 110 MISSILES ON UKRAINE",
        "body": [
            "One of the war's largest aerial barrages struck Kyiv's",
            "bridges and a residential block in Lviv, where 2 died and",
            "10 were hurt; Kyiv's toll still rising through the morning.",
        ],
        "tag": "REPORTED · Reuters / Al Jazeera wires",
        "region": "Europe", "field": "War & Security",
    },
    {
        "kicker": "IRAN WAR · STRAIT OF HORMUZ",
        "headline": "BAHRAIN SAYS IRANIAN ATTACK SETS INDUSTRIAL SITE ABLAZE",
        "body": [
            "Two tankers are struck near Oman as Tehran tightens its",
            "grip on Hormuz shipping; a third is said to have hit a",
            "naval mine. Gulf states condemn the attacks on Bahrain.",
        ],
        "tag": "REPORTED · Al Jazeera / UKMTO",
        "region": "Middle East", "field": "War & Security",
    },
    {
        "kicker": "CLIMATE · COP31, ANTALYA",
        "headline": "CLIMATE TALKS NEAR FINAL DEAL AFTER FOSSIL-FUEL DEADLOCK",
        "body": [
            "Summit presidents Australia and Turkey table a package",
            "they say every party can accept; the plenary reconvenes",
            "on Sunday morning in Antalya to approve the text.",
        ],
        "tag": "REPORTED · Reuters, Antalya, Nov 22",
        "region": "Europe", "field": "Climate",
    },
]

# region -> list of (headline, tag, field)
INDEX = {
    "EUROPE": [
        ("Russian missile crashes in Poland; Warsaw flags a 'provocation', NATO jets patrol", "REPORTED · Reuters wires", "War & Security"),
        ("Drones hit Russia-bound cargo ship in the Gulf of Finland; Helsinki tightens security", "REPORTED · BBC / ToI", "War & Security"),
        ("Denmark accuses Russia of plotting to assassinate a US-Ukrainian rapper", "REPORTED · BBC", "Crime & Law"),
        ("IG Metall calls 24-hour strike: 23,000 German car and shipyard workers out Monday", "CONFIRMED · Reuters, Nov 22", "Labour"),
        ("EU budget plan floats a 3% levy on big tech; France rejects it", "REPORTED · wires", "Economy"),
        ("Cost-of-living protests sweep across Europe's cities", "REPORTED · BBC", "Politics"),
        ("French officers sentenced over the filmed beating of producer Michel Zecler", "REPORTED · BBC", "Crime & Law"),
        ("France probes Depardieu and an author over a gang-rape claim", "REPORTED · AFP / ToI", "Crime & Law"),
        ("Blair: Britain should rejoin the EU only if it leads on technology", "REPORTED · BBC", "Politics"),
        ("Princess Catherine opens up about how cancer changed her, in a new documentary", "REPORTED · BBC", "Culture"),
    ],
    "MIDDLE EAST": [
        ("Iran's president: the country faces a 'silent economic war'", "REPORTED · Al Jazeera", "Politics"),
        ("Iran holds talks with Qatari mediators, urges the US to accept its conditions", "REPORTED · Al Jazeera", "Diplomacy"),
        ("Trump: 'I want a permanent deal that stops Iran getting nuclear weapons'", "REPORTED · Al Jazeera / Fox News", "Diplomacy"),
        ("Eisenkot invites Netanyahu's Likud into talks to form Israel's government", "REPORTED · ToI / wires", "Politics"),
        ("Lebanon's president demands an Israeli withdrawal, decries Iran's interference", "REPORTED · Al Jazeera", "Diplomacy"),
        ("UNIFIL begins handing control of south Lebanon positions to the Lebanese army", "REPORTED · wires", "War & Security"),
        ("Iraqi federal forces deploy in Jurf al-Sakhar as the first militia unit pulls out", "REPORTED · Reuters", "War & Security"),
        ("Palestinians killed and wounded as Israeli fire breaches the Gaza ceasefire", "REPORTED · Al Jazeera", "War & Security"),
        ("Yemen's Taiz faces a services collapse as the Houthi siege nears a third month", "REPORTED · wires", "War & Security"),
    ],
    "NORTH AMERICA": [
        ("FBI investigates an apparent hack of its own criminal database", "REPORTED · BBC", "Crime & Law"),
        ("Man convicted of starting the Palisades fire in Los Angeles", "REPORTED · BBC", "Crime & Law"),
        ("Trump orders federal contractors to clear Congress requests with the White House", "REPORTED · wires", "Politics"),
        ("US 'willing to accept' a Latin American as the next UN chief, says Waltz", "REPORTED · wires", "Diplomacy"),
        ("Mamdani announces a plan to close New York's Rikers Island jail by 2032", "REPORTED · BBC", "Politics"),
        ("Days of heavy rain flood streets across Florida", "REPORTED · Al Jazeera", "Weather"),
        ("Ottawa shrugs off a report of US military restrictions on Canada", "REPORTED · wires", "Diplomacy"),
        ("A lock of George Washington's hair sells for $4,000", "REPORTED · BBC", "Culture"),
    ],
    "LATIN AMERICA": [
        ("Mexico captures FBI most-wanted cartel boss 'El Chapo Isidro' in a shoot-out", "REPORTED · BBC / Al Jazeera", "Crime & Law"),
        ("Cartel arrest sparks deadly violence across Sinaloa; 11 killed", "REPORTED · ToI", "Crime & Law"),
        ("Brazil's jailed ex-president Bolsonaro is rushed to intensive care", "REPORTED · ToI / Reuters", "Health"),
    ],
    "ASIA-PACIFIC": [
        ("EU and Indonesia sign a trade pact after 10 years; 98.5% of tariffs to fall", "REPORTED · wires", "Trade"),
        ("Hong Kong's Election Committee polls open: 856 candidates chase 723 seats", "CONFIRMED · SCMP / CLB", "Elections"),
        ("Australia's Marles blasts the US budget office over its AUKUS submarine warning", "CONFIRMED · Reuters, Sydney, Nov 22", "Diplomacy"),
        ("A pilotless air taxi carries passengers in Japan in a first autonomous flight", "REPORTED · wires", "Technology"),
        ("Bootleg alcohol kills 11 and poisons 180 in India's Manipur state", "REPORTED · Al Jazeera", "Health"),
        ("India's Youth Congress gives Meta a 7-day ultimatum over removed accounts", "REPORTED · Al Jazeera", "Technology"),
        ("Pakistan's climate minister heads to New Delhi for an SCO dialogue", "REPORTED · ToI", "Diplomacy"),
    ],
    "AFRICA": [
        ("Sudan's army moves to restore security across Blue Nile state", "REPORTED · wires", "War & Security"),
        ("South Africa's ANC fights to hold its key cities after an election setback", "REPORTED · BBC", "Politics"),
    ],
    "SCIENCE, TECH & HEALTH": [
        ("A claimed proof of the Riemann hypothesis, drafted with Claude, stuns mathematicians", "REPORTED · Al Jazeera / BBC", "Science"),
        ("UN: one in four partnered women cannot refuse sex, one in three in Arab states", "REPORTED · UN via wires", "Health"),
        ("US declassifies more UFO footage filmed over the Middle East", "REPORTED · BBC", "Science"),
    ],
    "SPORT": [
        ("Sunday's Premier League headliner: Liverpool host Manchester United", "REPORTED · BBC", "Sport"),
        ("Zverev reaches the ATP Finals title match; the champion is crowned in Turin today", "REPORTED · Reuters wires", "Sport"),
        ("India v New Zealand, first Test: KL Rahul's long evolution in focus", "REPORTED · Cricbuzz", "Sport"),
        ("Sha Tin farewells Romantic Warrior, the world's highest-earning racehorse", "REPORTED · HKJC / CLB", "Sport"),
    ],
}

# Tempting headlines that belong to earlier days -- shown, dated, and left out.
LEFT_OUT = [
    ("Bayelsa, Nigeria: funeral boat disaster on the Nun River, 50+ dead, ~300 missing", "20 NOV"),
    ("Missouri, US: judge approves Bayer's $7.25bn Roundup cancer settlement", "20 NOV"),
    ("Wall Street: AI sell-off caps the worst week since Covid; Anthropic's debut flops", "20 NOV"),
    ("Kyiv: Zelensky hosts UK defence secretary Streeting, who calls Putin a 'killer'", "21 NOV"),
    ("Basra, Iraq: fire at the Hartha power station kills 4 and injures 35", "21 NOV"),
    ("Nations Championship rugby: Australia edge Wales 29-26; France beat Argentina", "21 NOV"),
    ("Riyadh: Saudi-led coalition downs Houthi missiles aimed at the capital", "21 NOV"),
    ("Sofia: Iotova is elected Bulgaria's first woman president", "1 NOV"),
]

TIMELINE = [
    ("00:00", "Polls open in Hong Kong"),
    ("OVERNIGHT", "400+ drones, 110 missiles hit Ukraine"),
    ("EARLY HRS", "Bahrain reports Iranian attack"),
    ("LATE NIGHT", "COP31 deal text tabled in Antalya"),
    ("SUNDAY AM", "AUKUS row; Berlin strike call"),
    ("SUNDAY", "Cartel boss captured in Mexico"),
]

# Numbered pins for the map: (number, place label, col, row) on the dot grid.
PINS = [
    (1, "Kyiv barrage", 67, 9),
    (2, "Missile in Poland", 62, 6),
    (3, "COP31 Antalya", 64, 14),
    (4, "Bahrain attack", 73, 19),
    (5, "Hormuz tankers", 77, 16),
    (6, "Gaza ceasefire breaches", 68, 17),
    (7, "Berlin strike call", 58, 8),
    (8, "Hong Kong polls", 93, 19),
    (9, "EU-Indonesia pact", 91, 28),
    (10, "AUKUS row, Sydney", 105, 38),
    (11, "Blue Nile, Sudan", 67, 22),
    (12, "Cartel boss held, Mexico", 20, 18),
    (13, "Palisades verdict, LA", 17, 13),
    (14, "Meta protest, Delhi", 81, 17),
]

NUMBERS_BOX = [
    "400+ drones and 110 missiles in one night over Ukraine",
    "98.5% of EU-Indonesia tariffs to be eliminated",
    "856 candidates for 723 Hong Kong committee seats",
    "23,000 German workers called out on strike Monday",
    "$7.25bn Roundup settlement -- filed under LEFT OUT (20 Nov)",
]
