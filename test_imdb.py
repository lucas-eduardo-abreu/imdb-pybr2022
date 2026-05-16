from unittest.mock import patch, MagicMock
import pytest
from imdb import MeuRobo

MOCK_HTML = """
<html><body>
<ul>
  <li class="ipc-metadata-list-summary-item">
    <h3 class="ipc-title__text">1. The Shawshank Redemption</h3>
    <span class="cli-title-metadata-item">1994</span>
  </li>
  <li class="ipc-metadata-list-summary-item">
    <h3 class="ipc-title__text">2. The Godfather</h3>
    <span class="cli-title-metadata-item">1972</span>
  </li>
</ul>
</body></html>
"""


def _mock_response(html=MOCK_HTML, status=200):
    mock = MagicMock()
    mock.status_code = status
    mock.content = html.encode()
    mock.raise_for_status = MagicMock()
    return mock


@patch('imdb.requests.get')
def test_returns_list_of_films(mock_get):
    mock_get.return_value = _mock_response()
    filmes = MeuRobo().get_site()
    assert len(filmes) == 2
    assert filmes[0] == {'Nome do Filme': 'The Shawshank Redemption', 'Ano': '1994'}
    assert filmes[1] == {'Nome do Filme': 'The Godfather', 'Ano': '1972'}


@patch('imdb.requests.get')
def test_strips_rank_prefix(mock_get):
    mock_get.return_value = _mock_response()
    filmes = MeuRobo().get_site()
    for filme in filmes:
        assert not filme['Nome do Filme'][0].isdigit()


@patch('imdb.requests.get')
def test_raises_on_http_error(mock_get):
    mock = _mock_response(status=503)
    mock.raise_for_status.side_effect = Exception('503 Server Error')
    mock_get.return_value = mock
    with pytest.raises(Exception, match='503'):
        MeuRobo().get_site()
