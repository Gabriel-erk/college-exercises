// dizendo que quero o pacote http
const http = require('http');

const requestListener = (req, res) => {
    // dizendo que quero retornar esta mensagem caso de certo (status 200 e o tipo texto puro)
    res.writeHead(200, {'Content-Type': 'text/plain'});

    // o que vai retornar pra gente no final da função
    res.end('Hello, World!');
}

// criando o servidor e passando de parâmetro a função requestListener que vai ficar ouvindo as requisições e vai me retornar algo depenendo do que eu pedir
const server = http.createServer(requestListener);

// dizendo que o servidor vai rodar na porta 3000
const porta = 3000;

server.listen(porta, () => {
    console.log(`Servidor rodando na porta ${porta}`);
});
