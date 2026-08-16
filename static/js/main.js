// MathEdu shared front-end behaviour.

// --- Color theme -------------------------------------------------
const themeToggle = document.getElementById("theme-toggle");

function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try { localStorage.setItem("mathedu-theme", theme); } catch (e) {}
    if (themeToggle) {
        themeToggle.setAttribute("aria-pressed", theme === "light" ? "true" : "false");
        themeToggle.setAttribute(
            "aria-label",
            theme === "light" ? "Switch to dark theme" : "Switch to light theme"
        );
    }
}

if (themeToggle) {
    themeToggle.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
        setTheme(current);
    });
    setTheme(document.documentElement.getAttribute("data-theme") || "dark");
}

// --- Dynamic copyright year --------------------------------------
const yearEl = document.getElementById("year");
if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
}

// --- Auto-hide alert messages after a few seconds ----------------
const alerts = document.querySelectorAll(".messages .alert");
alerts.forEach((alert) => {
    setTimeout(() => {
        alert.style.transition = "opacity .4s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 400);
    }, 8000);
});

// --- Clear red error outlines as the user starts typing again ----
document.querySelectorAll(".error-outline").forEach((el) => {
    el.addEventListener("input", () => el.classList.remove("error-outline"), { once: true });
});