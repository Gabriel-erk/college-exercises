import { createApp } from "vue";
import App from "./App.vue";
import "./assets/scss/styles.scss";

import router from "./router/router";

createApp(App)
  .use(router)
  .mount("#app");