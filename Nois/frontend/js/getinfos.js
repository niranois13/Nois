// Pro finder
function getProInfo(slug) {
  const url = `/api/professionals/${slug}`;
  console.log("Envoi de la requête à l'URL:", url);

  return fetch(url, {
    method: 'GET',
    credentials: 'include'
  })
  .then(response => {
    console.log("Réponse reçue:", response);
    if (response.ok) {
      return response.json();
    }
    throw new Error("Erreur lors de la récupération des informations de l'utilisateur");
  })
  .then(data => {
    console.log("Données récupérées:", data);
    localStorage.setItem('proInfo', JSON.stringify(data));
  })
  .catch(error => {
    console.error("Erreur lors de la récupération des informations de l'utilisateur:", error);
  });
}


// Fonction pour gérer la redirection et le call de getInfoPros:
document.addEventListener("DOMContentLoaded", () => {
  const resultsContainer = document.getElementById('results-container');

  resultsContainer.addEventListener("click", function(event) {
    const profileLink = event.target.closest(".profile-link");

    console.log("Élément de lien trouvé :", profileLink);

    if (profileLink) {
      event.preventDefault();
      const href = profileLink.getAttribute('href');
      console.log("href trouvé :", href);

      const slugMatch = href.match(/\/(\d{5})\/$/);
      const slug = slugMatch ? slugMatch[1] : null;
      console.log("Slug trouvé :", slug);

      getProInfo(slug).then(() => {
        window.location.href = `/professionel.html`;
      });
    }
  });
});
