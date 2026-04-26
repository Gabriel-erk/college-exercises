const listaCards = document.getElementById("lista-cards");

axios
  .get("https://thronesapi.com/api/v2/Characters")
  .then((response) => {
    const personagens = response.data;

    personagens.slice(0, 30).forEach((personagem) => {
      const card = `
                <div class="col-12 col-md-4 d-flex justify-content-center">
                    <div class="card bg-secondary text-white" style="width: 18rem;">
                        <img src="${personagem.imageUrl}" 
                             class="card-img-top" 
                             style="height: 20rem; object-fit: cover;">
                        <div class="card-body bg-secondary">
                            <h5 class="card-title">${personagem.fullName}</h5>
                            <p class="card-text">
                                Família: ${personagem.family}<br>
                                Título: ${personagem.title}
                            </p>
                            <a href="detalhes.html?id=${personagem.id}" class="btn btn-primary">Saiba mais</a>
                        </div>
                    </div>
                </div>
            `;

      listaCards.innerHTML += card;
    });
  })
  .catch((error) => {
    console.error("Erro ao buscar API:", error);
  });
