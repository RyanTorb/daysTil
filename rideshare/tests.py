from django.test import TestCase
from django.utils import timezone
from .models import Profile, requests, offer, SignUp
from django.contrib.auth.models import User

import unittest
# Create your tests here.

class ProfileSetupTestCase(TestCase):
	def setUp(self):
	  	Profile.objects.create(car='Chrysler',hometown='Sewickley',preferred_payment='venmo')
	  	requests.objects.create(start_location="Cville",end_location='NYC',depart_date = '2019-11-29', depart_time='12:00')

	def test_profile_setup(self):
	 	p = Profile.objects.get(preferred_payment='venmo')
	 	composite = p.car=='Chrysler' and p.hometown=='Sewickley'
	 	self.assertEqual(composite, True)
		 
	def test_prof_car(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="Ford Fusion 2019", hometown="Phoenixville", preferred_payment="Venmo")
		self.assertEqual(p.car, "Ford Fusion 2019")

	def test_prof_car_invalid_input(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", hometown="Phoenixville", preferred_payment="Venmo")
		self.assertNotEqual(p.car, 2)

	def test_prof_car_not_same(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		u2 = User.objects.get(username='cma3uj')
		p = Profile.objects.create(User=u, car="2", hometown="Phoenixville", preferred_payment="Venmo")
		p2 = Profile.objects.create(User=u2, car="Ford Fiesta", hometown="Phoenixville", preferred_payment="Venmo")
		self.assertNotEqual(p.car, p2.car)

	def test_prof_not_same(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		u2 = User.objects.get(username='cma3uj')
		p = Profile.objects.create(User=u, car="2", hometown="Phoenixville", preferred_payment="Venmo")
		p2 = Profile.objects.create(User=u2, car="Ford Fiesta", hometown="Phoenixville", preferred_payment="Venmo")
		self.assertNotEqual(p.User, p2.User)

	def test_prof_hometown(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", hometown="Phoenixville", preferred_payment="Venmo")
		self.assertEqual(p.hometown, "Phoenixville")

	def test_prof_hometown_default_val(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", preferred_payment="Venmo")
		self.assertEqual(p.hometown, '')

	def test_prof_payment(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", preferred_payment="Cash")
		self.assertEqual(p.preferred_payment, 'Cash')

	def test_prof_not_same_payment(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", preferred_payment="Cash")
		u2 = User.objects.get(username='cma3uj')
		p2 = Profile.objects.create(User=u2, car="2", preferred_payment="Venmo")
		self.assertNotEqual(p.preferred_payment, p2.preferred_payment)

	def test_prof_not_same_hometown(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		p = Profile.objects.create(User=u, car="2", hometown="chester, nj", preferred_payment="Cash")
		u2 = User.objects.get(username='cma3uj')
		p2 = Profile.objects.create(User=u2, car="2", hometown="chester, nj", preferred_payment="Venmo")
		self.assertEqual(p.hometown, p2.hometown)

	def test_default_payment(self):
	 	p = Profile.objects.get(hometown='Sewickley')
	 	self.assertEqual(p.preferred_payment, "venmo")

class RequestTestCase(TestCase):
	def test_req_start_loc(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertEqual(r.start_location, "Xville")

	def test_req_end_loc(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertEqual(r.end_location, "Pville")

	def test_req_author(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		r2 = requests.objects.create(start_location='Xville', end_location='North Pole', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertEqual(r.author, r2.author)

	def test_req_author2(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		u2 = User.objects.get(username='cma3uj')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		r2 = requests.objects.create(start_location='Xville', end_location='North Pole', author=u2, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertNotEqual(r.author, r2.author)

	def test_req_date(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		r2 = requests.objects.create(start_location='Xville', end_location='North Pole', author=u, depart_date="2019-12-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertNotEqual(r.depart_date, r2.depart_date)

	def test_req_not_equal_time(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", desired_price=1, notes="hi")
		r2 = requests.objects.create(start_location='Xville', end_location='North Pole', author=u, depart_date="2019-12-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertNotEqual(r.depart_time, r2.depart_time)

	def test_req_equal_time(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", desired_price=1, notes="hi")
		self.assertEqual(r.depart_time, "12:00")

	def test_price_invalid_input(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", desired_price=1, notes="hi")
		self.assertNotEqual(r.desired_price, "1")

	def test_notes_not_required(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		r = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", desired_price=1)
		self.assertEquals(r.notes, None)
	
	
class OfferTestCase(TestCase):
	def test_off_start_loc(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		self.assertEqual(o.start_location, "Xville")

	def test_req_end_loc(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		self.assertEqual(o.end_location, "Pville")

	def test_req_author(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		o2 = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		self.assertEqual(o.author, o2.author)

	def test_req_author2(self):
		User.objects.create(username='lmd2pg')
		User.objects.create(username='cma3uj')
		u = User.objects.get(username='lmd2pg')
		u2 = User.objects.get(username='cma3uj')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		o2 = offer.objects.create(start_location='Xville', end_location='Pville', author=u2, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		self.assertNotEqual(o.author, o2.author)

	def test_req_date(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = requests.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", desired_price=1, notes="hi")
		o2 = requests.objects.create(start_location='Xville', end_location='North Pole', author=u, depart_date="2019-12-12", depart_time="2:00", desired_price=1, notes="hi")
		self.assertNotEqual(o.depart_date, o2.depart_date)

	def test_req_not_equal_time(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		o2 = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-12-12", depart_time="12:00", price=1, seats=5, notes="hi")
		self.assertNotEqual(o.depart_time, o2.depart_time)

	def test_req_equal_time(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", price=1, seats=5, notes="hi")
		self.assertEqual(o.depart_time, "12:00")

	def test_price_invalid_input(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", price=1, seats=5, notes="hi")
		self.assertNotEqual(o.price, "1")

	def test_notes_not_required(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="12:00", price=1, seats=5)
		self.assertEquals(o.notes, None)

	
class SignUpTestCase(TestCase):
	def test_location_sign_up(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		s = SignUp.objects.create(user=u, offer=o)
		self.assertEqual(s.offer.start_location, "Xville")

	def test_sign_up_username(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		s = SignUp.objects.create(user=u, offer=o)
		self.assertEqual(s.user.username, "lmd2pg")

	def test_multiple_sign_up(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		User.objects.create(username='lukedeni')
		u2 = User.objects.get(username='lukedeni')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		s = SignUp.objects.create(user=u, offer=o)
		s1 = SignUp.objects.create(user=u2, offer=o)
		self.assertNotEqual(s.user, s1.user)

	def test_multiple_sign_up2(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		User.objects.create(username='lukedeni')
		u2 = User.objects.get(username='lukedeni')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		s = SignUp.objects.create(user=u, offer=o)
		s1 = SignUp.objects.create(user=u2, offer=o)
		self.assertEqual(s.offer, s1.offer)
	
	def test_capactiy(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		User.objects.create(username='lukedeni')
		u2 = User.objects.get(username='lukedeni')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		SignUp.objects.create(user=u, offer=o)
		SignUp.objects.create(user=u2, offer=o)
		x = len(SignUp.objects.all().filter(offer=o))
		self.assertLess(x, o.seats)

	def test_capacity2(self):
		User.objects.create(username='lmd2pg')
		u = User.objects.get(username='lmd2pg')
		User.objects.create(username='lukedeni')
		u2 = User.objects.get(username='lukedeni')
		o = offer.objects.create(start_location='Xville', end_location='Pville', author=u, depart_date="2019-11-12", depart_time="2:00", price=1, seats=5, notes="hi")
		SignUp.objects.create(user=u, offer=o)
		SignUp.objects.create(user=u2, offer=o)
		x = len(SignUp.objects.all().filter(offer=o))
		self.assertEqual(x, 2)
