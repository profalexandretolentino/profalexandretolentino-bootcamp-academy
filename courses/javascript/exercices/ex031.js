// Função Construtora para os carros
function CarroSuper(modelo, categoria, potenciaCavalos) {
    this.modelo = modelo;
    this.categoria = categoria;
    this.potenciaCavalos = potenciaCavalos;
}

// Função Construtora para os circuitos
function Circuito(nomePista, categoriaExigida) {
    this.nomePista = nomePista;
    this.categoriaExigida = categoriaExigida;

    this.testarCarro = function(carro) {
        if (carro.categoria === this.categoriaExigida) {
            console.log(
                `O carro ${carro.modelo} foi aprovado para correr no circuito ${this.nomePista}!`
            );
        } else {
            console.log(
                `Acesso negado. O circuito ${this.nomePista} exige carros da categoria ${this.categoriaExigida}.`
            );
        }
    };
}

// Instanciando a pista
const interlagos = new Circuito("Interlagos", "SuperSport");

// Instanciando os carros
const carro1 = new CarroSuper("Ferrari SF90", "SuperSport", 1000);
const carro2 = new CarroSuper("Subaru WRX", "Sport", 275);

// Testando os carros na pista
interlagos.testarCarro(carro1);
interlagos.testarCarro(carro2);