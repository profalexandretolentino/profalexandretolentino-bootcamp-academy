class CofreDigital {
    constructor(saldoInicial) {
        this._saldo = saldoInicial;
    }

    get saldo() {
        return this._saldo;
    }

    set saldo(novoValor) {
        // Blindagem contra inserção de dados inválidos (Regra de Negócio)
        if (novoValor < 0) {
            console.log("Operação bloqueada: O saldo não pode ser negativo!");
        } else {
            this._saldo = novoValor;
        }
    }
}

let meuCofre = new CofreDigital(100);
meuCofre.saldo = -50; // Saída: Operação bloqueada...
console.log(meuCofre.saldo); // Saída: 100 (O valor original permaneceu seguro)