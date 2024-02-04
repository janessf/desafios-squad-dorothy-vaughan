import sqlite3

conexao = sqlite3.connect('mercado.bd')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes(id_cliente int primary key, nome_cliente varchar(100), telefone_cliente int, endereco_cliente varchar(100))')
cursor.execute('CREATE TABLE produtos(id_produto int primary key, nome_produto varchar(100), categoria_produto varchar(50), qtde_produto int, valor_produto money, fornecedor_produto varchar(100))')
cursor.execute('CREATE TABLE transacoes(id_transacao int primary key, dt_compra DATE, qtde_comprada int,  id_cliente int, FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente))')


cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (1, "Ana", 12344321, "rua flores") ')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (2, "Maite", 12344377, "rua jardim")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (3, "Simone", 34544321, "rua rosas")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (4, "Jane", 12355321, "rua margaridas")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (5, "Isadora", 12346661, "rua tulipa")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (1, "sabao limpinho", "limpeza", 10, 5.00, "triex")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (2, "arroz", "mercado", 18, 15.00, "camil")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (3, "arroz", "mercado", 10, 18.00, "panela de ferro")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (4, "bolacha piraque", "biscoitos", 13, 4.50, "piraque")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (5, "coca cola", "bebidas", 15, 9.00, "ambev")')
cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (1, "2024-01-01", 1, 1)')
cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (2, "2024-02-01", 3, 4)')
cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (3, "2024-01-14", 4, 5)')
cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (4, "2024-02-02", 2, 2)')


conexao.commit()
conexao.close()

