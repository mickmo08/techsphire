"""Insights articles for the TechSphire site.

Each article becomes insight-<slug>.html and appears on insights.html and the home page.
Add new articles to the top of the list; body is HTML.
"""

ARTICLES = [
    {
        "slug": "agentic-ai-enterprise-starting-point",
        "title": "Agentic AI in the enterprise: a practical starting point",
        "category": "AI & Automation",
        "practice": "ai",
        "date": "2026-10-08",
        "read": "6 min read",
        "image": "hero-ai",
        "summary": "AI agents can now plan and complete multi-step work across business systems. Here is how to pick the right first use cases and put the guardrails in place before you scale.",
        "body": """
<p>Generative AI assistants answer questions. AI agents go a step further: given a goal, they plan the steps, call the systems and tools they have been granted, check the results and hand back finished work. That shift — from producing text to taking action — is why agentic AI is moving quickly from experiments to operating budgets.</p>
<p>It is also why the first deployments deserve more care than a chatbot pilot. An agent that can update records, raise purchase orders or close tickets needs clear boundaries. The organisations getting value fastest are the ones that treat agents like a new kind of team member: scoped responsibilities, the right access, supervision and measurable outcomes.</p>

<h2>Choose work that is frequent, rules-heavy and well documented</h2>
<p>Good first candidates share a few traits. The process runs many times a week, follows documented rules with a manageable number of exceptions, and spans systems people currently copy information between. Typical examples include:</p>
<ul>
  <li><strong>Service desk triage</strong> — classifying requests, gathering missing details and resolving routine issues such as access requests.</li>
  <li><strong>Invoice and order exceptions</strong> — investigating mismatches between purchase orders, receipts and invoices, and preparing the resolution for approval.</li>
  <li><strong>Customer onboarding</strong> — collecting documents, validating data across systems and keeping the customer informed.</li>
  <li><strong>IT operations</strong> — correlating alerts, running standard diagnostics and drafting incident summaries.</li>
</ul>
<p>Avoid starting with processes that rely on tacit knowledge nobody has written down, or where a single error is costly and hard to reverse.</p>

<h2>Design the guardrails before the agent</h2>
<p>Most of the effort in a successful agent project goes into the environment around the model, not the model itself:</p>
<ul>
  <li><strong>Least-privilege access.</strong> Give the agent its own identity with only the permissions its tasks require, and log every action it takes.</li>
  <li><strong>Human approval points.</strong> Start with the agent preparing actions for a person to approve, then remove approvals step by step as accuracy is proven.</li>
  <li><strong>Grounding in your data.</strong> Connect the agent to authoritative policies, knowledge articles and system records so it acts on facts rather than guesses.</li>
  <li><strong>Evaluation.</strong> Build a test set of real historical cases and measure the agent against it before go-live and after every change.</li>
</ul>

<h2>Measure outcomes, not activity</h2>
<p>Agree the business measures up front: cycle time, cost per transaction, first-time-right rate, customer or employee satisfaction. Track them for the human process before launch so you have a baseline. An agent that completes many tasks but shifts rework to another team has not created value.</p>

<h2>Plan for scale from the first use case</h2>
<p>Once the first agent is working, demand arrives quickly. A small set of shared foundations prevents every team from rebuilding the basics: an approved platform and model catalogue, reusable connectors to core systems, a common approach to identity and logging, and a lightweight governance process to review new use cases for risk.</p>

<h2>Where to begin</h2>
<p>A focused readiness assessment — reviewing candidate processes, data quality, integration points and governance — typically identifies two or three use cases with a clear business case within a few weeks. From there, a time-boxed pilot with production-grade guardrails is the fastest way to prove value safely.</p>
""",
    },
    {
        "slug": "sap-s4hana-migration-decisions",
        "title": "Planning an SAP S/4HANA migration: seven decisions to make early",
        "category": "Enterprise Applications",
        "practice": "erp",
        "date": "2026-09-16",
        "read": "7 min read",
        "image": "px-erp",
        "summary": "With mainstream maintenance for SAP ECC ending in 2027, migration planning can't wait. These are the decisions that shape cost, risk and timeline more than any others.",
        "body": """
<p>SAP has committed to mainstream maintenance for SAP ECC 6.0 until the end of 2027, with optional extended maintenance available at additional cost until 2030. For most organisations that makes an S/4HANA programme a question of <em>when and how</em>, not <em>whether</em>. The programmes that run smoothly make a handful of big decisions early and deliberately.</p>

<h2>1. Your transition approach</h2>
<p>A <strong>system conversion</strong> (often called brownfield) converts your existing system, keeping history and custom code. A <strong>new implementation</strong> (greenfield) starts clean on standard processes. A <strong>selective data transition</strong> combines elements of both. The right choice depends on how well your current processes serve the business, how much custom code you carry and how much history you need online.</p>

<h2>2. Deployment model</h2>
<p>Decide between public cloud, private cloud and on-premises deployment early, because it shapes the degree of customisation possible, your upgrade cadence and your operating model. Many organisations now evaluate this alongside SAP's subscription offerings, which bundle software, infrastructure and services.</p>

<h2>3. How much to standardise</h2>
<p>A migration is the best opportunity in a decade to retire customisations that no longer differentiate the business. Establish a "clean core" principle — keep extensions outside the core system where possible — and give process owners the authority to adopt standard processes.</p>

<h2>4. Custom code</h2>
<p>Run a custom code analysis early. It is common to find that a large share of custom objects are no longer used. Retiring them reduces testing effort and risk; the remainder needs remediation or redesign as side-by-side extensions.</p>

<h2>5. Data</h2>
<p>Data quality issues are among the most frequent causes of delay. Decide how much history to migrate, who owns each data domain and how cleansing will happen before migration — not during cutover. Archiving old data can shorten conversion downtime considerably.</p>

<h2>6. Integration and the wider landscape</h2>
<p>Map every interface to and from your current ERP. The migration is a chance to modernise point-to-point integrations onto an integration platform and to decide which satellite systems should be retired, upgraded or replaced.</p>

<h2>7. Programme governance and change</h2>
<p>Successful programmes treat S/4HANA as a business change, not an IT upgrade. That means executive sponsorship, empowered process owners, a realistic testing strategy with automation, and a training and adoption plan that starts months before go-live.</p>

<h2>Next steps</h2>
<p>A structured readiness assessment — covering system analysis, custom code, data, integrations and business priorities — gives you a fact-based recommendation on approach, a high-level roadmap and a budget range. It is the single most effective way to de-risk the programme before major spend begins.</p>
""",
    },
    {
        "slug": "soc-in-house-outsourced-hybrid",
        "title": "Building security operations: in-house, outsourced or hybrid SOC?",
        "category": "Cyber Security",
        "practice": "security",
        "date": "2026-08-27",
        "read": "5 min read",
        "image": "px-security",
        "summary": "Round-the-clock threat detection and response is now a baseline expectation. We compare the three operating models and the questions that should drive your choice.",
        "body": """
<p>Attackers do not keep office hours, and many intrusions are only detected long after the initial compromise. Regulators, insurers and enterprise customers increasingly expect organisations to show they can detect and respond to threats at any time of day. A Security Operations Center (SOC) — the people, processes and technology that monitor and respond to threats — is how that capability is delivered.</p>
<p>The question most leadership teams face is not whether they need SOC capability, but how to source it.</p>

<h2>In-house SOC</h2>
<p>Building your own SOC gives you maximum control and deep familiarity with your environment. It suits large organisations with complex, sensitive environments and the budget to sustain it. The challenges are significant: staffing a 24/7 rota requires multiple analysts per shift, experienced security talent is scarce, and the technology stack — SIEM, endpoint detection, threat intelligence, automation — needs continuous tuning.</p>

<h2>Outsourced SOC (managed detection and response)</h2>
<p>A managed provider monitors your environment around the clock, investigates alerts and responds or escalates according to agreed playbooks. You gain immediate 24/7 coverage, mature processes and access to specialists at a predictable cost. The trade-offs are less direct control and the need for a strong onboarding process so the provider understands your critical assets and business context.</p>

<h2>Hybrid SOC</h2>
<p>Many organisations combine the two: an internal team owns security strategy, high-impact decisions and knowledge of the business, while a partner provides out-of-hours monitoring, surge capacity and specialist skills such as threat hunting and forensics. Done well, a hybrid model offers the best balance of control, coverage and cost.</p>

<h2>Questions to guide your decision</h2>
<ul>
  <li>What are your regulatory, contractual and insurance obligations for monitoring and incident response?</li>
  <li>Can you realistically recruit and retain enough analysts to cover nights, weekends and holidays?</li>
  <li>Which assets and data would cause the most harm if compromised — and how well are they monitored today?</li>
  <li>Do you have documented incident response plans, and have they been tested recently?</li>
  <li>How mature are your identity, endpoint and logging foundations? A SOC can only act on the telemetry it receives.</li>
</ul>

<h2>Whatever the model, start with the foundations</h2>
<p>Strong identity security (multi-factor authentication everywhere, privileged access management), consistent endpoint protection and centralised logging make any SOC far more effective. A short security assessment will show where these foundations stand and which SOC model fits your risk profile and budget.</p>
""",
    },
]
