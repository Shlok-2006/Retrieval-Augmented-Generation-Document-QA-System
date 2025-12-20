async function ask() {
  const question = document.getElementById("q").value.trim();
  if (!question) return;

  document.getElementById("answerText").innerText = "Thinking...";
  document.getElementById("sourcesList").innerHTML = "";

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();

  document.getElementById("answerText").innerText = data.answer;

  data.sources.forEach(src => {
    const li = document.createElement("li");
    li.innerText = src;
    document.getElementById("sourcesList").appendChild(li);
  });
}
