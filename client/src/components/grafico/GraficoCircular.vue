<script setup lang="ts">
import { onMounted, ref } from "vue";
import CanvasJS from "@canvasjs/charts";
const props = defineProps<{ name: string; value: number; maximum: number }>();
const chartContainer = ref<HTMLDivElement | null>(null);
onMounted(() => {
  if (!chartContainer.value) {
    return;
  }
  const chart = new CanvasJS.Chart(chartContainer.value, {
    animationEnabled: false,
    title: { text: props.name },
    subtitles: [{ text: `${props.value}`, verticalAlign: "center" }],
    legend: { enabled: false },
    toolTip: { enabled: false },
    data: [
      {
        type: "doughnut",

        startAngle: 180,
        endAngle: 360,
        yValueFormatString: "##0",

        dataPoints: [
          {
            y: props.value,
            color: "#69C434",
          },
          {
            y: props.maximum - props.value,
            color: "#DEDEDE",
          },
        ],
      },
    ],
  });
  chart.render();
});
</script>
<template>
  <div class="main">
    <div class="titulo"></div>
    <div class="chart-wrapper">
      <div ref="chartContainer" class="chart-container">
        <div class="value">{{ props.value }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main {
  width: 100%;
}
.titulo {
  text-align: center;
}
.chart-wrapper {
  width: 100%;
  height: 150px;
  overflow: hidden;
}

.chart-container {
  width: 100%;
  height: 300px;
}

.value {
  position: absolute;
  color: black;
  left: 20%;
  bottom: 50%;
  transform: translateX(-50%);
  font-size: 24px;
}
</style>
