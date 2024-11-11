// User registration
document.getElementById("register-user").addEventListener("click", function(event){
  event.preventDefault();
  document.getElementById("UserRegisterModal").style.display = "flex";
});

document.querySelector(".register-close").addEventListener("click", function() {
  document.getElementById("UserRegisterModal").style.display = "none";
});

window.onclick = function(event) {
  if (event.target === document.getElementById("UserRegisterModal")) {
    document.getElementById("UserRegisterModal").style.display = "none";
  }
};

const form = document.getElementById("UserRegisterForm");
const submitButton = document.getElementById("user-register-button");

form.addEventListener('submit', async function(event) {
  event.preventDefault();
  submitButton.disabled = true;

  const formData = new FormData(this);

  const requiredFields = ["email", "password1", "password2", "first_name", "last_name"]
  for (let field of requiredFields) {
    if (!formData.get(field)) {
      alert(`Veuillez renseigner ${
        field === "first_name" ? "un prénom" :
        field === "last_name" ? "un nom de famille" :
        field === "email" ? "un email" :
        field === "pasword1" ? "un mot de passe" :
        field === "password2" ? "la confirmation du mot de passe" :
        field
      }.`);
      submitButton.disabled = false;
      return;
    }
  }

  let dataToSend = {};

  for (let [key, value] of formData.entries()) {
    if (
      key !== 'address' &&
      key !== "password1" &&
      key !== "password2"
    ) {
      if (key === "phone_number") {
        value = formatPhoneNumber(value);
      }
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
      alert("Erreur: L'adresse fournie semble incomplète.");
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


  try {
    fetch("/api/register/clients/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dataToSend),
      credentials: 'include'
    })
    .then(response => {
      if (!response.ok) {
        submitButton.disabled = false;
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then(data => {
      console.log("Success:", data);
      window.location.href = "/";
    })

    } catch (error) {
      submitButton.disabled = false;
      console.error("Error:", error);
      alert("Echec de l'enregistrement. Veuillez vérifier vos informations.")
    } finally {
      submitButton.disabled = false;
    }
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

// Function to toggle diplay on/off on form passwords
function toggleFormPassword1() {
  const password1Field = document.getElementById('user_password');
  const toggleIconPW1 = document.getElementById('form-password1-eye');

    if (password1Field.type === 'password') {
      password1Field.type = 'text';
      toggleIconPW1.classList.add("icon-eye-closed");
      toggleIconPW1.classList.remove("icon-eye-open");
    } else {
      password1Field.type = 'password';
      toggleIconPW1.classList.remove("icon-eye-closed");
      toggleIconPW1.classList.add("icon-eye-open");
    }
};

function toggleFormPassword2() {
    const password2Field = document.getElementById('user_password-confirm');
    const toggleIconPW2 = document.getElementById('form-password2-eye');

    if (password2Field.type === 'password') {
      password2Field.type = 'text';
      toggleIconPW2.classList.add("icon-eye-closed");
      toggleIconPW2.classList.remove("icon-eye-open");
    } else {
      password2Field.type = 'password';
      toggleIconPW2.classList.remove("icon-eye-closed");
      toggleIconPW2.classList.add("icon-eye-open");
    }
};
