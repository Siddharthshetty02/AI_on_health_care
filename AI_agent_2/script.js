document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded!");

    // Handle Symptom Checker Form Submission
    document.getElementById("symptom-form").addEventListener("submit", function (event) {
        event.preventDefault();

        let symptoms = [];
        document.querySelectorAll('input[name="symptom"]:checked').forEach((checkbox) => {
            symptoms.push(parseInt(checkbox.value));
        });

        // Send symptoms data to Flask API
        fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symptoms: symptoms })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("prediction-result").innerText = "Predicted Disease: " + data["Predicted Disease"];
        })
        .catch(error => console.error("Error:", error));
    });

    // Chatbot Functionality
    document.getElementById("send-btn").addEventListener("click", function () {
        sendMessage();
    });

    document.getElementById("user-input").addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        let userMessage = document.getElementById("user-input").value.trim();
        if (userMessage === "") return;

        let chatbox = document.getElementById("chatbox");
        chatbox.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            chatbox.innerHTML += `<p><strong>AI:</strong> ${data["response"]}</p>`;
            document.getElementById("user-input").value = "";
            chatbox.scrollTop = chatbox.scrollHeight; // Auto-scroll to latest message
        })
        .catch(error => console.error("Error:", error));
    }
});
