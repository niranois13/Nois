document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  const resultsContainer = document.getElementById('results-container');

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
    console.log(data);
    resultsContainer.innerHTML = '';

      if (data.professionals && data.professionals.results && data.professionals.results.length > 0) {

          const professionalsList = document.createElement('ul');
          data.professionals.results.forEach(professional => {
            const first_name = professional.first_name;
            const last_name = professional.last_name;
            const slug = professional.slug;
            let profession;

            if (!professional.profession) {
              if (professional.custom_profession) {
                profession = professional.custom_profession;
              }
            } else {
              profession = professional.profession;
            };

              const li = document.createElement('li');
              li.innerHTML = `
                  <a href="/professionals/${slug}/" class="profile-link">
                      ${first_name} ${last_name} - ${profession}
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

  searchButton.addEventListener('click', performSearch);
  searchInput.addEventListener('keypress', (event) => {
      if (event.key === 'Enter') {
          performSearch();
      }
  });
});
