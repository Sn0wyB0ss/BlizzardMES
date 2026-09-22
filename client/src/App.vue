<script setup lang="ts">
import { ref, computed } from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import TheWelcome from "./components/TheWelcome.vue";
import Test from "./components/Test.vue";

const routes = {
  "/": TheWelcome,
  "/hello_world": Test,
};

const currentPath = ref(window.location.hash);

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || HelloWorld;
});
</script>

<template>
  <div class="main">
    <header>
      <div class="wrapper">
        <a href="#/">TheWelcome</a>
        <a href="#/hello_world">Test</a>
      </div>
    </header>

    <div>
      <component :is="currentView" />
    </div>
  </div>
</template>

<style scoped>
.main {
  position: absolute;
  left: 50%;
  top: 0%;
  transform: translate(-50%, 0%);
  width: 600px;
  text-align: center;
}

header {
  position: sticky;
  top: 0;
  padding: 10px 16px;
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
