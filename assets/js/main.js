// TechSphire — site behaviour (mobile nav, scroll reveal, contact form, footer year)
(function () {
  document.documentElement.classList.remove("no-js");

  // Mobile navigation
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    links.addEventListener("click", (e) => {
      if (e.target.closest("a")) {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Header shadow once the page is scrolled
  const header = document.querySelector(".site-header");
  if (header) {
    const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Reveal elements as they scroll into view
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("visible"));
  }

  // Current year in footer
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  // Contact form
  // Set data-endpoint on the <form> to a form service URL (e.g. Formspree) to
  // submit via fetch. Without one, the form falls back to opening the user's
  // email client with the message pre-filled.
  const form = document.querySelector("#contact-form");
  if (form) {
    const status = form.querySelector(".form-status");
    const setStatus = (msg, ok) => {
      status.textContent = msg;
      status.className = "form-status " + (ok ? "ok" : "err");
    };

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      const data = new FormData(form);
      if (data.get("company_website")) return; // honeypot: likely a bot

      const endpoint = form.dataset.endpoint;
      const button = form.querySelector("button[type=submit]");

      if (!endpoint) {
        const to = form.dataset.email;
        const subject = encodeURIComponent(
          `Website enquiry: ${data.get("service") || "General"} — ${data.get("name")}`
        );
        const body = encodeURIComponent(
          `Name: ${data.get("name")}\nEmail: ${data.get("email")}\nCompany: ${data.get("company") || "-"}\n` +
            `Service: ${data.get("service") || "-"}\nUsers: ${data.get("users") || "-"}\n\n${data.get("message")}`
        );
        window.location.href = `mailto:${to}?subject=${subject}&body=${body}`;
        setStatus("Opening your email app to send the message…", true);
        return;
      }

      button.disabled = true;
      try {
        const res = await fetch(endpoint, {
          method: "POST",
          body: data,
          headers: { Accept: "application/json" },
        });
        if (!res.ok) throw new Error(res.statusText);
        form.reset();
        setStatus("Thanks! Your message has been sent. We'll be in touch within one business day.", true);
      } catch (err) {
        setStatus("Sorry, something went wrong. Please email us directly instead.", false);
      } finally {
        button.disabled = false;
      }
    });
  }
})();
