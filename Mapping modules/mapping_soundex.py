# -*- coding: utf-8 -*-
import sys
import ngram
import silpa_common
import unidecode
#sys.path.append('/Library/Python/2.7/site-packages/soundex')
import soundex

a = 'ఆదియందు'
b = 'ಆದಿಯಲ್ಲಿ'

#print soundex.compare(a,b)

#soundex.Soundex.silpaService = soundex.getInstance()

#print silpaService.Soundex.compare(a,b)

import unittest
from soundex import getInstance

silpaService = getInstance()

print silpaService.soundex(u'ఆదియందు')
print silpaService.soundex(u'ಆದಿಯಲ್ಲಿ')
print silpaService.soundex(u'దేవుడు')
print silpaService.soundex(u'ದೇವರು')
print silpaService.compare(u'ఆదియందు',u'ಆದಿಯಲ್ಲಿ')
print ngram.NGram.compare(u'ఆదియందు',u'ಆದಿಯಲ್ಲಿ')
print ngram.NGram.compare(u'దేవుడు',u'ದೇವರು',N=1)
print ngram.NGram.compare('span','spam')



# G = ngram.NGram([u'దేవుడు',u'దేవత',u'వేలుపు'])
# #print G.find(u'ದೇವರು')
# s1 = []
# s2 = []
# #print u'దేవుడు'.encode('ascii', 'ignore')
# #print u'ದೇವರು'.replace(u'ದೇವರು', u'\'').encode('ascii','ignore')
#
#
# s1.append( unidecode.unidecode(u'ದೇವರು'))
# s2.append( unidecode.unidecode(u'దేవుడు'))
# s2.append( unidecode.unidecode(u'దేవత'))
# s2.append( unidecode.unidecode(u'వేలుపు'))
#
# tel = ngram.NGram(s2)
# print tel.find(s1[0])




# class SoundexTest(unittest.TestCase):
#     def setUp(self):
#         self.s = getInstance()
#
#     def test_soundex(self):
#         '''TEST: Soundex calculation'''
#         self.assertEqual(self.s.soundex('vasudev'), 'v231')
#         self.assertEqual(self.s.soundex('Rupert'), 'R163')
#         self.assertEqual(self.s.soundex(u'ಬೆಂಗಳೂರು'), u'ಬDNFQCPC')
#         self.assertEqual(self.s.soundex(u'आम्र् फल्'), u'आNPMQ000')
#
#     def test_compare(self):
#         '''TEST: Soundex Comparison'''
#         self.assertEqual(self.s.compare('Bangalore', u'ಬೆಂಗಳೂರು'), -1)
#         self.assertEqual(self.s.compare(u'ಬೆಂಗಳೂರು', u'बॆंगळूरु'), 1)
#         self.assertEqual(self.s.compare(u'बॆंगळूरु', u'बॆंगळूरु'), 0)
#         self.assertEqual(self.s.compare(u'बॆंगळूरु', u'आम्र् फल्'), 2)

