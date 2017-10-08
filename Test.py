import requests
import unittest

class TestStringMethods(unittest.TestCase): 
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/')
		self.assertEquals(r.status_code, 200, 'status not correct')		
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/')
		self.assertEquals(r.status_code, 200, 'status not correct')
	def test_check200Responce(self):
		r = requests.get('https://recoursia.by/register/')
		self.assertEquals(r.status_code, 200, 'status not correct')
			

if __name__ == '__main__':
    unittest.main()