from django.test import TestCase

# Create your tests here.


from django.test import SimpleTestCase


# Create your tests here.
class testNearestHund(SimpleTestCase):
    def test_near_hund_89(self):
        response = self.client.get("/warmup-1/near-hundred/89/")
        self.assertContains(response, "False")

    def test_near_hund_90(self):
        response = self.client.get("/warmup-1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hund_93(self):
        response = self.client.get("/warmup-1/near-hundred/93/")
        self.assertContains(response, "True")


class testStringSplosion(SimpleTestCase):
    def test_splo_code(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_splo_abc(self):
        response = self.client.get("/warmup-2/string-splosion/abc/")
        self.assertContains(response, "aababc")

    def test_splo_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab/")
        self.assertContains(response, "aab")


class testString2(SimpleTestCase):
    def test_cat(self):
        response = self.client.get("/string-2/cat-dog/catdog/")
        self.assertContains(response, True)

    def test_catCat(self):
        response = self.client.get("/string-2/cat-dog/catcat/")
        self.assertContains(response, False)

    def test_catyaddayadda(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog/")
        self.assertContains(response, True)


class testLonesomenumber(SimpleTestCase):
    def test1_2_3(self):
        response = self.client.get("/Logic-2/lone-sum/1/2/3/")
        self.assertContains(response, 6)

    def test3_2_3(self):
        response = self.client.get("/Logic-2/lone-sum/3/2/3/")
        self.assertContains(response, 2)

    def test3_3_3(self):
        response = self.client.get("/Logic-2/lone-sum/3/3/3/")
        self.assertContains(response, 0)
