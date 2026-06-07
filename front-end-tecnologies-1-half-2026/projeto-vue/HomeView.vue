<script setup lang="ts">
import axios from "axios";
import { computed, onMounted, ref } from "vue";

import CharacterCard from "@/components/CharacterCard.vue";

const characters = ref<any[]>([]);
const search = ref("");

const currentPage = ref(1);

const itemsPerPage = 10;

onMounted(async () => {
    const response = await axios.get(
        "https://thronesapi.com/api/v2/Characters"
    );

    characters.value = response.data;
});

// realizando o filtro dos personagens da api
const filteredCharacters = computed(() => {
    return characters.value.filter((character: any) =>
        character.fullName
            .toLowerCase()
            .includes(search.value.toLowerCase())
    );
});

// realizando a paginação dos personagens filtrados
const totalPages = computed(() =>
    Math.ceil(filteredCharacters.value.length / itemsPerPage)
);

const paginatedCharacters = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;

    return filteredCharacters.value.slice(
        start,
        start + itemsPerPage
    );
});

// métodos par ir para próxima página e página anterior
function nextPage() {
    if (currentPage.value < totalPages.value) {
        currentPage.value++;
    }
}

function previousPage() {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
}
</script>

<template>

    <div class="container py-5">

        <div class="text-center mb-5">

            <img src="/img/got-logo.png" width="120">

            <h1 class="fw-bold">
                Game Of Thrones
            </h1>

            <p>
                Guia de Personagens
            </p>

        </div>

        <input v-model="search" class="form-control mb-4" placeholder="Buscar personagem...">

        <div class="row">

            <CharacterCard v-for="character in paginatedCharacters" :key="character.id" :character="character" />

        </div>

        <div class="d-flex justify-content-center gap-3 mt-4">

            <button class="btn btn-secondary" @click="previousPage">
                Anterior
            </button>

            <span class="align-self-center">
                Página {{ currentPage }}
            </span>

            <button class="btn btn-secondary" @click="nextPage">
                Próxima
            </button>

        </div>

    </div>

</template>