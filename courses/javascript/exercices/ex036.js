class Servidor {
    constructor(ip) {
        this.ip = ip;
        this.status = "online"; // Propriedade com valor inicial padrão (estático)
    }

    desligar() {
        this.status = "offline";
    }
}

var dataCenter = [
    new Servidor("192.168.0.1"),
    new Servidor("192.168.0.2"),
    new Servidor("192.168.0.3")
];

// Varrendo a lista utilizando o laço 'for' tradicional
for (var i = 0; i < dataCenter.length; i++) {
    dataCenter[i].desligar(); // Acessa o objeto pelo índice e roda o método
}

console.log(dataCenter); // Comprova que todos os status mudaram para "offline"