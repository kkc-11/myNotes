# My Notes — Django App

A simple, user-specific notes app built with Django. Each user can sign up, log in, and create, edit, or delete their own notes.

Built almost entirely with Django's built-in features (ORM, Auth, Class-Based Views, Templates) and styled with [Pico CSS](https://picocss.com/)

## Features

- User registration & login (Django's built-in auth system)
- Create, edit, and delete notes
- Notes are private — users only see their own
- Admin panel for managing all data
- Clean UI via Pico CSS (semantic HTML, no utility classes)
- SVG icons for edit/delete actions

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default, swappable)
- **Styling:** [Pico CSS](https://picocss.com/) via CDN
- **Auth:** `django.contrib.auth`

## Project Structure

```
myproject/
├── myproject/          # Project settings & root URLs
│   ├── settings.py
│   └── urls.py
├── accounts/            # Authentication app
│   ├── views.py         # SignUpView
│   ├── urls.py          # signup/, login/, logout/
│   └── templates/registration/
│       ├── login.html
│       └── signup.html
└── notes/                # Notes app
    ├── models.py         # Note model (owner, title, content)
    ├── views.py           # List, Update, Delete views
    ├── forms.py           # NoteForm (ModelForm)
    ├── urls.py
    └── templates/
        ├── base.html
        └── notes/
            ├── note_list.html
            ├── note_edit.html
            └── note_confirm_delete.html
```

## Setup & Installation

1. **Clone the repo / set up the project folder**
   ```bash
   git clone <your-repo-url>
   cd myproject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the app**
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`
   - Sign up: `http://127.0.0.1:8000/accounts/signup/`
   - Login: `http://127.0.0.1:8000/accounts/login/`

## How It Works

| Feature | Implementation |
|---|---|
| Notes tied to a user | `owner = ForeignKey(User)` on the `Note` model |
| Users see only their notes | `Note.objects.filter(owner=request.user)` |
| Auto-assign owner on create | `form.save(commit=False)` + `note.owner = request.user` |
| Only owner can edit/delete | `UserPassesTestMixin` with `test_func()` |
| Login required everywhere | `@login_required` / `LoginRequiredMixin` |
| Signup form | Django's built-in `UserCreationForm` |
| Login/logout/password reset | `django.contrib.auth.urls` |

## Key URLs

| URL | Purpose |
|---|---|
| `/` | List & create notes |
| `/<id>/edit/` | Edit a note |
| `/<id>/delete/` | Delete a note (with confirmation) |
| `/accounts/signup/` | Register a new account |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out |
| `/admin/` | Django admin panel |


This is a learning/demo project — feel free to use or modify it freely.