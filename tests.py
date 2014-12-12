import echoprint
import simplejson
import unittest

class EchoprintTest(unittest.TestCase):
    """Test EchoPrint code"""

    def test_codegen(self):
        d = echoprint.codegen(simplejson.load(open('test_data.json')))
        self.assertEqual(d['code'], 'eJyd0juuQyEMRdEp2cbYZjjgz_yHEKrHy1VCkWYVW0I6CAAAFX6G4sb9LMMNtBtMN3q_cV_V2g2U32n0FUusWpTsn0h1NukQooQjImzVPwiSn-0PlsIm1pe33K9S06QOOgjw0Q7YNMEEW7U1vRvGhMzBqmpTi2B23KNkjBg83YEOblrz0Q5WwV5jmWUsXct65YES9_T3dsC-ryO8mnwCPfZ2qsC2_1F6H2QH7jzw0Q4vGHW94A==')
        self.assertEqual(d['version'], 4.12)

