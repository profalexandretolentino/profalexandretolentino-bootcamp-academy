// Classe Base (Mãe ou Superclasse)
class Soldado {
    constructor(nome, forca) {
        this.nome = nome;
        this.forca = forca;
    }

    mover() {
        console.log(this.nome + " marchou para frente!");
    }
}

// Classe Derivada (Filha ou Subclasse)
class Arqueiro extends Soldado {
    constructor(nome, forca) {
        // PONTO DE ATENÇÃO DO NETACAD: super() chama o construtor da classe mãe obrigatoriamente
        super(nome, forca); 
    }

    atirarFlecha() {
        console.log(this.nome + " disparou uma flecha causando " + this.forca + " de dano!");
    }
}

let legolas = new Arqueiro("Legolas", 75);
legolas.mover();        // Método herdado da classe Soldado
legolas.atirarFlecha(); // Método exclusivo da classe Arqueiro