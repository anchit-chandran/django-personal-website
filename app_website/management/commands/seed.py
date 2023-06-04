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
    Category,
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

                contents = file.readlines()

                # header url
                header_img_url = contents[-1]

                # convert back to original
                contents = "".join(contents[:-1])

                # get date from name
                published_on_raw = filename[:8]

                # convert date to "YYYY-MM-DD" format
                published_on_str = f"{published_on_raw[:4]}-{published_on_raw[4:6]}-{published_on_raw[6:]}"

                # convert into datetime object
                date_string = published_on_str
                published_on = make_aware(
                    datetime.strptime(
                    date_string, "%Y-%m-%d"
                )
                )

                title = filename[9:].replace(".md", "").replace("-", " ").title()

                if not BlogPost.objects.filter(title=title).exists():
                    post = BlogPost(
                        posted_at=published_on,
                        title=title,
                        content=contents,
                        header_img=header_img_url,
                    )
                    print(f"Saving {post}")
                    post.save()

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