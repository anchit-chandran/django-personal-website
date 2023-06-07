import os
from datetime import datetime, time

from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
import frontmatter
import markdown as md

from app_website.models import (
    BlogPost,
    Project,
    Skill,
    )


class Command(BaseCommand):
    help = "Seed database with old markdown posts."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        if options["mode"] == "seed_posts":
            self.stdout.write("Seeding blog posts...")
            run_blog_post_seed()
        if options["mode"] == "reset_seed_posts":
            self.stdout.write("Resetting and seeding blog posts...")
            delete_and_run_blog_post_seed()
        elif options["mode"] == "seed_superuser":
            seed_superuser()
        elif options["mode"] == "seed_projects":
            self.stdout.write("Seeding blog posts...")
            run_projects_seed()

def run_projects_seed():
    # Specify the directory path
    directory = f"{settings.BASE_DIR}/app_website/projects"
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the current item is a file
        if os.path.isfile(filepath):
            # Open the file for reading
            with open(filepath, "r", encoding='UTF-8') as file:
                content = file.read()
                metadata, markdown_content = frontmatter.parse(content)
                
                # don't repeat seeding if project already exists
                if Project.objects.filter(title=metadata['title']):
                    print(f"{metadata['title']} already exists. Skipping...")
                    continue
                
                print('Seeding ', metadata['title'])
                
                project = Project(
                    title = metadata['title'],
                    content = markdown_content,
                    github = metadata['github'],
                    featured = metadata['featured'],
                    header_img = metadata['header_img'],
                )

                # project needs to be saved before adding skill
                project.save()
                
                # clean up and add skills
                for skill in metadata['skills']:
                    # if skill doesn't exist, add
                    if not Skill.objects.filter(name=skill).exists():
                        print(f"Skill {skill} doesn't exist - adding")
                        Skill.objects.create(name=skill)
                    else:
                        print(f"{skill} already present. Skipping...")
                    
                    print(f'Associating {skill} with {project.title}')
                    new_skill = Skill.objects.get(name=skill)
                    project.skills.add(new_skill)
            
                
                
                

def run_blog_post_seed():

    # Specify the directory path
    directory = f"{settings.BASE_DIR}/old-blog-markdown-json/posts"

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the current item is a file
        if os.path.isfile(filepath):
            # Open the file for reading
            with open(filepath, "r", encoding='UTF-8') as file:
                # Read the contents of the file

                content = file.read()
                metadata, markdown_content = frontmatter.parse(content)

                if not BlogPost.objects.filter(title=metadata["title"]).exists():
                    post = BlogPost(
                        posted_at=metadata["published_on"],
                        title=metadata["title"],
                        content=markdown_content,
                        header_img=metadata["header_img"],
                        published=True,
                    )
                    print(f"Saving {post}")
                    post.save()
                else:
                    print(f"{BlogPost.objects.get(title=metadata['title'])} already exists. Skipping...")

def delete_and_run_blog_post_seed():
    
    BlogPost.objects.all().delete()
    
    run_blog_post_seed()

def seed_superuser():
    username = 'a'
    email = 'a@a.com'
    password = 'pw'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser...")
        superuser = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        superuser.save()
    
    print(f"Superuser username: {username}\nSuperuser password: {password}")