from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


class Inventory:
    @staticmethod
    def read_file(file_doc):
        if file_doc.endswith(".csv"):
            data = CsvImporter.import_data(file_doc)
        if file_doc.endswith(".json"):
            data = JsonImporter.import_data(file_doc)
        return data

    @staticmethod
    def import_data(file_doc, type_report):
        data = Inventory.read_file(file_doc)

        if type_report == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
