from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_doc):
        if file_doc.endswith(".json"):
            with open(file_doc, "r", encoding="utf8") as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
