function askQuestion() {
    const input = document.getElementById("chat-input").value.toLowerCase().trim();
    const chatWindow = document.getElementById("chat-window");

    const responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm your hackathon assistant chatbot!",
        
        "when is the hackathon": "The hackathon is on *March 18, 2025*.",
        "where is the hackathon happening": "It will take place at *Takshashila University, Ongur, in the Multipurpose Hall*.",
        "how much is the fee": "The fee is *₹300 per team member*.",
        "how many members can be in a team": "A team can have *2 to 5 members*.",
        "can i participate alone": "No, you need at least one teammate.",
        "will food be provided": "Yes, *lunch and refreshments* will be available.",
        "what are the judging criteria": "Projects will be judged on *innovation, feasibility, technical execution, and presentation*.",

        "who can participate": "Any student of *Takshashila University* can participate. External participants may be allowed.",
        "how can i register": "Register through the *university portal* or contact the event coordinators.",
        "what time does the event start": "The event starts at *9:00 AM* and ends at *6:00 PM*."
    };

    let response = responses[input] || "Sorry, I don't have an answer for that. Try asking something else.";

    chatWindow.innerHTML += `<p><strong>You:</strong> ${input}</p>`;
    chatWindow.innerHTML += `<p><strong>Bot:</strong> ${response}</p>`;

    document.getElementById("chat-input").value = ""; // Clear input field
}

// Allows pressing Enter to send messages
function handleKeyPress(event) {
    if (event.key === "Enter") {
        askQuestion();
    }
}
