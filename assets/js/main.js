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
    const mobileCta = document.querySelector(".mobile-cta");
    const onScroll = () => {
      header.classList.toggle("scrolled", window.scrollY > 8);
      if (mobileCta) mobileCta.classList.toggle("show", window.scrollY > window.innerHeight * 0.7);
    };
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

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Animated dot globe: rotating points, travelling data arcs, drag to spin
  const canvas = document.getElementById("globe");
  if (canvas && canvas.getContext) {
    const ctx = canvas.getContext("2d");
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
    let velocity = 0.0035;
    let dragging = false;
    let lastX = 0;
    let running = true;
    const arcs = [];

    const project = ([px, py, pz], cr, sr) => {
      const x = px * cr - pz * sr;
      const z0 = px * sr + pz * cr;
      return [x, py * ct - z0 * st, py * st + z0 * ct];
    };
    const slerp = (a, b, t) => {
      const dot = Math.min(1, Math.max(-1, a[0] * b[0] + a[1] * b[1] + a[2] * b[2]));
      const om = Math.acos(dot);
      if (om < 1e-4) return a;
      const s1 = Math.sin((1 - t) * om) / Math.sin(om);
      const s2 = Math.sin(t * om) / Math.sin(om);
      return [a[0] * s1 + b[0] * s2, a[1] * s1 + b[1] * s2, a[2] * s1 + b[2] * s2];
    };
    const newArc = () => {
      const a = pts[(Math.random() * N) | 0];
      let b = pts[(Math.random() * N) | 0];
      for (let k = 0; k < 10 && a[0] * b[0] + a[1] * b[1] + a[2] * b[2] > 0.6; k++) b = pts[(Math.random() * N) | 0];
      return { a, b, t: 0, speed: 0.006 + Math.random() * 0.006 };
    };
    for (let i = 0; i < 7; i++) { const arc = newArc(); arc.t = Math.random(); arcs.push(arc); }

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

      ctx.save();
      ctx.translate(c, c);
      ctx.rotate(-0.42);
      ctx.strokeStyle = "rgba(147,197,253,0.28)";
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

      for (const p of pts) {
        const [x, y, z] = project(p, cr, sr);
        const depth = (z + 1) / 2;
        const k = (x + 1) / 2;
        ctx.fillStyle = `rgba(${Math.round(59 - 45 * k)},${Math.round(130 + 35 * k)},${Math.round(246 - 13 * k)},${0.12 + depth * 0.88})`;
        ctx.beginPath();
        ctx.arc(c + x * R, c + y * R, (0.7 + depth * 1.9) * s * 1.6, 0, Math.PI * 2);
        ctx.fill();
      }

      // data arcs lifted above the surface, drawn with a fading tail
      for (const arc of arcs) {
        const steps = 28;
        const head = Math.min(arc.t, 1);
        const tail = Math.max(0, head - 0.45);
        ctx.lineWidth = 1.6 * s;
        let prev = null;
        for (let i = 0; i <= steps; i++) {
          const t = tail + ((head - tail) * i) / steps;
          const lift = 1 + Math.sin(Math.PI * t) * 0.22;
          const q = slerp(arc.a, arc.b, t);
          const [x, y, z] = project([q[0] * lift, q[1] * lift, q[2] * lift], cr, sr);
          const pt = [c + x * R, c + y * R, z];
          if (prev) {
            const alpha = (i / steps) * (pt[2] > -0.15 ? 0.95 : 0.15);
            ctx.strokeStyle = `rgba(103,232,249,${alpha})`;
            ctx.beginPath();
            ctx.moveTo(prev[0], prev[1]);
            ctx.lineTo(pt[0], pt[1]);
            ctx.stroke();
          }
          prev = pt;
        }
        if (prev && head < 1 && prev[2] > -0.15) {
          ctx.fillStyle = "#fff";
          ctx.beginPath();
          ctx.arc(prev[0], prev[1], 2.2 * s, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    };

    const step = () => {
      if (!dragging) {
        velocity += (0.0035 - velocity) * 0.02;
        rot += velocity;
      }
      for (let i = 0; i < arcs.length; i++) {
        arcs[i].t += arcs[i].speed;
        if (arcs[i].t > 1.45) arcs[i] = newArc();
      }
    };

    const loop = () => {
      if (!running) return;
      step();
      draw();
      requestAnimationFrame(loop);
    };

    canvas.addEventListener("pointerdown", (e) => {
      dragging = true;
      lastX = e.clientX;
      canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener("pointermove", (e) => {
      if (!dragging) return;
      const dx = e.clientX - lastX;
      lastX = e.clientX;
      velocity = dx * 0.006;
      rot += velocity;
      if (reduceMotion) draw();
    });
    const endDrag = () => { dragging = false; };
    canvas.addEventListener("pointerup", endDrag);
    canvas.addEventListener("pointercancel", endDrag);

    resize();
    draw();
    window.addEventListener("resize", () => { resize(); draw(); });
    if (!reduceMotion) {
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

  // Hero slider: tabs with progress bars; the bar's animation end advances the slide
  const slider = document.querySelector("[data-slider]");
  if (slider) {
    const slides = slider.querySelectorAll(".slide");
    const tabs = slider.querySelectorAll(".slider-tab");
    const go = (i) => {
      slides.forEach((s, k) => s.classList.toggle("is-active", k === i));
      tabs.forEach((t, k) => {
        t.classList.toggle("is-active", k === i);
        t.setAttribute("aria-selected", String(k === i));
      });
      slider.classList.toggle("show-globe", i === 0);
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => go(i));
      t.querySelector("i").addEventListener("animationend", () => go((i + 1) % tabs.length));
    });
  }

  // Tab components (service explorer, industry selector)
  document.querySelectorAll("[data-tabs]").forEach((root) => {
    const tabs = root.querySelectorAll("[data-tab]");
    const panels = root.querySelectorAll("[data-panel]");
    const show = (id) => {
      tabs.forEach((t) => {
        const on = t.dataset.tab === id;
        t.classList.toggle("is-active", on);
        t.setAttribute("aria-selected", String(on));
      });
      panels.forEach((p) => p.classList.toggle("is-active", p.dataset.panel === id));
    };
    tabs.forEach((t) => {
      t.addEventListener("click", () => show(t.dataset.tab));
      if (root.hasAttribute("data-hover") && window.matchMedia("(hover: hover) and (min-width: 961px)").matches) {
        t.addEventListener("mouseenter", () => show(t.dataset.tab));
      }
    });
  });

  // Scroll story: the step in view drives the sticky visual
  const story = document.querySelector(".story");
  if (story && "IntersectionObserver" in window) {
    const steps = story.querySelectorAll(".story-step");
    const items = story.querySelectorAll(".sv-item");
    const so = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const i = [...steps].indexOf(entry.target);
          steps.forEach((s, k) => s.classList.toggle("is-active", k === i));
          items.forEach((s, k) => s.classList.toggle("is-active", k === i));
        });
      },
      { rootMargin: "-45% 0px -45% 0px" }
    );
    steps.forEach((s) => so.observe(s));
  }

  // Count-up numbers
  const counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window && !reduceMotion) {
    const co = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        co.unobserve(entry.target);
        const el = entry.target;
        const end = Number(el.dataset.count);
        const suffix = el.dataset.suffix || "";
        const start = performance.now();
        const tick = (now) => {
          const p = Math.min(1, (now - start) / 1400);
          el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    counters.forEach((el) => co.observe(el));
  }

  // Newsletter: opens the visitor's email app unless data-endpoint is set
  const nl = document.querySelector("#newsletter");
  if (nl) {
    const status = nl.querySelector(".nl-status");
    nl.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!nl.checkValidity()) { nl.reportValidity(); return; }
      const email = nl.querySelector("input[type=email]").value;
      if (!nl.dataset.endpoint) {
        window.location.href = `mailto:${nl.dataset.email}?subject=${encodeURIComponent("Newsletter subscription")}&body=${encodeURIComponent("Please subscribe " + email + " to TechSphire insights.")}`;
        status.textContent = "Opening your email app to confirm…";
        return;
      }
      try {
        const res = await fetch(nl.dataset.endpoint, { method: "POST", body: new FormData(nl), headers: { Accept: "application/json" } });
        if (!res.ok) throw new Error(res.statusText);
        nl.reset();
        status.textContent = "Thanks for subscribing!";
      } catch (err) {
        status.textContent = "Sorry, something went wrong. Please try again.";
      }
    });
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
