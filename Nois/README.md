# 🤝 Nois — Connecting People with Disabilities to Healthcare Professionals

**Nois** is a full-stack web platform designed to connect individuals with disabilities to independent healthcare and social work professionals.<br/>
Built with a strong focus on accessibility and purpose, this project is an educational prototype developed as part of a software engineering curriculum.

---

## ✨ Genesis

**Nois** was built as a portfolio project at the end of the **Fundamentals** program at [Holberton School](https://www.holbertonschool.com/).

As a former **medico-social worker in France**, I've witnessed first-hand the recurring problems in the field:
- A shortage of institutions and professionals
- Many people living without proper accompaniment
- Complex administrative systems that further isolate vulnerable individuals

These observations led my wife and me to brainstorm potential solutions. **Nois** is a first humble attempt to translate that vision into a working tool.

⚠️ **Note:**
This is an educational project with many limitations. It is **not production-ready**. Frontend design is basic and lacks polish, and many best practices (especially testing and accessibility) are still to be implemented.

---

## 🛠 Tech Stack

### Backend
- **Python** / **Django** / **Django REST Framework**
- **PostgreSQL**
- **Role-Based Authentication**
- **RESTful API**

### Frontend
- **HTML5**, **CSS3**, **Vanilla JavaScript**
- Minimalist, functional interface (currently underdeveloped)

### Infrastructure
- **Docker** (multi-container setup)
- **Nginx** reverse proxy for unified routing

---

## 📂 Project Structure

```
├── backend/       # Django project, API logic, database models
├── frontend/      # Static HTML/CSS/JS frontend
├── nginx/         # Nginx reverse proxy config
└── docker-compose.yml

````

---

## ✅ Features (Working MVP)

- 👤 **Account System with Roles**
  Users can register as:
  - Clients (those looking for help)
  - Professionals (health/social work service providers)
  - Admins (platform maintenance)
- 🔐 **Role-Based Access Control**
- 🔎 **Search System**
  Query-based search to find professionals in the database (e.g., by field, location)

---

## ⚠️ Current Limitations

- 🧪 **Missing Unit/Integration Tests**
- 🎨 **Minimal Frontend Design** (not fully responsive, not styled)
- ❌ No CI/CD or deployment yet
- 🗣️ No i18n/language support
- ♿ Accessibility and UX considerations still to be improved/added

> This project is intentionally unfinished in several areas, as part of the learning process. Improvements are ongoing.

---

## 🚀 Getting Started

- Docker & Docker Compose installed

```
git clone https://github.com/yourusername/inclusivecare.git
cd inclusivecare
docker-compose up --build
````

Frontend and API will be served via Nginx reverse proxy.

---

## 🧭 Roadmap Ideas

* Add booking/calendar module for professionals
* Implement messaging between users
* Improve frontend with modern framework (React or Vue)
* Full test coverage (backend + frontend)
* Admin dashboard & statistics
* Accessibility audit (WCAG 2.1)

---

## 🤝 Contributing

While this is a personal portfolio project, feedback and collaboration are welcome, especially from people working in the **healthcare**, **social work**, or **accessibility** fields.

Feel free to open an issue or submit a PR.

---

## Screenshots

![Homepage](https://i.imgur.com/lwBphyw.png)
![ConnexionModal](https://i.imgur.com/vrcyEHb.png)

## 👤 Author

Built with care by **Nicolas Doyen** — former medico-social worker turned developer.
[LinkedIn](https://www.linkedin.com/in/nicolas-doyen-9437b5322/)
