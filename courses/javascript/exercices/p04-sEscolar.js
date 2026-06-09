/*
====================================================
P04 - Sistema Escolar
JavaScript Essentials 2

Conceitos utilizados:

- Classes
- Constructor
- Herança
- extends
- super
- Getter
- Setter
- Encapsulamento
- Override
====================================================
*/

// =====================================
// CLASSE PAI
// =====================================

class Pessoa {

    constructor(nome, cpf) {

        this.nome = nome;
        this.cpf = cpf;

    }

    apresentar() {

        console.log(
            `Olá, meu nome é ${this.nome}.`
        );

    }

}

// =====================================
// CLASSE ALUNO
// =====================================

class Aluno extends Pessoa {

    constructor(nome, cpf, curso, nota) {

        // chama o constructor da classe pai
        super(nome, cpf);

        this.curso = curso;

        // passa pelo setter
        this.nota = nota;

    }

    // getter
    get nota() {

        return this._nota;

    }

    // setter
    set nota(valor) {

        if (valor < 0 || valor > 10) {

            console.log(
                "Nota inválida!"
            );

            return;

        }

        this._nota = valor;

    }

    verificarSituacao() {

        if (this._nota >= 6) {

            console.log(
                `${this.nome} está APROVADO.`
            );

        } else {

            console.log(
                `${this.nome} está REPROVADO.`
            );

        }

    }

    // override
    apresentar() {

        console.log(
            `Olá, meu nome é ${this.nome} e sou aluno do curso ${this.curso}.`
        );

    }

}

// =====================================
// CLASSE PROFESSOR
// =====================================

class Professor extends Pessoa {

    constructor(nome, cpf, disciplina) {

        super(nome, cpf);

        this.disciplina = disciplina;

    }

    // override
    apresentar() {

        console.log(
            `Olá, meu nome é ${this.nome} e sou professor da disciplina ${this.disciplina}.`
        );

    }

}

// =====================================
// CRIANDO ALUNOS
// =====================================

const aluno1 = new Aluno(
    "Lucas",
    "123.456.789-00",
    "Desenvolvimento de Sistemas",
    8
);

const aluno2 = new Aluno(
    "Maria",
    "987.654.321-00",
    "Redes de Computadores",
    9
);

// =====================================
// CRIANDO PROFESSORES
// =====================================

const professor1 = new Professor(
    "Ana",
    "111.111.111-11",
    "Banco de Dados"
);

const professor2 = new Professor(
    "Carlos",
    "222.222.222-22",
    "Programação Web"
);

// =====================================
// TESTE 1 - APRESENTAÇÃO
// =====================================

console.log("\n=== APRESENTAÇÃO ===");

aluno1.apresentar();
aluno2.apresentar();

professor1.apresentar();
professor2.apresentar();

// =====================================
// TESTE 2 - GETTER
// =====================================

console.log("\n=== CONSULTANDO NOTAS ===");

console.log(
    `${aluno1.nome}: ${aluno1.nota}`
);

console.log(
    `${aluno2.nome}: ${aluno2.nota}`
);

// =====================================
// TESTE 3 - SETTER
// =====================================

console.log("\n=== ALTERANDO NOTA ===");

aluno1.nota = 10;

console.log(
    `${aluno1.nome}: ${aluno1.nota}`
);

// =====================================
// TESTE 4 - VALIDAÇÃO
// =====================================

console.log("\n=== TESTE DE VALIDAÇÃO ===");

aluno1.nota = 20;
aluno2.nota = -5;

// =====================================
// TESTE 5 - SITUAÇÃO
// =====================================

console.log("\n=== SITUAÇÃO DOS ALUNOS ===");

aluno1.verificarSituacao();
aluno2.verificarSituacao();

// =====================================
// TESTE 6 - INSTANCEOF
// =====================================

console.log("\n=== INSTANCEOF ===");

console.log(
    aluno1 instanceof Aluno
);

console.log(
    professor1 instanceof Professor
);

console.log(
    aluno1 instanceof Pessoa
);

console.log(
    professor1 instanceof Pessoa
);

// =====================================
// RELATÓRIO FINAL
// =====================================

console.log("\n=== RELATÓRIO FINAL ===");

console.log(
    `Aluno: ${aluno1.nome} | Curso: ${aluno1.curso} | Nota: ${aluno1.nota}`
);

console.log(
    `Aluno: ${aluno2.nome} | Curso: ${aluno2.curso} | Nota: ${aluno2.nota}`
);

console.log(
    `Professor: ${professor1.nome} | Disciplina: ${professor1.disciplina}`
);

console.log(
    `Professor: ${professor2.nome} | Disciplina: ${professor2.disciplina}`
);