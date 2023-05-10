from inventory_report.inventory.product import Product


def test_cria_produto():
    mock_id = 1,
    mock_nome_do_produto = "PlayStation 5",
    mock_nome_da_empresa = "Sony",
    mock_data_de_fabricacao = "2020-11-12",
    mock_data_de_validade = "2030-11-12",
    mock_numero_de_serie = "123456",
    mock_instrucoes_de_armazenamento = "Não colocar em local úmido",

    product = Product(
        mock_id,
        mock_nome_do_produto,
        mock_nome_da_empresa,
        mock_data_de_fabricacao,
        mock_data_de_validade,
        mock_numero_de_serie,
        mock_instrucoes_de_armazenamento
    )

    assert product.id == 1
    assert product.nome_do_produto == "Playstation 5"
    assert product.nome_da_empresa == "Sony"
    assert product.data_de_fabricacao == "2020-11-12"
    assert product.data_de_validade == "2030-11-12"
    assert product.numero_de_serie == "123456"
    assert product.instrucoes_de_armazenamento == "Não colocar em local úmido"
