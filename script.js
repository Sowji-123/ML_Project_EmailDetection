document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const textarea = document.querySelector("textarea");
    const button = document.querySelector("button");

    // Handle form submission
    form.addEventListener("submit", (event) => {
        const message = textarea.value.trim();
        if (message === "") {
            event.preventDefault(); // Prevent form submission
            alert("Please enter a message before submitting.");
            textarea.focus();
        }
    });

    // Enhance textarea interaction
    textarea.addEventListener("input", () => {
        if (textarea.value.length > 0) {
            button.disabled = false;
            button.style.background = "#2575fc";
        } else {
            button.disabled = true;
            button.style.background = "#ccc";
        }
    });

    // Initialize button state
    button.disabled = true;
    button.style.background = "#ccc";
});
