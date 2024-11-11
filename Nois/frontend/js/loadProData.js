// Fonction pour charger les informations du professionnel depuis localStorage
function loadProfessionalData() {
  const professionalData = JSON.parse(localStorage.getItem('proInfo'));

  if (professionalData) {
    if (document.getElementById('display_pro_name')) {
    }
    if (document.getElementById('first_name')) {
      document.getElementById('first_name').textContent = professionalData.first_name;
    }
    if (document.getElementById('last_name')) {
      document.getElementById('last_name').textContent = professionalData.last_name;
    }
    if (professionalData.profession && professionalData.profession != 'Autre') {
      document.getElementById('profession').textContent = professionalData.profession;
    } else if (professionalData.custom_profession) {
      document.getElementById('profession').textContent = professionalData.custom_profession;
    }
    if (document.getElementById('email')) {
      document.getElementById('email').textContent = professionalData.email;
    }
    if (document.getElementById('phone_number')) {
      document.getElementById('phone_number').textContent = professionalData.phone_number;
    }
  } else {
    console.error('Données du professionnel non trouvées dans localStorage.');
  }
}

window.addEventListener('load', loadProfessionalData);
