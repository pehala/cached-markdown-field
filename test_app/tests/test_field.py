from test_app.forms import DescriptionForm
from test_app.models import NameAndDescription, VerboseNameAndHelpDescription


def test_fields_exists():
    get_field = NameAndDescription._meta.get_field
    get_field('name')
    get_field('description_markdown')
    get_field('description_cached')


def test_verbose_name_and_help_text():
    get_field = VerboseNameAndHelpDescription._meta.get_field
    markdown = get_field('description_markdown')
    assert markdown.verbose_name == "Description"
    assert markdown.help_text == "This should help you"


def test_form():
    form = DescriptionForm()
    assert "description_markdown" in form.fields
    assert "description_cached" not in form.fields
