// chamando pacote http
const http = require("http");
const express = require("express");
// chamando classe Utilitario para conseguir utiliza-la
const Utilitario = require("./models/utilitario");
// config do express para trabalhar com json
const app = express();
app.use(express.urlencoded({ extended: true }));

var utilitarioRouter = require('./routes/utilitarioRouter');
app.use('/', utilitarioRouter);

// colocando o servidor para rodar na porta 3000 no domínio local (127.0.0.1) = ip do localhost/localhost
app.listen(3000, "0.0.0.0", () => {
  console.log("Servidor rodando na porta 3000");
});
