import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_doc):
        if file_doc.endswith(".xml"):
            root = ET.parse(file_doc).getroot()
            data = []
            for element in root:
                content = {}
                for item in element:
                    content[item.tag] = item.text
                data.append(content)
            return data
        else:
            raise ValueError("Arquivo inválido")
