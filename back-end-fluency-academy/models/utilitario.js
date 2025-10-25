// importante importar a classe Carro
const Carro = require("./carro");

class Utilitario extends Carro {
    constructor(placa, ano, cor, modelo, quilometragem, vdiaria, observacao, qtPassageiro, tmBagageiro, kmLitro) {
        super(placa, ano, cor, modelo, quilometragem, vdiaria, observacao);

        if (typeof vdiaria !== 'number' || vdiaria <= 0) {
            throw new Error("Valor da diária deve ser maior que zero");
        }

        this.qtPassageiro = qtPassageiro;
        this.tmBagageiro = tmBagageiro;
        this.kmLitro = kmLitro;
    }
}

// exportar a classe Utilitario, para que possa ser utilizada em outros arquivos (para que seja vista)
module.exports = Utilitario;
