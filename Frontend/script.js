const API_URL = "http://127.0.0.1:5000/internships";

async function fetchInternships() {
  const res = await fetch(API_URL);
  const data = await res.json();
  displayInternships(data);
}

function displayInternships(internships) {
  const container = document.getElementById("internshipList");
  const searchTerm = document.getElementById("searchBox").value.toLowerCase();
  container.innerHTML = "";

  internships
    .filter(i => i.company.toLowerCase().includes(searchTerm))
    .forEach(intern => {
      const div = document.createElement("div");
      div.className = "internship-card";
      div.innerHTML = `
        <h3>${intern.company}</h3>
        <p>${intern.role}</p>
        <span>Duration: ${intern.duration}</span><br>
        <span>Status: <strong>${intern.status}</strong></span>
        <div class="actions">
          <button onclick="toggleStatus(${intern.id}, '${intern.status}')">🔁</button>
          <button onclick="deleteInternship(${intern.id})">🗑️</button>
        </div>
      `;
      container.appendChild(div);
    });
}

document.getElementById("internshipForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    company: company.value,
    role: role.value,
    duration: duration.value,
    status: status.value
  };
  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  e.target.reset();
  fetchInternships();
});

async function deleteInternship(id) {
  await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  fetchInternships();
}

async function toggleStatus(id, currentStatus) {
  const newStatus = currentStatus === "Completed" ? "Ongoing" : "Completed";
  await fetch(`${API_URL}/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: newStatus })
  });
  fetchInternships();
}

document.getElementById("searchBox").addEventListener("input", fetchInternships);

fetchInternships();
