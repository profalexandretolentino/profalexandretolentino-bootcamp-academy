alert("Bem-vindo ao sistema!");

let nome = prompt("Digite seu nome:");

let continuar = confirm("Deseja continuar?");

if (continuar) {
    alert(`Olá, ${nome}! Que bom que você decidiu continuar.`);
} else {
    alert(`Tudo bem, ${nome}! Até a próxima.`);
}