import os
from weasyprint import HTML

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_final_html(template_content, main_content):
    return template_content.replace('<!--CONTENT_PLACEHOLDER-->', main_content)

base_dir = os.path.dirname(os.path.abspath(__file__))
pages = [
        ('en/tp-cheatsheet-suko-index.html', 'en/tp-cheatsheet-suko-index-2pg.html', '../output/en/tp-cheatsheet-suko-2pg.pdf'),
        ('en/tp-cheatsheet-suko-index.html', 'en/tp-cheatsheet-suko-index-4pg.html', '../output/en/tp-cheatsheet-suko-4pg.pdf'),
        ('pl/tp-cheatsheet-suko-index.html', 'pl/tp-cheatsheet-suko-index-2pg.html', '../output/pl/tp-cheatsheet-suko-2pg.pdf'),
        ('pl/tp-cheatsheet-suko-index.html', 'pl/tp-cheatsheet-suko-index-4pg.html', '../output/pl/tp-cheatsheet-suko-4pg.pdf'),
        ]

for main_content_file, template_path, output_pdf in pages:
    main_content = read_file(main_content_file)
    template_content = read_file(template_path)
    final_html_content = create_final_html(template_content, main_content)
    HTML(string=final_html_content, base_url=base_dir).write_pdf(output_pdf)
    print(output_pdf + ' done')
