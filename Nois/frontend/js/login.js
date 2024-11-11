// Affiche la modale de connexion
document.getElementById("login_button").addEventListener("click", function (event) {
  event.preventDefault();
  document.getElementById("loginModal").style.display = "flex";
});

// Ferme la modale de connexion
document.querySelector(".close").addEventListener("click", function () {
  document.getElementById("loginModal").style.display = "none";
});

// Ferme la modale si l'utilisateur clique en dehors de celle-ci
window.onclick = function (event) {
  if (event.target === document.getElementById("loginModal")) {
    document.getElementById("loginModal").style.display = "none";
  }
};

// Gère demande de token
document.getElementById("login-button").addEventListener("click", function () {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Veuillez remplir tous les champs.");
    return;
  }

  const userData = { email: email, password: password };

  fetch("/api/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
    credentials: 'include'
  })
    .then(response => {
      if (!response.ok) throw new Error("Échec de la connexion");
      return response.json();
    })
    .then(() => {
      return checkAuthStatus();
    })
    .then(data => {
      const userType = data.userType;
      const redirectUrl = userType === "PROFESSIONAL" ? "/pro-dashboard.html" : "/user-dashboard.html";
      window.location.href = redirectUrl;
    })
    .catch((error) => {
      console.error("Erreur lors de la connexion:", error);
      alert("Connexion refusée. Veuillez vérifier vos informations.");
    });
});

// Fonction pour afficher ou masquer le mot de passe
function togglePassword() {
  const passwordField = document.getElementById('password');
  const toggleIcon = document.querySelector("i");

  if (passwordField.type === 'password') {
    passwordField.type = 'text';
    toggleIcon.classList.add("icon-eye-closed");
    toggleIcon.classList.remove("icon-eye-open");
  } else {
    passwordField.type = 'password';
    toggleIcon.classList.remove("icon-eye-closed");
    toggleIcon.classList.add("icon-eye-open");
  }
}

// Récuoère le status de user
function checkAuthStatus() {
  return fetch('/api/users/check-auth/', {
    method: 'GET',
    credentials: 'include'
  })
  .then(response => {
    if (response.ok) return response.json();
    throw new Error("Utilisateur non authentifié");
  })
  .catch(error => {
    console.error("Erreur de vérification d'authentification:", error);
    throw error;
  });
}
