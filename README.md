# Django-powered Personal Website with CMS and Emailing

A personal website made in Django, to replace my Ghost blog!

![image](https://github.com/anchit-chandran/django-personal-website/assets/68898006/495fc386-1f75-4f9b-af03-8cb673091691)

This website was made using Django, styled using Bootstrap5, and deployed using Digital Oceans managed App Platform.

Initially, I had toyed around with various different static site generators. Finally, I'd settled on Jekyll and was developing my own custom theme from scratch. However, it was hard to achieve more complex customisations.

For this reason, I moved to my own Django website, hosting the server and database with my own CMS. It was a good excuse to learn more Django!

## Highlights

These are some key features of the project.

### Custom admin pages to manage markdown posts

![image](https://github.com/anchit-chandran/django-personal-website/assets/68898006/8016dc0e-fb64-4f5c-b1dc-da734dafdf39)


When logged in, extra admin tools become available in the nav. These custom pages allow me to manage and write blog posts / project pages in markdown, which are converted into HTML within the template.

![image](https://github.com/anchit-chandran/django-personal-website/assets/68898006/7c87f9d2-ad86-4bfb-b4da-9d6ac4583333)


### Email newsletter functionality

![image](https://github.com/anchit-chandran/django-personal-website/assets/68898006/e770ba15-b7aa-4f34-9577-e95dcc5c4211)


Every new blog post I upload, I have the option to send it out to my subscribers too!

### Dockerized with Docker-compose for ease of local development

I dockerized the application for easy local development.
