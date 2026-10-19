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
        closeDrops();
      }
    });
  }

  // Mega menu and dropdowns: click to toggle, close on outside click or Escape
  const drops = document.querySelectorAll(".has-drop");
  function closeDrops(except) {
    drops.forEach((d) => {
      if (d === except) return;
      d.classList.remove("open");
      d.querySelector(".nav-trigger").setAttribute("aria-expanded", "false");
    });
  }
  drops.forEach((d) => {
    const btn = d.querySelector(".nav-trigger");
    btn.addEventListener("click", () => {
      const open = !d.classList.contains("open");
      closeDrops(d);
      d.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".has-drop")) closeDrops();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeDrops();
  });

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

  // Highlight the service catalog section in view
  const catLinks = document.querySelectorAll(".catalog-nav a");
  if (catLinks.length && "IntersectionObserver" in window) {
    const spy = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          catLinks.forEach((a) => a.classList.toggle("active", a.hash === "#" + entry.target.id));
        });
      },
      { rootMargin: "-30% 0px -60% 0px" }
    );
    document.querySelectorAll(".practice-section").forEach((s) => spy.observe(s));
  }

  // Animated dot globe in the home page hero
  const canvas = document.getElementById("globe");
  if (canvas && canvas.getContext) {
    const ctx = canvas.getContext("2d");
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const N = 900;
    const pts = [];
    const golden = Math.PI * (3 - Math.sqrt(5));
    for (let i = 0; i < N; i++) {
      const y = 1 - (i / (N - 1)) * 2;
      const r = Math.sqrt(1 - y * y);
      const t = golden * i;
      pts.push([Math.cos(t) * r, y, Math.sin(t) * r]);
    }
    const tilt = 0.38;
    const ct = Math.cos(tilt);
    const st = Math.sin(tilt);
    let w = 0;
    let rot = 0;
    let running = true;

    const resize = () => {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      w = canvas.clientWidth;
      canvas.width = w * dpr;
      canvas.height = w * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };

    const draw = () => {
      ctx.clearRect(0, 0, w, w);
      const R = w * 0.38;
      const c = w / 2;
      const cr = Math.cos(rot);
      const sr = Math.sin(rot);
      const s = w / 520;

      // orbit ring behind and in front of the globe
      ctx.save();
      ctx.translate(c, c);
      ctx.rotate(-0.42);
      ctx.strokeStyle = "rgba(165,180,252,0.28)";
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.ellipse(0, 0, R * 1.24, R * 0.36, 0, 0, Math.PI * 2);
      ctx.stroke();
      const a = rot * 1.6;
      ctx.fillStyle = "#67e8f9";
      ctx.shadowColor = "#67e8f9";
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(Math.cos(a) * R * 1.24, Math.sin(a) * R * 0.36, 5 * s, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      for (const [px, py, pz] of pts) {
        const x = px * cr - pz * sr;
        const z0 = px * sr + pz * cr;
        const y = py * ct - z0 * st;
        const z = py * st + z0 * ct;
        const depth = (z + 1) / 2;
        const k = (x + 1) / 2;
        const rr = Math.round(129 - 115 * k);
        const gg = Math.round(140 + 25 * k);
        const bb = Math.round(248 - 15 * k);
        ctx.fillStyle = `rgba(${rr},${gg},${bb},${0.12 + depth * 0.88})`;
        ctx.beginPath();
        ctx.arc(c + x * R, c + y * R, (0.7 + depth * 1.9) * s * 1.6, 0, Math.PI * 2);
        ctx.fill();
      }
    };

    const loop = () => {
      if (!running) return;
      rot += 0.0035;
      draw();
      requestAnimationFrame(loop);
    };

    resize();
    draw();
    window.addEventListener("resize", () => { resize(); draw(); });
    if (!reduce) {
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(([entry]) => {
          const was = running;
          running = entry.isIntersecting;
          if (running && !was) loop();
        }).observe(canvas);
      }
      loop();
    }
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
