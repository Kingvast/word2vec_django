from django.contrib.auth.models import User
from django.test import TestCase

from .models import Word2Vec


class Word2VecTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='test', email='a@b.com', password='testonly')
        Word2Vec.objects.create(
            word='the',
            vec='-0.038194 -0.24487 0.72812 -0.39961 0.083172 0.043953 -0.39141'
                ' 0.3344 -0.57545 0.087459 0.28787 -0.06731 0.30906 -0.26384 '
                '-0.13231 -0.20757 0.33395 -0.33848 -0.31743 -0.48336 0.1464 '
                '-0.37304 0.34577 0.052041 0.44946 -0.46971 0.02628 -0.54155 '
                '-0.15518 -0.14107 -0.039722 0.28277 0.14393 0.23464 -0.31021 '
                '0.086173 0.20397 0.52624 0.17164 -0.082378 -0.71787 -0.41531 '
                '0.20335 -0.12763 0.41367 0.55187 0.57908 -0.33477 -0.36559 '
                '-0.54857 -0.062892 0.26584 0.30205 0.99775 -0.80481 -3.0243 '
                '0.01254 -0.36942 2.2167 0.72201 -0.24978 0.92136 0.034514 '
                '0.46745 1.1079 -0.19358 -0.074575 0.23353 -0.052062 -0.22044 '
                '0.057162 -0.15806 -0.30798 -0.41625 0.37972 0.15006 -0.53212 '
                '-0.2055 -1.2526 0.071624 0.70565 0.49744 -0.42063 0.26148 '
                '-1.538 -0.30223 -0.073438 -0.28312 0.37104 -0.25217 0.016215 '
                '-0.017099 -0.38984 0.87424 -0.72569 -0.51058 -0.52028 -0.1459 '
                '0.8278 0.27062'
        )
        Word2Vec.objects.create(
            word='of',
            vec='-0.1529 -0.24279 0.89837 0.16996 0.53516 0.48784 -0.58826 '
                '-0.17982 -1.3581 0.42541 0.15377 0.24215 0.13474 0.41193 '
                '0.67043 -0.56418 0.42985 -0.012183 -0.11677 0.31781 '
                '0.054177 -0.054273 0.35516 -0.30241 0.31434 -0.33846 '
                '0.71715 -0.26855 -0.15837 -0.47467 0.051581 -0.33252 0.15003 '
                '-0.1299 -0.54617 -0.37843 0.64261 0.82187 -0.080006 0.078479 '
                '-0.96976 -0.57741 0.56491 -0.39873 -0.057099 0.19743 0.065706 '
                '-0.48092 -0.20125 -0.40834 0.39456 -0.02642 -0.11838 1.012 '
                '-0.53171 -2.7474 -0.042981 -0.74849 1.7574 0.59085 0.04885 '
                '0.78267 0.38497 0.42097 0.67882 0.10337 0.6328 -0.026595 '
                '0.58647 -0.44332 0.33057 -0.12022 -0.55645 0.073611 0.20915 '
                '0.43395 -0.012761 0.089874 -1.7991 0.084808 0.77112 0.63105 '
                '-0.90685 0.60326 -1.7515 0.18596 -0.50687 -0.70203 0.66578 '
                '-0.81304 0.18712 -0.018488 -0.26757 0.727 -0.59363 -0.34839 '
                '-0.56094 -0.591 1.0039 0.20664'
        )

    def test_get_all_word2vec(self):
        response = self.client.get('/v1/words/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data['results'])
        self.assertEqual(data['count'], 2)

    def test_word_search_vec(self):
        response = self.client.get('/v1/words/?word=the')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        print(data['results'])
        self.assertEqual(data['count'], 1)
