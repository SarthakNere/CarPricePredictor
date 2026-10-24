const form = document.getElementById("estimate-form");
const companySelect = document.getElementById("company");
const modelSelect = document.getElementById("car_model");
const errorMessage = document.getElementById("form-error");
const resultCard = document.getElementById("result-card");
const resultValue = document.getElementById("result-value");

companySelect.addEventListener("change", () => {
    modelSelect.replaceChildren(new Option("Choose a model", ""));
    const models = window.companyModels[companySelect.value] || [];
    models.forEach((model) => modelSelect.add(new Option(model, model)));
    modelSelect.disabled = models.length === 0;
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    errorMessage.hidden = true;
    resultCard.hidden = true;
    const submitButton = form.querySelector("button[type='submit']");
    submitButton.disabled = true;
    submitButton.querySelector("span:first-child").textContent = "Calculating...";

    try {
        const response = await fetch("/predict", { method: "POST", body: new FormData(form) });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || "The estimate could not be calculated.");
        }
        resultValue.textContent = new Intl.NumberFormat("en-IN", {
            style: "currency",
            currency: "INR",
            maximumFractionDigits: 0
        }).format(data.prediction);
        resultCard.hidden = false;
        resultCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } catch (error) {
        errorMessage.textContent = error.message || "Could not connect to the server. Please try again.";
        errorMessage.hidden = false;
    } finally {
        submitButton.disabled = false;
        submitButton.querySelector("span:first-child").textContent = "Calculate my estimate";
    }
});
