from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
      id=1,
      nome_do_produto="PlayStation 5",
      nome_da_empresa="Sony",
      data_de_fabricacao="2020-11-12",
      data_de_validade="2030-11-12",
      numero_de_serie="123456",
      instrucoes_de_armazenamento="Não colocar em local úmido",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Playstation 5"
    assert product.nome_da_empresa == "Sony"
    assert product.data_de_fabricacao == "2020-11-12"
    assert product.data_de_validade == "2030-11-12"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "Não colocar em local úmido"
