import re
from pypdf import PdfReader
from utils import generate_response
from freelancer.prompts import get_profile_fields_extraction_prompt

class ResumeReader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)
        self.content = None
        self.fields = ['Name', 'Email', 'Phone Number', 'Date of Birth', 'Education', 'Skills', 
                       'Experience', 'Designation']

    def extract_text_from_pdf(self):
        content = []
        for page in self.reader.pages:
            content.append(page.extract_text())

        self.content = '\n'.join(content)#.replace('\n', ' ')
        print(self.content)

    def _parse_raw_fields(self, text):
        # parse fields from text
        fields = {}
        for field in self.fields:
            match = re.search(f"{field}:(.*)", text, re.IGNORECASE)
            if match:
                fields[field] = match.group(1).strip()
            else:
                fields[field] = None

        return fields

    def get_fields(self):
        # extract fields from text
        prompts = get_profile_fields_extraction_prompt(self.content, self.fields)
        response = generate_response(prompts['system_prompt'], prompts['user_prompt'])
        print(response)
        extracted_fields = self._parse_raw_fields(response)
        return extracted_fields
