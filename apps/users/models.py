from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150, null=False)
    first_name = models.CharField(max_length=150, blank= True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=30, null=False)
    email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.username



class Author(models.Model):
    name = models.CharField(max_length=100)  
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

  
class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.ManyToManyField(Author, related_name='books')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.DateField()
    cover_url = models.ImageField(upload_to='book_cover')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5
        
        
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    rating = models.IntegerField(choices=Rating.choices, default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    




class ReviewLike(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
