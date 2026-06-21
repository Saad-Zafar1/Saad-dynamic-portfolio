"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const navigationMenu = document.querySelector(".navigation-menu");

    if (!menuToggle || !navigationMenu) {
        console.error("Mobile navigation elements were not found.");
        return;
    }

    menuToggle.addEventListener("click", () => {
        const menuIsOpen =
            navigationMenu.classList.toggle("is-open");

        menuToggle.classList.toggle("is-open", menuIsOpen);

        menuToggle.setAttribute(
            "aria-expanded",
            menuIsOpen.toString()
        );
    });

    navigationMenu.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navigationMenu.classList.remove("is-open");
            menuToggle.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        });
    });

    document.addEventListener("click", (event) => {
        const clickedInsideMenu =
            navigationMenu.contains(event.target);

        const clickedToggle =
            menuToggle.contains(event.target);

        if (!clickedInsideMenu && !clickedToggle) {
            navigationMenu.classList.remove("is-open");
            menuToggle.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        }
    });

    window.addEventListener("resize", () => {
        if (window.innerWidth > 760) {
            navigationMenu.classList.remove("is-open");
            menuToggle.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        }
    });
});