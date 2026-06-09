// 1. DECLARAÇÃO DO OBJETO (Criação da estrutura)
var guerreiro = {
    // Propriedades (Dados/Atributos)
    nome: "Thorin",
    vida: 100,
    escudoAtivo: true,
    xp: 0,

    // Métodos (Comportamentos/Ações)
    
    // Método 1: Exibe informações lendo propriedades com 'this'
    exibirStatus: function() {
        console.log("--------------------------------------");
        console.log("HERÓI: " + this.nome);
        console.log("VIDA ATUAL: " + this.vida + " HP");
        console.log("ESCUDO ATIVO: " + (this.escudoAtivo ? "Sim" : "Não"));
        console.log("EXPERIÊNCIA: " + this.xp + " XP");
        console.log("--------------------------------------");
    },

    // Método 2: Modifica uma propriedade diretamente
    ganharXp: function(pontos) {
        console.log("✨ " + this.nome + " ganhou " + pontos + " de experiência!");
        this.xp += pontos; // Altera o valor interno da propriedade xp
    },

    // Método 3: Possui uma tomada de decisão (Lógica Condicional com 'this')
    receberDano: function(quantidadeDano) {
        console.log("💥 " + this.nome + " foi atacado! Dano recebido: " + quantidadeDano);

        // Se o escudo estiver ativo, o dano é reduzido pela metade
        if (this.escudoAtivo === true) {
            console.log("🛡️ O escudo absorveu metade do impacto!");
            this.vida -= (quantidadeDano / 2);
        } else {
            this.vida -= quantidadeDano;
        }

        // Validação extra: A vida não pode ser menor que zero
        if (this.vida < 0) {
            this.vida = 0;
            console.log("💀 " + this.nome + " foi derrotado...");
        }
    }
};

// ==========================================
// 2. EXECUÇÃO PASSO A PASSO (A "Historinha" do Código)
// ==========================================

// Passo A: Ver o estado inicial do guerreiro
guerreiro.exibirStatus();

// Passo B: O guerreiro treina e ganha experiência (Uso de parâmetros)
guerreiro.ganharXp(50);
guerreiro.ganharXp(30);

// Passo C: O guerreiro é atacado enquanto o escudo está ligado
guerreiro.receberDano(40); // Deve tirar apenas 20 de vida


// Passo D: Desligamos o escudo (CRUD - Update de propriedade fora do objeto)
guerreiro.escudoAtivo = false; 
guerreiro.exibirStatus();

// Passo E: Novo ataque sem escudo
guerreiro.receberDano(50); // Deve tirar 50 de vida cheio
guerreiro.exibirStatus();