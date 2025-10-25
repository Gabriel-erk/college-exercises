const mongoose = require("mongoose");
const Promocao = mongoose.Schema;
({
    titulo: { type: String, required: true },
    descricao: { type: String, required: true },
    dtValidade: { type: Date, unique: true, required: true },
}),
  { versionKey: false };

module.exports = mongoose.model("Promocao", Promocao);
