// chamando pacote http
const http = require("http");
const express = require("express");

// config do express para trabalhar com json
const app = express();
app.use(express.urlencoded({ extended: true }));

var utilitarioRouter = require('./routes/utilitarioRouter');
app.use('/', utilitarioRouter);

var carroRouter = require('./routes/utilitarioRouter');
app.use('/', carroRouter);

var esportivoRouter = require('./routes/carroRouter');
app.use('/', esportivoRouter);

var clienteRouter = require('./routes/clienteRouter');
app.use('/', clienteRouter);

var funcionarioRouter = require('./routes/funcioarioRouter');
app.use('/', funcionarioRouter);

var promocaoRouter = require('./routes/promocaoRouter');
app.use('/', promocaoRouter);

var reservaRouter = require('./routes/reservaRouter');
app.use('/', reservaRouter);

const PORT = 3000;
const HOST = '0.0.0.0';
// colocando o servidor para rodar na porta 3000 no domínio local (127.0.0.1) = ip do localhost/localhost
app.listen(PORT, HOST, () => {
  console.log("Servidor rodando na porta 3000");
});
