# TechSphire website

A fast, responsive, multi-page website for TechSphire, an IT services and IT consulting company, built with plain HTML, CSS and JavaScript — no build step or dependencies.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home — hero, services overview, why us, process, technologies, FAQ |
| `services.html` | Detailed service descriptions (linkable sections, e.g. `services.html#consulting`) |
| `about.html` | Story, mission, values and leadership team |
| `careers.html` | Benefits and open roles |
| `contact.html` | Contact form and company details |
| `privacy.html` | Starter privacy policy |
| `404.html` | Not-found page |

Shared assets live in `assets/` (`css/styles.css`, `js/main.js`, `img/logo.svg`).

## Preview locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Customise before going live

Search and replace these placeholders across all `.html` files:

- `hello@techsphire.com`, `support@techsphire.com`, `careers@techsphire.com` — your real email addresses
- `+1 (000) 000-0000` / `tel:+10000000000` — your phone number
- `123 Business Street…` in `contact.html` — your office address
- Social icons in the footer (`href="#"`) — links to your LinkedIn, X and Facebook pages
- Leadership names and roles in `about.html`
- Open roles in `careers.html`
- Privacy policy text in `privacy.html` (have it reviewed for your jurisdiction)

**Branding:** colours are defined as CSS variables at the top of `assets/css/styles.css` — change `--brand`, `--brand-hover` and `--brand-tint` to recolour every button, link and accent. Replace `assets/img/logo.svg` with your own logo.

**Header/footer:** these are repeated in each page, so update every `.html` file when you change navigation or footer links.

## Contact form

By default, submitting the form opens the visitor's email app with the message pre-filled, addressed to the `data-email` value on the form.

To receive submissions directly instead, create a free form endpoint (e.g. [Formspree](https://formspree.io)) and add it to the form in `contact.html`:

```html
<form ... id="contact-form" data-endpoint="https://formspree.io/f/your-id">
```

## Deploy

This is a static site and can be hosted anywhere:

- **GitHub Pages:** repository *Settings → Pages → Deploy from a branch*, choose the branch and `/ (root)`.
- **Netlify / Vercel / Cloudflare Pages:** import the repository; no build command, publish directory is the root.
