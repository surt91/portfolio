from datetime import date

EVENTS = [
    {
        "date": date(2013, 9, 5),
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Bachelor of Science",
        "presentations": [{
            "title": "Ising-Ferromagnet auf Ad-HocNetzwerken",
            "pdf": "bachelorThesis.pdf",
            "type": "thesis",
        }],
    },
    {
        "date": date(2014, 8, 25),
        "date_end": date(2014, 9, 5),
        "place": "Oldenburg",
        "name": "5th International Summer School on Modern Compuational Science Compuational Quantum Chemistry",
        "link": "https://www.mcs.uni-oldenburg.de/64155.html",
    },
    {
        "date": date(2014, 3, 30),
        "date_end": date(2014, 4, 4),
        "place": "Dresden",
        "name": "DPG-Frühjahrstagung",
        "link": "http://dresden14.dpg-tagungen.de/",
        "presentations": [{
            "title": "Ising-Ferromagnet on Proximity Graphs",
            "pdf": "2014DPG.pdf",
            "type": "poster",
        }],
    },
    {
        "date": date(2015, 9, 20),
        "date_end": date(2015, 9, 25),
        "place": "Bad Honnef",
        "name": "Bad Honnef Physics School: Computational Physics of Complex and Disordered Systems",
        "link": "https://www.dpg-physik.de/veranstaltungen/2015/bad-honnef-physics-school-computational-physics-of-complex-and-disordered-systems",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming",
            "pdf": "2015MCS.pdf",
            "type": "poster",
        }],
    },
    {
        "date": date(2015, 11, 6),
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Master of Science",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming and Cutting Planes",
            "pdf": "masterThesis.pdf",
            "type": "thesis",
        }],
    },
    {
        "date": date(2016, 3, 6),
        "date_end": date(2016, 3, 11),
        "place": "Regensburg",
        "name": "DPG-Frühjahrstagung",
        "link": "http://regensburg16.dpg-tagungen.de/",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming and Cutting Planes",
            "pdf": "2016DPG",
            "type": "talk",
        }],
    },
    {
        "date": date(2016, 11, 24),
        "date_end": date(2016, 11, 26),
        "place": "Leipzig",
        "name": "CompPhys16, 17th International NTZ-Workshop on New Developments in Computational Physics",
        "link": "https://www.physik.uni-leipzig.de/~janke/CompPhys16/",
        "presentations": [{
            "title": "Convex Hulls of Self-Avoiding Random Walks: A Large-Deviation Study",
            "pdf": "2016CompPhys",
            "type": "poster",
        }],
    },
    {
        "date": date(2017, 3, 19),
        "date_end": date(2017, 3, 24),
        "place": "Dresden",
        "name": "DPG-Frühjahrstagung",
        "link": "http://dresden17.dpg-tagungen.de/",
        "presentations": [
            {
                "title": "Convex Hulls of Self-Avoiding Random Walks: A Large-Deviation Study",
                "pdf": "2017DPG.pdf",
                "type": "poster",
            },
            {
                "title": "Convex Hulls of Random Walks in High Dimensions: A Large-Deviation Study",
                "link": "https://dpg2017.schawe.me/",
                "type": "talk"
            }
        ]
    },
    {
        "date": date(2017, 7, 16),
        "date_end": date(2017, 7, 29),
        "place": "Bruneck, Italia",
        "name": "Fundamental Problems in Statistical Physics XIV",
        "link": "https://fpspxiv.sciencesconf.org/",
    },
    {
        "date": date(2017, 11, 30),
        "date_end": date(2017, 12, 2),
        "place": "Leipzig",
        "name": "CompPhys17, 18th International NTZ-Workshop on New Developments in Computational Physics",
        "link": "https://www.physik.uni-leipzig.de/~janke/CompPhys17/",
        "presentations": [{
            "title": "Linear Programming and Cutting Planes for Ground States and Excited States of the Traveling Salesperson Problem",
            "pdf": "2017CompPhys",
            "type": "talk",
        }],
    },
    {
        "date": date(2018, 3, 11),
        "date_end": date(2018, 3, 16),
        "place": "Berlin",
        "name": "DPG-Frühjahrstagung",
        "link": "http://berlin18.dpg-tagungen.de/",
        "presentations": [{
            "title": "Linear Programming and Cutting Planes for Ground States and Excited States of the Traveling Salesperson Problem",
            "pdf": "2018DPG",
            "type": "talk",
        }],
    },
    {
        "date": date(2018, 7, 29),
        "date_end": date(2018, 8, 2),
        "place": "Davis, USA",
        "name": "XXX IUPAP Conference on Computational Physics",
        "link": "http://ccp2018.physics.ucdavis.edu/",
        "presentations": [{
            "title": "Large Deviations of Convex Hulls of Self-Avoiding Random Walks",
            "pdf": "2018CCP",
            "type": "talk",
        }],
    },
    {
        "date": date(2018, 3, 31),
        "date_end": date(2018, 4, 5),
        "place": "Regensburg",
        "name": "DPG-Frühjahrstagung",
        "link": "http://regensburg19.dpg-tagungen.de/",
        "presentations": [{
            "title": "Ground-state energy distribution of noninteracting fermions with a random energy spectrum",
            "pdf": "2019DPG",
            "type": "talk",
        }],
    },
]