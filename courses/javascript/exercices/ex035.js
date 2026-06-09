class ProdutoEcom {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }

    aplicarDesconto(valorDesconto) {
        this.preco -= valorDesconto;
    }
}

// PONTO CHAVE: Armazenando instâncias diretamente dentro de um Array
var carrinhoDeCompras = [
    new ProdutoEcom("Mouse Gamer", 150),
    new ProdutoEcom("Teclado Mecânico", 250),
    new ProdutoEcom("Headset USB", 200)
];

// Varrendo a lista de objetos utilizando o forEach
carrinhoDeCompras.forEach(function(produto) {
    produto.aplicarDesconto(5); // Aplica a lógica em cada objeto individualmente
    console.log("Produto: " + produto.nome + " | Novo Preço: R$ " + produto.preco);
});