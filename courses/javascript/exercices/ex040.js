class InimigoComum {
    constructor(nome, pontosVida) {
        this.nome = nome;
        this.pontosVida = pontosVida;
    }

    receberDano(pontos) {
        this.pontosVida -= pontos;
    }
}

class Chefao extends InimigoComum {
    constructor(nome, pontosVida, escudoAbsorcao) {
        super(nome, pontosVida); // Envia os dados padrão para a classe mãe
        this.escudoAbsorcao = escudoAbsorcao; // Propriedade exclusiva do Chefão
    }

    // PONTO CHAVE (POLIMORFISMO): Sobrescrita do método receberDano
    receberDano(pontos) {
        let danoReal = pontos - this.escudoAbsorcao;
        
        // Se o escudo for maior que o ataque, o dano real não pode ser negativo (curar o chefe)
        if (danoReal < 0) danoReal = 0; 
        
        this.pontosVida -= danoReal;
        console.log(this.nome + " recebeu " + danoReal + " de dano real. Vida restante: " + this.pontosVida);
    }
}

let vilao = new Chefao("Bowser", 500, 20);
vilao.receberDano(60); // O dano seria 60, mas o escudo absorve 20. Vida cai de 500 para 460.