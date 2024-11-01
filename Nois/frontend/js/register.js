document.getElementById("register-patient").addEventListener("click", function(event){
  event.preventDefault();
  document.getElementById("UserRegisterModal").style.display = "flex";
});

document.querySelector(".close").addEventListener("click", function() {
  document.getElementById("UserRegisterModal").style.display = "none";
});

window.onclick = function(event) {
  if (event.target === document.getElementById("UserRegisterModal")) {
    document.getElementById("UserRegisterModal").style.display = "none";
  }
};


document.getElementById("register-button").addEventListener("click", function() {
  const first_name = document.getElementById("user_first_name").value;
  const last_name = document.getElementById("user_last_name").value;
  const phone_number = document.getElementById("user_phone_number").value;
  const is_helper = document.getElementById("user_is_helper").value;
  const email = document.getElementById("user_email").value;
  const password = document.getElementById("user_password").value;
  const address = document.getElementById("user_address").value;

  if (!email || !password || !first_name || !last_name) {
    alert("Veuillez fournir un nom, un prénom, un email et un mot de passe.");
    return;
  }
  if (!phone_number.value) {
    phone_number.value = "null";
  }
  if (!address.value) {
    address.value = "null";
  }

  const userData = {
    first_name: first_name,
    last_name: last_name,
    phone_number: phone_number,
    is_helper: is_helper,
    email: email,
    password: password,
    address: address,
  };

  fetch("/register/clients/", {
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
    return response.json()
  })
  .then(data => {
    console.log("Success:", data);
    window.location.href = "/html/";
  })
  .catch((error) => {
    console.error("Error:", error);
    alert("Echec de l'enregistrement. Veuillez vérifier vos informations.")
  });
});