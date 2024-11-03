
// Professional registration
const form = document.getElementById("ProRegisterForm");
const submitButton = document.getElementById("pro_register-button");

form.addEventListener('submit', function(event) {
  event.preventDefault();
  console.log("Formulaire soumis, preventDefault appelé");
  submitButton.disabled = true;

  const formData = new FormData(this);

  const requiredFields = ["email", "password", "first_name", "last_name", "intervention_radius"];
  for (let field of requiredFields) {
    if (!formData.get(field)) {
      alert(`Veuillez fournir ${
        field === "first_name" ? "un prénom" :
        field === "last_name" ? "un nom de famille" :
        field === "email" ? "un email" :
        field === "password" ? "un mot de passe" :
        field === "intervention_radius" ? "un rayon d'intervention" :
        field
      }.`);
      submitButton.disabled = false;
      return;
    }
  }

  let dataToSend = {};

  for (let [key, value] of formData.entries()) {
    if (key !== 'address') {
      dataToSend[key] = value;
    }
    if (key === "phone_number") {
      value = formatPhoneNumber(value);
    }
  }

  if (formData.has("phone_number") === false) {
    dataToSend["phone_number"] = null;
  }

  if (formData.has("is_mobile") === false) {
    dataToSend["is_mobile"] = false;
  }

  const fullAddress = formData.get("address");
  if (fullAddress && fullAddress.trim() !== "") {
    const addressParts = parseAddress(fullAddress);

    if (!addressParts.street || !addressParts.postal_code || !addressParts.city) {
      alert("L'adresse fournie semble incomplète. Veuillez vérifier que vous avez bien indiqué la rue, le code postal et la ville.");
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
    submitButton.disabled = false;
  })
  .catch((error) => {
    console.error('Erreur:', error);
    alert("Une erreur est survenue lors de l'inscription. Veuillez réessayer.");
    submitButton.disabled = false;
  });
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
