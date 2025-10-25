// importante importar a classe Carro
const Carro = require('./carro');

class Utilitario extends Carro {
    constructor(placa, cor, ano, modelo, quilometragem, vdiaria, observacao, qtPassageiro, tmBagageiro, kmLitro) {
        super(placa, cor, ano, modelo, quilometragem, vdiaria, observacao);
        this.qtPassageiro = qtPassageiro;
        this.tmBagageiro = tmBagageiro;
        this.kmLitro = kmLitro;
    }
}

// exportar a classe Utilitario, para que possa ser utilizada em outros arquivos (para que seja vista)
module.exports = Utilitario;