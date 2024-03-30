import pytest
from graphene.test import Client

from context import get_context
from schema import schema


@pytest.fixture
def context_fixture():
    yield get_context()


def test_get_places(context_fixture):
    query = """
        {
          places {
            latitude
            longitude
            description
            city
            locality
          }
        }
    """
    client = Client(schema, context_value=context_fixture)
    executed = client.execute(query)
    assert isinstance(executed, dict)

    places = executed["data"]["places"]
    assert len(places) == 6

    place = places[0]
    assert place["latitude"] == 58.0081
    assert place["longitude"] == 56.249
    assert place["description"] == "Супер место!"
    assert place["city"] == "Perm"
    assert place["locality"] == "Sverdlovsky City District"


def test_places_with_country_and_news(context_fixture):
    query = """
        {
          places {
            description
            city
            country {
              name
              alpha2code
              capital
            }
            news {
              title
            }
          }
        }
    """
    client = Client(schema, context_value=context_fixture)
    executed = client.execute(query)
    assert isinstance(executed, dict)

    places = executed["data"]["places"]
    assert len(places) == 6

    place = places[0]
    # проверка, что не пришло то, что не заказывали
    assert place.get("latitude", None) is None
    assert place.get("longitude", None) is None
    assert place["description"] == "Супер место!"
    assert place["city"] == "Perm"

    country = place["country"]
    assert country["name"] == "Russian Federation"
    assert country["capital"] == "Moscow"
    assert country["alpha2code"] == "RU"


def test_place_with_country_and_news(context_fixture):
    query = """
    {
      place(placeId: 57) {
        description
        city
        locality
        country {
          name
          capital
          alpha2code
        }
        news {
          author
          title
          description
          url
          publishedAt
        }
      }
    }
    """

    client = Client(schema, context_value=context_fixture)
    executed = client.execute(query)
    assert isinstance(executed, dict)

    place = executed["data"]["place"]
    assert len(place) == 5

    assert place["description"] == "Графтон-стрит."
    assert place["city"] == "Dublin"
    assert place["locality"] == "Portobello"
    # проверка, что не пришло то, что не заказывали
    assert place.get("latitude", None) is None
    assert place.get("longitude", None) is None

    country = place["country"]
    assert country["name"] == "Ireland"
    assert country["capital"] == "Dublin"
    assert country["alpha2code"] == "IE"

    news = place["news"]
    assert len(news) == 3
    assert (
        news[0]["title"]
        == "Sunak tells Stormont leaders 'real work starts now' - RTE.ie"
    )
    assert (
        news[1]["title"]
        == "Cern aims to build €20bn atom-smasher to unlock secrets of universe - The Guardian"
    )
    assert (
        news[2]["title"]
        == "Dad's Army star Ian Lavender has died at the age of 77 - RTE.ie"
    )