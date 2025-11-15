const http = require("http");
const express = require("express");

const app = express();

// ESSENCIAL para ler JSON enviado pelo Postman
app.use(express.json());

// Para aceitar dados enviados como formulário
app.use(express.urlencoded({ extended: true }));

var utilitarioRouter = require('./routes/utilitarioRouter');
app.use('/', utilitarioRouter);

var carroRouter = require('./routes/carroRouter');
app.use('/', carroRouter);

var esportivoRouter = require('./routes/carroRouter');
app.use('/', esportivoRouter);

var clienteRouter = require('./routes/clienteRouter');
app.use('/', clienteRouter);

var funcionarioRouter = require('./routes/funcionarioRouter');
app.use('/', funcionarioRouter);

var promocaoRouter = require('./routes/promocaoRouter');
app.use('/', promocaoRouter);

var reservaRouter = require('./routes/reservaRouter');
app.use('/', reservaRouter);

const PORT = 3000;
const HOST = '0.0.0.0';

app.listen(PORT, HOST, () => {
  console.log("Servidor rodando na porta 3000");
});
