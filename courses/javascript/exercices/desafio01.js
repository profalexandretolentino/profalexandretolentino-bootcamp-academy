let nome = " maria oliveira ";
let curso = "Desenvolvimento de Sistemas";
let media = "8.756";

/* Padronizando o nome */
nome = nome.trim().toUpperCase();

/* Verificando o curso */
let contemSistemas = curso.includes("Sistemas");

/* Convertendo a média */
media = Number(media).toFixed(2);

/* Exibindo resultados */
console.log(`Nome do aluno: ${nome}`);
console.log(`Curso: ${curso}`);
console.log(`O curso contém "Sistemas"? ${contemSistemas}`);
console.log(`Média final: ${media}`);