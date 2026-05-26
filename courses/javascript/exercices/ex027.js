let carro = {
    modelo: "Ford GT40",
    velocidadeMaxima: 180,
    velocidadeAtual: 0,

    acelerar: function() {
        if (this.velocidadeAtual + 20 <= this.velocidadeMaxima) {
            this.velocidadeAtual += 20;
        } else {
            this.velocidadeAtual = this.velocidadeMaxima;
        }
        console.log("Velocidade atual do carro: " + this.velocidadeAtual + "km/h");
    }
};

let pista = {
    nome: "Interlagos",
    extensaoKm: 4.3,

    verificarSeCarroDisputa: function(objetoCarro) {
        if (objetoCarro.velocidadeMaxima > 150) {
            console.log("O " + objetoCarro.modelo + " está autorizado a correr na pista " + this.nome);
        } else {
            console.log("O " + objetoCarro.modelo + " NÃO tem velocidade suficiente para a pista " + this.nome);
        }
    }
};

// Teste
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
carro.acelerar(); // 20km/h
pista.verificarSeCarroDisputa(carro); // Autorizado