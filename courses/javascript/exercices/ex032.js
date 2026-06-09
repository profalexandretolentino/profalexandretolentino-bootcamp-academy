// Constructor Function
function Filme(titulo, duracaoMinutos, genero) {
    this.titulo = titulo;
    this.duracaoMinutos = duracaoMinutos;
    this.genero = genero;
    this.minutosAssistidos = 0;

    this.assistir = function(tempo) {
        this.minutosAssistidos += tempo;

        // Impede que ultrapasse a duração total
        if (this.minutosAssistidos > this.duracaoMinutos) {
            this.minutosAssistidos = this.duracaoMinutos;
        }
    };

    this.exibirProgresso = function() {
        const porcentagem =
            (this.minutosAssistidos * 100) / this.duracaoMinutos;

        console.log(
            `Você já assistiu ${porcentagem.toFixed(2)}% do filme ${this.titulo}.`
        );
    };
}

// Instanciando um filme
const filme1 = new Filme(
    "Vingadores: Ultimato",
    120,
    "Ação"
);

// Assistindo 30 minutos
filme1.assistir(30);
filme1.exibirProgresso();

// Assistindo mais 40 minutos
filme1.assistir(40);
filme1.exibirProgresso();