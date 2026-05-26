let produto = {
    nome: "Teclado Mecânico RGB",
    preco: 250.00,
    emEstoque: true,

    exibirDetalhes: function() {
        console.log("O produto " + this.nome + " custa R$ " + this.preco);
    },

    alterarPreco: function(novoPreco) {
        this.preco = novoPreco;
    }
};

// Teste
produto.exibirDetalhes(); // O produto Teclado Mecânico RGB custa R$ 250
produto.alterarPreco(229.90);
//produto.exibirDetalhes(); // O produto Teclado Mecânico RGB custa R$ 229.9