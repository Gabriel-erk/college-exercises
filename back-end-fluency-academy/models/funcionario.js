const mongoose = require("mongoose");

const FuncionarioSchema = new mongoose.Schema(
  {
    nome: { type: String, required: true },
    cpf: { type: String, unique: true, required: true },
    idade: { type: Number, required: true },
    dtNascimento: { type: Date, required: true },
    telefone: { type: String, required: true },
    email: { type: String, required: true },
    endereco: { type: String, required: true },
    nuCarteiraMotorista: { type: String, required: true },
    anoVencimentoCarteira: { type: Number, required: true }, // corrigido
  },
  { versionKey: false }
);

module.exports = mongoose.model("Funcionario", FuncionarioSchema);
