from django.test import TestCase
from .models import ExcerciseDate, ExcerciseDetail, 

# Create your tests here.
class ExcerciseDetailTest(TestCase):
    def setUp(self):
        self.type=ExcerciseDetail(liftname='dumbell curl')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'dumbell curl' )

    def test_tablename(self):
        self.assertEqual(str(ExerciseDetail._meta.db_table), 'excercisedetail')
