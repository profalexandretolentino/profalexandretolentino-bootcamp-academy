class Corrida {
    // O constructor é o primeiro método executado quando fazemos o 'new'
    constructor(passageiro, distanciaKm, tarifaPorKm) {
        this.passageiro = passageiro;
        this.distanciaKm = distanciaKm;
        this.tarifaPorKm = tarifaPorKm;
    }

    // Método focado puramente em processar e retornar um dado
    calcularValorTotal() {
        return this.distanciaKm * this.tarifaPorKm;
    }

    finalizarCorrida() {
        // PONTO CHAVE: Usamos o 'this.' para chamar um método de dentro da própria classe
        var valorFinal = this.calcularValorTotal();
        console.log("Corrida finalizada! Passageiro: " + this.passageiro + ". Valor a pagar: R$ " + valorFinal.toFixed(2));
    }
}

// Execução do Teste (Instanciação)
var minhaCorrida = new Corrida("Mateus", 12, 2.50);
minhaCorrida.finalizarCorrida(); // Saída: Valor a pagar: R$ 30.00