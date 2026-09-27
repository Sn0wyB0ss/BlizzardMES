<script setup lang="ts">
import { ref } from 'vue';

const emit = defineEmits(['onChangeFilter'])

const props = defineProps(['list_items']);

const show_filter = ref(false);

const selected_filter = ref("");

const change_filter_visibility = () => {
    show_filter.value = !show_filter.value
};

const change_filter = (event: any) => {
    if (event.target == null) {return;}
    change_filter_visibility();
    selected_filter.value = event.target.innerText;
    emit('onChangeFilter', selected_filter.value);
}

</script>

<template>
<main>
    <div class="filtro" @click="change_filter_visibility">Filtro</div>
    <div class="dropdown-container" v-show="show_filter">
        <div class="dropdown" v-for="item in props.list_items" @click="change_filter">
            {{ item }}
        </div>
    </div>
</main>
</template>

<style scoped>

.filtro {
  background-color: grey;
  width: 60px;
  height: 30px;
}

.dropdown-container {
    background-color: grey;
    position: absolute;
    z-index: 1;
}
</style>