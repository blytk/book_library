from django.db.models import Max
from django.test import Client, TestCase

from .models import User, Book, Note, Reading, Read, Wish

# Create your test here

class BookLibraryTestCase(TestCase):

    def setUp(self):
        # Create users.
        user1 = User.objects.create(username="user1", password="1")
        user2 = User.objects.create(username="user2", password="1")
        user3 = User.objects.create(username="user3", password="1")

        # Create books.
        b1 = Book.objects.create(title="Dune", author="Frank Herbert", genre=4)
        b2 = Book.objects.create(title="The Three Musketeers", author="Alexandre Dumas", genre=4)
        b3 = Book.objects.create(title="Atomic Habits", author="James Clear", genre=1)

        # Create reading objects
        reading1 = Reading.objects.create(user=user1, book=b1, why="I felt like it")
        reading2 = Reading.objects.create(user=user2, book=b2, why="")
        reading3 = Reading.objects.create(user=user3, book=b3, why="Can't say")

        # Create read objects
        read1 = Read.objects.create(user=user1, book=b1, why="I felt like it")
        read2 = Read.objects.create(user=user2, book=b2, why="")
        read3 = Read.objects.create(user=user3, book=b3, why="Can't say")

        # Create wish objects
        wish1 = Wish.objects.create(user=user1, book=b1, why="I felt like it")
        wish2 = Wish.objects.create(user=user2, book=b2, why="")
        wish3 = Wish.objects.create(user=user3, book=b3, why="Can't say")

        # Create notes

        note1 = Note.objects.create(user=user1, book=b1, text="Note number 1 for user1 b1")
        note2 = Note.objects.create(user=user2, book=b2, text="Note number 2 for user2 b2")
        note3 = Note.objects.create(user=user3, book=b3, text="Note number 3 for user3 b3")
    

    def test_book_count(self):
        b = Book.objects.all()
        self.assertEqual(b.count(), 3)
    
    def test_reading_objects_count(self):
        r = Reading.objects.all()
        self.assertEqual(r.count(), 3)

    def test_read_objects_count(self):
        read = Read.objects.all()
        self.assertEqual(read.count(), 3)
    
    def test_wish_objects_count(self):
        wish = Wish.objects.all()
        self.assertEqual(wish.count(), 3)
    
    def test_note_objects_count(self):
        n = Note.objects.all()
        self.assertEqual(n.count(), 3)

    def test_note_per_user_count(self):
        n1 = Note.objects.filter(user=1)
        n2 = Note.objects.filter(user=1)
        n3 = Note.objects.filter(user=1)

        self.assertEqual(n1.count(), 1)
        self.assertEqual(n2.count(), 1)
        self.assertEqual(n3.count(), 1)

    def test_index(self):
        c = Client()
        response = c.get("")
        print(response)
        self.assertEqual(response.status_code, 302)
            

    """
    def test_duplicate_book_on_list(self):
        user4 = User.objects.create(username="user4", password="1")
        b1 = Book.objects.get(pk=1)

        
        a = Reading.objects.create(user=user4, book=b1)
        b = Reading.objects.create(user=user4, book=b1)
        q = Reading.objects.filter(user=user4, book=b1)
        self.assertEqual(q.count(), 1)
        
        c = Read.objects.create(user=user4, book=b1)
        d = Read.objects.create(user=user4, book=b1)
        q = Read.objects.filter(user=user4, book=b1)
        self.assertEqual(q.count(), 1)

        e = Wish.objects.create(user=user4, book=b1)
        f = Wish.objects.create(user=user4, book=b1)
        q = Wish.objects.filter(user=user4, book=b1)
        self.assertEqual(q.count(), 1)
    """

    


