import random
from blog.models import Blog, Category
from faker import Faker

# for i in range(1, 10):
#     fake = Faker()
#     cat = Category(title=fake.name())
#     cat.save()


thumbnail = 'thumbnail/19/09/15/photo-1561732027-f3d689667250.jpeg'


def slugify(postTitle):
    return '-'.join(map(lambda title: title.lower(), postTitle.split(' ')))


for i in range(1, 500):
    fake = Faker()
    title = fake.sentence()
    slug = slugify(title)
    blog = Blog(
        title=title,
        author_id=1,
        excerpt=fake.text(),
        body=fake.text(),
        slug=slug,
        thumbnail=thumbnail,
        category_id=random.randint(1, 9))
    blog.save()


# b = Blog(title="title 2", author_id=1, slug="dfkjfhdskffffj", category_id=1)
# b.save()
