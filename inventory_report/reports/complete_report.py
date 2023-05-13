from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista):
        report = SimpleReport.generate(lista)
        report += "\nProdutos estocados por empresa:\n"
        companies = Counter(item["nome_da_empresa"] for item in lista)

        for product in companies.items():
            report += f"- {product[0]}: {product[1]}\n"

        return report
