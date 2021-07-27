from django import template
from ..models import Catergory

register = template.Library()

@register.simple_tag
def title():
    return "مرجع خبری مادرید"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "category":Catergory.objects.filter(status=True)
    }