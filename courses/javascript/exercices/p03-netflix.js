// Classe para representar um conteúdo do streaming
class Conteudo {
    constructor(titulo, genero) {
        this.titulo = titulo;
        this.genero = genero;
    }

    reproduzir() {
        console.log(`▶ Reproduzindo: ${this.titulo}`);
    }

    exibirInformacoes() {
        console.log(`Título: ${this.titulo}`);
        console.log(`Gênero: ${this.genero}`);
    }
}

// Instâncias de filmes
const filme1 = new Conteudo("Vingadores: Ultimato", "Ação");
const filme2 = new Conteudo("Toy Story", "Animação");

// Instâncias de séries
const serie1 = new Conteudo("Stranger Things", "Ficção Científica");
const serie2 = new Conteudo("Breaking Bad", "Drama");

// Exibindo conteúdos cadastrados
console.log("=== FILMES ===");
filme1.exibirInformacoes();
filme2.exibirInformacoes();

console.log("\n=== SÉRIES ===");
serie1.exibirInformacoes();
serie2.exibirInformacoes();

// Reproduzindo conteúdos
console.log("\n=== REPRODUÇÃO ===");
filme1.reproduzir();
serie1.reproduzir();

console.log(serie1 instanceof Conteudo)
console.log(filme1 instanceof Conteudo)