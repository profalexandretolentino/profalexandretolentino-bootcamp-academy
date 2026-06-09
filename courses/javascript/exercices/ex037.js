class UsuarioSeguro {
    constructor(email, senha) {
        this.email = email;
        this._senha = senha; // O prefixo '_' sinaliza convenção de propriedade privada/protegida
    }

    // O Getter finge ser uma propriedade, mas roda uma função de máscara
    get senha() {
        return "********"; 
    }

    // O Setter intercepta e valida a tentativa de alteração
    set senha(novaSenha) {
        if (novaSenha.length < 6) {
            console.log("Erro: A senha precisa ter no mínimo 6 caracteres.");
        } else {
            this._senha = novaSenha;
            console.log("Senha alterada com sucesso!");
        }
    }
}

let usuario = new UsuarioSeguro("aluno@escola.com", "123456");
usuario.senha = "123"; // Saída: Erro: A senha precisa ter...
usuario.senha = "mudar123"; // Saída: Senha alterada com sucesso!
console.log(usuario.senha); // Saída: ******** (A senha real nunca é exibida)