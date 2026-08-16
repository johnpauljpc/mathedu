// MathEdu shared front-end behaviour.

// Dynamic copyright year.
const yearEl = document.getElementById("year");
if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
}

// Auto-hide alert messages after a few seconds.
const alerts = document.querySelectorAll(".messages .alert");
alerts.forEach((alert) => {
    setTimeout(() => {
        alert.style.transition = "opacity .4s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 400);
    }, 8000);
});

// Clear red error outlines as the user starts typing again.
document.querySelectorAll(".error-outline").forEach((el) => {
    el.addEventListener("input", () => el.classList.remove("error-outline"), { once: true });
});