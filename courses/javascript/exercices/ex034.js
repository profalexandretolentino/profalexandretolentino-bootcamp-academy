class Estudante {
    constructor(nome, curso, modulosConcluidos) {
        this.nome = nome;
        this.curso = curso;
        this.modulosConcluidos = modulosConcluidos;
    }

    // Método modificador de estado interno
    avancarModulo() {
        this.modulosConcluidos += 1; // Incrementa a propriedade do próprio objeto
    }

    exibirPerfil() {
        console.log("O estudante " + this.nome + " está no curso " + this.curso + " e já concluiu " + this.modulosConcluidos + " módulos.");
    }
}

// Execução do Teste
var aluno1 = new Estudante("Carlos", "Dev de Sistemas", 2);
aluno1.avancarModulo();
aluno1.exibirPerfil(); // Saída: ... já concluiu 3 módulos.