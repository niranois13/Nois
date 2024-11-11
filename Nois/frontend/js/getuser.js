// Valide authentificaion et retourne userType
function checkAuthStatus() {
  return fetch('/api/users/check-auth/', {
    method: 'GET',
    credentials: 'include',
    cache: 'no-cache'
  })
  .then(response => {
    console.log("Réponse checkAuth :", response);
    if (response.ok) return response.json();
    throw new Error('Utilisateur non authentifié');
  })
  .then(data => {
    updateNavigation(data.isAuthenticated, data.userType);
    console.log("Data reçues :", data);
    return data;
  })
  .catch(error => {
    console.error("Erreur de vérification d'authentification:", error);
    updateNavigation(false);
    throw error;
  });
}

// Slug handler
function getUserSlug() {
  return fetch('/api/users/get_my_slug/', {
    method: 'GET',
    credentials: 'include'
  })
  .then(response => {
    if (response.ok) return response.json();
    throw new Error('Erreur lors de la récupération du slug');
  })
  .then(data => data.slug)
  .catch(error => {
    console.error("Erreur lors de la récupération du slug:", error);
    throw error;
  });
}

// User info
function getUserInfo() {
  checkAuthStatus()
    .then(data => {
      if (data.isAuthenticated) {
        return getUserSlug().then(slug => ({ userType: data.userType, slug }));
      }
      throw new Error('Utilisateur non authentifié');
    })
    .then(({ userType, slug }) => {
      const endpoint = userType === 'PROFESSIONAL' ? `/api/professionals/${slug}/` : `/api/clients/${slug}/`;
      return fetch(endpoint, { method: 'GET', credentials: 'include' });
    })
    .then(response => {
      console.log("Réponse reçue fetch professionals :", response);
      if (response.ok) return response.json();
      throw new Error("Erreur lors de la récupération des informations de l'utilisateur");
    })
    .then(data => {
      console.log("Données utilisateur reçues:", data);
      document.getElementById('first_name').textContent = data.first_name;
      document.getElementById('last_name').textContent = data.last_name;
      document.getElementById('email').textContent = data.email;
      if (data.phone_number) {
        document.getElementById('phone_number').textContent = data.phone_number;
      } else {
        document.getElementById('phone_number').parentElement.style.display = 'none';
      }
      if (data.profession && data.profession != 'Autre') {
        document.getElementById('profession').textContent = data.profession;
      } else if (data.custom_profession) {
        document.getElementById('profession').textContent = data.custom_profession;
      }
      document.getElementById('display_user_name').textContent = `${data.first_name} ${data.last_name}`;
    })
    .catch(error => console.error("Erreur lors de la récupération des informations de l'utilisateur:", error));
}

// Navbar handler
function updateNavigation(isLoggedIn, userType) {
  const homeButton = document.getElementById('home_button');
  const loginButton = document.getElementById('login_button');
  const logoutButton = document.getElementById('logout_button');

  if (isLoggedIn) {
    homeButton.textContent = 'Mon profil';
    homeButton.href = userType === "PROFESSIONAL" ? '/pro-dashboard.html' : '/user-dashboard.html';
    loginButton.style.display = 'none';
    logoutButton.style.display = 'inline-block';
    logoutButton.onclick = logout;
  } else {
    homeButton.textContent = 'Accueil';
    homeButton.href = '/';
    loginButton.style.display = 'inline-block';
    logoutButton.style.display = 'none';
    loginButton.onclick = showLoginModal;
  }
}

// Logout
function logout() {
  fetch('/api/logout/', { method: 'POST', credentials: 'include' })
  .then(response => {
    if (response.ok) window.location.href = '/';
    else throw new Error("Erreur lors de la déconnexion");
  })
  .catch(error => console.error("Erreur de déconnexion:", error));
}

document.addEventListener('DOMContentLoaded', () => {
  const pathname = window.location.pathname;

  if (pathname === '/pro-dashboard.html' || pathname === '/user-dashboard.html') {
    getUserInfo();
  } else {
    checkAuthStatus();
  }
});
