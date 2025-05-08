from django.contrib.auth.models import User
from News.models import Author, Category, Post, PostCategory, Comment

user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Технологии')

article1 = Post.objects.create(
    author=author1,
    type=Post.ARTICLE,
    title='Первая статья',
    text='Текст первой статьи. Здесь размещена информация о важных событиях. Много интересных фактов и деталей описано в данной статье. Читатели могут найти полезную информацию.'
)

article2 = Post.objects.create(
    author=author2,
    type=Post.ARTICLE,
    title='Вторая статья',
    text='Содержание второй статьи. Автор поделился своим мнением о последних тенденциях. Представлены различные точки зрения на актуальную проблему.'
)

news1 = Post.objects.create(
    author=author1,
    type=Post.NEWS,
    title='Первая новость',
    text='Срочная новость! Произошло важное событие, которое повлияет на многих. Подробности и комментарии экспертов в материале.'
)

PostCategory.objects.create(post=article1, category=category1)
PostCategory.objects.create(post=article1, category=category2)
PostCategory.objects.create(post=article2, category=category3)
PostCategory.objects.create(post=news1, category=category2)
PostCategory.objects.create(post=news1, category=category4)

comment1 = Comment.objects.create(
    post=article1,
    user=user1,
    text='Отличная статья! Очень информативно.'
)

comment2 = Comment.objects.create(
    post=article1,
    user=user2,
    text='Интересная точка зрения, но есть некоторые неточности.'
)

comment3 = Comment.objects.create(
    post=article2,
    user=user1,
    text='Не согласен с автором. Тема раскрыта поверхностно.'
)

comment4 = Comment.objects.create(
    post=news1,
    user=user2,
    text='Спасибо за оперативность!'
)

article1.like()
article1.like()
article1.like()
article2.dislike()
news1.like()
news1.like()

comment1.like()
comment1.like()
comment2.like()
comment3.dislike()
comment4.like()
comment4.like()

author1.update_rating()
author2.update_rating()

best_author = Author.objects.order_by('-rating').first()
print(f"Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating}")

best_post = Post.objects.filter(type=Post.ARTICLE).order_by('-rating').first()
print(f"Лучшая статья:")
print(f"Дата: {best_post.created_at}")
print(f"Автор: {best_post.author.user.username}")
print(f"Рейтинг: {best_post.rating}")
print(f"Заголовок: {best_post.title}")
print(f"Превью: {best_post.preview()}")

print("\nКомментарии к лучшей статье:")
for comment in Comment.objects.filter(post=best_post):
    print(f"Дата: {comment.created_at}")
    print(f"Пользователь: {comment.user.username}")
    print(f"Рейтинг: {comment.rating}")
    print(f"Текст: {comment.text}")
    print() 