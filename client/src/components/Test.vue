<script setup lang="ts">
import { reactive } from "vue";

const styleObjectHorizontal = {
  flexDirection: "row",
} as const;

const styleObjectVertical = {
  flexDirection: "column",
} as const;
</script>

<template>
  <div class="principal">
    <div class="filtro">Filtro</div>

    <div class="painel">
      <div class="titulo">OEE Geral</div>
      <div class="conteudo" :style="styleObjectHorizontal">
        <div class="grafico-circular">OEE</div>
        <div class="grafico-circular">Disponibilidade</div>
        <div class="grafico-circular">Performance</div>
        <div class="grafico-circular">Qualidade</div>
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

.filtro {
  background-color: grey;
  width: 60px;
  height: 30px;
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
  text-justify:;
}
</style>
