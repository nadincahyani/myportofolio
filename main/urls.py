from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_education,
    show_projects,
    create_project,
    get_projects_json,
    delete_project,
    update_project,
    get_experience_json_by_id,
    create_experience,
    get_experience_json,
    delete_experience,
    update_experience,
    get_projects_json_by_id,
    register,
    login_user,
    logout_user,
    toggle_star,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("projects/", show_projects, name='show_projects'),

    # Project
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:id>/delete/",delete_project,name="delete_project"),
    path("projects/update/<uuid:id>/", update_project, name="update_project"),
    path("projects/json/<uuid:id>/", get_projects_json_by_id, name="get_projects_json_by_id"),
    path("projects/<uuid:id>/star/", toggle_star, name="toggle_star"),

    # Experience
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/delete/<uuid:id>/", delete_experience, name="delete_experience"), 
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/update/<uuid:id>/", update_experience, name="update_experience"),
    path("experience/json/<uuid:id>/", get_experience_json_by_id, name="get_experience_json_by_id"),

    # Registes, Login, dan Logout
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]