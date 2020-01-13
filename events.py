from datetime import date

EVENTS = [
    {
        "date": date(2013, 9, 5),
        "country": "DE",
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Bachelor of Science",
        "type": "graduation",
        "presentations": [{
            "title": "Ising-Ferromagnet auf Ad-HocNetzwerken",
            "pdf": "bachelorThesis.pdf",
            "type": "thesis",
        }],
    },
    {
        "date": date(2014, 8, 25),
        "date_end": date(2014, 9, 5),
        "country": "DE",
        "place": "Oldenburg",
        "name": "5th International Summer School on Modern Compuational Science: Compuational Quantum Chemistry",
        "link": "https://www.mcs.uni-oldenburg.de/64155.html",
        "type": "summerschool",
    },
    {
        "date": date(2014, 3, 30),
        "date_end": date(2014, 4, 4),
        "country": "DE",
        "place": "Dresden",
        "name": "DPG-Frühjahrstagung",
        "link": "https://dresden14.dpg-tagungen.de/",
        "type": "conference",
        "presentations": [{
            "title": "Ising-Ferromagnet on Proximity Graphs",
            "pdf": "2014DPG.pdf",
            "type": "poster",
        }],
    },
    {
        "date": date(2015, 9, 20),
        "date_end": date(2015, 9, 25),
        "country": "DE",
        "place": "Bad Honnef",
        "name": "Bad Honnef Physics School: Computational Physics of Complex and Disordered Systems",
        "link": "https://www.dpg-physik.de/veranstaltungen/2015/bad-honnef-physics-school-computational-physics-of-complex-and-disordered-systems",
        "type": "summerschool",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming",
            "pdf": "2015MCS.pdf",
            "type": "poster",
        }],
    },
    {
        "date": date(2015, 11, 6),
        "country": "DE",
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Master of Science",
        "type": "graduation",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming and Cutting Planes",
            "pdf": "masterThesis.pdf",
            "type": "thesis",
        }],
    },
    {
        "date": date(2016, 3, 1),
        "date_end": date(2019, 8, 31),
        "country": "DE",
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Institut für Physik (IfP), AG Compphys",
        "title": "wissenschaftlicher Mitarbeiter",
        "type": "work",
    },
    {
        "date": date(2016, 3, 6),
        "date_end": date(2016, 3, 11),
        "country": "DE",
        "place": "Regensburg",
        "name": "DPG-Frühjahrstagung",
        "link": "https://regensburg16.dpg-tagungen.de/",
        "type": "conference",
        "presentations": [{
            "title": "Phase Transitions of Disordered Travelling Salesperson Problems solved with Linear Programming and Cutting Planes",
            "pdf": "2016DPG.pdf",
            "type": "talk",
        }],
    },
    {
        "date": date(2016, 9, 1),
        "date_end": date(2016, 9, 30),
        "country": "FR",
        "place": "Université Paris-Sud, Orsay",
        "name": "Laboratoire de Physique Théorique et Modèles Statistiques (LPTMS)",
        "title": "research visitor",
        "type": "visit",
    },
    {
        "date": date(2016, 11, 24),
        "date_end": date(2016, 11, 26),
        "country": "DE",
        "place": "Leipzig",
        "name": "CompPhys16, 17th International NTZ-Workshop on New Developments in Computational Physics",
        "link": "https://www.physik.uni-leipzig.de/~janke/CompPhys16/",
        "type": "conference",
        "presentations": [{
            "title": "Convex Hulls of Self-Avoiding Random Walks: A Large-Deviation Study",
            "pdf": "2016CompPhys.pdf",
            "type": "poster",
        }],
    },
    {
        "date": date(2017, 3, 19),
        "date_end": date(2017, 3, 24),
        "country": "DE",
        "place": "Dresden",
        "name": "DPG-Frühjahrstagung",
        "link": "https://dresden17.dpg-tagungen.de/",
        "type": "conference",
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
        "country": "IT",
        "place": "Bruneck",
        "name": "Fundamental Problems in Statistical Physics XIV",
        "link": "https://fpspxiv.sciencesconf.org/",
        "type": "summerschool",
    },
    {
        "date": date(2017, 11, 30),
        "date_end": date(2017, 12, 2),
        "country": "DE",
        "place": "Leipzig",
        "name": "CompPhys17, 18th International NTZ-Workshop on New Developments in Computational Physics",
        "link": "https://www.physik.uni-leipzig.de/~janke/CompPhys17/",
        "type": "conference",
        "presentations": [{
            "title": "Linear Programming and Cutting Planes for Ground States and Excited States of the Traveling Salesperson Problem",
            "pdf": "2017CompPhys.pdf",
            "type": "talk",
        }],
    },
    {
        "date": date(2018, 3, 11),
        "date_end": date(2018, 3, 16),
        "country": "DE",
        "place": "Berlin",
        "name": "DPG-Frühjahrstagung",
        "link": "https://berlin18.dpg-tagungen.de/",
        "type": "conference",
        "presentations": [{
            "title": "Linear Programming and Cutting Planes for Ground States and Excited States of the Traveling Salesperson Problem",
            "pdf": "2018DPG.pdf",
            "type": "talk",
        }],
    },
    {
        "date": date(2018, 7, 29),
        "date_end": date(2018, 8, 2),
        "country": "US",
        "place": "Davis, CA",
        "name": "XXX IUPAP Conference on Computational Physics",
        "link": "http://ccp2018.physics.ucdavis.edu",
        "type": "conference",
        "presentations": [{
            "title": "Large Deviations of Convex Hulls of Self-Avoiding Random Walks",
            "pdf": "2018CCP.pdf",
            "type": "talk",
        }],
    },
    {
        "date": date(2019, 3, 31),
        "date_end": date(2019, 4, 5),
        "country": "DE",
        "place": "Regensburg",
        "name": "DPG-Frühjahrstagung",
        "link": "https://regensburg19.dpg-tagungen.de/",
        "type": "conference",
        "presentations": [{
            "title": "Ground-state energy distribution of noninteracting fermions with a random energy spectrum",
            "pdf": "2019DPG.pdf",
            "type": "talk",
        }],
    },
    {
        "date": date(2019, 3, 19),
        "country": "DE",
        "place": "Carl von Ossietzky Universität Oldenburg",
        "name": "Doktor der Naturwissenschaften (Dr. rer. nat.)",
        "type": "graduation",
        "presentations": [
            {
                "title": "Large Deviations of Convex Hulls of Random Walks and Other Stochastic Models",
                "pdf": "dissertation.pdf",
                "type": "thesis",
                "doi": "10.5281/zenodo.3377931",
            },
            {
                "title": "Large Deviations of Convex Hulls of Random Walks and Other Stochastic Models",
                "pdf": "disputation.pdf",
                "type": "talk",
            }
        ],
    },
    {
        "date": date(2019, 9, 1),
        "date_end": date(2020, 8, 31),
        "country": "FR",
        "place": "CY Cergy Paris Université",
        "name": "Laboratoire de Physique Théorique et Modélisation (LPTM)",
        "title": "Postdoc",
        "type": "work",
    },
]

import pycountry
for i in EVENTS:
    if "country" in i:
        i["country"] = pycountry.countries.get(alpha_2=i["country"]).name
