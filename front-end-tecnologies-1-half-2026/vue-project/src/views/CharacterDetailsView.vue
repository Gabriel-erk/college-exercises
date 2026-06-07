<script setup lang="ts">
import axios from "axios";

import { onMounted, ref } from "vue";

import { useRoute } from "vue-router";

const route = useRoute();

const character = ref<any>(null);

onMounted(async () => {
    const response = await axios.get(
        `https://thronesapi.com/api/v2/Characters/${route.params.id}`
    );

    character.value = response.data;
});
</script>

<template>

    <div class="container py-5" v-if="character">

        <div class="row">

            <div class="col-md-5">

                <img :src="character.imageUrl" class="img-fluid rounded">

            </div>

            <div class="col-md-7">

                <h1 class="fw-bold">
                    {{ character.fullName }}
                </h1>

                <div class="bg-secondary p-4 rounded mt-3">

                    <h5>Família</h5>

                    <p>
                        {{ character.family }}
                    </p>

                    <h5>Título</h5>

                    <p>
                        {{ character.title }}
                    </p>

                </div>

                <router-link to="/" class="btn btn-primary mt-4">
                    Voltar
                </router-link>

            </div>

        </div>

    </div>

</template>