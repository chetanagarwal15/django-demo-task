# Django Demo Task

This is a simple web application built with **Django** and **PostgreSQL**.  
It demonstrates CRUD operations via REST APIs, external API integration, and simple reporting with data visualization.

---

## **Features**

1. **CRUD API for Tasks**
   - Create, Read, Update, Delete tasks.
   - API endpoint: `/api/tasks/`

2. **External API Integration**
   - Fetches top 10 posts from JSONPlaceholder.
   - API endpoint: `/api/external_posts/`

3. **Reporting / Data Visualization**
   - Counts tasks by status (`todo`, `in-progress`, `done`).
   - API endpoint: `/api/status_counts/`

---

## **Live Demo**

Check the live deployed project here:  
[https://django-demo-task.onrender.com](https://django-demo-task.onrender.com)

---

## **Installation & Setup (Local Testing)**

1. Clone the repo:
   ```bash
   git clone https://github.com/chetanagarwal15/django-demo-task.git
   cd django-demo-task
