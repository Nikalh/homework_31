import pytest

from ads.serializer import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def ads_list_test(client, access_token):
    ad_list = AdFactory.create_batch(5)

    response = client.get("/ad/",HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }