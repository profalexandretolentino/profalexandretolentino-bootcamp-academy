let contaBancaria = {
    titular: "Mariana Silva",
    saldo: 500.00,

    depositar: function(valor) {
        this.saldo += valor;
        console.log("Depósito de R$ " + valor + " realizado. Novo saldo: R$ " + this.saldo);
    },

    sacar: function(valor) {
        if (this.saldo >= valor) {
            this.saldo -= valor;
            console.log("Saque de R$ " + valor + " realizado. Novo saldo: R$ " + this.saldo);
        } else {
            console.log("Saldo insuficiente para o saque de R$ " + valor + ". Saldo atual: R$ " + this.saldo);
        }
    }
};

// Teste
contaBancaria.depositar(200); //Depositou 200
contaBancaria.sacar(1000); // Saldo insuficiente
contaBancaria.sacar(300);  // Sucesso