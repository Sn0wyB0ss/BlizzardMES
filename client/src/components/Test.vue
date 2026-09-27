<script setup lang="ts">
import { reactive, ref } from "vue";
import GraficoCircular from "./grafico/GraficoCircular.vue";
import DropdownFilter from "./grafico/DropdownFilter.vue";


const period_dict_data = {
  "Today": {
    oee: 10,
    disponibilidade: 40,
    performance: 80,
    qualidade: 100,
  },
  "This Month": {
    oee: 36,
    disponibilidade: 90,
    performance: 56,
    qualidade: 85,
  },
  "This Year": {
    oee: 0,
    disponibilidade: 100,
    performance: 34,
    qualidade: 36,
  },
  "This Week": {
    oee: 40,
    disponibilidade: 10,
    performance: 70,
    qualidade: 90,
  },
} as const;

type PeriodFilter = keyof typeof period_dict_data;

const period_filter = ref<PeriodFilter>("Today");

const drop_list_options = [
    "Today",
    "This Week",
    "This Month",
    "This Year"
] as const;

const styleObjectHorizontal = {
  flexDirection: "row",
} as const;

const styleObjectVertical = {
  flexDirection: "column",
} as const;

const change_filter = (value: PeriodFilter) => {
  period_filter.value = value;
  const data = period_dict_data[value];
  oee_value.value = data.oee;
  disponibilidade_value.value = data.disponibilidade;
  qualidade_value.value = data.qualidade;
  perfomance_value.value = data.performance;
  console.log(data);
};

const oee_value: any = ref(0);
const disponibilidade_value = ref(0);
const qualidade_value = ref(0);
const perfomance_value = ref(0);
</script>

<template>
  <div class="principal">
    <DropdownFilter :list_items="drop_list_options" @on-change-filter="change_filter"></DropdownFilter>

    <div class="painel">
      
      <div class="titulo">OEE Geral</div>
      <div class="conteudo" :style="styleObjectHorizontal">
        <GraficoCircular name="OEE" :value="oee_value" :maximum="100" />
        <GraficoCircular name="Disponibilidade" :value="disponibilidade_value" :maximum="100" />
        <GraficoCircular name="Performance" :value="perfomance_value" :maximum="100" />
        <GraficoCircular name="Qualidade" :value="qualidade_value" :maximum="100" />
      </div>
    </div>

    <div class="painel">
      <div class="titulo">Tempo de Inatividade</div>
      <div class="conteudo" :style="styleObjectVertical">
        <div class="grafico-horizontal">Falta de Material</div>
        <div class="grafico-horizontal">Problema de Material</div>
        <div class="grafico-horizontal">Almoço</div>
        <div class="grafico-horizontal">Mudança de Material</div>
        <div class="grafico-horizontal">Defeito Elétrico</div>
        <div class="grafico-horizontal">Setup</div>
      </div>
    </div>
  </div>
  {{ period_filter }}
</template>

<style scoped>
.principal {
  flex: auto;
  display: flex;
  flex-direction: column;
}
.painel {
  display: flex;
  flex: auto;
  flex-direction: column;
  width: 100%;
  background-color: darkslategray;
  min-height: 100%;
}

.conteudo {
  display: flex;
  flex: auto;
  align-self: center;
  width: 100%;
}

.titulo {
  background-color: blue;
}


.grafico-circular {
  background-color: cornflowerblue;
  width: 150px;
  min-height: 100px;
  margin: 1%;
}

.grafico-horizontal {
  background-color: cornflowerblue;
  width: 98%;
  height: 100%;
  margin: 1%;
  text-align: left;
  text-justify: left;
}
</style>
