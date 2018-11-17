from unittest import mock
import unittest
from get_picture import download_image
from unittest.mock import patch

class Test_download_image(unittest.TestCase):
    def test_get_picture(self):
        with patch('requests.get') as mock_request:
            url = 'https://dummyimage.com/600x400/000/fff'
            mock_request.return_value.content = b'picture'
            self.assertEqual(download_image(url), b'picture')
