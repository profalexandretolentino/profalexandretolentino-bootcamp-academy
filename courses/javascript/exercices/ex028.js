var personagem = {
    nome: "Arqueiro Verde",
    posicaoX: 0,
    posicaoY: 0,
    estado: "parado",

    andarParaDireita: function() {
        this.posicaoX += 10;
        this.estado = "andando";
    },

    pular: function() {
        this.posicaoY += 5;
        this.estado = "pulando";
    },

    abaixar: function() {
        this.estado = "abaixado";
    },

    resetarPosicao: function() {
        this.posicaoX = 0;
        this.posicaoY = 0;
        this.estado = "parado";
    }
};

// Teste
personagem.andarParaDireita();
personagem.pular();
console.log(personagem); // Mostra o estado atualizado {posicaoX: 10, posicaoY: 5, estado: "pulando"}
personagem.resetarPosicao();

personagem.abaixar();
console.log(personagem);
personagem.resetarPosicao();