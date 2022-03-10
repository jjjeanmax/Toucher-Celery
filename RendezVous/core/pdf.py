from io import BytesIO

from django.template.loader import get_template
from django.conf import settings

from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    file_name = "Talon_%s" % ("Pour_") + context_dict['username']
    try:
        with open(str(settings.BASE_DIR)+ f"/media/pdf/{file_name}.pdf", "wb+") as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), output)
    except Exception as e:
        print(e)
    if not pdf.err:
        return file_name, True
    return '', False
