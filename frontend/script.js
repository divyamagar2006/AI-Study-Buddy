async function askAI() {

    let question = document.getElementById("question").value;

    if (question.trim() === "") {
        alert("Please enter a question.");
        return;
    }

    document.getElementById("answer").innerHTML =
        "<p style='text-align:center;'>⏳ AI is thinking...</p>";

    let response = await fetch("https://ai-study-buddy-production-dfb2.up.railway.app/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    });

    let data = await response.json();

    document.getElementById("answer").innerHTML = data.answer;
}

function copyAnswer() {

    let answer = document.getElementById("answer").innerText;

    navigator.clipboard.writeText(answer);

    alert("✅ Answer copied successfully!");

}

function toggleTheme() {

    document.body.classList.toggle("dark-mode");

    let btn = document.getElementById("themeBtn");

    if (document.body.classList.contains("dark-mode")) {
        btn.innerHTML = "☀️ Light Mode";
    } else {
        btn.innerHTML = "🌙 Dark Mode";
    }

}