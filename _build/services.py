"""Builds one page per service: <slug>/index.html.

Run from the repo root:  python _build/services.py
Edit the copy in PAGES below, then run it again. Every page links back to the
quote form on the home page with its service already ticked (?service=...#contact).
"""
import json
import os
from html import escape

SITE = "https://www.oakgroup.company"
EMAIL = "info@oakgroup.ltd"
TODAY = "2026-10-21"

AC_AREAS = ["London", "Essex", "Brentwood", "Havering", "Thurrock", "Romford", "Hertfordshire", "Kent", "Surrey"]
BUILD_AREAS = ["West Horndon", "Brentwood", "Upminster", "Hornchurch", "Romford", "Havering", "Thurrock", "Basildon", "Billericay", "East London"]

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

PROCESS = [
    ("Get in Touch", "Fill in the quote form with what needs doing and where. We'll tell you honestly if it's a job for us."),
    ("Site Visit &amp; Fixed Quote", "We look at the job before pricing it. The number doesn't move."),
    ("Work Scheduled Around You", "A start date agreed in advance, not a rough window you have to chase."),
    ("Aftercare", "Maintenance offered for AC. Snagging handled directly for building work."),
]

PAGES = [
    {
        "slug": "garden-rooms",
        "trade": "build",
        "nav": "Garden Rooms",
        "service_param": "garden-room",
        "title": "Garden Rooms in Essex &amp; East London | OAK Group",
        "description": "Insulated, cedar-clad garden rooms and summer houses built to measure in Essex and East London. Wired for power, with AC that heats in winter. Fixed quote after a site visit.",
        "schema_name": "Garden rooms and summer houses",
        "eyebrow": "Garden Rooms &amp; Summer Houses",
        "h1": "Garden Rooms in <em>Essex</em> &amp; East London",
        "lead": "Insulated, cedar-clad and wired for power. Built to measure for your garden, and warm enough to use in January, not just July.",
        "facts": ["Built to measure", "Insulated &amp; wired", "AC that heats, fitted by us"],
        "img": "summerhouse.jpg",
        "img_alt": "Insulated cedar-clad garden room built in an Essex back garden",
        "tag": "Most requested",
        "kicker": "Most garden rooms get used four months a year. Ours are built for <mark>all twelve</mark>.",
        "intro": [
            "A garden room is only worth the money if you actually use it. That comes down to what you can't see: the base, the insulation, the wiring and how it's heated.",
            "<strong>We build the room and fit the air conditioning ourselves.</strong> The split system cools it in summer and heats it in winter, so the office, gym or studio works all year. One company, one quote, one phone number.",
        ],
        "included_title": "What's Included",
        "included_sub": "Every room is specified for your plot and how you'll use it.",
        "included": [
            ("Proper base", "A solid base chosen for your ground, so the room stays level for years."),
            ("Insulated walls, floor and roof", "Insulated all round, so the room holds heat in winter and stays cool in summer."),
            ("Cedar cladding", "Cedar outside, built to measure, with doors and windows placed where you want the light."),
            ("Electrics and lighting", "Wired for power, sockets, lighting and data, ready for a desk, gym kit or TV."),
            ("Air conditioning that heats", "A split system fitted by our own engineers. Cools in summer, heats in winter."),
            ("One team start to finish", "Groundwork, build, electrics and AC handled by one crew. No chasing four trades."),
        ],
        "why": [
            ("Built and heated by one company", "We build the room and fit the AC. Nobody blames someone else's work."),
            ("Based where we work", "We're in West Horndon. Less time on the road, more of your quote in the room."),
            ("The price quoted is the price paid", "We see the garden before we price it, so the quote doesn't move."),
        ],
        "faq": [
            ("Do I need planning permission for a garden room?",
             ["Usually not. In England most garden rooms count as permitted development if they sit behind the house, cover no more than half the garden, and stay under 2.5m tall when within 2m of a boundary.",
              "Listed buildings, flats and conservation areas have tighter rules. We check this at the site visit, before you pay anything."]),
            ("Do I need building regulations approval?",
             ["Rooms under 15m² of floor space that nobody sleeps in usually don't. Between 15m² and 30m² they're usually exempt if they sit at least 1m from the boundary. We'll tell you which applies to yours."]),
            ("Can I use it in winter?",
             ["Yes. That's the point of the insulation and the AC. A split system heats as well as cools, so the room stays comfortable in January."]),
            ("How long does a build take?",
             ["It depends on the size and the base. You get an agreed start date and a clear timeline with your quote, not a rough window."]),
            ("Do you build in my area?",
             ["We build in East London and Essex, including Brentwood, Havering and Thurrock. Residential only."]),
        ],
        "related": ["air-conditioning-installation", "landscaping", "house-extensions"],
    },
    {
        "slug": "air-conditioning-installation",
        "trade": "ac",
        "nav": "AC Installation",
        "service_param": "ac-install",
        "title": "Air Conditioning Installation in London &amp; Essex | OAK Group",
        "description": "Split system air conditioning that cools in summer and heats in winter. Sized from a proper survey, most homes fitted in a day. London, Essex and the Home Counties. Free quote.",
        "schema_name": "Air conditioning installation",
        "eyebrow": "Air Conditioning Installation",
        "h1": "Air Conditioning Installation in <em>London</em> &amp; Essex",
        "lead": "Split systems that cool in summer and heat in winter. Sized from a proper survey, and most homes are fitted in a day.",
        "facts": ["Cools and heats", "Most installs in a day", "Homes and businesses"],
        "img": "aircon-install-residential.jpg",
        "img_alt": "Engineer installing a wall-mounted split air conditioning unit in a British living room",
        "tag": "Residential",
        "kicker": "AC isn't just for heatwaves. The same unit <mark>heats your room</mark> all winter.",
        "intro": [
            "A modern split system is a heat pump. It moves heat out of the room in summer and into the room in winter, so one unit replaces a fan and a heater.",
            "<strong>We size every system from a survey of the room</strong>, not from a brochure. A unit that's too small runs flat out and never catches up. One that's too big wastes money. Getting it right is most of the job.",
        ],
        "included_title": "What's Included",
        "included_sub": "From the survey to the handover, done by the same engineers.",
        "included": [
            ("Room survey", "We measure the room, check the walls and plan where the indoor and outdoor units go."),
            ("System sized to the room", "Capacity chosen for the size, windows and use of the room, not the biggest unit on the van."),
            ("Neat installation", "Pipework routed and covered cleanly, outdoor unit mounted securely, mess cleared away."),
            ("Commissioning and testing", "Pressure tested, checked on cooling and heating, and shown working before we leave."),
            ("How to use it", "We show you the remote and the settings that keep running costs down."),
            ("Servicing after", "The same team can service it every year, so it keeps running like day one."),
        ],
        "why": [
            ("Certified to handle refrigerant", "Refrigerant handling is a legal requirement. Our engineers hold the licence."),
            ("Installed right, kept running", "The team that fits your unit services it next year. No handoffs."),
            ("You call David, not a script", "You speak to the person who schedules the work, not a call centre."),
        ],
        "faq": [
            ("Can air conditioning heat my home in winter?",
             ["Yes. A split system works as an air to air heat pump. In heating mode it pulls heat from the outside air, even on cold days, and puts it into the room."]),
            ("How long does an installation take?",
             ["Most single room installs in a home are done in a day. Multi room systems take longer, and we give you the timeline with your quote."]),
            ("Do I need planning permission for an AC unit?",
             ["It depends on the property. Flats, listed buildings and conservation areas can need consent. We check this at the survey before you commit to anything."]),
            ("Is it noisy?",
             ["Modern indoor units are quiet enough for bedrooms. We place the outdoor unit with you and your neighbours in mind."]),
            ("Which areas do you cover?",
             ["London and the Home Counties for homes, and further for larger commercial projects. We're based in West Horndon, Essex."]),
        ],
        "related": ["air-conditioning-maintenance", "commercial-air-conditioning", "garden-rooms"],
    },
    {
        "slug": "air-conditioning-maintenance",
        "trade": "ac",
        "nav": "AC Servicing",
        "service_param": "ac-maintenance",
        "title": "Air Conditioning Servicing &amp; Maintenance in London &amp; Essex | OAK Group",
        "description": "Annual air conditioning servicing, maintenance contracts and repairs for homes and businesses in London, Essex and the Home Counties. Faults caught before the heatwave.",
        "schema_name": "Air conditioning maintenance and servicing",
        "eyebrow": "Servicing, Maintenance &amp; Repairs",
        "h1": "Air Conditioning <em>Servicing</em> &amp; Maintenance",
        "lead": "One scheduled visit a year keeps your system efficient and catches faults before the first hot day, when every engineer is booked up.",
        "facts": ["Annual service visits", "Maintenance contracts", "Repairs and faults"],
        "img": "aircon-maintenance.jpg",
        "img_alt": "HVAC engineer servicing an outdoor air conditioning condenser unit",
        "tag": "Ongoing",
        "kicker": "Serviced units outlast neglected ones. And they <mark>cost less to run</mark>.",
        "intro": [
            "Dirty filters and coils make a system work harder for the same result. That shows up on the electricity bill, then as a breakdown in the middle of summer.",
            "<strong>A yearly service stops that.</strong> We clean it, test it and fix small problems while they're still small. For businesses, a maintenance contract puts every unit on a schedule so nothing gets missed.",
        ],
        "included_title": "What a Service Covers",
        "included_sub": "The same checklist on every visit, so nothing is left to memory.",
        "included": [
            ("Filters cleaned", "Filters cleaned or replaced so air flows freely and the air in the room stays clean."),
            ("Coils and fans checked", "Indoor and outdoor coils cleaned, fans checked for wear and balance."),
            ("Refrigerant and pressures", "System pressures checked by a certified engineer, leaks traced if something's off."),
            ("Drain and condensate", "Drain line cleared so there are no drips, smells or water damage."),
            ("Electrical checks", "Connections and controls checked and tightened."),
            ("Performance test", "Cooling and heating tested and logged, so you know it's running as it should."),
        ],
        "why": [
            ("Faults caught before the heatwave", "We service ahead of the season, not in the July rush."),
            ("Any make, homes and businesses", "We service systems we didn't fit, for homes and commercial sites."),
            ("Repairs by the same team", "If the service finds a fault, the same engineers fix it."),
        ],
        "faq": [
            ("How often should air conditioning be serviced?",
             ["Once a year for most homes. Busy commercial sites, like kitchens and pubs, can need more."]),
            ("Do you service systems you didn't install?",
             ["Yes. We service and repair most makes, for homes and businesses."]),
            ("My AC isn't cooling or heating properly. Can you fix it?",
             ["Usually, yes. Tell us what it's doing in the quote form, and add the make and model if you have them. We'll book a visit to find the cause."]),
            ("What's a maintenance contract?",
             ["A scheduled service plan for one or more units. You don't have to remember to book, and faults get picked up early. It's popular with pubs, restaurants and offices."]),
        ],
        "related": ["air-conditioning-installation", "commercial-air-conditioning", "garden-rooms"],
    },
    {
        "slug": "commercial-air-conditioning",
        "trade": "ac",
        "nav": "Commercial AC",
        "service_param": "ac-install",
        "property_param": "Pub / restaurant / hotel",
        "title": "Commercial Air Conditioning for Pubs, Restaurants &amp; Hotels | OAK Group",
        "description": "Commercial air conditioning installation and maintenance for pubs, restaurants, hotels, offices and shops across London and the Home Counties. Fitted around your opening hours.",
        "schema_name": "Commercial air conditioning",
        "eyebrow": "Commercial Air Conditioning",
        "h1": "Commercial AC for <em>Pubs</em>, Restaurants &amp; Hotels",
        "lead": "Installed around your opening hours, so the kitchen stays cool and the doors stay open. Then serviced on a schedule, so it doesn't fail on your busiest night.",
        "facts": ["Fitted around service times", "Maintenance contracts", "London, Home Counties and further"],
        "img": "aircon-commercial-pub.jpg",
        "img_alt": "Commercial air conditioning condenser units outside an East London pub",
        "tag": "Commercial",
        "kicker": "Every hour your doors are shut costs money. So we <mark>work around your hours</mark>.",
        "intro": [
            "A hot dining room empties fast, and a kitchen without cooling is a hard place to keep staff. Commercial AC has to be planned around the business, not the other way round.",
            "<strong>We plan the install around your service times</strong>, then keep every unit on a maintenance schedule. One company for the fit and the upkeep.",
        ],
        "included_title": "What We Do",
        "included_sub": "Hospitality and small business sites, from one unit to a full fit-out.",
        "included": [
            ("Site survey", "We walk the site, check the loads and plan unit positions with you."),
            ("System designed for the space", "Capacity sized for dining rooms, kitchens, bars, guest rooms or offices."),
            ("Install around opening hours", "Work scheduled early, late or between services, so you keep trading."),
            ("Commissioning", "Every unit tested, controls set up and staff shown how to use them."),
            ("Maintenance contract", "Scheduled servicing for every unit, logged so nothing gets missed."),
            ("Repairs", "Faults handled by the engineers who know your system."),
        ],
        "why": [
            ("Fitted around service times", "Kitchen stays cool, doors stay open, trade carries on."),
            ("One company for fit and upkeep", "The team that installs it services it. No handoffs."),
            ("Further for larger projects", "London and the Home Counties, and further for bigger jobs."),
        ],
        "faq": [
            ("Can you work outside our opening hours?",
             ["Yes. We plan the install around your service times, including early starts and late finishes where needed."]),
            ("Do you cover businesses outside London?",
             ["Yes. London and the Home Counties are our main area, and we travel further for larger commercial projects."]),
            ("Do you offer maintenance contracts for multiple units?",
             ["Yes. Every unit goes on a schedule, so filters, drains and pressures are checked before problems start."]),
            ("What types of business do you work with?",
             ["Pubs, restaurants, hotels, offices and shops. Tell us about your site in the quote form and we'll say honestly if it's a fit."]),
        ],
        "related": ["air-conditioning-maintenance", "air-conditioning-installation", "refurbishments"],
    },
    {
        "slug": "house-extensions",
        "trade": "build",
        "nav": "Extensions",
        "service_param": "extension",
        "title": "House Extensions in Essex &amp; East London | OAK Group",
        "description": "Single-storey rear and side extensions in Essex and East London, fully project-managed from foundation to plaster. Fixed quote after a site visit. Based in West Horndon.",
        "schema_name": "House extensions",
        "eyebrow": "House Extensions",
        "h1": "House Extensions in <em>Essex</em> &amp; East London",
        "lead": "Foundation to plaster, fully project-managed by one team. We price it after seeing the house, so the quote doesn't move.",
        "facts": ["Fully project-managed", "Fixed quote", "Residential only"],
        "img": "extension.jpg",
        "img_alt": "Single-storey rear extension nearing completion with bi-fold doors",
        "tag": "Extensions",
        "kicker": "The worst part of most extensions is the bill <mark>going up halfway</mark>. Ours doesn't.",
        "intro": [
            "Extensions go over budget when the price is guessed from photos and the surprises turn up once the ground is open.",
            "<strong>We look at the job properly before we price it</strong>, then manage every stage ourselves. You deal with one company, from the foundations to the final coat of paint.",
        ],
        "included_title": "What's Included",
        "included_sub": "Every stage handled by one team, so nothing falls between trades.",
        "included": [
            ("Site visit and fixed quote", "We see the house before we price it. The number doesn't move."),
            ("Groundwork and foundations", "Dug, poured and inspected properly, the part nobody sees and everything depends on."),
            ("Structure and roof", "Walls, steels, roof and openings, including bi-fold or sliding doors."),
            ("First and second fix", "Electrics, plumbing, plastering and finishing, coordinated by us."),
            ("Heating and cooling", "AC that heats and cools can be fitted by our own engineers."),
            ("Snagging", "Snags handled directly by us, not passed around."),
        ],
        "why": [
            ("The price quoted is the price paid", "We see the job before pricing it, so the quote doesn't move."),
            ("One point of contact", "One phone number from start to finish, not four trades."),
            ("Based where we work", "We're in West Horndon, Essex. Close enough to be on site when it matters."),
        ],
        "faq": [
            ("Do I need planning permission for an extension?",
             ["Many single-storey rear extensions fall under permitted development, but it depends on the house, its size and its history. We check this with you at the site visit."]),
            ("Do you manage building regulations?",
             ["Extensions need building regulations sign-off. We build to the regulations and work with the inspector through each stage."]),
            ("Will the price change once work starts?",
             ["No. We price after seeing the job, and the quote is fixed for the work agreed."]),
            ("Which areas do you cover?",
             ["East London and Essex, including Brentwood, Havering and Thurrock. Residential only."]),
        ],
        "related": ["refurbishments", "garden-rooms", "media-walls"],
    },
    {
        "slug": "refurbishments",
        "trade": "build",
        "nav": "Refurbishments",
        "service_param": "refurbishment",
        "title": "Kitchen &amp; Bathroom Refurbishments in Essex &amp; East London | OAK Group",
        "description": "Kitchen, bathroom and full home refurbishments in Essex and East London. One point of contact from strip-out to finish. Fixed quote after a site visit.",
        "schema_name": "Kitchen and bathroom refurbishments",
        "eyebrow": "Refurbishments",
        "h1": "Kitchen &amp; Bathroom <em>Refurbishments</em>",
        "lead": "Kitchens, bathrooms and full refits across Essex and East London. One phone number from strip-out to finish, not four different trades.",
        "facts": ["Kitchens and bathrooms", "Full home refits", "One point of contact"],
        "img": "refurbishment.jpg",
        "img_alt": "British kitchen mid refurbishment with new cabinets being fitted",
        "tag": "Refurbishments",
        "kicker": "A refit goes wrong in the gaps <mark>between trades</mark>. We close the gaps.",
        "intro": [
            "When the plumber, electrician, plasterer and fitter all work for different people, every delay is somebody else's fault and you end up managing the job yourself.",
            "<strong>We run the whole refurbishment.</strong> One team, one schedule and one person to call, from the strip-out to the last tile.",
        ],
        "included_title": "What's Included",
        "included_sub": "Planned and run by one team from the first visit.",
        "included": [
            ("Site visit and fixed quote", "We see the room before pricing it, so the number holds."),
            ("Strip-out and prep", "Old fittings removed, walls and floors made good."),
            ("Plumbing and electrics", "Moved or upgraded where the new layout needs it."),
            ("Plastering and finishing", "Walls, ceilings and floors finished properly before anything is fitted."),
            ("Fitting", "Kitchens, bathrooms, tiling and joinery fitted by our team."),
            ("Snagging", "Anything not right is handled by us directly."),
        ],
        "why": [
            ("One point of contact", "One phone number, start to finish."),
            ("The price quoted is the price paid", "Priced after a site visit. The quote doesn't move."),
            ("Two trades under one roof", "Need AC in the new room? Our own engineers fit it."),
        ],
        "faq": [
            ("Do you supply the kitchen or bathroom, or just fit it?",
             ["Either. You can choose your own units and fittings, or we can source them as part of the quote."]),
            ("Can I stay at home during the work?",
             ["Usually, yes. We plan the order of work so you keep as much of the house usable as possible, and we tell you upfront if there are days without water or power."]),
            ("Which areas do you cover?",
             ["East London and Essex, including Brentwood, Havering and Thurrock. Residential only."]),
        ],
        "related": ["house-extensions", "media-walls", "air-conditioning-installation"],
    },
    {
        "slug": "landscaping",
        "trade": "build",
        "nav": "Landscaping",
        "service_param": "landscaping",
        "title": "Garden Landscaping in Essex &amp; East London | OAK Group",
        "description": "Garden landscaping in Essex and East London: patios, paving, decking, fencing and planting specified for your plot. Pairs with a garden room. Fixed quote after a site visit.",
        "schema_name": "Garden landscaping",
        "eyebrow": "Landscaping",
        "h1": "Garden <em>Landscaping</em> in Essex &amp; East London",
        "lead": "Paving, decking and planting chosen for your garden, not the yard's leftovers. Specified for the plot, then built by our own team.",
        "facts": ["Patios and paving", "Decking and fencing", "Planting"],
        "img": "landscaping.jpg",
        "img_alt": "Completed garden landscaping with patio, decking and planting in Essex",
        "tag": "Landscaping",
        "kicker": "A good garden starts with <mark>drainage and levels</mark>, not the paving catalogue.",
        "intro": [
            "Patios crack and lawns flood when the ground underneath is rushed. The part you walk on only lasts if the part you don't see was done properly.",
            "<strong>We specify every garden for its plot</strong>: the soil, the slope, the light and how you use it. Building a garden room too? We plan both together.",
        ],
        "included_title": "What We Build",
        "included_sub": "Hard and soft landscaping, planned as one design.",
        "included": [
            ("Patios and paving", "Laid on a proper sub-base with the right falls, so water runs away from the house."),
            ("Decking", "Built to last, on a frame that stays level."),
            ("Fencing and boundaries", "Fences, gates and walls that suit the garden and the house."),
            ("Lawns and planting", "Turf and planting chosen for your soil and light."),
            ("Paths and edging", "Clean edges and paths that connect the garden."),
            ("Garden room ready", "Base, paths and power planned in if a garden room is going in."),
        ],
        "why": [
            ("Specified for the plot", "Chosen for your garden, not whatever's left in the yard."),
            ("Garden and garden room together", "One team plans the room and the garden around it."),
            ("Based where we work", "We're in West Horndon, Essex. More of your quote goes into the garden."),
        ],
        "faq": [
            ("Can you landscape the garden around a new garden room?",
             ["Yes, and it's better planned together. Paths, levels and power for the room are designed in from the start."]),
            ("Do you do small jobs, like just a patio?",
             ["Yes. Tell us what you need in the quote form and we'll say honestly if it's a job for us."]),
            ("Which areas do you cover?",
             ["East London and Essex, including Brentwood, Havering and Thurrock. Residential only."]),
        ],
        "related": ["garden-rooms", "house-extensions", "refurbishments"],
    },
    {
        "slug": "media-walls",
        "trade": "build",
        "nav": "Media Walls",
        "service_param": "media-wall",
        "title": "Media Walls in Essex &amp; East London | OAK Group",
        "description": "Built-in media walls with the TV and electric fire recessed flush into the wall, cables hidden. Designed and built in Essex and East London. Fixed quote.",
        "schema_name": "Media walls",
        "eyebrow": "Media Walls",
        "h1": "Media Walls in <em>Essex</em> &amp; East London",
        "lead": "TV and electric fire recessed flush into the wall, cables hidden, finish clean. Built in, not bolted on.",
        "facts": ["Recessed TV and fire", "Hidden cables", "Shelving and lighting"],
        "img": "media-wall.jpg",
        "img_alt": "Built-in media wall with recessed TV and electric fireplace in a living room",
        "tag": "Media Walls",
        "kicker": "A media wall should look like it was <mark>always part of the room</mark>.",
        "intro": [
            "A TV on a bracket with cables down the wall is the first thing you notice in a room. A media wall hides all of it and gives the room a focal point.",
            "<strong>We build the wall around your TV and fire</strong>, with power, sockets and cable routes planned before the first board goes up.",
        ],
        "included_title": "What's Included",
        "included_sub": "Designed around your room, your TV and how you use the space.",
        "included": [
            ("Design to your room", "Sized for the wall, the TV and the fire you choose."),
            ("Recessed TV and fire", "Both set flush into the wall for a clean finish."),
            ("Hidden cables and power", "Sockets and cable routes built in, so nothing shows."),
            ("Shelving and storage", "Alcoves, shelves or cupboards if you want them."),
            ("Lighting", "LED lighting built into the wall if you want it."),
            ("Plastered and finished", "Taped, plastered and ready to paint, or painted by us."),
        ],
        "why": [
            ("Recessed, not bolted on", "TV and fire flush with the wall, cables hidden."),
            ("One team does it all", "Framing, electrics and plastering by one crew."),
            ("Fixed quote", "We see the room before pricing it. The quote doesn't move."),
        ],
        "faq": [
            ("Can you fit my existing TV and fire?",
             ["Yes. We design the wall around the TV and fire you have or plan to buy, so share the models in the quote form."]),
            ("How long does a media wall take?",
             ["Most take a few days, depending on size, shelving and finish. You'll get the timeline with your quote."]),
            ("Which areas do you cover?",
             ["East London and Essex, including Brentwood, Havering and Thurrock. Residential only."]),
        ],
        "related": ["refurbishments", "house-extensions", "air-conditioning-installation"],
    },
]

BY_SLUG = {p["slug"]: p for p in PAGES}
AC_SLUGS = [p["slug"] for p in PAGES if p["trade"] == "ac"]
BUILD_SLUGS = [p["slug"] for p in PAGES if p["trade"] == "build"]


def plain(s):
    """Visible HTML string -> plain text for JSON-LD."""
    import re
    from html import unescape
    return unescape(re.sub(r"<[^>]+>", "", s))


def quote_href(p):
    q = "?service=" + p["service_param"]
    if p.get("property_param"):
        q += "&amp;property=" + p["property_param"].replace(" ", "%20").replace("/", "%2F")
    return "../" + q + "#contact"


def mail_href(p):
    from urllib.parse import quote
    return "mailto:" + EMAIL + "?subject=" + quote("Quote request: " + plain(p["schema_name"]))


def schema(p):
    url = f"{SITE}/{p['slug']}/"
    areas = AC_AREAS if p["trade"] == "ac" else BUILD_AREAS
    graph = [
        {
            "@type": "Service",
            "@id": url + "#service",
            "name": plain(p["schema_name"]),
            "serviceType": plain(p["schema_name"]),
            "description": plain(p["description"]),
            "url": url,
            "image": f"{SITE}/assets/{p['img']}",
            "areaServed": [{"@type": "Place", "name": a} for a in areas],
            "provider": {
                "@type": ["HVACBusiness", "GeneralContractor"],
                "@id": f"{SITE}/#business",
                "name": "OAK Group",
                "url": f"{SITE}/",
                "email": EMAIL,
                "address": {"@type": "PostalAddress", "addressLocality": "West Horndon", "addressRegion": "Essex", "postalCode": "CM13 3XL", "addressCountry": "GB"},
            },
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": plain(p["nav"]), "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": " ".join(a)}}
                for q, a in p["faq"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)


def nav_links(current):
    items = [("Garden Rooms", "garden-rooms"), ("AC Installation", "air-conditioning-installation"),
             ("AC Servicing", "air-conditioning-maintenance"), ("Extensions", "house-extensions")]
    out = []
    for label, slug in items:
        cur = ' aria-current="page"' if slug == current else ""
        out.append(f'<a href="../{slug}/"{cur}>{label}</a>')
    out.append('<a href="../#work">Our Work</a>')
    return "\n      ".join(out)


def mobile_links():
    links = [f'<a href="../{p["slug"]}/">{p["nav"]}</a>' for p in PAGES]
    return "\n  ".join(['<a href="../">Home</a>'] + links)


def footer_col(slugs):
    return "\n        ".join(f'<a href="../{s}/">{BY_SLUG[s]["nav"]}</a>' for s in slugs)


def page(p):
    qh = quote_href(p)
    mh = mail_href(p)
    areas = AC_AREAS if p["trade"] == "ac" else BUILD_AREAS
    if p["trade"] == "ac":
        area_title = "Air Conditioning Across London &amp; the Home Counties"
        area_text = "Homes across London and the Home Counties, and further for larger commercial projects. Based in West Horndon, Essex."
        area_fine = "Not sure if you're in range? Put your postcode in the quote form and we'll tell you straight away."
    else:
        area_title = "Built Across East London &amp; Essex"
        area_text = "Residential building work within reach of West Horndon. Staying local means more of your quote goes into the job, not fuel."
        area_fine = "Residential only. We're not insured for commercial construction, so we keep to what we can stand behind."

    facts = "\n          ".join(f"<li>{f}</li>" for f in p["facts"])
    intro = "\n        ".join(f"<p>{x}</p>" for x in p["intro"])
    inc = "\n      ".join(
        f'<div class="inc-card"><span class="num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(p["included"], 1))
    why = "\n      ".join(
        f'<div class="why-card"><span class="num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(p["why"], 1))
    process = "\n      ".join(
        f'<div class="process-step"><span class="num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(PROCESS, 1))
    faq = "\n      ".join(
        "<details><summary>" + escape(q) + '</summary><div class="answer">'
        + "".join(f"<p>{escape(x)}</p>" for x in a) + "</div></details>"
        for q, a in p["faq"])
    pills = "".join(f"<span>{a}</span>" for a in areas)
    related = "\n      ".join(
        f'<a class="related-card" href="../{s}/"><div class="img"><img loading="lazy" decoding="async" src="../assets/{BY_SLUG[s]["img"]}" alt="{BY_SLUG[s]["img_alt"]}"></div>'
        f'<div class="body"><h3>{BY_SLUG[s]["nav"]}</h3>{ICON_ARROW}</div></a>'
        for s in p["related"])

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['description']}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{SITE}/{p['slug']}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="OAK Group">
<meta property="og:url" content="{SITE}/{p['slug']}/">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['description']}">
<meta property="og:image" content="{SITE}/assets/{p['img']}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="GB-ESS">
<meta name="geo.placename" content="West Horndon, Brentwood, Essex">
<meta name="theme-color" content="#0A0A0B">
<link rel="icon" type="image/png" href="../assets/favicon.png">
<link rel="apple-touch-icon" href="../assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800;900&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/pages.css">
<script type="application/ld+json">
{schema(p)}
</script>
</head>
<body>

<!-- Generated by _build/services.py. Edit the copy there, not here. -->

<nav class="nav">
  <div class="container nav-row">
    <a href="../" class="brand">
      <img class="brand-icon" src="../assets/logo-oak-icon-white.png" alt="" width="52" height="34">
      <span class="brand-text">
        <span class="brand-mark">OAK Group</span>
        <span class="brand-sub">Air Conditioning &amp; Construction</span>
      </span>
    </a>
    <div class="nav-links">
      {nav_links(p['slug'])}
    </div>
    <div class="nav-actions">
      <a class="btn btn-red nav-cta" href="{qh}">Get a Free Quote</a>
      <button class="burger" id="burgerBtn" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
        <svg id="burgerIconOpen" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        <svg id="burgerIconClose" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" style="display:none;"><path d="M6 6l12 12M18 6 6 18"/></svg>
      </button>
    </div>
  </div>
</nav>

<div class="mobile-menu" id="mobileMenu">
  {mobile_links()}
  <a class="btn btn-red" href="{qh}">Get a Free Quote</a>
</div>

<header class="svc-hero">
  <div class="container svc-hero-grid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a><span>/</span><span aria-current="page">{p['nav']}</span></nav>
      <span class="eyebrow">{p['eyebrow']}</span>
      <h1>{p['h1']}</h1>
      <p class="lead">{p['lead']}</p>
      <div class="hero-ctas">
        <a class="btn btn-red" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
        <a class="btn btn-ghost-ink" href="{mh}">Email Us</a>
      </div>
      <ul class="hero-facts">
          {facts}
      </ul>
    </div>
    <div class="svc-hero-media">
      <span class="tag">{p['tag']}</span>
      <img fetchpriority="high" decoding="async" width="1600" height="893" src="../assets/{p['img']}" alt="{p['img_alt']}">
    </div>
  </div>
</header>

<main>
<section>
  <div class="container intro-grid">
    <p class="intro-kicker">{p['kicker']}</p>
    <div class="intro-body">
        {intro}
    </div>
  </div>
</section>

<section class="included">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{p['eyebrow']}</span>
      <h2>{p['included_title']}</h2>
      <p>{p['included_sub']}</p>
    </div>
    <div class="inc-grid">
      {inc}
    </div>
  </div>
</section>

<aside class="mid-cta">
  <div class="container mid-cta-row">
    <div>
      <h2>Get a Price for Your {p['nav']}</h2>
      <p>Tell us what you need and your postcode. We reply within one working day.</p>
    </div>
    <div class="btns">
      <a class="btn btn-red" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
    </div>
  </div>
</aside>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Why OAK Group</span>
      <h2>No Middlemen, No Guesswork</h2>
    </div>
    <div class="why-grid">
      {why}
    </div>
  </div>
</section>

<section class="process">
  <div class="container on-ink">
    <div class="section-head">
      <span class="eyebrow">How It Works</span>
      <h2>Four Steps, No Surprises</h2>
    </div>
    <div class="process-grid">
      {process}
    </div>
    <div class="process-foot">
      <a class="btn btn-red" href="{qh}">{ICON_MAIL}Start With Step 01</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Questions</span>
      <h2>Frequently Asked</h2>
    </div>
    <div class="faq-list">
      {faq}
    </div>
  </div>
</section>

<section class="areas">
  <div class="container areas-row">
    <div class="section-head" style="margin-bottom:0;">
      <span class="eyebrow">Areas We Cover</span>
      <h2>{area_title}</h2>
      <p>{area_text}</p>
    </div>
    <div>
      <div class="area-pills">{pills}</div>
      <p class="fine">{area_fine}</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Also From OAK Group</span>
      <h2>Related Services</h2>
    </div>
    <div class="related-grid">
      {related}
    </div>
  </div>
</section>

<section class="final-cta" id="contact">
  <div class="container">
    <span class="eyebrow">Get Started</span>
    <h2>Get a Straight Answer on Price</h2>
    <p>Tell us what needs doing and where. We'll tell you honestly whether it's a job for us, and what it costs.</p>
    <div class="btns">
      <a class="btn btn-white" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
      <a class="btn btn-ghost-white" href="{mh}">Email {EMAIL}</a>
    </div>
    <p class="fine">Usually answered within one working day</p>
  </div>
</section>
</main>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="footer-logo" href="../"><img loading="lazy" decoding="async" src="../assets/logo-oak-white.png" alt="OAK Construction &amp; Project Management Limited" width="260" height="125"></a>
        <p>Air conditioning and residential construction, based in West Horndon, Essex. Two trades, one point of contact.</p>
      </div>
      <div class="footer-col">
        <h5>Air Conditioning</h5>
        {footer_col(AC_SLUGS)}
      </div>
      <div class="footer-col">
        <h5>Construction</h5>
        {footer_col(BUILD_SLUGS)}
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 OAK Group Limited</span>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</footer>

<div class="sticky-cta">
  <a class="btn btn-red" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
  <a class="btn btn-ghost-ink" href="{mh}" aria-label="Email OAK Group">Email</a>
</div>

<script>
(function(){{
  var burger = document.getElementById('burgerBtn');
  var menu = document.getElementById('mobileMenu');
  var iconOpen = document.getElementById('burgerIconOpen');
  var iconClose = document.getElementById('burgerIconClose');
  function setOpen(open){{
    menu.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    iconOpen.style.display = open ? 'none' : 'block';
    iconClose.style.display = open ? 'block' : 'none';
  }}
  burger.addEventListener('click', function(){{ setOpen(!menu.classList.contains('is-open')); }});
  menu.querySelectorAll('a').forEach(function(a){{ a.addEventListener('click', function(){{ setOpen(false); }}); }});
}})();
</script>
</body>
</html>
"""


def sitemap():
    urls = [(f"{SITE}/", "1.0")] + [(f"{SITE}/{p['slug']}/", "0.8") for p in PAGES]
    rows = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for u, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n'


if __name__ == "__main__":
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for p in PAGES:
        d = os.path.join(root, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(p))
        print("wrote", p["slug"])
    with open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write(sitemap())
    print("wrote sitemap.xml")
