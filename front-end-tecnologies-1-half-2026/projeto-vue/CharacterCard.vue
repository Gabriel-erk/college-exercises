<!-- CharacterCard.vue == componente, esse arquivo é o nosso componente atual -->
<!-- script: local onde escrevemos js/ts do componente -->
<!-- setup == sintaxe moderna do Vue 3 (mais simples e curta), ou seja, sem ele, seria necessário escrever mais código para atingir um objetivo que, graćas ao 'setup' permite escrevermos menos e ter o mesmo resultado -->
<!-- lang="ts" indica que o arquivo usa TypeScript -->
<script setup lang="ts">
// defineProps quer dizer: esse componente (CharacterCard.vue) espera receber dados do componente pai (nesse caso, o pai é a HomeView), exemplo, na linha (que provavelmente estaria na HomeView == componente pai): <CharacterCard :character="character" /> ele está enviando para meu componente filho (CharacterCard) um "character" como podemos ver em "character="character == o que vamos receber no componente filho""
// em resumo, defineProps diz: este componente recebe uma PROPRIEDADE chamada character, que é um objeto do componente pai (HomeView)
defineProps({
  character: Object,
});
// aqui se encerra a parte lógica do componente, pois estamosfechando o script
</script>

<!-- tudo dentro da tag <template></template no vue é o HTML que será exibido na tela do usuário -->
<template>
  <div class="col-md-4 col-lg-3 mb-4">
    <div class="card bg-secondary text-white h-100">
      <!-- : antes do "src" é equivalente a outro comando do vue (v-bind:src) que basicamente diz: pegue o valor do JS e coloque no atributo HTML (atributo HTML == src), e o valor do JS que queremos é o valor imageUrl dentro do objeto character, então a partir do objeto "character" passado para nosso componente atual (Character Card) pelo componente pai (HomeView) acesse o atributo imageUrl dele, o ? logo após character (character?) quer dizer que ele só vai acessar imageUrl se o objeto character existir (ou seja, se não for nulo, ele mostra) -->
      <img :src="character?.imageUrl" class="card-img-top" style="height: 320px; object-fit: cover" />

      <div class="card-body">
        <!-- as chaves aqui, são como no laravel, servem como uma espécia de interpolaćão e exibem valores do JS no html (como exibir valores php no blade) -->
        <h5>{{ character?.fullName }}</h5>

        <p>
          Família:
          {{ character?.family }}
        </p>

        <!-- router-link == link do Vue Router (pacote npm, que muda a página sem recarregar o site), o to:="" define para onde ele vai, ficando a rota dentro das aspas "", como estamos usando 'template string' significa, no js, que dentro das nossas crases `` queremos converter um valor JS (no caso, do nosso objeto) para a string, queremos incluir um valor js na nossa string html, pois o caminho da nossa rota até a página detalhes precisa do id de um personagem, no caso, passamos o id do personagem atual (character?.id) para a rota /character/{id}  == equivalente a passar o id de um cara no formulário de atualizaćão de dados de um laravel -->
        <router-link :to="`/character/${character?.id}`" class="btn btn-primary">
          Detalhes
        </router-link>
      </div>

    </div>
  </div>
</template>