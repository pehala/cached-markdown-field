import pytest

from test_app.forms import DescriptionForm
from test_app.models import VerboseNameAndHelpDescription


@pytest.fixture(scope="function")
def existing_entity(db):
    entity = VerboseNameAndHelpDescription(description_markdown="test")
    entity.save()
    return entity


@pytest.mark.django_db
def test_create_form_caching():
    form = DescriptionForm({
        "description_markdown": "dummy",
        "name": "name"
    })
    model = form.save()
    assert model.description == "<p>dummy</p>"


@pytest.mark.django_db
def test_dynamic_caching(use_runtime_cache):
    entity = VerboseNameAndHelpDescription(description_markdown="test")
    entity.save()
    assert entity.description == "<p>test</p>"


@pytest.mark.django_db
def test_no_caching(no_cache):
    entity = VerboseNameAndHelpDescription(description_markdown="test", description_cached="dummy")
    assert entity.description_cached == "dummy"
    entity.save()
    assert entity.description == "<p>test</p>"


@pytest.mark.django_db
def test_dynamic_caching_disabled():
    with pytest.raises(ValueError):
        entity = VerboseNameAndHelpDescription(description_markdown="test")
        entity.save()
        assert entity.description == "<p>test</p>"


@pytest.mark.django_db
def test_update_caching(existing_entity):
    form = DescriptionForm(instance=existing_entity, data={"description_markdown": "dummy_test"})
    model = form.save()
    assert model.description == "<p>dummy_test</p>"
    assert existing_entity.description == "<p>dummy_test</p>"
