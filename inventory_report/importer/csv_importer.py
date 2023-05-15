from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_doc):
        if file_doc.endswith(".csv"):
            with open(file_doc, "r", encoding="utf8") as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        else:
            raise ValueError("Arquivo inválido")
