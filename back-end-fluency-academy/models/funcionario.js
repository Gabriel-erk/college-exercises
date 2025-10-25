const mongoose = require("mongoose");
const Funcionario = mongoose.Schema;
({
    nome: { type: String, required: true },
    cpf: { type: String, unique: true, required: true },
    idade: { type: Number, unique: true, required: true },
    dtNascimento: { type: Date, unique: true, required: true },
    telefone: { type: String, required: true },
    email: { type: String, required: true },
    endereco: { type: String, required: true },
    nuCarteiraMotorista: { type: String, required: true },
    anoVecimentoCarteira: { type: Number, required: true },
}),
  { versionKey: false };

module.exports = mongoose.model("Funcionario", Funcionario);
