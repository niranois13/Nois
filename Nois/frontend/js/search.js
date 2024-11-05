document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  const resultsContainer = document.getElementById('results-container');

  // Fonction pour effectuer la recherche
  async function performSearch() {
      const query = searchInput.value.trim();
      if (query.length === 0) {
          resultsContainer.innerHTML = '<p>Veuillez entrer un terme de recherche.</p>';
          return;
      }

      try {
          const response = await fetch(`/api/search/?q=${encodeURIComponent(query)}`);
          if (!response.ok) {
              throw new Error('Erreur lors de la récupération des résultats.');
          }
          const data = await response.json();
          displayResults(data);
      } catch (error) {
          console.error('Erreur:', error);
          resultsContainer.innerHTML = '<p>Une erreur est survenue lors de la recherche.</p>';
      }
  }

  // Fonction pour afficher les résultats
  function displayResults(data) {
      resultsContainer.innerHTML = ''; // Réinitialiser le conteneur des résultats

      if (data.professionals && data.professionals.length > 0) {
          const professionalsList = document.createElement('ul');
          data.professionals.forEach(professional => {
              const li = document.createElement('li');
              li.innerHTML = `
                  <a href="/professionnel/${professional.slug}/">
                      ${professional.first_name} ${professional.last_name}<br>
                      ${professional.profession ? professional.profession.name : 'Profession non renseignée'}
                  </a>
              `;
              professionalsList.appendChild(li);
          });
          resultsContainer.appendChild(professionalsList);
      } else {
          resultsContainer.innerHTML += '<p>Aucun professionnel trouvé.</p>';
      }

      if (data.services && data.services.length > 0) {
          const servicesList = document.createElement('ul');
          data.services.forEach(service => {
              const li = document.createElement('li');
              li.textContent = service.service_name;
              servicesList.appendChild(li);
          });
          resultsContainer.appendChild(servicesList);
      }

      if (data.professions && data.professions.length > 0) {
          const professionsList = document.createElement('ul');
          data.professions.forEach(profession => {
              const li = document.createElement('li');
              li.textContent = profession.name;
              professionsList.appendChild(li);
          });
          resultsContainer.appendChild(professionsList);
      }
  }

  // Écouter l'événement de clic sur le bouton de recherche
  searchButton.addEventListener('click', performSearch);

  // Optionnel : Écouter l'événement "Enter" dans le champ de recherche
  searchInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
          performSearch();
      }
  });
});
