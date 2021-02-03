from docxtpl import DocxTemplate
import yaml

from utils import get_context, get_document_name, print_output_information

with open(r'settings/settings.yaml') as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)

with open(r'input/input.yaml') as file:
    all_docs = yaml.load_all(file, Loader=yaml.FullLoader)
    current_period_data = next(all_docs)


def main():
    doc = DocxTemplate(f'templates/{settings["template_filename"]}.docx')
    context = get_context(settings, current_period_data)
    doc.render(context)
    doc.save(f'output/{context["output_doc_name"]}.docx')
    print_output_information(context)


if __name__ == "__main__":
    main()
