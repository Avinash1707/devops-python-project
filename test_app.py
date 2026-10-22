import unittest
from unittest.mock import patch
from io import BytesIO
from app import AppHandler


class TestApp(unittest.TestCase):

    @patch("app.BaseHTTPRequestHandler.send_response")
    @patch("app.BaseHTTPRequestHandler.send_header")
    @patch("app.BaseHTTPRequestHandler.end_headers")
    def test_home_response(self, mock_end, mock_header, mock_response):
        request = AppHandler.__new__(AppHandler)
        request.wfile = BytesIO()

        request.do_GET()

        mock_response.assert_called_once_with(200)
        mock_header.assert_called_once_with(
            "Content-type", "text/plain"
        )
        self.assertEqual(
            request.wfile.getvalue(),
            b"Hello! My first DevOps project is running."
        )


if __name__ == "__main__":
    unittest.main()