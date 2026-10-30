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
PHONE = "07413 965823"
PHONE_INTL = "+447413965823"
SAME_AS = ["https://www.instagram.com/group.oak/", "https://www.facebook.com/people/Oak-Group-Company/61595795720572/"]
ADDRESS = {"@type": "PostalAddress", "streetAddress": "Station Road", "addressLocality": "West Horndon, Brentwood", "addressRegion": "Essex", "postalCode": "CM13 3XL", "addressCountry": "GB"}
TODAY = "2026-10-27"

AC_AREAS = ["London", "Essex", "Brentwood", "Havering", "Thurrock", "Romford", "Hertfordshire", "Kent", "Surrey"]
BUILD_AREAS = ["West Horndon", "Brentwood", "Upminster", "Hornchurch", "Romford", "Havering", "Thurrock", "Basildon", "Billericay", "East London"]

ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

PROCESS = [
    ("Get in Touch", "Fill in the quote form with what needs doing and where. We'll tell you honestly if it's a job for us."),
    ("Site Visit &amp; Fixed Quote", "We look at the job before pricing it. The number doesn't move."),
    ("Work Scheduled Around You", "A start date agreed in advance, not a rough window you have to chase."),
    ("Aftercare", "Maintenance offered for AC. Snagging handled directly for building work."),
]

PAGES = [{'slug': 'air-conditioning',
  'trade': 'ac',
  'nav': 'Air Conditioning',
  'service_param': 'ac-install',
  'title': 'Air Conditioning &amp; Heat Pumps in Essex | Install, Service, Repair | OAK Group',
  'description': 'Air conditioning and heat pumps that heat in winter and cool in summer. Installation, servicing and repairs for homes '
                 'and businesses in Brentwood, Upminster, West Horndon and across Essex.',
  'schema_name': 'Air conditioning and heat pump installation, servicing and repair',
  'eyebrow': 'Air Conditioning &middot; Heat Pumps &middot; Servicing',
  'h1': 'Air Conditioning &amp; Heat Pumps in <em>Essex</em>',
  'lead': 'We install, service and repair air conditioning and heat pumps that heat your home in winter and cool it in summer. Homes and '
          'businesses in Brentwood, Upminster, West Horndon, Hornchurch, Romford, Billericay and across Essex and East London.',
  'facts': ['Installation', 'Heating &amp; heat pumps', 'Servicing &amp; repairs', 'Homes and businesses'],
  'img': 'ac-living-room-winter.jpg',
  'img_alt': 'Engineer installing a wall-mounted air conditioning unit in a British living room',
  'gallery': [('ac-living-room-winter.jpg', 'Wall-mounted unit heating a living room on a winter evening'), ('heat-pump-outdoor-frost.jpg', 'Outdoor unit on a frosty morning in Essex'), ('ac-install-bedroom.jpg', 'Installing a split unit in a bedroom'), ('heat-pump-install.jpg', 'Connecting a heat pump outdoor unit'), ('ac-service-gauges.jpg', 'Checking pressures on a yearly service'), ('ac-handover-kitchen.jpg', 'Showing the homeowner the controls'), ('ac-home-office.jpg', 'Split unit in a home office'), ('ac-commercial-pub.jpg', 'Ceiling cassettes in a pub dining room'), ('ac-commercial-roof.jpg', 'Commercial condensers on a flat roof')],
  'kicker': 'One unit, all year. It <mark>heats your home in winter</mark> and cools it in summer.',
  'intro': ['A modern split air conditioner is a heat pump. In winter it pulls heat from the outside air, even on frosty mornings, and '
            'moves it into the room. In summer it does the reverse. For every unit of electricity it uses, it delivers roughly three units '
            'of heat, which is why it costs less to run than storage heaters or a fan heater.',
            '<strong>We size every system from a survey of your rooms</strong>, fit it neatly, and service it every year after. '
            'Installation, heating, servicing and repairs, all from the same local team.'],
  'included_title': 'What We Do',
  'included_sub': 'Everything to do with air conditioning and heat pumps, from one team.',
  'included': [('Air conditioning installation',
                'Split and multi-split systems for bedrooms, living rooms, lofts, offices and garden rooms. Most single rooms fitted in a '
                'day.'),
               ('Heating with AC and heat pumps',
                'Air to air and air source heat pumps that keep your home warm all winter. A smart swap for old storage heaters.'),
               ('Servicing', 'A yearly visit: filters, coils, drains, pressures and a full heating and cooling test.'),
               ('Repairs and faults', 'Not heating, not cooling, leaking or noisy? We find the cause and fix it, on most makes.'),
               ('Commercial', 'Pubs, restaurants, offices and shops. Fitted around your opening hours, then kept on a service plan.'),
               ('Survey before any price', "We look at the rooms first, so the system is the right size and the quote doesn't move.")],
  'cta_title': 'Get a Price for Your Air Conditioning',
  'why': [('Local engineers', 'Based in West Horndon. Brentwood, Upminster and the rest of Essex are on our doorstep.'),
          ('Installed right, kept running', 'The team that fits your system services it next year. No handoffs.'),
          ('You speak to the engineer', 'Call and you get the person who plans the job, not a call centre.')],
  'faq': [('Can air conditioning heat my home in winter?',
           ['Yes. A split system works as an air to air heat pump. In heating mode it pulls heat from the outside air, even below '
            'freezing, and puts it into the room.']),
          ('What is the difference between air to air and air source heat pumps?',
           ['Air to air heats the room directly through a wall-mounted unit, and cools in summer too. Air to water heats water for '
            'radiators or underfloor heating. We tell you at the survey which suits your home.']),
          ('Can it replace my storage heaters?',
           ['Yes, and it is one of the best swaps you can make. Storage heaters charge overnight and often run out by the evening. A heat '
            'pump heats when you need it, using less electricity.']),
          ('How long does an installation take?',
           ['Most single room installs are done in a day. Multi-room systems take longer, and you get the timeline with your quote.']),
          ('How often should it be serviced?',
           ['Once a year for most homes. Busy commercial sites, like kitchens and pubs, can need more.']),
          ("Do you service and repair systems you didn't fit?",
           ['Yes. We service and repair most makes. Add the make and model in the quote form if you have them.']),
          ('Which areas do you cover?',
           ['Brentwood, Upminster, West Horndon, Hornchurch, Romford, Billericay and across Essex and East London. We are based in West '
            'Horndon.'])],
  'areas': ['Brentwood',
            'Upminster',
            'West Horndon',
            'Hornchurch',
            'Romford',
            'Billericay',
            'Basildon',
            'Thurrock',
            'Essex',
            'East London'],
  'area_title': 'Air Conditioning Across Essex',
  'area_text': 'Based in West Horndon, so most of Essex is a short drive. Less time on the road, more of your quote in the job.',
  'area_fine': "Not sure if you're in range? Put your postcode in the quote form and we'll tell you straight away.",
  'related': ['garden-rooms', 'building-works', 'landscaping']},
 {'slug': 'garden-rooms',
  'trade': 'build',
  'nav': 'Garden Rooms',
  'service_param': 'garden-room',
  'title': 'Garden Rooms in Essex &amp; East London | OAK Group',
  'description': 'Insulated, cedar-clad garden rooms and summer houses built to measure in Essex and East London. Wired for power, with AC '
                 'that heats in winter. Fixed quote after a site visit.',
  'schema_name': 'Garden rooms and summer houses',
  'eyebrow': 'Garden Rooms &amp; Summer Houses',
  'h1': 'Garden Rooms in <em>Essex</em> &amp; East London',
  'lead': 'We build insulated, cedar-clad garden rooms and summer houses, wired for power and fitted with AC that heats in winter. Homes '
          'in Brentwood, Upminster, West Horndon, Hornchurch, Romford, Billericay and across Essex and East London.',
  'facts': ['Built to measure', 'Insulated &amp; wired', 'AC that heats, fitted by us'],
  'img': 'summerhouse.jpg',
  'img_alt': 'Insulated cedar-clad garden room built in an Essex back garden',
  'kicker': 'Most garden rooms get used four months a year. Ours are built for <mark>all twelve</mark>.',
  'intro': ["A garden room is only worth the money if you actually use it. That comes down to what you can't see: the base, the "
            "insulation, the wiring and how it's heated.",
            '<strong>We build the room and fit the air conditioning ourselves.</strong> The split system cools it in summer and heats it '
            'in winter, so the office, gym or studio works all year. One company, one quote, one phone number.'],
  'included_title': "What's Included",
  'included_sub': "Every room is specified for your plot and how you'll use it.",
  'included': [('Proper base', 'A solid base chosen for your ground, so the room stays level for years.'),
               ('Insulated walls, floor and roof', 'Insulated all round, so the room holds heat in winter and stays cool in summer.'),
               ('Cedar cladding', 'Cedar outside, built to measure, with doors and windows placed where you want the light.'),
               ('Electrics and lighting', 'Wired for power, sockets, lighting and data, ready for a desk, gym kit or TV.'),
               ('Air conditioning that heats', 'A split system fitted by our own engineers. Cools in summer, heats in winter.'),
               ('One team start to finish', 'Groundwork, build, electrics and AC handled by one crew. No chasing four trades.')],
  'why': [('Built and heated by one company', "We build the room and fit the AC. Nobody blames someone else's work."),
          ('Based where we work', "We're in West Horndon. Less time on the road, more of your quote in the room."),
          ('The price quoted is the price paid', "We see the garden before we price it, so the quote doesn't move.")],
  'faq': [('Do I need planning permission for a garden room?',
           ['Usually not. In England most garden rooms count as permitted development if they sit behind the house, cover no more than '
            'half the garden, and stay under 2.5m tall when within 2m of a boundary.',
            'Listed buildings, flats and conservation areas have tighter rules. We check this at the site visit, before you pay '
            'anything.']),
          ('Do I need building regulations approval?',
           ["Rooms under 15m² of floor space that nobody sleeps in usually don't. Between 15m² and 30m² they're usually exempt if they sit "
            "at least 1m from the boundary. We'll tell you which applies to yours."]),
          ('Can I use it in winter?',
           ["Yes. That's the point of the insulation and the AC. A split system heats as well as cools, so the room stays comfortable in "
            'January.']),
          ('How long does a build take?',
           ['It depends on the size and the base. You get an agreed start date and a clear timeline with your quote, not a rough window.']),
          ('Do you build in my area?',
           ['We build in East London and Essex, including Brentwood, Havering and Thurrock. Residential only.'])],
  'related': ['air-conditioning', 'landscaping', 'building-works'],
  'gallery': [('garden-room-winter.jpg', 'Garden room with AC, warm in winter'), ('garden-room-office.jpg', 'Garden room used as a home office'), ('garden-room-build.jpg', 'Fitting cedar cladding to a new garden room'), ('summerhouse.jpg', 'Cedar-clad garden room in an Essex garden')]},
 {'slug': 'building-works',
  'trade': 'build',
  'nav': 'Extensions &amp; Refurbs',
  'service_param': 'extension',
  'title': 'Extensions, Refurbishments &amp; Media Walls in Essex | OAK Group',
  'description': 'House extensions, kitchen and bathroom refurbishments and media walls in Brentwood, Upminster, West Horndon and across '
                 'Essex and East London. One team, fixed quote after a site visit.',
  'schema_name': 'House extensions, refurbishments and media walls',
  'eyebrow': 'Extensions &middot; Refurbishments &middot; Media Walls',
  'h1': 'Extensions &amp; Refurbishments in <em>Essex</em>',
  'lead': 'We build house extensions, refit kitchens and bathrooms and build media walls, fully managed by one team. Homes in Brentwood, '
          'Upminster, West Horndon, Hornchurch, Romford, Billericay and across Essex and East London.',
  'facts': ['Extensions', 'Kitchens &amp; bathrooms', 'Media walls', 'Fixed quote after a site visit'],
  'img': 'extension.jpg',
  'img_alt': 'Single-storey rear extension on an Essex home',
  'gallery': [('extension-rear.jpg', 'Single-storey rear extension with roof lantern'), ('kitchen-refit.jpg', 'Refitted shaker kitchen'), ('media-wall-evening.jpg', 'Media wall with fire and shelving'), ('extension.jpg', 'Extension on an Essex home')],
  'kicker': 'One phone number from strip-out to finish, <mark>not four different trades</mark>.',
  'intro': ['Most building jobs go wrong in the gaps between trades: the builder blames the plumber, the plumber blames the electrician, '
            'and you chase all of them.',
            "<strong>We manage the whole job with one team</strong>, and we price it after seeing the house, so the quote doesn't move."],
  'included_title': 'What We Do',
  'included_sub': 'Residential building work, managed start to finish.',
  'included': [('House extensions', 'Single-storey and kitchen extensions, from drawings and approvals to the finished room.'),
               ('Kitchen refits', 'Strip-out, plumbing, electrics, plastering and fitting by one crew.'),
               ('Bathroom refits', 'Full bathrooms and en-suites, tiled and finished.'),
               ('Media walls', 'Built around your TV and fire, with shelving and lighting.'),
               ('Full refurbishments', 'Whole-room and whole-house refits, planned around you.'),
               ('Site visit and fixed quote', "We see the job before pricing it. The number doesn't move.")],
  'cta_title': 'Get a Price for Your Project',
  'why': [('The price quoted is the price paid', "We see the job before pricing it, so the quote doesn't move."),
          ('One point of contact', 'One phone number from start to finish, not four trades.'),
          ('Based where we work', "We're in West Horndon, Essex. Close enough to be on site when it matters.")],
  'faq': [('Do I need planning permission for an extension?',
           ['Many single-storey rear extensions fall under permitted development, but it depends on the house, its size and its history. '
            'We check this with you at the site visit.']),
          ('Do you manage building regulations?',
           ['Extensions need building regulations sign-off. We build to the regulations and work with the inspector through each stage.']),
          ('Will the price change once work starts?', ['No. We price after seeing the job, and the quote is fixed for the work agreed.']),
          ('Do you supply the kitchen or bathroom, or just fit it?',
           ['Either. You can choose your own units and fittings, or we can source them as part of the quote.']),
          ('Can I stay at home during the work?',
           ['Usually, yes. We plan the order of work so you keep as much of the house usable as possible, and we tell you upfront if there '
            'are days without water or power.']),
          ('Can you fit my existing TV and fire?',
           ['Yes. We design the wall around the TV and fire you have or plan to buy, so share the models in the quote form.'])],
  'areas': ['Brentwood', 'Upminster', 'West Horndon', 'Hornchurch', 'Romford', 'Billericay', 'Basildon', 'Thurrock', 'East London'],
  'related': ['garden-rooms', 'landscaping', 'air-conditioning']},
 {'slug': 'landscaping',
  'trade': 'build',
  'nav': 'Landscaping',
  'service_param': 'landscaping',
  'title': 'Garden Landscaping in Essex &amp; East London | OAK Group',
  'description': 'Garden landscaping in Essex and East London: patios, paving, decking, fencing and planting specified for your plot. '
                 'Pairs with a garden room. Fixed quote after a site visit.',
  'schema_name': 'Garden landscaping',
  'eyebrow': 'Landscaping',
  'h1': 'Garden <em>Landscaping</em> in Essex &amp; East London',
  'lead': 'We design and build patios, paths, decking, fencing and planting, often alongside a garden room. Homes in Brentwood, Upminster, '
          'West Horndon, Hornchurch, Romford, Billericay and across Essex and East London.',
  'facts': ['Patios and paving', 'Decking and fencing', 'Planting'],
  'img': 'landscaping.jpg',
  'img_alt': 'Completed garden landscaping with patio, decking and planting in Essex',
  'kicker': 'A good garden starts with <mark>drainage and levels</mark>, not the paving catalogue.',
  'intro': ["Patios crack and lawns flood when the ground underneath is rushed. The part you walk on only lasts if the part you don't see "
            'was done properly.',
            '<strong>We specify every garden for its plot</strong>: the soil, the slope, the light and how you use it. Building a garden '
            'room too? We plan both together.'],
  'included_title': 'What We Build',
  'included_sub': 'Hard and soft landscaping, planned as one design.',
  'included': [('Patios and paving', 'Laid on a proper sub-base with the right falls, so water runs away from the house.'),
               ('Decking', 'Built to last, on a frame that stays level.'),
               ('Fencing and boundaries', 'Fences, gates and walls that suit the garden and the house.'),
               ('Lawns and planting', 'Turf and planting chosen for your soil and light.'),
               ('Paths and edging', 'Clean edges and paths that connect the garden.'),
               ('Garden room ready', 'Base, paths and power planned in if a garden room is going in.')],
  'why': [('Specified for the plot', "Chosen for your garden, not whatever's left in the yard."),
          ('Garden and garden room together', 'One team plans the room and the garden around it.'),
          ('Based where we work', "We're in West Horndon, Essex. More of your quote goes into the garden.")],
  'faq': [('Can you landscape the garden around a new garden room?',
           ["Yes, and it's better planned together. Paths, levels and power for the room are designed in from the start."]),
          ('Do you do small jobs, like just a patio?',
           ["Yes. Tell us what you need in the quote form and we'll say honestly if it's a job for us."]),
          ('Which areas do you cover?', ['East London and Essex, including Brentwood, Havering and Thurrock. Residential only.'])],
  'related': ['garden-rooms', 'building-works', 'air-conditioning'],
  'gallery': [('decking-garden.jpg', 'Composite decking with raised planters'), ('landscaping-paving.jpg', 'Laying new paving slabs'), ('landscaping.jpg', 'Finished landscaped garden')]}]

BY_SLUG = {p["slug"]: p for p in PAGES}
# Real customer reviews only (Google, Checkatrade, WhatsApp with permission). Never invent one.
# Key = page slug, or "ac" / "build" for every page of that trade. Each review: (quote, name, town, service).
# The reviews section only appears on a page once it has at least one review.
REVIEWS = {}
AREA_LINKS = {}  # no town pages: the towns are named in each page's subheadline
AC_SLUGS = [p["slug"] for p in PAGES if p["trade"] == "ac"]
BUILD_SLUGS = [p["slug"] for p in PAGES if p["trade"] == "build"]


def plain(s):
    """Visible HTML string -> plain text for JSON-LD."""
    import re
    from html import unescape
    return unescape(re.sub(r"<[^>]+>", "", s))


def quote_href(p):
    if not p.get("service_param"):
        return "../#contact"
    q = "?service=" + p["service_param"]
    if p.get("property_param"):
        q += "&amp;property=" + p["property_param"].replace(" ", "%20").replace("/", "%2F")
    return "../" + q + "#contact"


def mail_href(p):
    from urllib.parse import quote
    return "mailto:" + EMAIL + "?subject=" + quote("Quote request: " + plain(p["schema_name"]))


def schema(p):
    url = f"{SITE}/{p['slug']}/"
    areas = p.get("areas") or (AC_AREAS if p["trade"] == "ac" else BUILD_AREAS)
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
                "telephone": "+44 7413 965823",
                "sameAs": SAME_AS,
                "address": ADDRESS,
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
    out = []
    for p in PAGES:
        cur = ' aria-current="page"' if p["slug"] == current else ""
        out.append(f'<a href="../{p["slug"]}/"{cur}>{p["nav"]}</a>')
    out.append('<a href="../#work">Our Work</a>')
    return "\n      ".join(out)


def mobile_links():
    links = [f'<a href="../{p["slug"]}/">{p["nav"]}</a>' for p in PAGES]
    return "\n  ".join(['<a href="../">Home</a>'] + links)


def area_col():
    return "\n        ".join(f"<span>{t}</span>" for t in ["Brentwood", "Upminster", "West Horndon", "Hornchurch", "Romford", "Essex"])


def footer_col(slugs):
    return "\n        ".join(f'<a href="../{s}/">{BY_SLUG[s]["nav"]}</a>' for s in slugs)


def page(p):
    qh = quote_href(p)
    mh = mail_href(p)
    areas = p.get("areas") or (AC_AREAS if p["trade"] == "ac" else BUILD_AREAS)
    if p.get("area_title"):
        area_title, area_text, area_fine = p["area_title"], p["area_text"], p["area_fine"]
    elif p["trade"] == "ac":
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
    shots = p.get("gallery") or [(p["img"], p["img_alt"])]
    slides = "\n        ".join(
        f'<figure class="slide"><img {"fetchpriority=\"high\"" if i == 0 else "loading=\"lazy\""} decoding="async" src="../assets/{f}" alt="{a}"><figcaption>{a}</figcaption></figure>'
        for i, (f, a) in enumerate(shots))
    revs = REVIEWS.get(p["slug"], []) + REVIEWS.get(p["trade"], [])
    reviews = ""
    if revs:
        cards = "\n      ".join(
            f'<figure class="review-card"><div class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>{escape(q)}</blockquote><figcaption><strong>{escape(n)}</strong> &middot; {escape(t)}<span>{escape(sv)}</span></figcaption></figure>'
            for q, n, t, sv in revs)
        reviews = f"""<section class="reviews">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Reviews</span>
      <h2>What Customers Say</h2>
    </div>
    <div class="review-grid">
      {cards}
    </div>
  </div>
</section>

"""
    pills = "".join(f'<a href="../{AREA_LINKS[a]}/">{a}</a>' if a in AREA_LINKS and AREA_LINKS[a] != p["slug"] else f"<span>{a}</span>" for a in areas)
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
  <div class="container">
    <div class="svc-hero-text">
      <span class="eyebrow">{p['eyebrow']}</span>
      <h1>{p['h1']}</h1>
      <p class="lead">{p['lead']}</p>
      <div class="hero-ctas">
        <a class="btn btn-red" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
        <a class="btn btn-ghost-ink" href="tel:{PHONE_INTL}">{ICON_PHONE}Call {PHONE}</a>
      </div>
      <ul class="hero-facts">
          {facts}
      </ul>
    </div>
    <div class="hero-carousel" aria-label="Photos">
      <div class="track">
        {slides}
      </div>
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

<section class="included" id="services">
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
      <h2>{p.get('cta_title') or 'Get a Price for Your ' + p['nav']}</h2>
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

{reviews}<section class="process">
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

<section id="faq">
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

<section class="areas" id="areas">
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
    <p class="fine"><a href="tel:{PHONE_INTL}" style="color:inherit;">{PHONE}</a> &middot; usually answered within one working day</p>
  </div>
</section>
</main>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="footer-logo" href="../"><img loading="lazy" decoding="async" src="../assets/logo-oak-white.png" alt="OAK Construction &amp; Project Management Limited" width="260" height="125"></a>
        <p>Air conditioning and residential construction, based in West Horndon, Essex. Two trades, one point of contact.</p>
        <address class="footer-nap">Station Road, West Horndon, Brentwood CM13 3XL<br><a href="tel:{PHONE_INTL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></address>
      </div>
      <div class="footer-col">
        <h5>Air Conditioning</h5>
        {footer_col(AC_SLUGS)}
      </div>
      <div class="footer-col">
        <h5>Construction</h5>
        {footer_col(BUILD_SLUGS)}
      </div>
      <div class="footer-col">
        <h5>Areas</h5>
        {area_col()}
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 OAK Construction &amp; Project Management Limited, trading as OAK Group</span>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</footer>

<div class="sticky-cta">
  <a class="btn btn-red" href="{qh}">{ICON_MAIL}Get a Free Quote</a>
  <a class="btn btn-ghost-ink" href="tel:{PHONE_INTL}" aria-label="Call OAK Group">{ICON_PHONE}Call</a>
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
  // Photo carousel: slides on its own, pauses while the visitor is touching or hovering it
  var track = document.querySelector('.hero-carousel .track');
  if(track && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){{
    var paused = false;
    ['mouseenter','touchstart','focusin'].forEach(function(ev){{ track.addEventListener(ev, function(){{ paused = true; }}, {{passive:true}}); }});
    ['mouseleave','touchend','focusout'].forEach(function(ev){{ track.addEventListener(ev, function(){{ setTimeout(function(){{ paused = false; }}, 2500); }}, {{passive:true}}); }});
    setInterval(function(){{
      if(paused || track.scrollWidth <= track.clientWidth) return;
      var step = track.querySelector('.slide').getBoundingClientRect().width + 12;
      var atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
      track.scrollTo({{left: atEnd ? 0 : track.scrollLeft + step, behavior: 'smooth'}});
    }}, 3500);
  }}
  menu.querySelectorAll('a').forEach(function(a){{ a.addEventListener('click', function(){{ setOpen(false); }}); }});
}})();
</script>
</body>
</html>
"""


def sitemap():
    urls = [(f"{SITE}/", "1.0")] + [(f"{SITE}/{p['slug']}/", "0.8") for p in PAGES] + [(f"{SITE}/{slug}/", "0.7") for slug in AREA_LINKS.values()]
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
