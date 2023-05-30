import os
from datetime import datetime, time

from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.timezone import make_aware
from django.contrib.auth.models import User

from app_website.models import BlogPost


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


def run_blog_post_seed():
    # Specify the directory path
    directory = f"{settings.BASE_DIR}/old-blog-markdown-json/posts"

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Check if the current item is a file
        if os.path.isfile(filepath):
            # Open the file for reading
            with open(filepath, "r") as file:
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