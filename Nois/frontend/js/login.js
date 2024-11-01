
document.querySelector(".login-link").addEventListener("click", function(event) {
  event.preventDefault();
  document.getElementById("loginModal").style.display = "flex";
});

document.querySelector(".close").addEventListener("click", function() {
  document.getElementById("loginModal").style.display = "none"; // Masque le modal
});

// Fermer le modal lorsque l'utilisateur clique en dehors de la boîte
window.onclick = function(event) {
  if (event.target === document.getElementById("loginModal")) {
      document.getElementById("loginModal").style.display = "none";
  }
};


document.getElementById("login-button").addEventListener("click", function() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Veuillez remplir tous les champs.");
    return;
  }

  const userData = {
      email: email,
      password: password
  };

  fetch("/api/token/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(userData),
    credentials: 'include'
  })
  .then(response => {
      if (!response.ok) {
          throw new Error("Network response was not ok");
      }
      return response.json();
  })
  .then(data => {
      console.log("Success:", data);
      window.location.href = "/html/";
  })
  .catch((error) => {
      console.error("Error:", error);
      alert("Connexion refusée. Veuillez vérifier vos informations.");
  });
});
