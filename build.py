# Static page builder for the Contempo Austin concept. Run: python3 build.py
from lib import CFG, img, page, bc, finish
BASE='https://contempo-austin-demo.vercel.app/'
TEL,TEL_H='+15127484351','(512) 748&#8209;4351'
O='<span class="o" aria-hidden="true"></span>'
ORG={"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Contempo Austin","legalName":"ContempoAustin Homes, LLC","url":BASE,"telephone":"+1-512-748-4351",
 "founder":{"@type":"Person","name":"Khamla Santhavi","jobTitle":"President and Creative Director"},
 "address":{"@type":"PostalAddress","streetAddress":"1409 Allen Road","addressLocality":"Austin","addressRegion":"TX","postalCode":"78746","addressCountry":"US"},
 "areaServed":"Austin, Texas","image":BASE+"img/modern-dusk.webp"}
CFG.update(base=BASE,name='Contempo Austin',theme='#1c1e20',org=ORG,
 fonthead='<link rel="preload" as="font" type="font/woff2" href="fonts/bodoni-moda-normal-500-latin.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="fonts/manrope-normal-400-latin.woff2" crossorigin>',
 icon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231c1e20'/%3E%3Ccircle cx='16' cy='16' r='8' stroke='%23b5653a' stroke-width='2.5' fill='none'/%3E%3C/svg%3E",
 bar='Not the official Contempo Austin site. Photos and project text come from Contempo&rsquo;s current Wix site and are used for this pitch only.',
 nav=[('homes.html','Homes'),('approach.html','Approach'),('contact.html','Contact')],
 mark='<a class="mark" href="index.html" aria-label="Contempo Austin home"><span class="wordmark">C'+O+'ntemp'+O+'</span><small>Austin</small></a>',
 cta='<a class="btn" href="contact.html">Start a home</a>',
 foot=f'''<footer class="foot"><div class="wrap">
<p class="foot-mast">C{O}ntemp{O}</p>
<div class="foot-grid"><div><p class="kicker" style="color:var(--copper)">Talk to Khamla</p><p class="foot-call"><a href="tel:{TEL}">{TEL_H}</a></p></div>
<address>Contempo Austin<br>1409 Allen Road<br>Austin, Texas 78746</address>
<ul><li><a href="homes.html">Finished homes</a></li><li><a href="homes.html#in-progress">In progress</a></li><li><a href="approach.html">Approach</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div class="foot-row"><span>Luxury homes, built in Austin, Texas.</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>''')

FIN=['Redbud','Barn Swallow',"Bird&rsquo;s Eye View",'Bohn House','Lake House','Chelsea','EastSide Gem','Nest in the City','Thousand Oaks','Cueva de Oro','Barn Swallow #2']
page('index.html','Contempo Austin | Luxury Custom Homes in Westlake and Austin',
 'Contempo Austin finds the lot, designs the home and builds it, with finishes imported for each project. See Bird&rsquo;s Eye View and Bohn House, then call us.', f'''
<section class="cover"><div class="cover-photo">{img('modern-dusk.webp','A modern Contempo home lit up at dusk, with a stepped stone path across the lawn',eager=True,sizes='100vw')}</div>
<div class="wrap cover-in">
 <p class="cover-mast rv" aria-hidden="true">C{O}ntemp{O}</p>
 <div class="cover-lines rv"><p class="kicker" style="color:#f3c9a8">Austin, Texas &middot; Luxury custom homes</p>
 <h1>Luxury homes with their own personality and soul.</h1>
 <p class="lede">Contempo Austin tailors every step: finding the lot in one of Austin&rsquo;s finest neighborhoods, designing something unique, and building it with finishes imported for each home.</p>
 <div class="cta"><a class="btn light" href="homes.html">See the homes</a><a class="btn btn--plain light" href="contact.html">Start a home</a></div></div>
 <ul class="cover-index rv" aria-label="In this issue"><li><span>01</span>Bird&rsquo;s Eye View, Westlake</li><li><span>02</span>Bohn House, 1937</li><li><span>03</span>Lake House, Lake Travis</li><li><span>04</span>Now building: Darter Lane</li></ul>
</div></section>

<section class="feature"><div class="wrap ft-grid">
 <div class="ft-copy rv"><p class="kicker">{O} Feature &middot; Bird&rsquo;s Eye View</p><h2>Sunrise and sunset with the turn of a chair.</h2>
 <p>A house at the top of the hill with 360 degrees of views, right in the heart of Westlake. One of the only places in Austin where you can watch both ends of the day from the same seat.</p><a class="btn btn--plain" href="homes.html#birds-eye-view">The project</a></div>
 <figure class="ft-a rv">{img('poolside.webp','Pool and terrace at Bird&rsquo;s Eye View',sizes='(max-width:900px) 100vw, 40vw')}</figure>
 <figure class="ft-b rv">{img('bedroom-glass.webp','Bedroom with full height glass at Bird&rsquo;s Eye View',sizes='(max-width:900px) 60vw, 25vw')}</figure>
</div></section>

<section class="bohn"><div class="wrap bh-grid">
 <figure class="bh-circle rv">{img('round-door.webp','The round doorway at Bohn House',sizes='(max-width:900px) 80vw, 40vw')}</figure>
 <div class="rv"><p class="kicker" style="color:var(--copper)">{O} Renovation &middot; Bohn House</p><h2>Designed in 1937 after <em>Lost Horizon.</em> Renovated by Contempo in 2013.</h2>
 <p>A home based on the science fiction film, completely renovated so it reads as modern Austin without losing its original soul and history.</p></div>
</div></section>

<section class="range"><div class="wrap rg-grid">
 <div class="rv"><p class="kicker">{O} Range</p><h2>Over 15 years building more than houses.</h2></div>
 <ul class="rg-list rv"><li>Single family homes</li><li>Multifamily apartment complexes</li><li>Commercial buildings</li><li>Industrial parks</li><li class="hl">Now: high end technical construction and luxury homes</li></ul>
</div></section>

<section class="index-strip"><div class="wrap"><p class="kicker rv">{O} Finished homes</p>
<ol class="names rv">{''.join(f'<li>{n}</li>' for n in FIN)}</ol><a class="btn" href="homes.html">Browse the portfolio</a></div></section>

<section class="closing"><div class="closing-photo">{img('lawn-steps.webp','A Contempo home with stepping stones across the lawn',sizes='100vw')}</div><div class="wrap"><div class="cl-card rv"><h2>Have a lot in mind? Or need help finding one?</h2><p>Contempo starts there.</p><a class="btn" href="contact.html">Talk to Contempo</a></div></div></section>''', extra_ld=[bc(('Home',''))])

PROJ=[('birds-eye-view',"Bird&rsquo;s Eye View",'Westlake','Finished','A house at the top of the hill with 360 degrees of jaw dropping views, right in the heart of Westlake. One of the only places in Austin where you can see the sunrise and the sunset with the turn of a chair.',['poolside.webp','bedroom-glass.webp']),
 ('bohn-house','Bohn House','Austin','Renovated 2013','A unique home designed in 1937 based on the science fiction film Lost Horizon. Completely renovated by Contempo in 2013, it has become an emblematic reflection of modern and contemporary Austin, without losing its original soul and rich history.',['round-door.webp','stair.webp']),
 ('lake-house','Lake House','Lake Travis','Finished','An ideal family house, framed within Lake Travis and the Hill Country, that makes you feel like you are on vacation every day.',['interior-dining.webp'])]
page('homes.html','Homes by Contempo Austin | Finished and In Progress Projects',
 'Bird&rsquo;s Eye View in Westlake, the 1937 Bohn House, Lake House on Lake Travis and two homes now underway. Browse the Contempo Austin portfolio, then call.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{O} The portfolio</p><h1 class="rv">Every home gets its own personality.</h1></div></section>
{''.join(f"""<section class="proj" id="{s}"><div class="wrap pj-grid"><div class="pj-copy rv"><p class="kicker">{O} {st} &middot; {loc}</p><h2>{n}</h2><p>{d}</p></div><div class="pj-imgs">{''.join(f'<figure class="rv">'+img(i,n+' by Contempo Austin',sizes='(max-width:900px) 100vw, 50vw')+'</figure>' for i in ims)}</div></div></section>""" for s,n,loc,st,d,ims in PROJ)}
<section class="proj inprog" id="in-progress"><div class="wrap"><p class="kicker rv">{O} In progress</p><h2 class="rv">Now building</h2>
<div class="ip-grid"><figure class="rv">{img('hero-pool-dusk.webp','Image from the 1306 Darter Lane project page',sizes='(max-width:900px) 100vw, 50vw')}<figcaption><b>1306 Darter Lane</b> In progress</figcaption></figure>
<figure class="rv">{img('hill-house.webp','Image from the 801 Terrace Mountain Drive project page',sizes='(max-width:900px) 100vw, 50vw')}<figcaption><b>801 Terrace Mountain Drive</b> In progress</figcaption></figure></div>
<p class="note rv">Images as posted on each project page. Contempo to confirm which are renderings.</p></div></section>
<section class="more"><div class="wrap"><p class="kicker rv">{O} More finished homes</p><div class="more-grid">
{''.join(f'<figure class="rv">'+img(i,'A finished home from the Contempo Austin portfolio',sizes='(max-width:700px) 100vw, 33vw')+'</figure>' for i in ['two-story.webp','infinity-pool.webp','courtyard.webp','street-modern.webp','oak-house.webp','lawn-steps.webp'])}</div>
<p class="note rv">Also finished: {', '.join(FIN)}.</p>
<div class="ph rv"><b>Placeholder</b>Project names, locations and photo credits for each image above, from Contempo.</div></div></section>''',
 extra_ld=[bc(('Home',''),('Homes','homes.html'))])

page('approach.html','How Contempo Austin Builds a Luxury Home, From Lot to Finish',
 'Contempo Austin tailors each step: the lot, the design, the craftsmanship and finishes imported for each home. Read the approach, then call (512) 748 4351.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{O} Approach</p><h1 class="rv">Tailored at every step, from the lot to the last finish.</h1></div></section>
<section class="steps"><div class="wrap"><ol class="st">{''.join(f'<li class="rv"><span class="num">{i+1:02d}</span><div><h2>{a}</h2><p>{b}</p></div></li>' for i,(a,b) in enumerate([('Find the location','Contempo starts by finding the ideal lot in one of Austin&rsquo;s finest residential areas.'),('Develop a unique design','Each home gets an outstanding and unique design, built around open layouts and the people who will live there.'),('Build it with skill','Highly skilled craftsmanship combined with cutting edge technical expertise.'),('Import the finishes','Distinctive finishes are imported specifically for each home, so no two feel the same.')]))}</ol></div></section>
<section class="leader"><div class="wrap ld-grid"><div class="ph-portrait rv" role="img" aria-label="Placeholder for a portrait of Khamla Santhavi"><span>Portrait of Khamla</span></div>
<div class="rv"><p class="kicker">{O} Leadership</p><h2>Khamla Santhavi</h2><p>President and creative director of ContempoAustin Homes since 2013, leading interior and architectural design and the company&rsquo;s daily operations.</p>
<div class="ph"><b>Placeholder</b>A few lines from Khamla on how Contempo chooses a lot and a design.</div></div></div></section>''',
 extra_ld=[bc(('Home',''),('Approach','approach.html'))])

page('contact.html','Contact Contempo Austin | Start a Custom Home in Austin, Texas',
 'Tell Contempo Austin about your lot or the neighborhood you want. Call (512) 748 4351 or send a note to start a luxury custom home in Austin, Texas today.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{O} Contact</p><h1 class="rv">Start with the lot. Or the idea.</h1></div></section>
<section class="contact"><div class="wrap ct-grid">
<form class="rv" data-demo="Thank you. On the live site this goes to Contempo. (Demo: nothing was sent.)" novalidate>
<div class="fld"><label for="nm">Name</label><input id="nm" name="nm" autocomplete="name" required></div>
<div class="fld"><label for="em">Email</label><input id="em" name="em" type="email" autocomplete="email" required></div>
<div class="fld"><label for="ph">Phone</label><input id="ph" name="ph" type="tel" autocomplete="tel"></div>
<div class="fld"><label for="st">Where are you?</label><select id="st" name="st"><option>I own a lot</option><option>I need help finding one</option><option>I want to renovate</option></select></div>
<div class="fld"><label for="msg">Tell us about the home</label><textarea id="msg" name="msg"></textarea></div>
<button class="btn" type="submit">Send</button><p class="formmsg" role="status" aria-live="polite"></p></form>
<aside class="rv"><p class="ct-big"><a href="tel:{TEL}">{TEL_H}</a></p><address>1409 Allen Road<br>Austin, Texas 78746</address>
<div class="ph"><b>Placeholder</b>A Contempo email address. The current site lists a personal Gmail; Khamla to confirm the right inbox.</div></aside></div></section>''',
 extra_ld=[bc(('Home',''),('Contact','contact.html'))])

page('404.html','Page Not Found | Contempo Austin Concept, Homes in Austin',
 'That page is not part of the Contempo Austin concept. Head back to the cover, browse the finished homes, or call Contempo to start a custom home in Austin.', f'''
<section class="page-head"><div class="wrap"><p class="kicker">{O} Not found</p><h1>This page was never built.</h1><a class="btn" href="index.html">Back to the cover</a></div></section>''')
finish(['index.html','homes.html','approach.html','contact.html'])
print('built')
