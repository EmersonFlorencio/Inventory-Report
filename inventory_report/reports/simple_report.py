from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(lista):
        currennt_date = datetime.now().strftime("%Y-%m-%d")
        oldest_date = [date["data_de_fabricacao"] for date in lista]
        expiry_date = [
            date["data_de_validade"]
            for date in lista
            if date["data_de_validade"] > currennt_date
        ]
        companies = [company["nome_da_empresa"] for company in lista]
        company = Counter(companies).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(oldest_date)}\n"
            f"Data de validade mais próxima: {min(expiry_date)}\n"
            f"Empresa com mais produtos: { company}"
        )
