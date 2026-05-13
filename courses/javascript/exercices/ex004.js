let temCarteira = true;
let estaSober = false;

// AND (&&)
const podeDirigir = temCarteira && estaSober;

// OR (||)
const podeEntrar = temCarteira || estaSober;

// NOT (!)
const naoTemCarteira = !temCarteira;

console.log("Tem carteira:", temCarteira);
console.log("Está sóbrio:", estaSober);

console.log("Pode dirigir (AND):", podeDirigir);
console.log("Pode entrar (OR):", podeEntrar);
console.log("Não tem carteira (NOT):", naoTemCarteira);