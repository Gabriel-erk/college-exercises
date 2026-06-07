import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import CharacterDetailsView from "@/views/CharacterDetailsView.vue";

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },

    {
      path: "/character/:id",
      name: "character-details",
      component: CharacterDetailsView,
      props: true,
    },
  ],
});

export default router;