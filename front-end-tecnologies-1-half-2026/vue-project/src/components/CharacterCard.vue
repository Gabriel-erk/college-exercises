<script setup lang="ts">
defineProps({
  character: Object,
});
</script>

<template>
  <div class="col-md-4 col-lg-3 mb-4">
    <div class="card bg-secondary text-white h-100">

      <img :src="character?.imageUrl" class="card-img-top" style="height: 320px; object-fit: cover" />

      <div class="card-body">
        <h5>{{ character?.fullName }}</h5>

        <p>
          Família:
          {{ character?.family }}
        </p>

        <router-link :to="`/character/${character?.id}`" class="btn btn-primary">
          Detalhes
        </router-link>
      </div>

    </div>
  </div>
</template>