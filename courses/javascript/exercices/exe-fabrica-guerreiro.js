// =========================================================================
// PADRÃO A: FACTORY FUNCTION (Função Fábrica)
// =========================================================================
function criarGuerreiro(nomeItem, forcaItem) {
    return {
        nome: nomeItem,
        forca: forcaItem,
        atacar: function() {
            console.log(this.nome + " ataca com força de " + this.forca + "!");
        }
    };
}

// Criando Instâncias via Fábrica:
let guerreiro1 = criarGuerreiro("Thorin", 85); 
let guerreiro2 = criarGuerreiro("Aragorn", 90);


// =========================================================================
// PADRÃO B: CONSTRUCTOR FUNCTION (Função Construtora) - Letra Maiúscula!
// =========================================================================
function Arqueiro(nomeItem, precisaoItem) {
    // O 'this' molda o objeto que está nascendo através do operador 'new'
    this.nome = nomeItem;
    this.precisao = precisaoItem;
    this.flechas = 5; // Toda instância já nasce com 5 flechas por padrão
    
    this.atirarFlecha = function() {
        if (this.flechas > 0) {
            this.flechas--;
            console.log(this.nome + " disparou uma flecha com precisão de " + this.precisao + "%! Flechas restantes: " + this.flechas);
        } else {
            console.log(this.nome + " está sem flechas no aljava!");
        }
    };
}

// Criando Instâncias via Construtor (Uso obrigatório do 'new'):
let arqueiro1 = new Arqueiro("Legolas", 98);
let arqueiro2 = new Arqueiro("Robin Hood", 95);


// =========================================================================
// TESTANDO AS INSTÂNCIAS NO CONSOLE
// =========================================================================
guerreiro1.atacar();

arqueiro1.atirarFlecha(); // Legolas dispara e fica com 4 flechas
arqueiro1.atirarFlecha(); // Legolas dispara e fica com 3 flechas
arqueiro2.atirarFlecha(); // Robin Hood dispara e fica com 4 flechas (o estado de um não afeta o outro!)

console.log(guerreiro1); // Objeto comum {...}
console.log(arqueiro1);  // Arqueiro { nome: 'Legolas', precisao: 98, flechas: 3 }