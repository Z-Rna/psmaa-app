<template>
    <button @click="generateResults">generate Results</button>
    <div>
        <Bar ref='bar' :options="chartOptions" :data="chartData" />
    </div>
    
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, reactive } from 'vue';
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = reactive({
    labels: [],
    datasets: []
})

const chartOptions = reactive({
    plugins: {
        title: {
            display: true,
            text: 'Result'
        },
    },
    responsive: true,
    scales: {
        x: {
            stacked: true,
        },
        y: {
            stacked: true
        }
    }
})

const bar = ref(null)


const updateChart = (data) => {
    bar.value.chart.config.data.labels = data.data.labels
    bar.value.chart.config.data.datasets = data.data.datasets
    bar.value.chart.update()
    console.log(bar.value.chart)
}


const generateResults =  () => {
    const savedAltList = JSON.parse(localStorage.getItem('altList'));
    const savedCriList = JSON.parse(localStorage.getItem('criList'));
    const savedPreferenceOption = JSON.parse(localStorage.getItem('preferenceOption'));
    if (savedPreferenceOption && savedCriList) {
        savedPreferenceOption.isEditing = false;
        a = true
        const body = {
            "criList": { "data": savedCriList },
            "preference": savedPreferenceOption
        }
        const results = axios.post(
            "/smaa2results",
            body, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((data) => updateChart(data))
    }
}


</script>

<style lang="scss" scoped>
button {
    padding: 8px 16px;
    border: none;
}
</style>