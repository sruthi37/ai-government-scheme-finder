const form = document.getElementById("schemeForm");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const userData = {
        age: document.getElementById("age").value,
        income: document.getElementById("income").value
    };

    try {

        const response = await fetch("https://ai-government-scheme-finder.onrender.com/match", 
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(userData)
            }
        );

        const schemes = await response.json();

        resultsDiv.innerHTML = "<h2>Recommended Schemes</h2>";

        if (schemes.length === 0) {

            resultsDiv.innerHTML +=
                "<p>No matching schemes found.</p>";

            return;
        }

        schemes.forEach((scheme) => {

            resultsDiv.innerHTML += `
                <div class="scheme-card">
                    <h3>${scheme.name}</h3>
                    <p><strong>Category:</strong> ${scheme.category}</p>
                    <p>${scheme.benefit}</p>
                </div>
            `;
        });

    } catch (error) {

        console.error(error);

        resultsDiv.innerHTML =
            "<p>Backend connection failed.</p>";
    }
});
