// Classe base para os carros
class Carro {
    constructor(nome) {
        this.nome = nome;
        this.velocidade = 0;
    }

    acelerar(valor) {
        this.velocidade += valor;
        console.log(`${this.nome} acelerou para ${this.velocidade} km/h`);
    }

    frear(valor) {
        this.velocidade -= valor;

        if (this.velocidade < 0) {
            this.velocidade = 0;
        }

        console.log(`${this.nome} reduziu para ${this.velocidade} km/h`);
    }

    penalidade(valor) {
        this.velocidade -= valor;

        if (this.velocidade < 0) {
            this.velocidade = 0;
        }

        console.log(
            `${this.nome} recebeu penalidade e ficou com ${this.velocidade} km/h`
        );
    }

    exibirStatus() {
        console.log(`${this.nome}: ${this.velocidade} km/h`);
    }
}

// Instâncias
const ferrari = new Carro("Ferrari");
const mclaren = new Carro("McLaren");
const porsche = new Carro("Porsche");

// Simulação da corrida
ferrari.acelerar(100);
ferrari.acelerar(50);
ferrari.frear(30);

mclaren.acelerar(120);
mclaren.penalidade(20);

porsche.acelerar(90);
porsche.acelerar(40);
porsche.penalidade(15);
porsche.frear(25);

// Resultado final
console.log("\n=== STATUS FINAL ===");
ferrari.exibirStatus();
mclaren.exibirStatus();
porsche.exibirStatus();


console.log(porsche instanceof Carro)