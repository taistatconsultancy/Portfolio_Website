from pathlib import Path

root = Path(r"C:\Users\MULINGWA STEPHEN\Documents\Portfolio\My Portfolio")

def apply(path, replacements, label):
    text = path.read_text(encoding="utf-8")
    for a, b in replacements:
        if a not in text:
            print(f"{label} MISS:", a[:90].replace("\n", " "))
        else:
            text = text.replace(a, b, 1)
    path.write_text(text, encoding="utf-8")
    print(f"{label} done")

kiki_reps = [
    (
        "TaiStat AgroLink Case Study | Stephen Mulingwa — Data &amp; Platform",
        "Kiki's Mobile Wellness Case Study | Stephen Mulingwa — Software &amp; Web",
    ),
    (
        "TaiStat AgroLink blockchain marketplace for Kenyan agriculture — portfolio project by Stephen Mulingwa, data scientist &amp; TaiStat founder.",
        "Kiki's Mobile Wellness operations portal — appointments, sales, stock, and staff PWA built by Stephen Mulingwa.",
    ),
    (
        "https://stephenmulingwa.com/project-taistat-agrolink.html",
        "https://stephenmulingwa.com/project-kiki-mobile-wellness.html",
    ),
    ("<span>TaiStat AgroLink</span>", "<span>Kiki's Mobile Wellness</span>"),
    (
        '<h1>TaiStat <span class="text-gradient">AgroLink</span></h1>',
        '<h1>Kiki\'s <span class="text-gradient">Mobile Wellness</span></h1>',
    ),
    (
        "A Kenya-first blockchain marketplace connecting verified farmers with trusted buyers through transparent pricing, fair markets, and guaranteed sales.",
        "A role-based operations portal for a Nairobi wellness business — appointments, sales, stock, staff, and expenses in one installable web app.",
    ),
    (
        """      <span class="meta-chip"><i class="bi bi-shield-check"></i> Blockchain</span>
      <span class="meta-chip"><i class="bi bi-geo-alt"></i> 34 Counties</span>
      <span class="meta-chip"><i class="bi bi-people"></i> Farmer–Buyer Platform</span>
      <span class="meta-chip"><i class="bi bi-bar-chart"></i> Smart Pricing</span>""",
        """      <span class="meta-chip"><i class="bi bi-phone"></i> PWA</span>
      <span class="meta-chip"><i class="bi bi-calendar-check"></i> Appointments</span>
      <span class="meta-chip"><i class="bi bi-box-seam"></i> Stock &amp; Sales</span>
      <span class="meta-chip"><i class="bi bi-people"></i> Staff Roles</span>""",
    ),
    (
        'src="assets/img/portfolio/taistat-agrolink.jpg.png" alt="TaiStat AgroLink"',
        'src="assets/img/portfolio/kiki-mobile-wellness.png" alt="Kiki\'s Mobile Wellness"',
    ),
    (
        """        <p>Farmers and buyers in Kenya often dealt with unclear pricing, little traceability from farm to buyer, and no single place to trade with trust. Middlemen and information gaps made it hard for farmers to get fair prices and for buyers to be sure of origin and quality.</p>
        <p>A transparent, verifiable marketplace was missing — one that could level the playing field between producers and buyers across Kenya's diverse agricultural regions.</p>""",
        """        <p>Kiki's Mobile Wellness was running appointments, payments, inventory, staff duties, and referrals across spreadsheets and ad-hoc tools. Revenue, stock levels, and day-to-day ops were hard to track in one place.</p>
        <p>The business needed a single, mobile-friendly operations system staff could install and use daily — with clear roles for admin, front desk, and therapists.</p>""",
    ),
    (
        """        <p>I contributed to the design and implementation of a <strong style="color:var(--text-heading)">blockchain-based agri-marketplace</strong> so that every crop could be traced from farm to buyer. The system supports verified farmer onboarding with KYC-style checks, so only vetted producers can list produce. Buyers see clear provenance and can connect with farmers in real time.</p>
        <p>Smart pricing and a tender system were built so that offers and bids are visible and fair. The platform also uses a coin-based model for payments and bidding, making it easier to settle and to run auctions.</p>
        <p>My work focused on the data and analytics side: how traceability data is stored and queried, how pricing and tender data feed into the platform, and how dashboards and reports can sit on top of the blockchain and application data.</p>

        <div class="county-strip">
          <div class="county-num">34</div>
          <div class="county-text">
            <strong>Kenyan Counties Covered</strong>
            A nationwide rollout giving farmers and buyers across Kenya access to a verified, fair marketplace.
          </div>
        </div>""",
        """        <p>I designed and built a <strong style="color:var(--text-heading)">Next.js operations PWA</strong> with JWT auth, Neon Postgres (Prisma), and role-based portals for Admin, Front Desk, and Staff.</p>
        <p>The app covers appointment calendars (with Google Calendar sync), multi-step checkout (cash, M-Pesa, card, and more), sales and client records, stock movements, expense tracking, service referrals, and admin analytics with P&amp;L views.</p>
        <p>It ships as an installable Progressive Web App so the team can run the business from phones and desktops without a separate native app store release.</p>

        <div class="county-strip">
          <div class="county-num">3</div>
          <div class="county-text">
            <strong>Role-Based Portals</strong>
            Admin, Front Desk, and Staff experiences with permissions tailored to daily wellness operations.
          </div>
        </div>""",
    ),
    (
        """        <p>The platform gives verified farmers and trusted buyers a single place to trade with end-to-end visibility, fairer pricing, and clearer accountability. It supports better market access for farmers and more reliable supply and traceability for buyers.</p>
        <ul>
          <li>End-to-end traceability from farm to buyer via blockchain</li>
          <li>Verified KYC onboarding for all farmers and buyers</li>
          <li>Real-time farmer–buyer connections across 34 counties</li>
          <li>Smart pricing and open tender system for fair bidding</li>
          <li>Coin-based payment and auction settlement model</li>
          <li>Analytics dashboards and reports on top of platform data</li>
        </ul>""",
        """        <p>Staff now manage bookings, sales, stock, and expenses in one branded system — with clearer accountability and faster day-to-day workflows for a Westlands, Nairobi wellness business.</p>
        <ul>
          <li>Appointment scheduling with complete / cancel / no-show flows</li>
          <li>Checkout supporting cash, M-Pesa, card, bank, gift card, and split payments</li>
          <li>Stock inventory, movements, and staff product possessions</li>
          <li>Expense tracking by category and referral payment statuses</li>
          <li>Admin revenue, expenses, P&amp;L, and stock-value dashboards</li>
          <li>Installable PWA with offline-friendly service worker support</li>
        </ul>""",
    ),
    (
        """          <span class="label">Category</span>
          <span class="value">Blockchain</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Client</span>
          <span class="value">TaiStat Firm</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Reach</span>
          <span class="value">34 Counties</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Type</span>
          <span class="value">Marketplace Platform</span>
        </div>""",
        """          <span class="label">Category</span>
          <span class="value">Software / Web App</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Client</span>
          <span class="value">Kiki's Mobile Wellness</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Location</span>
          <span class="value">Nairobi, Kenya</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Type</span>
          <span class="value">Operations PWA</span>
        </div>""",
    ),
    (
        """          <span class="tag">Blockchain</span>
          <span class="tag">Smart Contracts</span>
          <span class="tag">Python</span>
          <span class="tag">Node.js</span>
          <span class="tag">Database</span>
          <span class="tag">Data Analytics</span>
          <span class="tag">KYC / Identity</span>""",
        """          <span class="tag">Next.js</span>
          <span class="tag">React</span>
          <span class="tag">TypeScript</span>
          <span class="tag">Prisma</span>
          <span class="tag">Neon Postgres</span>
          <span class="tag">JWT Auth</span>
          <span class="tag">PWA</span>
          <span class="tag">Vercel</span>""",
    ),
    (
        """          <a href="https://www.mkulimasokoni.com/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="bi bi-box-arrow-up-right"></i> Visit Mkulima Sokoni
          </a>""",
        """          <a href="https://kiki-mobile.vercel.app" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="bi bi-box-arrow-up-right"></i> Visit App
          </a>""",
    ),
    (
        "Stephen Mulingwa &nbsp;·&nbsp; Data Scientist",
        "Stephen Mulingwa &nbsp;·&nbsp; Software Developer &amp; Data Scientist",
    ),
]

web_reps = [
    (
        "TaiStat AgroLink Case Study | Stephen Mulingwa — Data &amp; Platform",
        "TaiStat Website Case Study | Stephen Mulingwa — Web Development",
    ),
    (
        "TaiStat AgroLink blockchain marketplace for Kenyan agriculture — portfolio project by Stephen Mulingwa, data scientist &amp; TaiStat founder.",
        "TaiStat Firm website — AI and data consultancy site built and delivered by Stephen Mulingwa.",
    ),
    (
        "https://stephenmulingwa.com/project-taistat-agrolink.html",
        "https://stephenmulingwa.com/project-taistat-website.html",
    ),
    ("<span>TaiStat AgroLink</span>", "<span>TaiStat Website</span>"),
    (
        '<h1>TaiStat <span class="text-gradient">AgroLink</span></h1>',
        '<h1>TaiStat <span class="text-gradient">Firm Website</span></h1>',
    ),
    (
        "A Kenya-first blockchain marketplace connecting verified farmers with trusted buyers through transparent pricing, fair markets, and guaranteed sales.",
        "The public web presence for TaiStat Firm — showcasing AI, data consultancy, agriculture solutions, and services to clients worldwide.",
    ),
    (
        """      <span class="meta-chip"><i class="bi bi-shield-check"></i> Blockchain</span>
      <span class="meta-chip"><i class="bi bi-geo-alt"></i> 34 Counties</span>
      <span class="meta-chip"><i class="bi bi-people"></i> Farmer–Buyer Platform</span>
      <span class="meta-chip"><i class="bi bi-bar-chart"></i> Smart Pricing</span>""",
        """      <span class="meta-chip"><i class="bi bi-globe2"></i> Web Development</span>
      <span class="meta-chip"><i class="bi bi-building"></i> Company Site</span>
      <span class="meta-chip"><i class="bi bi-robot"></i> AI &amp; Data</span>
      <span class="meta-chip"><i class="bi bi-newspaper"></i> Blog &amp; Services</span>""",
    ),
    (
        'src="assets/img/portfolio/taistat-agrolink.jpg.png" alt="TaiStat AgroLink"',
        'src="assets/img/portfolio/taistat-website.png" alt="TaiStat Firm Website"',
    ),
    (
        """        <p>Farmers and buyers in Kenya often dealt with unclear pricing, little traceability from farm to buyer, and no single place to trade with trust. Middlemen and information gaps made it hard for farmers to get fair prices and for buyers to be sure of origin and quality.</p>
        <p>A transparent, verifiable marketplace was missing — one that could level the playing field between producers and buyers across Kenya's diverse agricultural regions.</p>""",
        """        <p>TaiStat needed a clear, professional website that explained its AI and data consultancy offering — especially agriculture impact — and made it easy for clients to explore services, portfolio work, and get in touch.</p>
        <p>Without a strong web presence, it was harder to communicate capability, showcase flagship products like Mkulima Sokoni, and convert enquiries into conversations.</p>""",
    ),
    (
        """        <p>I contributed to the design and implementation of a <strong style="color:var(--text-heading)">blockchain-based agri-marketplace</strong> so that every crop could be traced from farm to buyer. The system supports verified farmer onboarding with KYC-style checks, so only vetted producers can list produce. Buyers see clear provenance and can connect with farmers in real time.</p>
        <p>Smart pricing and a tender system were built so that offers and bids are visible and fair. The platform also uses a coin-based model for payments and bidding, making it easier to settle and to run auctions.</p>
        <p>My work focused on the data and analytics side: how traceability data is stored and queried, how pricing and tender data feed into the platform, and how dashboards and reports can sit on top of the blockchain and application data.</p>

        <div class="county-strip">
          <div class="county-num">34</div>
          <div class="county-text">
            <strong>Kenyan Counties Covered</strong>
            A nationwide rollout giving farmers and buyers across Kenya access to a verified, fair marketplace.
          </div>
        </div>""",
        """        <p>I delivered the <strong style="color:var(--text-heading)">TaiStat Firm website</strong> at taistat.com — structuring home messaging, services, industries, portfolio highlights, about content, blog entry points, and contact paths.</p>
        <p>The site positions TaiStat as an AI and data consultancy rooted in Nairobi, with clear CTAs and sections for agriculture technology, enterprise analytics, training, and custom software.</p>
        <p>This was a full web development delivery: layout, content hierarchy, responsive behaviour, and production launch for a client-facing brand site.</p>

        <div class="county-strip">
          <div class="county-num">1</div>
          <div class="county-text">
            <strong>Live Company Website</strong>
            Public brand presence for TaiStat Firm serving clients worldwide from Nairobi.
          </div>
        </div>""",
    ),
    (
        """        <p>The platform gives verified farmers and trusted buyers a single place to trade with end-to-end visibility, fairer pricing, and clearer accountability. It supports better market access for farmers and more reliable supply and traceability for buyers.</p>
        <ul>
          <li>End-to-end traceability from farm to buyer via blockchain</li>
          <li>Verified KYC onboarding for all farmers and buyers</li>
          <li>Real-time farmer–buyer connections across 34 counties</li>
          <li>Smart pricing and open tender system for fair bidding</li>
          <li>Coin-based payment and auction settlement model</li>
          <li>Analytics dashboards and reports on top of platform data</li>
        </ul>""",
        """        <p>TaiStat now has a clear digital front door that explains services, highlights flagship agriculture work, and routes prospects to contact and content.</p>
        <ul>
          <li>Responsive company website at taistat.com</li>
          <li>Services and industries structured for consultancy discovery</li>
          <li>Portfolio and flagship project storytelling (including Mkulima Sokoni)</li>
          <li>Blog and newsletter entry points for ongoing content</li>
          <li>Contact and CTA paths for client acquisition</li>
          <li>Brand-aligned layout for a Nairobi-based AI &amp; data firm</li>
        </ul>""",
    ),
    (
        """          <span class="label">Category</span>
          <span class="value">Blockchain</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Client</span>
          <span class="value">TaiStat Firm</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Reach</span>
          <span class="value">34 Counties</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Type</span>
          <span class="value">Marketplace Platform</span>
        </div>""",
        """          <span class="label">Category</span>
          <span class="value">Web Development</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Client</span>
          <span class="value">TaiStat Firm</span>
        </div>
        <div class="sidebar-row">
          <span class="label">URL</span>
          <span class="value">taistat.com</span>
        </div>
        <div class="sidebar-row">
          <span class="label">Type</span>
          <span class="value">Company Website</span>
        </div>""",
    ),
    (
        """          <span class="tag">Blockchain</span>
          <span class="tag">Smart Contracts</span>
          <span class="tag">Python</span>
          <span class="tag">Node.js</span>
          <span class="tag">Database</span>
          <span class="tag">Data Analytics</span>
          <span class="tag">KYC / Identity</span>""",
        """          <span class="tag">Web Development</span>
          <span class="tag">HTML / CSS</span>
          <span class="tag">JavaScript</span>
          <span class="tag">Responsive Design</span>
          <span class="tag">SEO</span>
          <span class="tag">Content Architecture</span>""",
    ),
    (
        """          <a href="https://www.mkulimasokoni.com/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="bi bi-box-arrow-up-right"></i> Visit Mkulima Sokoni
          </a>""",
        """          <a href="https://taistat.com/" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="bi bi-box-arrow-up-right"></i> Visit TaiStat
          </a>""",
    ),
    (
        "Stephen Mulingwa &nbsp;·&nbsp; Data Scientist",
        "Stephen Mulingwa &nbsp;·&nbsp; Software Developer &amp; Data Scientist",
    ),
]

apply(root / "project-kiki-mobile-wellness.html", kiki_reps, "Kiki")
apply(root / "project-taistat-website.html", web_reps, "Web")
