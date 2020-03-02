import markdown
from django import template
from django.template.defaultfilters import stringfilter
from pygments.formatters import HtmlFormatter

register = template.Library()

@stringfilter
@register.filter(name='markdown', is_safe=True)
def markdown_to_html(value):
    md_template_string = markdown.markdown(value, extensions=['extra', 'codehilite'])
    return md_template_string
    # formatter = HtmlFormatter(style="tango",full=True,cssclass="codehilite")
    # css_string = formatter.get_style_defs()
    # md_css_string = "<style>" + css_string + "</style>"
    
    # md_template = md_css_string + md_template_string
    # return md_template


# register.filter('markdown', markdown_to_html)