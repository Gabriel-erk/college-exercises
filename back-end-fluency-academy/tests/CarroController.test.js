const CarroController = require("../controllers/carroController");
const Carro = require("../models/Carro");

jest.mock("../models/Carro");

// ambiente que vai receber cenário de testes para o CarroController
// describe para descrever o que estou testando neste controller
// posso ter vários it dentro do describe
// describe pode ser tamém um conjunto de testes, ou seja, posso ter vários describe dentro de outro describe
describe("CarroController", () => {
  let req, res;

  // vai ser executado para preparar o cenário de testes / metódo especifico para o cenário de testes
  beforeEach(() => {
    req = { body: {} };
    res = {
      send: jest.fn(),
      status: jest.fn().mockReturnThis(),
    };
  });

  describe("metódo inserir", () => {
    it("deve inserir um carro quando o método inserir for chamado", async () => {
      req.body = {
        placa: "ABC1237",
        ano: 2020,
        modelo: "Fiat Argo",
        cor: "Prata",
        tipo: "Hatch",
        quilometragem: 45200,
        vdiaria: 129.9,
        observacao: "Revisão em dia",
      };

      Carro.prototype.save = jest.fn().mockResolvedValue(req.body);

      await CarroController.inserir(req, res);

      expect(res.send).toHaveBeenCalledWith(req.body);
    });
  });
});
