"""Builds one page per town we cover: <slug>/index.html.

Run from the repo root after services.py:  python _build/areas.py
Uses the same template as the service pages (services.page), so layout, nav,
footer and schema stay identical. Edit the copy in AREAS below.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import services as S

COMMON_INCLUDED = [
    ("Air conditioning installation", "Split and multi-split systems for bedrooms, lofts, offices and garden rooms. Cools in summer, heats in winter."),
    ("AC servicing and repairs", "Annual servicing, cleaning and fault-finding, so the system stays efficient and the warranty stays valid."),
    ("Garden rooms and offices", "Insulated, cedar-clad and wired for power. Built to measure, with AC fitted by our own engineers."),
    ("Extensions", "Single-storey and kitchen extensions, from planning drawings to the finished room."),
    ("Refurbishments", "Kitchens and bathrooms stripped out and refitted by one crew."),
    ("Landscaping", "Patios, paths, fencing and lawns, often finished alongside a garden room."),
]

AREAS = [
    {
        "slug": "brentwood",
        "trade": "ac",
        "nav": "Brentwood",
        "cta_title": "Get a Price for Your Job in Brentwood",
        "service_param": None,
        "title": "Air Conditioning &amp; Garden Rooms in Brentwood | OAK Group",
        "description": "Air conditioning installation and servicing, garden rooms and extensions in Brentwood, Shenfield, Hutton and Ingatestone. Based in West Horndon, minutes away. Free site visit and fixed quote.",
        "schema_name": "Air conditioning and building work in Brentwood",
        "eyebrow": "Brentwood, Essex",
        "h1": "Air Conditioning &amp; Garden Rooms in <em>Brentwood</em>",
        "lead": "We're based in West Horndon, inside the Brentwood borough. AC that heats and cools, garden rooms and extensions, from a local team you can actually reach.",
        "facts": ["Based in the borough", "Free site visit", "Fixed quote"],
        "img": "hero-garden-aircon-summerhouse.jpg",
        "img_alt": "Garden room with an air conditioning unit in an Essex garden",
        "tag": "Local to CM13, CM14, CM15",
        "kicker": "Brentwood is our <mark>home patch</mark>. Most jobs here are a short drive from the yard.",
        "intro": [
            "A lot of Brentwood homes are 1930s semis and detached houses with long gardens, and plenty of people here now work from home a few days a week. That usually means one of two things: a bedroom or loft that gets too hot in summer, or the need for a proper room to work in that isn't the kitchen table.",
            "<strong>We do both.</strong> Our engineers fit air conditioning that cools in summer and heats in winter, and our builders put up insulated garden rooms with the AC already in. One company, one quote, one person to call.",
        ],
        "included_title": "What We Do in Brentwood",
        "included_sub": "Covering Brentwood town, Shenfield, Hutton, Ingatestone, Ingrave, Herongate, Warley and Pilgrims Hatch.",
        "included": COMMON_INCLUDED,
        "why": [
            ("Local, not a call centre", "We're based in West Horndon. The person who quotes is the person who stays on the job."),
            ("Two trades, one company", "Building work and air conditioning under one roof, so nobody blames someone else's work."),
            ("The price quoted is the price paid", "We see the job before we price it, so the number doesn't move."),
        ],
        "faq": [
            ("Do you cover my part of Brentwood?",
             ["Yes. We cover the whole borough, including Shenfield, Hutton, Ingatestone, Ingrave, Herongate, Warley, Pilgrims Hatch and Doddinghurst. Put your postcode in the quote form and we'll confirm."]),
            ("Do I need planning permission for air conditioning?",
             ["Most single outdoor units on a house count as permitted development, as long as they're sited sensibly and kept away from the boundary. Flats, listed buildings and conservation areas, including parts of Brentwood, can need consent. We check at the site visit."]),
            ("Can a garden room be used as a home office all year?",
             ["Yes, if it's insulated properly and heated. We fit a split AC system that heats in winter and cools in summer, so the room works in January as well as July."]),
            ("How quickly can you come out?",
             ["We're local, so site visits are usually quick to arrange. We reply to every quote request within one working day."]),
        ],
        "areas": ["Brentwood", "Shenfield", "Hutton", "Ingatestone", "Ingrave", "Herongate", "Warley", "Pilgrims Hatch", "Doddinghurst", "West Horndon"],
        "area_title": "Covering the Whole Brentwood Borough",
        "area_text": "From Shenfield and Hutton to Ingatestone and West Horndon, where we're based.",
        "area_fine": "Not sure if you're in range? Put your postcode in the quote form and we'll tell you straight away.",
        "related": ["air-conditioning-installation", "garden-rooms", "air-conditioning-maintenance"],
    },
    {
        "slug": "upminster",
        "trade": "ac",
        "nav": "Upminster",
        "cta_title": "Get a Price for Your Job in Upminster",
        "service_param": None,
        "title": "Air Conditioning &amp; Garden Rooms in Upminster | OAK Group",
        "description": "Air conditioning installation and servicing, garden rooms, extensions and refurbishments in Upminster, Cranham and Corbets Tey. A local team from nearby West Horndon. Free site visit.",
        "schema_name": "Air conditioning and building work in Upminster",
        "eyebrow": "Upminster, Havering",
        "h1": "Air Conditioning &amp; Garden Rooms in <em>Upminster</em>",
        "lead": "Just up the road from our base in West Horndon. AC that keeps bedrooms cool in summer and warm in winter, plus garden rooms, extensions and refurbishments.",
        "facts": ["Minutes from our base", "Free site visit", "Fixed quote"],
        "img": "aircon-install-residential.jpg",
        "img_alt": "Wall-mounted air conditioning unit installed in a bedroom",
        "tag": "Local to RM14",
        "kicker": "Upminster homes are built to last. We make them <mark>comfortable all year</mark>.",
        "intro": [
            "Upminster and Cranham are full of solid 1930s houses with good-sized gardens. They hold heat in the loft bedrooms in summer and lose it in winter, and the gardens have room for more than a shed.",
            "<strong>We fit split air conditioning that heats as well as cools</strong>, sized for the room rather than oversold, and we build insulated garden rooms and extensions with the same crew. You deal with one company from the first visit to the handover.",
        ],
        "included_title": "What We Do in Upminster",
        "included_sub": "Covering Upminster, Cranham, Corbets Tey, Upminster Bridge and North Ockendon.",
        "included": COMMON_INCLUDED,
        "why": [
            ("Close enough to come back", "We're a few minutes away in West Horndon, so aftercare and servicing are easy to book."),
            ("Two trades, one company", "Build the room and heat it, without chasing four different trades."),
            ("The price quoted is the price paid", "We see the job before we price it, so the number doesn't move."),
        ],
        "faq": [
            ("Do you cover Cranham and Corbets Tey?",
             ["Yes, along with Upminster Bridge and North Ockendon. Put your postcode in the quote form and we'll confirm."]),
            ("Will air conditioning heat my home in winter?",
             ["Yes. A split system is an air-to-air heat pump, so the same unit heats in winter and cools in summer. It's an efficient way to heat a single room, a loft conversion or a garden office."]),
            ("Can you build a garden room and fit the AC at the same time?",
             ["Yes, that's what we do most. One team handles the base, the build, the electrics and the air conditioning, so the room is ready to use when we hand it over."]),
            ("How quickly will you reply?",
             ["Within one working day of your quote request."]),
        ],
        "areas": ["Upminster", "Cranham", "Corbets Tey", "Upminster Bridge", "North Ockendon", "Hornchurch", "Brentwood", "West Horndon"],
        "area_title": "Upminster and Around",
        "area_text": "Cranham, Corbets Tey and the rest of RM14, a few minutes from our base in West Horndon.",
        "area_fine": "Not sure if you're in range? Put your postcode in the quote form and we'll tell you straight away.",
        "related": ["air-conditioning-installation", "garden-rooms", "house-extensions"],
    },
    {
        "slug": "hornchurch",
        "trade": "ac",
        "nav": "Hornchurch",
        "cta_title": "Get a Price for Your Job in Hornchurch",
        "service_param": None,
        "title": "Air Conditioning &amp; Garden Rooms in Hornchurch | OAK Group",
        "description": "Air conditioning installation and servicing, garden rooms and house extensions in Hornchurch, Emerson Park and Elm Park. Local team based in West Horndon. Free site visit and fixed quote.",
        "schema_name": "Air conditioning and building work in Hornchurch",
        "eyebrow": "Hornchurch, Havering",
        "h1": "Air Conditioning &amp; Garden Rooms in <em>Hornchurch</em>",
        "lead": "Air conditioning that heats and cools, garden rooms and extensions across Hornchurch, Emerson Park and Elm Park, from a local team in West Horndon.",
        "facts": ["Local Havering team", "Free site visit", "Fixed quote"],
        "img": "extension.jpg",
        "img_alt": "Single-storey rear extension with bifold doors on a semi-detached house",
        "tag": "Local to RM11, RM12",
        "kicker": "More space and the right temperature, <mark>from one team</mark>.",
        "intro": [
            "Hornchurch has everything from terraces near the station to large detached homes in Emerson Park. What people ask us for changes with the house: an extension to open up the kitchen, a garden room for work, or air conditioning for bedrooms that never cool down in July.",
            "<strong>We handle the building and the air conditioning ourselves.</strong> No subcontracted crews you've never met, and one fixed quote after we've seen the job.",
        ],
        "included_title": "What We Do in Hornchurch",
        "included_sub": "Covering Hornchurch, Emerson Park, Elm Park, Harold Wood and Ardleigh Green.",
        "included": COMMON_INCLUDED,
        "why": [
            ("A local team", "Based in West Horndon, a short drive away. The same people from quote to handover."),
            ("Two trades, one company", "Extensions, garden rooms and AC from one crew, so the jobs fit together."),
            ("The price quoted is the price paid", "We see the job before we price it, so the number doesn't move."),
        ],
        "faq": [
            ("Do you cover Emerson Park and Elm Park?",
             ["Yes, along with Harold Wood and Ardleigh Green. Put your postcode in the quote form and we'll confirm."]),
            ("Do I need planning permission for a rear extension?",
             ["Many single-storey rear extensions fall under permitted development, within limits on depth and height. Larger ones can go through the prior approval route. We check what applies to your house at the site visit."]),
            ("Can you add air conditioning to a new extension?",
             ["Yes. It's easiest to plan it in during the build, so the pipe runs are hidden and the unit sits where you want it."]),
            ("How quickly will you reply?",
             ["Within one working day of your quote request."]),
        ],
        "areas": ["Hornchurch", "Emerson Park", "Elm Park", "Harold Wood", "Ardleigh Green", "Upminster", "Romford", "Brentwood"],
        "area_title": "Hornchurch and Around",
        "area_text": "Emerson Park, Elm Park and the rest of RM11 and RM12, a short drive from our base in West Horndon.",
        "area_fine": "Not sure if you're in range? Put your postcode in the quote form and we'll tell you straight away.",
        "related": ["house-extensions", "air-conditioning-installation", "garden-rooms"],
    },
]

if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in AREAS:
        d = os.path.join(root, p["slug"])
        os.makedirs(d, exist_ok=True)
        html = S.page(p).replace("Generated by _build/services.py", "Generated by _build/areas.py")
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote", p["slug"])
