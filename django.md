# Django Basics

**Django** is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

It helps developers build secure and maintainable websites quickly — **without writing all the low-level code** like request handling or database management manually.

---

## ⚙️ What Django Does
- Manages **view–model–app logic** relationships.
- Handles **routing, ORM (database layer), authentication, and admin panels** automatically.
- Provides a powerful **templating engine** and built-in tools for testing and deployment.
- You mainly define:
  - Your **models** (data structure)
  - Your **views** (logic)
  - Your **URLs** (routes)
  - And Django handles the rest.

> “You don't need to write code for everything — the framework handles most of the heavy lifting.”

---

## 🧠 Key Concept
Django follows the **MTV pattern** (Model–Template–View), which is conceptually similar to MVC.

---

## 🔗 Official Documentation
To learn Django professionally, check out the official documentation:
👉 [https://www.djangoproject.com/](https://www.djangoproject.com/)

---

## 🚀 Run Your Django Server
Once your project is created, you can start the development server using:
```bash
python manage.py runserver
```
## Then open your browser and visit:
```bash
http://127.0.0.1:8000/
```
### 💬 Pro Tip

**Keep your Django version updated and always use a virtual environment for project isolation.**
