catalogoProdutos = [
  {
    'id': 1,
    'nome': 'Laptop Gamer Nitro 5',
    'categoria': 'Eletrônicos',
    'preco': 5500.00,
    'emEstoque': True
  },
  {
    'id': 2,
    'nome': 'Mouse Logitech G203',
    'categoria': 'Acessórios',
    'preco': 149.90,
    'emEstoque': True
  },
  {
    'id': 3,
    'nome': 'Monitor Curvo Samsung 27',
    'categoria': 'Eletrônicos',
    'preco': 1800.00,
    'emEstoque': False
  },
  {
    'id': 4,
    'nome': 'Cadeira de Escritório Ergonômica',
    'categoria': 'Móveis',
    'preco': 1200.50,
    'emEstoque': True
  },
  {
    'id': 5,
    'nome': 'Teclado Mecânico Redragon',
    'categoria': 'Acessórios',
    'preco': 350.00,
    'emEstoque': True
  },
  {
    'id': 6,
    'nome': 'SSD Kingston 1TB',
    'categoria': 'Eletrônicos',
    'preco': 450.00,
    'emEstoque': False
  },
  {
    'id': 7,
    'nome': 'Webcam Full HD',
    'categoria': 'Acessórios',
    'preco': 280.00,
    'emEstoque': True
  },
  {
    'id': 8,
    'nome': 'Mesa de Escritório em L',
    'categoria': 'Móveis',
    'preco': 799.99,
    'emEstoque': True
  },
  {
    'id': 9,
    'nome': 'Pacote 500 Folhas Sulfite A4',
    'categoria': 'Papelaria',
    'preco': 29.90,
    'emEstoque': True
  },
  {
    'id': 10,
    'nome': 'Kit Canetas Coloridas',
    'categoria': 'Papelaria',
    'preco': 15.50,
    'emEstoque': False
  },
  {
    'id': 11,
    'nome': 'Headset Gamer HyperX',
    'categoria': 'Acessórios',
    'preco': 600.00,
    'emEstoque': True
  }
]

# Listar produtos por categoria
def listarPorCategoria(categoriaDesejada):
    print(f"\nProdutos da categoria '{categoriaDesejada}':")
    produtos = list(filter(lambda p: p['categoria'].lower() == categoriaDesejada.lower(), catalogoProdutos))
    if not produtos:
        print("Nenhum produto encontrado nessa categoria.")
    else:
        for p in produtos:
            print(f"ID: {p['id']}, Nome: {p['nome']}, Preço: R$ {p['preco']:.2f}, Categoria: {p['categoria']}, Em estoque: {p['emEstoque']}")


# Encontrar produto por ID
def encontrarPorId(idDesejado):
    try:
        encontrado = False
        for i, p in enumerate(catalogoProdutos):
            if p['id'] == idDesejado:
                encontrado = True
                print(f"\nProduto encontrado (posição {i}):")
                print(f"ID: {p['id']}, Nome: {p['nome']}, Categoria: {p['categoria']}, Preço: R$ {p['preco']:.2f}, Em estoque: {p['emEstoque']}")
                break
        if not encontrado:
            print(f"\nProduto com ID {idDesejado} não encontrado.")
    except Exception as e:
        print(f"Erro: Ao tentar buscar produto pelo ID. Detalhes: {e}")


# Listar produtos em estoque
def listarProdutosEmEstoque():
    print("\nProdutos em estoque:")
    produtosEmEstoque = list(filter(lambda p: p['emEstoque'], catalogoProdutos))
    for p in produtosEmEstoque:
        print(f"ID: {p['id']}, Nome: {p['nome']}, Preço: R$ {p['preco']:.2f}, Categoria: {p['categoria']}, Em estoque: {p['emEstoque']}")


# Calcular valor total do estoque por categoria
def calcularValorEstoquePorCategoria(categoriaDesejada):
    produtos = list(filter(lambda p: p['categoria'].lower() == categoriaDesejada.lower() and p['emEstoque'], catalogoProdutos))
    total = 0
    for p in produtos:
        total += p['preco']
    print(f"\nO valor total em estoque da categoria '{categoriaDesejada}' é de R$ {total:.2f}")


# Alterar todos os produtos em estoque
def alterarTodosProdutosEmEstoque(valor):
    print(f"\nAlterando todos os produtos para emEstoque = {valor}")
    for p in catalogoProdutos:
        p['emEstoque'] = valor
    for p in catalogoProdutos:
        print(f"ID: {p['id']}, Nome: {p['nome']}, Preço: R$ {p['preco']:.2f}, Categoria: {p['categoria']}, Em estoque: {p['emEstoque']}")


# Gerar relatório de categorias
def gerarRelatorioCategorias():
    print("\nRelatório de Categorias:")
    categorias = list(set([p['categoria'] for p in catalogoProdutos]))
    relatorio = []

    for cat in categorias:
        produtos = list(filter(lambda p: p['categoria'] == cat and p['emEstoque'], catalogoProdutos))
        relatorio.append({
            'categoria': cat,
            'quantidadeTotal': len(produtos)
        })

    for r in relatorio:
        print(f"Categoria: {r['categoria']}, Quantidade em estoque: {r['quantidadeTotal']}")


#  CHAMADAS DE TESTE 
listarPorCategoria("Acessórios")
encontrarPorId(3)
listarProdutosEmEstoque()
calcularValorEstoquePorCategoria("Acessórios")
alterarTodosProdutosEmEstoque(False)
gerarRelatorioCategorias()