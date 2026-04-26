const params = new URLSearchParams(window.location.search);
const id = params.get("id");
console.log("ID:", id);

const img = document.getElementById("imagem-carinha");
const nome = document.getElementById("nome-personagem");
const descricao = document.getElementById("descricao-personagem");
const detNome = document.getElementById("det-nome");
const detTitulo = document.getElementById("det-titulo");
const detFamilia = document.getElementById("det-familia");

axios
  .get(`https://thronesapi.com/api/v2/Characters/${id}`)
  .then((response) => {
    const p = response.data;

    img.src = p.imageUrl;
    nome.innerText = p.fullName;

    descricao.innerText = `${p.fullName} pertence à ${p.family} e é conhecido(a) por ${p.title}.`;

    detNome.innerText = p.fullName;
    detTitulo.innerText = p.title;
    detFamilia.innerText = p.family;
  })
  .catch(() => {
    nome.innerText = "Personagem não encontrado.";
  });
