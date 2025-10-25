// chamando pacote http
const http = require("http");
// chamando classe Utilitario para conseguir utiliza-la
const Utilitario = require("./models/utilitario");

// função que observa quando aconteceu alguma coisa
const server = http.createServer((req, res) => {
  const { method, url } = req;

  if (method == "POST" && url == "/carro/construir") {
    let body = new Utilitario(
      "ABC-1234",
      "Prata",
      2020,
      "Fiat Doblo",
      50000,
      150,
      "Carro em bom estado",
      5,
      "500L",
      12
    );

    req.on("/data", (chunk) => {
      body = chunk.toString();
    });

    // o que quero fazer quando finalizar a requisição
    req.on("end", () => {
      // retornando código 200 e o body em formato json (resposta que iremos receber ao finalizar a requisição é do tipo json)
      res.writeHead(200, { "Content-Type": "application/json" });
      // quero retorarnar o body (objeto) convertido em json (JSON.stringify)
      res.end(JSON.stringify(body));
    });
  }
});

// colocando o servidor para rodar na porta 3000 no domínio local (127.0.0.1) = ip do localhost/localhost
server.listen(3000, "127.0.0.1", () => {
  console.log("Servidor rodando na porta 3000");
});
