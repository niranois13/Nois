// Professional registration
const form = document.getElementById("ProRegisterForm");
const submitButton = document.getElementById("pro_register-button");

form.addEventListener('submit', function(event) {
  event.preventDefault();
  console.log("Formulaire soumis, preventDefault appelé");
  submitButton.disabled = true;

  const formData = new FormData(this);

  const requiredFields = ["email", "password1", "password2", "first_name", "last_name", "intervention_radius", "name"];
  for (let field of requiredFields) {
    if (!formData.get(field)) {
      alert(`Veuillez fournir ${field === "first_name" ? "un prénom" :
        field === "last_name" ? "un nom de famille" :
        field === "email" ? "un email" :
        field === "password1" ? "un mot de passe" :
        field === "password2" ? "la confirmation du mot de passe" :
        field === "intervention_radius" ? "un rayon d'intervention" :
        field === "name" ? "une profession" :
        field
      }.`);
      submitButton.disabled = false;
      return;
    }
  }

  let dataToSend = {};

  for (let [key, value] of formData.entries()) {
    if (key !== 'address' && key !== "password1" && key !== "password2") {
      if (key === "phone_number") {
      value = formatPhoneNumber(value);
      };
      dataToSend[key] = value;
    }
  }

  if (formData.get("password1") === formData.get("password2")) {
    dataToSend["password"] = formData.get("password1");
  } else {
    submitButton.disabled = false;
    alert('Erreur: Les deux mots de passe doivent être identiques.');
    return;
  }

  if (!formData.has("phone_number")) {
    dataToSend["phone_number"] = null;
  }

  if (!formData.has("is_mobile")) {
    dataToSend["is_mobile"] = false;
  }

  const fullAddress = formData.get("address");
  if (fullAddress && fullAddress.trim() !== "") {
    const addressParts = parseAddress(fullAddress);

    if (!addressParts.street || !addressParts.postal_code || !addressParts.city) {
      alert("Erreur: L'adresse fournie semble incomplète. Veuillez vérifier que vous avez bien indiqué la rue, le code postal et la ville.");
      submitButton.disabled = false;
      return;
    }

    dataToSend.Address = {
      street: addressParts.street,
      postal_code: addressParts.postal_code,
      city: addressParts.city
    };
  } else {
    console.log("Aucune adresse fournie");
  }

  fetch('api/register/professionals/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataToSend),
    credentials: 'include'
  })
    .then(response => {
      if (!response.ok) {
        alert("Une erreur technique est survenue, veuillez nous en excuser.")
        throw new Error("Network response was not ok");
      }
      console.log("Réponse reçue:", response);
      response.json();
    })
    .then(data => {
      console.log('Succès:', data);
      alert("Inscription réussie ! Merci de votre confiance.");
      window.location.href = "/";
    })
    .catch((error) => {
      console.error('Erreur:', error);
      alert("Une erreur est survenue lors de l'inscription. Veuillez réessayer.");
    })
    .finally(() => {
      submitButton.disabled = false;
    })
});


// Helper function to parse addresses
function parseAddress(fullAddress) {
  const postalCodeRegex = /\b\d{5}\b/;
  const postalCodeMatch = fullAddress.match(postalCodeRegex);
  const postalCode = postalCodeMatch ? postalCodeMatch[0] : '';
  const parts = fullAddress.split(postalCode);
  const street = parts[0].trim();
  const city = parts[1] ? parts[1].trim() : '';

  return {
    street: street,
    postal_code: postalCode,
    city: city
  };
}


// Helper function to format phone numbers
function formatPhoneNumber(phoneNumber) {
  if (phoneNumber.startsWith("0")) {
    return "+33" + phoneNumber.slice(1);
  } else {
    return phoneNumber;
  }
}


// Profession handler
document.addEventListener('DOMContentLoaded', function () {
  const professionSelect = document.getElementById('pro_profession');
  const customProfessionContainer = document.getElementById('custom-profession-container');
  const customProfessionInput = document.getElementById('custom_profession_input');

  const PROFESSION_CHOICES = [
    "Aide médico-psychologique",
    "Animateur.ice",
    "Autre",
    "Aide soignant.e",
    "Assistant.e de service social",
    "Assistant.e familial.e",
    "Auxiliaire de vie sociale",
    "Conseiller.e en économie sociale et familiale",
    "Educateur.ice spécialisé.e",
    "Moniteur.ice éducateur.ice",
    "Educateur.ice de jeunes enfants",
    "Ergothérapeute",
    "Educateur.ice technique spécialisé.e",
    "Masseur.se-kinésithérapeute",
    "Infirmier.e",
    "Psychomotricien.ne",
    "Puericulteur.ice",
    "Technicien.ne d'intervention sociale et familiale"
  ];

  professionSelect.innerHTML = '<option value="">Sélectionnez une profession</option>';

  PROFESSION_CHOICES.forEach(profession => {
    const option = document.createElement('option');
    option.value = profession;
    option.textContent = profession;
    professionSelect.appendChild(option);
  });

  professionSelect.addEventListener('change', function() {
    if (this.value === "Autre") {
      customProfessionContainer.style.display = 'block';
      customProfessionInput.required = true;
    } else {
      customProfessionContainer.style.display = 'none';
      customProfessionInput.required = false;
    }
  });
});
