// Classe de gerenciamento de produtos
class Produto {

    constructor() {

        // Array dos produtos
        this["listaProdutos"] = [];
    }

    // CREATE
    cadastrarProduto(id, nome, preco, estoque) {

        // Objeto produto
        let produto = {
            "id": id,
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        };

        // Adiciona no array
        this["listaProdutos"]["push"](produto);

        console["log"]("Produto cadastrado!");
    }

    // READ
    listarProdutos() {

        console["log"]("LISTA DE PRODUTOS:");

        this["listaProdutos"]["forEach"](function(produto) {

            console["log"](produto);

        });
    }

    // UPDATE
    atualizarEstoque(id, novoEstoque) {

        this["listaProdutos"]["forEach"](function(produto) {

            // Procura pelo ID
            if(produto["id"] === id) {

                // Atualiza estoque
                produto["estoque"] = novoEstoque;

                console["log"]("Estoque atualizado!");
            }
        });
    }

    // DELETE
    excluirProduto(id) {

        this["listaProdutos"] =
        this["listaProdutos"]["filter"](function(produto) {

            return produto["id"] !== id;
        });

        console["log"]("Produto removido!");
    }
}


// Instanciando objeto
let loja = new Produto();


// CREATE
loja["cadastrarProduto"](
    1,
    "Notebook Gamer",
    4500,
    10
);

loja["cadastrarProduto"](
    2,
    "Mouse Sem Fio",
    120,
    50
);


// READ
loja["listarProdutos"]();


// UPDATE
loja["atualizarEstoque"](
    2,
    35
);


// READ novamente
loja["listarProdutos"]();


// DELETE
loja["excluirProduto"](1);


// READ final
loja["listarProdutos"]();