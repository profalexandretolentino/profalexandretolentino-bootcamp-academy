class Personagem{

    constructor(personagem, vida, ataque){
        this.personagem = personagem
        this.vida = vida
        this.ataque = ataque
    }
    atacar(alvo){
        alvo.receberDano(this.ataque)
        //console.log("O",this.personagem, "atacou: ",dano)
    }
    receberDano(dano){
        this.vida -= dano
        console.log("O dano recebido no ", this.personagem," foi: " , dano)
        console.log("o total de vida restante do ",this.personagem," é: ", this.vida)
    }
    apresentaPersonagem(){
        console.log("Status Personagem : ", this.personagem,
                    "| Ataque: ", this.ataque,
                    "| HP: ", this.vida

        )
    }
}


const guerreiro = new Personagem("Guerreiro", 80, 20)
const arqueiro = new Personagem("Arqueiro", 60, 10)

guerreiro.apresentaPersonagem()
arqueiro.apresentaPersonagem()
guerreiro.atacar(arqueiro)
arqueiro.atacar(guerreiro)
guerreiro.apresentaPersonagem()
arqueiro.apresentaPersonagem()


console.log(guerreiro instanceof Personagem)
