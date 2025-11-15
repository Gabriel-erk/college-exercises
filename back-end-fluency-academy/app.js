const http = require("http");
const express = require("express");
const mongoose = require("mongoose");

const app = express();

// ESSENCIAL
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Conexão com o MongoDB, utilizando nossas informações de banco criadas no docker-compose.yml
mongoose
  .connect("mongodb://user:password@0.0.0.0:27017/carrofacil?authSource=admin", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB conectado!"))
  .catch((err) => console.log("Erro ao conectar ao MongoDB:", err));

// Suas rotas
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

// Servidor
const PORT = 3000;
const HOST = '0.0.0.0';
app.listen(PORT, HOST, () => {
  console.log("Servidor rodando na porta 3000");
});
