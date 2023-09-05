<script setup>
import { reactive, watch } from "vue";

const lambda = reactive({
  min: 0.5,
  max: 1.0,
})

const fetchLamda = () => {
  const savedLambda = JSON.parse(localStorage.getItem('lambda'));
  if (savedLambda) {
    lambda.min = savedLambda.min
    lambda.max = savedLambda.max
    return
  }
  setLambdaLocalStorage();
};

fetchLamda();

watch(lambda, () => {
  setLambdaLocalStorage();
}, {
  deep: true,
})

const setLambdaLocalStorage = () => {
  localStorage.setItem("lambda", JSON.stringify(lambda));
}

const changeMin = (value) => {
  if (value > lambda.max) {
    return
  }
  lambda.min = value
}

const changeMax = (value) => {
  if (value < lambda.min) {
    return
  }
  lambda.max = value
}
</script>

<template>
  <div class="range_container">
    <div class="sliders_control">
      <input id="fromSlider" type="range" :value="lambda.min" min="0.5" max="1.0" @change="changeMin($event.target.value)"
        step="0.01" />
      <input id="toSlider" type="range" :value="lambda.max" min="0.5" max="1.0" @change="changeMax($event.target.value)"
        step="0.01" />
    </div>
    <div class="form_control">
      <div class="form_control_container">
        <div class="form_control_container__time">Min</div>
        <input class="form_control_container__time__input" type="number" id="fromInput" :value="lambda.min" min="0.5"
          max="1.0" @change="changeMin($event.target.value)" step="0.01" />
      </div>
      <div class="form_control_container">
        <div class="form_control_container__time">Max</div>
        <input class="form_control_container__time__input" type="number" id="toInput" :value="lambda.max" min="0.5"
          max="1.0" @change="changeMax($event.target.value)" step="0.01" />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.range_container {
  display: flex;
  flex-direction: column;
  width: 100%;
  //   margin: 35% auto;
}

.sliders_control {
  position: relative;
  min-height: 50px;
}

.form_control {
  position: relative;
  display: flex;
  justify-content: space-between;
  font-size: 24px;
  color: #635a5a;
}

input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  pointer-events: all;
  width: 24px;
  height: 24px;
  background-color: #fff;
  border-radius: 50%;
  box-shadow: 0 0 0 1px #C6C6C6;
  cursor: pointer;
}

input[type=range]::-moz-range-thumb {
  -webkit-appearance: none;
  pointer-events: all;
  width: 24px;
  height: 24px;
  background-color: #fff;
  border-radius: 50%;
  box-shadow: 0 0 0 1px #C6C6C6;
  cursor: pointer;
}

input[type=range]::-webkit-slider-thumb:hover {
  background: #f7f7f7;
}

input[type=range]::-webkit-slider-thumb:active {
  box-shadow: inset 0 0 3px #41b080, 0 0 9px #41b080;
  -webkit-box-shadow: inset 0 0 3px #41b080, 0 0 9px #41b080;
}

input[type="number"] {
  color: #8a8383;
  width: 50px;
  height: 30px;
  font-size: 20px;
  border: none;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none
}

input[type="range"] {
  -webkit-appearance: none;
  appearance: none;
  height: 2px;
  width: 100%;
  position: absolute;
  background-color: #C6C6C6;
  pointer-events: none;
}

#fromSlider {
  height: 0;
  z-index: 1;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}</style>
