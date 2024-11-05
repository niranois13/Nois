// // Services handler
// document.addEventListener('DOMContentLoaded', function () {
//   const categorySelect = document.getElementById('pro_service_category');
//   const serviceSelect = document.getElementById('pro_service');
//   const customCategoryContainer = document.getElementById('custom-category-container');
//   const customServiceContainer = document.getElementById('custom-service-container');
//   const customCategoryInput = document.getElementById('custom_service_category_input');
//   const customServiceInput = document.getElementById('custom_service_name_input');
//   const addServiceButton = document.getElementById('pro_add_service_button');
//   const mainFormServices = document.querySelector('.main-form-services');


//   // Mettre à jour /Nois/backend/apps/models/Service.py pour toute modification
//   const SERVICE_CATEGORY_CHOICES = {
//     "SOIN_ET_HYGIENE": "Soins et hygiène",
//     "ACCOMPAGNEMENT": "Accompagnement et transport",
//     "EDUCATION_ET_LOISIRS": "Éducation et loisirs",
//     "THERAPIE": "Thérapie et soutien psychologique",
//     "ADMINISTRATIF": "Gestion administrative et financière",
//     "VIE_QUOTIDIENNE": "Assistance à la vie quotidienne",
//     "AUTRE": "Autre"
//   };

//   // Mettre à jour /Nois/backend/apps/models/Service.py pour toute modification
//   const SERVICE_NAME_CHOICES = {
//     "SOIN_ET_HYGIENE": ["Coiffure à domicile", "Aide à la toilette", "Massage relaxant"],
//     "ACCOMPAGNEMENT": ["Transport médical", "Aide aux courses", "Compagnie à domicile"],
//     "EDUCATION_ET_LOISIRS": ["Cours de musique", "Activités manuelles", "Sorties culturelles"],
//     "THERAPIE": ["Psychothérapie", "Groupe de soutien", "Conseil familial"],
//     "ADMINISTRATIF": ["Gestion de documents", "Aide à la déclaration d'impôts", "Assistance bancaire"],
//     "VIE_QUOTIDIENNE": ["Aide au repas", "Entretien ménager", "Aide aux démarches"],
//     "AUTRE": ["Autre service"]
//   };

//   for (let [value, text] of Object.entries(SERVICE_CATEGORY_CHOICES)) {
//     let option = new Option(text, value);
//     categorySelect.add(option);
//   }

//   function updateServices(category) {
//     serviceSelect.innerHTML = '<option value="">Sélectionnez un service</option>';
//     if (category && SERVICE_NAME_CHOICES[category]) {
//       SERVICE_NAME_CHOICES[category].forEach(service => {
//         let option = new Option(service, service);
//         serviceSelect.add(option);
//       });
//     }
//   }

//   categorySelect.addEventListener('change', function () {
//     updateServices(this.value);
//     customCategoryContainer.style.display = this.value === 'AUTRE' ? 'block' : 'none';
//     customCategoryInput.required = this.value === 'AUTRE';
//   });

//   serviceSelect.addEventListener('change', function () {
//     customServiceContainer.style.display = this.value === 'Autre service' ? 'block' : 'none';
//     customServiceInput.required = this.value === 'Autre service';
//   });

//   addServiceButton.addEventListener('click', function (event) {
//     debugger;
//     event.preventDefault();

//     if (categorySelect.value && (serviceSelect.value || customServiceInput.value)) {
//       const newServiceSection = document.createElement('div');
//       newServiceSection.classList.add('main-form-services');
//       newServiceSection.innerHTML = mainFormServices.innerHTML;

//       newServiceSection.querySelectorAll('[id]').forEach(element => element.removeAttribute('id'));
//       mainFormServices.parentNode.insertBefore(newServiceSection, addServiceButton.parentNode);

//       const newCategorySelect = newServiceSection.querySelector('select[name="service_category"]');
//       const newServiceSelect = newServiceSection.querySelector('select[name="service_name"]');
//       const newCustomCategoryContainer = newServiceSection.querySelector('.custom-category-container');
//       const newCustomServiceContainer = newServiceSection.querySelector('.custom-service-container');
//       const newCustomCategoryInput = newServiceSection.querySelector('input[name="custom_service_category"]');
//       const newCustomServiceInput = newServiceSection.querySelector('input[name="custom_service_name"]');

//       newCategorySelect.addEventListener('change', function () {
//         updateServices(this.value);
//         newCustomCategoryContainer.style.display = this.value === 'AUTRE' ? 'block' : 'none';
//         newCustomCategoryInput.required = this.value === 'AUTRE';
//       });

//       newServiceSelect.addEventListener('change', function () {
//         newCustomServiceContainer.style.display = this.value === 'Autre service' ? 'block' : 'none';
//         newCustomServiceInput.required = this.value === 'Autre service';
//       });
//     } else {
//       alert("Veuillez remplir tous les champs avant d'ajouter un nouveau service.");
//     }
//   });
// });
