"""Builds every HTML page of the TechSphire site.

All navigation, footer, service, industry and page content lives here.
Edit this file, then run:  python3 tools/build_site.py
"""
import html
import pathlib
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent

EMAIL = "hello@techsphire.com"
SUPPORT = "support@techsphire.com"
CAREERS = "careers@techsphire.com"
PHONE, TEL = "+1 (000) 000-0000", "+10000000000"
SHAPES = '<div class="shapes" aria-hidden="true"><span></span><span></span><span></span></div>'


def icon(d):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')


CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'

IC = {
    "erp": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/>',
    "digital": '<path d="m16 18 6-6-6-6M8 6l-6 6 6 6"/>',
    "data": '<path d="M3 3v18h18"/><path d="M7 16v-4M12 16V8M17 16v-7"/>',
    "ai": '<path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/><circle cx="12" cy="12" r="3"/>',
    "consulting": '<circle cx="12" cy="12" r="10"/><path d="m16.24 7.76-2.12 6.36-6.36 2.12 2.12-6.36z"/>',
    "managed": '<path d="M3 11h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5a9 9 0 0 1 18 0v5a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "security": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
    "gcc": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
    "engineering": '<circle cx="12" cy="12" r="3"/><path d="M12 1v3M12 20v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M1 12h3M20 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
}

# --------------------------------------------------------------------------- service catalog
# (key, title, short blurb, intro, [(id, name, description)])
PRACTICES = [
    ("erp", "Enterprise Applications",
     "Implement, upgrade and integrate the platforms that run your business.",
     "Modernise the core systems that run your business. We implement, upgrade, integrate and support the world's leading enterprise platforms — and connect them into one seamless landscape.",
     [("sap", "SAP", "S/4HANA implementation and migration, SAP BTP extensions, and application management services."),
      ("oracle", "Oracle", "Oracle Cloud ERP, HCM and SCM implementation, upgrades and managed support."),
      ("microsoft", "Microsoft Dynamics 365", "Finance, Supply Chain, Business Central and CRM solutions on the Microsoft cloud."),
      ("enterprise-integration", "Enterprise Integration", "API-led integration with MuleSoft, Boomi and Azure Integration Services that connects every system."),
      ("servicenow", "ServiceNow", "ITSM, ITOM, HR and customer service workflows that automate the enterprise."),
      ("salesforce", "Salesforce", "Sales, Service and Marketing Cloud implementations that put the customer at the centre.")]),
    ("digital", "Digital Transformation",
     "Modern applications, products and experiences built for scale.",
     "Reimagine how you serve customers and run operations. Our engineering teams design, build and modernise digital products that are secure, scalable and a pleasure to use.",
     [("application-services", "Application Services", "Custom application development, legacy modernisation and long-term application management."),
      ("digital-services", "Digital Services", "Web platforms, customer portals and mobile apps that deliver exceptional digital experiences."),
      ("devops", "DevOps", "CI/CD pipelines, infrastructure as code and platform engineering for faster, safer releases."),
      ("product-engineering", "Product Engineering", "End-to-end SaaS and software product development — from MVP to global scale."),
      ("iot", "Internet of Things (IoT)", "Connected devices, edge computing and IoT platforms that turn sensor data into action."),
      ("experience-design", "Experience Design", "Research-led UX and UI design that makes complex systems simple and intuitive.")]),
    ("data", "Data &amp; Analytics",
     "Trusted data foundations and insight that drive better decisions.",
     "Turn data into a competitive advantage. We build modern data platforms, establish governance you can trust and deliver insight to every decision-maker.",
     [("data-engineering", "Data Engineering", "Modern data platforms, pipelines and lakehouses on Azure, AWS, Snowflake and Databricks."),
      ("data-management", "Data Management", "Master data, data quality and governance programmes that make your data trustworthy."),
      ("epm", "Enterprise Performance Management (EPM)", "Planning, budgeting, consolidation and financial reporting on leading EPM platforms."),
      ("bi", "BI &amp; Visualization", "Self-service dashboards and reporting in Power BI, Tableau and Looker.")]),
    ("ai", "AI &amp; Automation",
     "Agentic and generative AI, data science and intelligent automation.",
     "Put AI to work safely and at scale. Our AI Centre of Excellence takes you from use-case discovery to production — with governance, security and measurable ROI built in.",
     [("agentic-ai", "Agentic AI", "Autonomous AI agents that plan, act and complete multi-step business workflows."),
      ("generative-ai", "Generative AI", "Copilots, assistants and content generation grounded securely in your own data."),
      ("data-science", "Data Science &amp; ML", "Predictive models and machine learning that forecast demand, risk and opportunity."),
      ("quality-engineering", "Intelligent Quality Engineering", "AI-assisted test automation that accelerates releases and raises quality."),
      ("rpa", "Robotic Process Automation", "Software bots that eliminate repetitive, rules-based work across your systems.")]),
    ("consulting", "IT Strategy &amp; Consulting",
     "Roadmaps, architecture and leadership for confident technology decisions.",
     "Make confident technology decisions. Our senior consultants align IT with your business strategy and lead complex change from boardroom to delivery.",
     [("it-strategy", "IT Strategy &amp; Roadmaps", "Clear, prioritised technology roadmaps aligned to your business goals and budget."),
      ("transformation-advisory", "Digital Transformation Advisory", "Operating model, value case and change leadership for transformation programmes."),
      ("enterprise-architecture", "Enterprise Architecture", "Target-state architecture, rationalisation and technology governance."),
      ("virtual-cio", "Virtual CIO / CTO", "Experienced technology leadership on a flexible, fractional basis."),
      ("program-management", "Program Management", "PMO and programme leadership that delivers complex initiatives on time and on budget.")]),
    ("managed", "Managed Services",
     "24/7 operations, application management and business process services.",
     "Hand day-to-day operations to a team that prevents problems before they happen — with predictable costs, clear service levels and continuous improvement.",
     [("managed-it", "Managed IT Services", "24/7 monitoring, service desk and maintenance for a predictable monthly fee."),
      ("application-management", "Application Management", "Support, enhancements and optimisation of your business-critical applications."),
      ("business-process", "Business Process Services", "Finance, HR and back-office operations delivered with process expertise and automation."),
      ("staffing", "IT Staffing", "Vetted specialists and dedicated teams that scale with your demand.")]),
    ("cloud", "Infrastructure &amp; Cloud",
     "Resilient infrastructure and multi-cloud operations, run around the clock.",
     "Build on a foundation that never sleeps. We design, migrate and operate resilient infrastructure across data centres and every major cloud.",
     [("service-desk", "Service Desk &amp; Smart Hands", "Multilingual 24/7 service desk and on-site technical support wherever you operate."),
      ("data-center", "Data Center Services", "Design, consolidation, migration and management of data centre infrastructure."),
      ("multi-cloud", "Multi-Cloud Services", "Migration, landing zones, FinOps and managed operations on Azure, AWS and Google Cloud."),
      ("sre", "Site Reliability Engineering (SRE)", "Observability, automation and incident engineering that keep critical services available."),
      ("m365", "Microsoft 365 Services", "Deployment, migration, security and adoption for Microsoft 365 and Teams."),
      ("noc", "Network Operations Center (NOC)", "Proactive 24/7 network monitoring, management and incident response.")]),
    ("security", "Cyber Security",
     "Round-the-clock protection, identity security and compliance.",
     "Protect your people, data and reputation. Our security teams detect and stop threats around the clock and help you prove compliance to customers and regulators.",
     [("soc", "Security Operations Center (SOC)", "24/7 threat monitoring, detection and response by certified security analysts."),
      ("iam", "Identity &amp; Access Management (IAM)", "SSO, MFA and privileged access management that protect every identity."),
      ("vulnerability", "Vulnerability &amp; Penetration Testing", "Continuous scanning and expert-led testing that find weaknesses before attackers do."),
      ("grc", "Governance, Risk &amp; Compliance", "ISO 27001, SOC 2, GDPR and industry compliance programmes, end to end.")]),
    ("gcc", "Global Capability Centers",
     "Set up, operate and scale your own global capability center.",
     "Build world-class capability at scale. We help enterprises design, launch and run Global Capability Centers that become engines of innovation and efficiency.",
     [("gcc-setup", "GCC Strategy &amp; Setup", "Location strategy, entity setup, talent acquisition and infrastructure for your own center."),
      ("build-operate-transfer", "Build-Operate-Transfer", "We build and run your center, then transfer it to you when you're ready."),
      ("gcc-operations", "GCC Operations &amp; Scaling", "Governance, talent and service management to grow capability with confidence.")]),
    ("engineering", "Engineering Services",
     "Product lifecycle, design and smart manufacturing solutions.",
     "Accelerate innovation from design to the shop floor. Our engineering services connect product data, design and manufacturing into one digital thread.",
     [("plm", "Product Lifecycle Management (PLM)", "PLM implementation, migration and integration that unify product data across the enterprise."),
      ("product-design", "Product Design &amp; Development", "Mechanical, electrical and embedded design services from concept to production."),
      ("mes", "Manufacturing Execution Systems (MES)", "Shop-floor systems that improve quality, traceability and throughput."),
      ("transformational-services", "Transformational Services", "Digital thread, smart factory and Industry 4.0 programmes that modernise engineering.")]),
]
P = {p[0]: p for p in PRACTICES}
TOTAL_SERVICES = sum(len(p[4]) for p in PRACTICES)
MEGA_COLUMNS = [["erp", "digital"], ["data", "ai", "gcc"], ["consulting", "managed", "engineering"], ["cloud", "security"]]

INDUSTRIES = [
    ("healthcare", "Healthcare &amp; Life Sciences", "#e11d48",
     '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>',
     "Secure, compliant platforms that protect patient data and accelerate better outcomes.",
     ["Electronic health record integration", "HIPAA-ready cloud and security", "Clinical data platforms and analytics", "Patient engagement apps"]),
    ("financial-services", "Banking &amp; Financial Services", "#0284c7",
     '<path d="M3 22h18M6 18v-7M10 18v-7M14 18v-7M18 18v-7M12 2l8 5H4z"/>',
     "Resilient, regulated technology for banks, insurers, wealth managers and fintechs.",
     ["Core modernisation and cloud migration", "Fraud analytics and AI", "Regulatory compliance and reporting", "Digital onboarding and self-service"]),
    ("retail", "Retail &amp; Consumer Goods", "#d97706",
     '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
     "Omnichannel commerce, supply chain visibility and data-driven customer experiences.",
     ["E-commerce and order management", "Demand forecasting with AI", "Store and POS systems support", "Customer data platforms"]),
    ("manufacturing", "Manufacturing", "#475569",
     '<path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/>',
     "Connected operations from engineering and ERP to the shop floor.",
     ["ERP and MES implementation", "PLM and digital thread", "IoT and predictive maintenance", "Supply chain analytics"]),
    ("energy", "Energy &amp; Utilities", "#16a34a",
     '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
     "Reliable, secure systems for generation, grid operations and customer service.",
     ["Asset and work management", "OT and IT security", "Smart metering data platforms", "Field service mobility"]),
    ("hi-tech", "Hi-Tech &amp; Software", "#7c3aed",
     '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M15 2v2M15 20v2M2 15h2M2 9h2M20 15h2M20 9h2M9 2v2M9 20v2"/>',
     "Product engineering, platform scale and AI for technology companies.",
     ["SaaS product engineering", "Cloud-native platforms and SRE", "Quality engineering at scale", "Generative AI features"]),
    ("public-sector", "Public Sector &amp; Education", "#2563eb",
     '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
     "Cost-effective, secure digital services for government, education and non-profits.",
     ["Citizen and student portals", "Cloud and Microsoft 365 adoption", "Cybersecurity and compliance", "Data and reporting platforms"]),
    ("logistics", "Logistics &amp; Transportation", "#ea580c",
     '<path d="M10 17h4V5H2v12h3M20 17h2v-3.34a4 4 0 0 0-1.17-2.83L19 9h-5v8h1"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
     "Real-time visibility, integration and automation that keep goods moving.",
     ["Transport and warehouse systems", "Track-and-trace and IoT", "Partner and EDI integration", "Route and capacity optimisation"]),
    ("professional-services", "Professional Services", "#0f766e",
     '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
     "Secure, efficient IT for legal, accounting and consulting firms.",
     ["Managed IT and 24/7 support", "Document and knowledge management", "Client portals and automation", "Data protection and compliance"]),
]

FAQ = [
    ("What size of organisations do you work with?",
     "We partner with organisations of every size — from fast-growing mid-market companies to global enterprises — scaling our teams and engagement model to fit your needs."),
    ("What's the difference between IT consulting and managed services?",
     "IT consulting helps you decide what to do: strategy, architecture, roadmaps and major programmes. Managed services take care of running it day to day — monitoring, support, security and maintenance — under agreed service levels. Many clients use both."),
    ("How do you ensure quality and security?",
     "Every engagement follows defined delivery and security practices: experienced leads, peer review, automated testing, least-privilege access and full documentation. We align with your own policies and compliance requirements."),
    ("Can you work alongside our in-house IT team?",
     "Absolutely. We regularly co-deliver with internal teams — adding specialist skills, extra capacity, after-hours cover or a complete managed service — while you keep full control."),
    ("Do we own everything you build for us?",
     "Yes. All code, configurations, documentation and credentials belong to you. We document everything so you're never locked in."),
    ("How do we get started?",
     "Book a free consultation. We'll learn about your goals and current landscape, then send a clear proposal with scope, timeline and transparent pricing — no obligation."),
]

PLATFORMS = ["Microsoft", "AWS", "Google Cloud", "SAP", "Oracle", "Salesforce",
             "ServiceNow", "Snowflake", "Databricks", "Cisco", "CrowdStrike", "Okta"]


# --------------------------------------------------------------------------- layout
def head(title, desc):
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{t}</title>
  <meta name="description" content="{d}">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#0f2130">
  <link rel="icon" href="assets/img/logo-small.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
"""


def mega_menu():
    cols = []
    for col in MEGA_COLUMNS:
        groups = []
        for key in col:
            _, title, _, _, svcs = P[key]
            items = "".join(f'<li><a href="services.html#{sid}">{name}</a></li>' for sid, name, _ in svcs)
            groups.append(f'<div class="mega-group"><h4><a href="services.html#{key}">{icon(IC[key])}{title}</a></h4><ul>{items}</ul></div>')
        cols.append(f'<div>{"".join(groups)}</div>')
    promo = """<div class="mega-promo">
                <img src="assets/img/photos/px-ai.webp" alt="" loading="lazy" width="260" height="130">
                <div><strong>Free AI Readiness Assessment</strong><p>Find the AI use cases that will move the needle for your business — in two weeks.</p><a href="contact.html">Book your assessment →</a></div>
              </div>"""
    return f"""<div class="mega">
            <div class="container mega-grid">{"".join(cols)}{promo}</div>
            <div class="mega-foot"><div class="container"><span>{len(PRACTICES)} practice areas · {TOTAL_SERVICES} specialist services · one accountable partner</span><a href="contact.html">Not sure where to start? Talk to an expert →</a></div></div>
          </div>"""


def dropdown(items):
    links = "".join(f'<a href="{h}">{t}<small>{s}</small></a>' for h, t, s in items)
    return f'<div class="dropdown">{links}</div>'


def trigger(label, active):
    style = ' style="color:var(--brand)"' if active else ""
    return f'<button class="nav-trigger" aria-expanded="false"{style}>{label} {CHEVRON}</button>'


def header(current):
    ind_menu = '<div class="dropdown">' + "".join(
        f'<a href="industries.html#{k}">{n}</a>' for k, n, *_ in INDUSTRIES) + \
        '<a href="industries.html" style="color:var(--brand)">All industries →</a></div>'
    about_menu = dropdown([
        ("about.html", "About TechSphire", "Our story, mission and values"),
        ("about.html#approach", "Our approach", "Advise, build and run"),
        ("about.html#leadership", "Leadership", "Meet the team"),
        ("careers.html", "Careers", "Join our team"),
    ])
    careers_cur = ' aria-current="page"' if current == "careers.html" else ""
    return f"""
  <div class="topbar">
    <div class="container">
      <span>IT services &amp; consulting for ambitious enterprises</span>
      <nav aria-label="Utility">
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="tel:{TEL}">{PHONE}</a>
        <a href="careers.html">Careers</a>
        <a href="contact.html#support">Client support</a>
      </nav>
    </div>
  </div>

  <header class="site-header">
    <nav class="container nav" aria-label="Main">
      <a class="logo" href="index.html"><img src="assets/img/logo-small.svg" alt="" width="38" height="38"><span>Tech<b>Sphire</b></span></a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <ul class="nav-links" id="nav-links">
        <li class="has-drop">
          {trigger("Services &amp; Solutions", current == "services.html")}
          {mega_menu()}
        </li>
        <li class="has-drop small">
          {trigger("Industries", current == "industries.html")}
          {ind_menu}
        </li>
        <li class="has-drop small">
          {trigger("About", current == "about.html")}
          {about_menu}
        </li>
        <li><a href="careers.html"{careers_cur}>Careers</a></li>
        <li class="nav-cta"><a class="btn btn-primary" href="contact.html">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <main id="main">
"""


SOCIAL = {
    "LinkedIn": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/>',
    "X": '<path d="M4 4l16 16M20 4 4 20"/>',
    "Facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
    "YouTube": '<path d="M22.5 6.4a2.8 2.8 0 0 0-2-2C18.8 4 12 4 12 4s-6.8 0-8.5.4a2.8 2.8 0 0 0-2 2A29 29 0 0 0 1 12a29 29 0 0 0 .5 5.6 2.8 2.8 0 0 0 2 2c1.7.4 8.5.4 8.5.4s6.8 0 8.5-.4a2.8 2.8 0 0 0 2-2A29 29 0 0 0 23 12a29 29 0 0 0-.5-5.6z"/><path d="m10 15 5-3-5-3z"/>',
}
social = "".join(f'<a href="#" aria-label="{n}">{icon(d)}</a>' for n, d in SOCIAL.items())
foot_services = "".join(f'<li><a href="services.html#{k}">{t}</a></li>' for k, t, *_ in PRACTICES)
foot_ind = "".join(f'<li><a href="industries.html#{k}">{n}</a></li>' for k, n, *_ in INDUSTRIES[:7])

FOOTER = f"""  </main>

  <footer class="site-footer">
    <div class="footer-top">
      <div class="container">
        <h2>Let's build the <span class="grad-text">intelligent enterprise</span> together.</h2>
        <!-- Add data-endpoint="https://formspree.io/f/your-id" to collect sign-ups directly. -->
        <form class="newsletter" id="newsletter" data-email="{EMAIL}" novalidate>
          <label for="nl-email">Get insights on AI, cloud and security in your inbox</label>
          <div class="nl-row">
            <input id="nl-email" name="email" type="email" placeholder="Your work email" autocomplete="email" required>
            <button class="btn btn-primary" type="submit">Subscribe</button>
          </div>
          <p class="nl-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
    <div class="footer-main">
      <div class="container footer-grid wide">
        <div class="footer-brand">
          <a class="logo" href="index.html"><img src="assets/img/logo-small.svg" alt="" width="38" height="38"><span>Tech<b>Sphire</b></span></a>
          <p>IT services &amp; consulting for ambitious enterprises</p>
          <div class="social">{social}</div>
        </div>
        <div>
          <h4>Services</h4>
          <ul>{foot_services}</ul>
        </div>
        <div>
          <h4>Industries</h4>
          <ul>{foot_ind}<li><a href="industries.html">All industries</a></li></ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About us</a></li>
            <li><a href="about.html#leadership">Leadership</a></li>
            <li><a href="careers.html">Careers</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Get in touch</h4>
          <ul>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="tel:{TEL}">{PHONE}</a></li>
            <li><a href="contact.html#support">Client support</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <span>© <span data-year>2026</span> TechSphire. All rights reserved.</span>
        <nav aria-label="Legal"><a href="privacy.html">Privacy Policy</a><a href="contact.html">Contact</a></nav>
      </div>
    </div>
  </footer>

  <div class="mobile-cta">
    <a class="btn btn-ghost" href="tel:{TEL}">Call us</a>
    <a class="btn btn-primary" href="contact.html">Talk to an expert</a>
  </div>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def page_hero(crumb, eyebrow, h1, p, photo=None):
    cls = " photo" if photo else ""
    bg = f'\n      <div class="ph-bg" style="background-image:url(assets/img/photos/{photo}.webp)"></div>' if photo else ""
    return f"""    <section class="page-hero dark{cls}">{bg}
      <div class="container">
        <div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
        <span class="eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p>{p}</p>
      </div>
    </section>
"""


CTA_BG = """<div class="cta-bg" aria-hidden="true">
            <div class="bar"><i></i><i></i><i></i></div>
            <table>
              <tr><th>Ticket</th><th>Request</th><th>Priority</th><th>Status</th></tr>
              <tr><td>#1042</td><td>New starter laptop &amp; accounts</td><td>Normal</td><td>Resolved</td></tr>
              <tr><td>#1041</td><td>VPN access for remote team</td><td>High</td><td>Resolved</td></tr>
              <tr><td>#1040</td><td>Microsoft 365 licence change</td><td>Normal</td><td>Resolved</td></tr>
              <tr><td>#1039</td><td>Firewall rule update</td><td>High</td><td>Resolved</td></tr>
              <tr><td>#1038</td><td>Monthly backup restore test</td><td>Normal</td><td>Passed</td></tr>
            </table>
          </div>"""


def cta(h, p, label, extra=""):
    return f"""
    <section class="section" style="padding-top:24px">
      <div class="container">
        <div class="cta reveal">
          {CTA_BG}
          <h2>{h}</h2>
          <p>{p}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="contact.html">{label}</a>{extra}
          </div>
        </div>
      </div>
    </section>
"""


def section_head(eyebrow, h2, p="", center=True):
    eb = f'          <span class="eyebrow">{eyebrow}</span>\n' if eyebrow else ""
    pp = f"\n          <p>{p}</p>" if p else ""
    return f"""        <div class="section-head{" center" if center else ""} reveal">
{eb}          <h2>{h2}</h2>{pp}
        </div>
"""


def write(name, title, desc, body):
    (ROOT / name).write_text(head(title, desc) + header(name) + body + FOOTER)


def ind_card(k, n, color, d, desc, bullets, link=True):
    if link:
        return f"""          <a class="industry-card reveal" href="industries.html#{k}">
            <div class="ind-icon" style="--c:{color}">{icon(d)}</div>
            <h3>{n}</h3>
            <p>{desc}</p>
            <span class="more">Explore →</span>
          </a>"""
    items = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""          <article class="industry-card photo reveal" id="{k}">
            <img src="assets/img/photos/ind-{k}.webp" alt="" loading="lazy" width="1100" height="720">
            <div class="ic-body">
              <div class="ind-icon" style="--c:{color}">{icon(d)}</div>
              <h3>{n}</h3>
              <p>{desc}</p>
              <ul>{items}</ul>
            </div>
          </article>"""


# --------------------------------------------------------------------------- home
FEATURED = {"ai", "cloud"}
ORDER = ["ai", "erp", "digital", "data", "consulting", "cloud", "managed", "security", "gcc", "engineering"]


def practice_card(key):
    _, title, blurb, _, svcs = P[key]
    chips = "".join(f'<li><a href="services.html#{sid}">{name}</a></li>' for sid, name, _ in svcs)
    feat = " featured" if key in FEATURED else ""
    return f"""          <article class="practice{feat} reveal">
            <div class="icon">{icon(IC[key])}</div>
            <h3><a href="services.html#{key}">{title}</a></h3>
            <p>{blurb}</p>
            <ul>{chips}</ul>
            <a class="more" href="services.html#{key}">Explore →</a>
          </article>"""


practice_cards = "\n".join(practice_card(k) for k in ORDER)
industry_cards = "\n".join(ind_card(*i) for i in INDUSTRIES)
wordmarks = "".join(f"<span>{w}</span>" for w in PLATFORMS)
faq = "\n".join(f"""          <details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>""" for q, a in FAQ)

TL = [
    ('<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>', "Discover",
     "A senior consultant reviews your goals, landscape, risks and costs — usually within a week."),
    ('<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>', "Strategise",
     "A practical roadmap and proposal with priorities, milestones and transparent pricing."),
    ('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>', "Deliver",
     "Certified teams implement, migrate and test with agile governance and minimal disruption."),
    (IC["managed"], "Run &amp; optimise",
     "24/7 operations, service management and continuous improvement against agreed SLAs."),
]
timeline = "\n".join(f"""            <li>
              <span class="t-icon">{icon(d)}</span>
              <div><h3>{t}</h3><p>{p}</p></div>
            </li>""" for d, t, p in TL)

WHY = [
    (IC["security"], "Security by design", "Best-practice controls built into every project and service — never bolted on."),
    ('<circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/>', "Certified experts", "Senior architects, consultants and engineers across every major platform."),
    ('<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>', "Outcome-based pricing", "Fixed-price projects, managed services and outcome-linked commercial models."),
    ('<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>', "24/7 global delivery", "Follow-the-sun operations with agreed response times for every priority."),
    (IC["consulting"], "Vendor-neutral advice", "We recommend what's right for you — never what's easiest to sell."),
    ('<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>', "No lock-in", "You own everything we build — fully documented and transferable."),
]
why = "\n".join(f"""          <div class="feature reveal">
            <div class="f-icon">{icon(d)}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </div>""" for d, t, p in WHY)

ROWS = [("Infrastructure & cloud", "reviewed"), ("Applications & data", "mapped"), ("Security posture", "scored"),
        ("AI & automation readiness", "assessed"), ("Cost optimisation", "identified")]
term_rows = "".join(f'  <span class="t-ok">✓</span> {l.ljust(29).replace("&", "&amp;")}<span class="t-dim">{v}</span>\n' for l, v in ROWS)
TERMINAL = f"""<div class="terminal reveal" role="img" aria-label="Example IT assessment: infrastructure, applications, security, AI readiness and costs reviewed; roadmap ready.">
<pre><span class="t-dim">$</span> <span class="t-cmd">techsphire</span> assess <span class="t-dim">--org</span> <span class="t-str">"your-enterprise"</span>

{term_rows}
<span class="t-acc">→</span> Your transformation roadmap is ready.</pre>
        </div>"""

SLIDES = [
    (None, "Intelligent enterprise", "IT services &amp; consulting",
     'Engineering the <span class="grad-text">intelligent enterprise</span>',
     "TechSphire helps enterprises modernise core systems, harness data and AI, secure every layer and run technology at scale — with one accountable partner from strategy to 24/7 operations.",
     ("Talk to an expert", "contact.html"), ("Explore services", "services.html")),
    ("hero-ai", "AI &amp; Automation", "AI &amp; automation",
     'Put <span class="grad-text">AI to work</span> across your business',
     "From agentic AI and copilots to intelligent automation — we take AI from idea to production safely, with governance and measurable ROI built in.",
     ("Book an AI readiness assessment", "contact.html"), ("Explore AI services", "services.html#ai")),
    ("hero-cloud", "Cloud &amp; Security", "Infrastructure, cloud &amp; cyber security",
     'Resilient cloud. <span class="grad-text">Secure by design.</span>',
     "Migrate, modernise and operate across every major cloud — protected by a 24/7 Security Operations Center and identity-first security.",
     ("Talk to a cloud expert", "contact.html"), ("Explore cloud &amp; security", "services.html#cloud")),
    ("hero-consulting", "Strategy &amp; Consulting", "IT strategy &amp; consulting",
     'Strategy that turns into <span class="grad-text">measurable results</span>',
     "Senior consultants align technology with your business goals — and stay accountable through delivery and beyond.",
     ("Book a free consultation", "contact.html"), ("Our approach", "about.html#approach")),
]


def slide(i, s):
    photo, _, eyebrow, heading, lead, (l1, h1), (l2, h2) = s
    tag = "h1" if i == 0 else "h2"
    bg = f' style="background-image:url(assets/img/photos/{photo}.webp)"' if photo else ""
    plain = " data-plain" if not photo else ""
    active = " is-active" if i == 0 else ""
    return f"""          <div class="slide{active}"{plain} id="slide-{i}" role="tabpanel">
            <div class="slide-bg"{bg}></div>
            <div class="container slide-inner">
              <div class="slide-copy">
                <span class="eyebrow">{eyebrow}</span>
                <{tag}>{heading}</{tag}>
                <p class="lead">{lead}</p>
                <div class="hero-actions">
                  <a class="btn btn-primary" href="{h1}">{l1}</a>
                  <a class="btn btn-ghost" href="{h2}">{l2}</a>
                </div>
              </div>
            </div>
          </div>"""


slides_html = "\n".join(slide(i, s) for i, s in enumerate(SLIDES))
slider_tabs = "".join(
    f'<button class="slider-tab{" is-active" if i == 0 else ""}" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="slide-{i}"><i></i><b>{i + 1:02d}</b><span>{s[1]}</span></button>'
    for i, s in enumerate(SLIDES))

# Service explorer
ex_tabs = "\n".join(
    f'            <button class="ex-tab{" is-active" if n == 0 else ""}" role="tab" data-tab="{k}" aria-selected="{"true" if n == 0 else "false"}"><span class="ex-ic">{icon(IC[k])}</span>{P[k][1]}</button>'
    for n, k in enumerate(ORDER))
ex_panels = []
for n, k in enumerate(ORDER):
    _, title, _, intro, svcs = P[k]
    items = "".join(f'<li><a href="services.html#{sid}">{name}</a></li>' for sid, name, _ in svcs)
    ex_panels.append(f"""            <div class="ex-panel{" is-active" if n == 0 else ""}" data-panel="{k}" role="tabpanel">
              <div class="ex-media"><img src="assets/img/photos/px-{k}.webp" alt="" loading="lazy" width="1000" height="680"><span class="num">{n + 1:02d} / {len(ORDER):02d}</span></div>
              <div class="ex-body">
                <h3>{title}</h3>
                <p>{intro}</p>
                <ul>{items}</ul>
                <a class="btn btn-primary" style="border-radius:999px" href="services.html#{k}">Explore {title}</a>
              </div>
            </div>""")
ex_panels = "\n".join(ex_panels)

# Industry selector
ind_tabs = "".join(
    f'<button class="ind-tab{" is-active" if n == 0 else ""}" role="tab" data-tab="{k}" aria-selected="{"true" if n == 0 else "false"}" style="--c:{color}">{icon(d)}{name}</button>'
    for n, (k, name, color, d, *_ ) in enumerate(INDUSTRIES))
ind_panels = "\n".join(f"""          <div class="ind-panel{" is-active" if n == 0 else ""}" data-panel="{k}" role="tabpanel">
            <img src="assets/img/photos/ind-{k}.webp" alt="" loading="lazy" width="1100" height="720">
            <div class="ind-body">
              <h3>{name}</h3>
              <p>{desc}</p>
              <ul class="checklist">{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
              <a class="btn btn-primary" href="industries.html#{k}">Explore {name}</a>
            </div>
          </div>""" for n, (k, name, color, d, desc, bullets) in enumerate(INDUSTRIES))

# Scroll story
STORY = [
    ("Discover", "px-consulting", "A senior consultant reviews your goals, landscape, risks and costs — usually within a week.",
     ["Stakeholder workshops", "Current-state assessment", "Quick wins identified"]),
    ("Strategise", "px-data", "A practical roadmap and proposal with priorities, milestones and transparent pricing.",
     ["Target architecture", "Business case and ROI", "Phased delivery plan"]),
    ("Deliver", "px-digital", "Certified teams implement, migrate and test with agile governance and minimal disruption.",
     ["Agile delivery with regular demos", "Automated testing and quality gates", "Change management and training"]),
    ("Run &amp; optimise", "px-managed", "24/7 operations, service management and continuous improvement against agreed SLAs.",
     ["24/7 monitoring and support", "Executive reporting and reviews", "Continuous optimisation"]),
]
story_visual = "\n".join(f"""            <div class="sv-item{" is-active" if n == 0 else ""}">
              <img src="assets/img/photos/{img}.webp" alt="" loading="lazy" width="1000" height="680">
              <div class="sv-cap"><b>{n + 1:02d}</b><span>{t}</span></div>
            </div>""" for n, (t, img, _, _) in enumerate(STORY))
story_steps = "\n".join(f"""            <div class="story-step{" is-active" if n == 0 else ""}">
              <span class="num">STEP {n + 1:02d}</span>
              <h3>{t}</h3>
              <p>{p}</p>
              <ul>{"".join(f"<li>{b}</li>" for b in bl)}</ul>
            </div>""" for n, (t, _, p, bl) in enumerate(STORY))

ROW1 = ["Microsoft Azure", "AWS", "Google Cloud", "SAP", "Oracle", "Salesforce", "ServiceNow", "Microsoft 365"]
ROW2 = ["Snowflake", "Databricks", "Power BI", "Cisco", "CrowdStrike", "Okta", "Palo Alto Networks", "Kubernetes"]
marq = lambda row: "".join(f"<span>{w}</span>" for w in row * 2)

home = f"""    <section class="hero-slider show-globe" data-slider aria-roledescription="carousel">
      <div class="slides">
{slides_html}
      </div>
      <div class="globe-wrap" aria-hidden="true"><canvas id="globe"></canvas></div>
      <div class="slider-tabs"><div class="container" role="tablist">{slider_tabs}</div></div>
    </section>

    <section class="stats-band">
      <div class="container">
        <div class="stat"><strong data-count="{len(PRACTICES)}">{len(PRACTICES)}</strong><span>Practice areas</span></div>
        <div class="stat"><strong data-count="{TOTAL_SERVICES}">{TOTAL_SERVICES}</strong><span>Specialist services</span></div>
        <div class="stat"><strong>24/7</strong><span>Global operations &amp; support</span></div>
        <div class="stat"><strong data-count="{len(INDUSTRIES)}">{len(INDUSTRIES)}</strong><span>Industries served</span></div>
      </div>
    </section>

    <section class="section">
      <div class="container">
{section_head("Services &amp; solutions", "End-to-end capabilities for the modern enterprise", "Explore our practice areas — from strategy and enterprise platforms to AI, cloud and cyber security.")}        <div class="explorer reveal" data-tabs data-hover>
          <div class="ex-list" role="tablist">
{ex_tabs}
          </div>
          <div class="ex-panels">
{ex_panels}
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="marquee-panel reveal">
          <h2>Deep expertise across the platforms that power the enterprise</h2>
          <p>Certified architects and engineers who design, implement and run solutions on the world's leading cloud, enterprise and security platforms.</p>
          <div class="marquee" aria-label="Platforms we work with"><div class="marquee-track">{marq(ROW1)}</div></div>
          <div class="marquee reverse" aria-hidden="true"><div class="marquee-track">{marq(ROW2)}</div></div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
{section_head("Industries", "Industry depth that accelerates results", "We combine technology expertise with a deep understanding of the regulations, processes and pressures in your sector.")}        <div class="reveal" data-tabs>
          <div class="ind-tabs" role="tablist">{ind_tabs}</div>
{ind_panels}
        </div>
      </div>
    </section>

    <section class="section story-sec">
      <div class="container">
{section_head("How we engage", "From first conversation to 24/7 operations", "A proven approach that de-risks transformation and keeps value flowing long after go-live.", center=False)}        <div class="story">
          <div class="story-visual" aria-hidden="true">
{story_visual}
          </div>
          <div class="story-steps">
{story_steps}
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container spotlight">
        <div class="reveal">
          <span class="eyebrow">Free enterprise IT assessment</span>
          <h2>Know exactly where you stand — and what to do next</h2>
          <p style="color:var(--muted);font-size:1.1rem">Our consultants review your infrastructure, applications, data, security and AI readiness, then deliver a prioritised roadmap with clear costs and quick wins.</p>
          <ul class="checklist">
            <li>Independent, vendor-neutral findings</li>
            <li>Risk, cost and opportunity scoring</li>
            <li>A 90-day action plan and long-term roadmap</li>
          </ul>
          <div class="hero-actions" style="justify-content:flex-start"><a class="btn btn-primary" style="border-radius:999px" href="contact.html">Request your assessment</a></div>
        </div>
        {TERMINAL}
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
{section_head("Why TechSphire", "The partner enterprises trust to deliver", "Senior expertise, transparent engagement and service you can count on.")}        <div class="features center stagger">
{why}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
{section_head("FAQ", "Frequently asked questions")}        <div class="faq reveal">
{faq}
        </div>
      </div>
    </section>
{cta("Ready to build your intelligent enterprise?", "Talk to our experts about your goals. We'll respond within one business day to arrange a free consultation.", "Talk to an expert")}"""


write("index.html", "TechSphire — IT Services & Consulting for the Intelligent Enterprise",
      "TechSphire is an IT services and consulting company: enterprise applications, digital transformation, data & AI, cloud, cyber security, managed services and more.",
      home)

# --------------------------------------------------------------------------- services
catalog_nav = "".join(f'<a href="#{k}">{t}</a>' for k, t, *_ in PRACTICES)
sections = []
for n, (k, t, _, intro, svcs) in enumerate(PRACTICES, 1):
    cards = "\n".join(f"""            <div class="svc reveal" id="{sid}">
              <h3>{name}</h3>
              <p>{d}</p>
            </div>""" for sid, name, d in svcs)
    sections.append(f"""        <section class="practice-section" id="{k}">
          <div class="practice-head reveal">
            <div class="icon">{icon(IC[k])}</div>
            <div>
              <span class="num">{n:02d}</span>
              <h2>{t}</h2>
              <p>{intro}</p>
            </div>
          </div>
          <div class="svc-grid stagger">
{cards}
          </div>
        </section>""")

services = page_hero("Services &amp; Solutions", "Services &amp; solutions", "End-to-end services for the intelligent enterprise",
                     f"{len(PRACTICES)} practice areas and {TOTAL_SERVICES} specialist services — from strategy and enterprise platforms to AI, cloud, cyber security and 24/7 operations.", "page-services") + f"""
    <section class="section">
      <div class="container catalog">
        <aside class="catalog-nav">
          <p>Practice areas</p>
          {catalog_nav}
        </aside>
        <div>
{chr(10).join(sections)}
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
{section_head("Engagement models", "Flexible ways to work with us", "Choose the model that fits your organisation — or combine them.")}        <div class="features">
          <div class="feature reveal"><span class="tag">Consulting</span><h3>Advisory engagements</h3><p>Assessments, strategy and expert advice, scoped to exactly what you need.</p></div>
          <div class="feature reveal"><span class="tag">Projects</span><h3>Fixed-scope delivery</h3><p>Defined deliverables, milestones and price for implementations, migrations and builds.</p></div>
          <div class="feature reveal"><span class="tag">Managed</span><h3>Managed services</h3><p>Outcome-based operations with agreed SLAs and 24/7 coverage.</p></div>
        </div>
      </div>
    </section>
{cta("Not sure where to start?", "Book a free consultation. We'll review your landscape, identify risks and opportunities, and recommend practical next steps.", "Talk to an expert")}"""

write("services.html", "Services & Solutions — TechSphire",
      "Enterprise applications, digital transformation, data & analytics, AI & automation, IT consulting, managed services, infrastructure & cloud, cyber security, GCCs and engineering services.",
      services)

# --------------------------------------------------------------------------- industries
ind_detail = "\n".join(ind_card(*i, link=False) for i in INDUSTRIES)
industries = page_hero("Industries", "Industries", "Industry expertise that accelerates results",
                       "Technology works best when it fits your sector. Our teams bring the domain knowledge, compliance experience and proven solutions your industry demands.", "page-industries") + f"""
    <section class="section">
      <div class="container">
        <div class="industry-grid stagger">
{ind_detail}
        </div>
      </div>
    </section>
{cta("Don't see your industry?", "Our capabilities apply across sectors. Tell us about your organisation and we'll show you how we can help.", "Talk to an expert")}"""

write("industries.html", "Industries — TechSphire",
      "Industry-focused IT services and consulting for healthcare, financial services, retail, manufacturing, energy, hi-tech, public sector, logistics and professional services.",
      industries)

# --------------------------------------------------------------------------- about
def value(ic, t, p):
    return f"""          <div class="card value reveal">
            <div class="icon">{icon(ic)}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </div>"""


def person(initials, name, role):
    return f"""          <div class="card reveal" style="text-align:center">
            <div class="icon" style="margin:0 auto 18px;width:88px;height:88px;border-radius:50%;font-size:1.6rem;font-weight:800">{initials}</div>
            <h3>{name}</h3>
            <p>{role}</p>
          </div>"""


about = page_hero("About", "About TechSphire", "Your partner for the intelligent enterprise",
                  "TechSphire is an IT services and consulting company helping organisations modernise, innovate with data and AI, stay secure and run technology at scale.", "page-about") + f"""
    <section class="section">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Our story</span>
          <h2>Built on expertise, integrity and partnership</h2>
          <p>TechSphire was founded on a simple belief: every organisation deserves enterprise-grade technology and genuinely independent advice.</p>
          <p>We brought together consultants, architects, engineers, data scientists and security specialists under one roof — so our clients get a single accountable partner from strategy through delivery to round-the-clock operations.</p>
          <p>Today we help organisations across industries modernise their core systems, put data and AI to work, protect what matters and keep their business running.</p>
        </div>
        <div class="story-img reveal"><img src="assets/img/photos/about-story.webp" alt="TechSphire office" loading="lazy" width="1100" height="900"></div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="mv-band reveal">
          <div><span class="eyebrow" style="color:#67e8f9">Mission</span><h3>Why we exist</h3><p>To help organisations grow by delivering reliable, secure and innovative technology — and by being a partner they can always count on.</p></div>
          <div><span class="eyebrow" style="color:#67e8f9">Vision</span><h3>Where we're going</h3><p>To be the most trusted technology partner for the enterprises we serve.</p></div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
{section_head("Our values", "What guides everything we do")}        <div class="grid grid-4 stagger">
{value('<path d="M20 6 9 17l-5-5"/>', "Integrity", "Honest advice, transparent pricing and no surprises — ever.")}
{value('<path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/>', "Excellence", "High standards in every project, every ticket and every line of code.")}
{value('<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>', "Partnership", "We succeed only when our clients succeed.")}
{value('<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2z"/>', "Innovation", "Always learning, always looking for a better way.")}
        </div>
      </div>
    </section>

    <section class="section" id="approach" style="scroll-margin-top:80px">
      <div class="container split">
        <div class="reveal">
          <span class="eyebrow">Our approach</span>
          <h2>Advise. Build. Run.</h2>
          <p>Our integrated model means the people who design your solution understand how it will be operated — and the people who operate it understand why it was built.</p>
          <ul class="checklist">
            <li><strong>Advise</strong> — strategy, architecture and roadmaps grounded in business outcomes.</li>
            <li><strong>Build</strong> — enterprise platforms, cloud, data, AI and software delivered by certified teams.</li>
            <li><strong>Run</strong> — 24/7 managed services that keep everything secure, available and improving.</li>
          </ul>
        </div>
        <div class="reveal">
          <span class="eyebrow">Our commitments</span>
          <h2>What you can expect</h2>
          <ul class="checklist">
            <li>A named engagement lead who knows your business.</li>
            <li>Clear proposals with fixed or transparent pricing.</li>
            <li>Agreed service levels and regular executive reporting.</li>
            <li>Full documentation — you own everything we build.</li>
            <li>Security and data protection built into every engagement.</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section-alt" id="leadership" style="scroll-margin-top:80px">
      <div class="container">
{section_head("Leadership", "Meet our leadership team", "Replace these placeholders with your leadership team's names, roles and photos.")}        <div class="grid grid-3 stagger">
{person("AB", "Your Name", "Founder &amp; Chief Executive Officer")}
{person("CD", "Team Member", "Chief Technology Officer")}
{person("EF", "Team Member", "Head of Consulting &amp; Delivery")}
        </div>
      </div>
    </section>
{cta("Want to work with us?", "Whether you're a potential client or a future teammate, we'd love to hear from you.", "Contact us", chr(10) + '            <a class="btn btn-ghost" href="careers.html">View careers</a>')}"""

write("about.html", "About us — TechSphire",
      "TechSphire is an IT services and consulting company. Learn about our story, mission, values, approach and leadership.",
      about)

# --------------------------------------------------------------------------- careers
ROLES = [
    ("SAP S/4HANA Consultant", "Enterprise Applications · Hybrid · Full-time"),
    ("Cloud Solutions Architect", "Infrastructure &amp; Cloud · Hybrid · Full-time"),
    ("Generative AI Engineer", "AI &amp; Automation · Remote / Hybrid · Full-time"),
    ("SOC Analyst", "Cyber Security · On-site / Hybrid · Full-time"),
    ("Data Engineer", "Data &amp; Analytics · Remote / Hybrid · Full-time"),
    ("Full-Stack Developer", "Digital Transformation · Remote / Hybrid · Full-time"),
]


def role(t, meta):
    subj = "Application: " + html.unescape(t)
    return f"""          <article class="card reveal">
            <h3>{t}</h3>
            <p>{meta}</p>
            <a class="link" href="mailto:{CAREERS}?subject={quote(subj)}">Apply now →</a>
          </article>"""


careers = page_hero("Careers", "Careers", "Build what's next with TechSphire",
                    "Join consultants, engineers and data scientists solving meaningful problems for leading organisations — and grow your career while you do it.", "page-careers") + f"""
    <section class="section">
      <div class="container">
{section_head("Why join us", "Life at TechSphire")}        <div class="grid grid-3 stagger">
          <div class="card reveal">
            <div class="icon">{icon('<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2zM22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>')}</div>
            <h3>Learning &amp; growth</h3>
            <p>Paid certifications across SAP, Microsoft, AWS, Google Cloud, security and AI, plus mentoring and clear career paths.</p>
          </div>
          <div class="card reveal">
            <div class="icon">{icon(IC["gcc"])}</div>
            <h3>Meaningful work</h3>
            <p>Complex, high-impact programmes for enterprises across industries and technologies.</p>
          </div>
          <div class="card reveal">
            <div class="icon">{icon('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>')}</div>
            <h3>Flexibility &amp; wellbeing</h3>
            <p>Hybrid working, competitive pay, health benefits and generous time off.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
{section_head("Open roles", "Current openings", "Update this list as roles open and close.", center=False)}        <div class="grid grid-2 stagger">
{chr(10).join(role(t, m) for t, m in ROLES)}
        </div>
        <p class="reveal" style="margin-top:32px;text-align:center">Don't see the right role? Send your CV to <a href="mailto:{CAREERS}">{CAREERS}</a> — we're always happy to meet talented people.</p>
      </div>
    </section>
"""

write("careers.html", "Careers — TechSphire",
      "Join TechSphire. Careers in enterprise applications, cloud, AI, data, cyber security and digital engineering.",
      careers)

# --------------------------------------------------------------------------- contact
options = "\n".join(f"                <option>{t}</option>" for _, t, *_ in PRACTICES)
contact = page_hero("Contact", "Contact us", "Let's talk about your goals",
                    "Book a free consultation, request a proposal or get support — we'll respond within one business day.", "page-contact") + f"""
    <section class="section">
      <div class="container contact-grid">
        <!-- To submit via a form service (e.g. Formspree), add data-endpoint="https://formspree.io/f/your-id" below.
             Without it, the form opens the visitor's email app addressed to data-email. -->
        <form class="form reveal" id="contact-form" data-email="{EMAIL}" novalidate>
          <div class="form-row">
            <div>
              <label for="name">Full name *</label>
              <input id="name" name="name" type="text" autocomplete="name" required>
            </div>
            <div>
              <label for="email">Work email *</label>
              <input id="email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="company">Company</label>
              <input id="company" name="company" type="text" autocomplete="organization">
            </div>
            <div>
              <label for="phone">Phone</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel">
            </div>
          </div>
          <div class="form-row">
            <div>
              <label for="service">I'm interested in</label>
              <select id="service" name="service">
                <option value="">Select a practice area</option>
{options}
                <option>Something else</option>
              </select>
            </div>
            <div>
              <label for="users">Company size</label>
              <select id="users" name="users">
                <option value="">Select</option>
                <option>1 – 50 employees</option>
                <option>51 – 200 employees</option>
                <option>201 – 1,000 employees</option>
                <option>1,001 – 5,000 employees</option>
                <option>5,000+ employees</option>
              </select>
            </div>
          </div>
          <div>
            <label for="message">How can we help? *</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <input class="hp" type="text" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div>
            <button class="btn btn-primary" type="submit">Send message</button>
          </div>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>

        <aside class="contact-info">
          <div class="card reveal" id="support" style="scroll-margin-top:100px;border-color:var(--brand)">
            <h3>Existing clients — get support</h3>
            <p>Email <a href="mailto:{SUPPORT}">{SUPPORT}</a> or call the support line in your service agreement. Critical issues are handled 24/7.</p>
          </div>
          <div class="card reveal">
            <h3>Email</h3>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </div>
          <div class="card reveal">
            <h3>Phone</h3>
            <p><a href="tel:{TEL}">{PHONE}</a></p>
          </div>
          <div class="card reveal">
            <h3>Headquarters</h3>
            <p>123 Business Street<br>Suite 100<br>Your City, Country</p>
          </div>
        </aside>
      </div>
    </section>
"""

write("contact.html", "Contact — TechSphire",
      "Contact TechSphire to book a free consultation on enterprise applications, data & AI, cloud, cyber security or managed services.",
      contact)

# --------------------------------------------------------------------------- privacy & 404
privacy = page_hero("Privacy Policy", "Legal", "Privacy policy",
                    "This is a starter template. Please have it reviewed so it matches your actual practices and local laws.") + f"""
    <section class="section">
      <div class="container" style="max-width:780px">
        <h2>Information we collect</h2>
        <p>When you contact us through this website, we collect the information you provide, such as your name, email address, phone number, company and the contents of your message.</p>
        <h2>How we use it</h2>
        <p>We use this information only to respond to your enquiry, provide our services and, where you have agreed, send you relevant updates. We do not sell your personal information.</p>
        <h2>Cookies &amp; analytics</h2>
        <p>This website does not set tracking cookies by default. If analytics tools are added, this section should describe them and how to opt out.</p>
        <h2>Data retention &amp; security</h2>
        <p>We keep personal information only as long as needed for the purposes above and protect it using appropriate technical and organisational measures.</p>
        <h2>Your rights</h2>
        <p>You may request access to, correction of or deletion of your personal information at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        <p style="color:var(--muted)">Last updated: <span data-year>2026</span></p>
      </div>
    </section>
"""
write("privacy.html", "Privacy policy — TechSphire", "How TechSphire collects, uses and protects your personal information.", privacy)

notfound = f"""    <section class="section not-found">
      {SHAPES}
      <div class="container">
        <div class="code">404</div>
        <h1 style="font-size:2rem">This page drifted out of orbit</h1>
        <p>The page you're looking for doesn't exist or has moved.</p>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-primary" href="index.html">Back to home</a>
          <a class="btn btn-soft" href="contact.html">Contact us</a>
        </div>
      </div>
    </section>
"""
write("404.html", "Page not found — TechSphire", "The page you were looking for could not be found.", notfound)
print("built", TOTAL_SERVICES, "services")
