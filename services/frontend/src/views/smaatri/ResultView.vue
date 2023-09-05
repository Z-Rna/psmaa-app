<template>
    <button @click="generateResults">generate results</button>
    <div v-if="barEditing.value">
        <Table ref='table' :fields='fields' :labels="tableData"></Table>
    </div>
    <div>
        <Bar ref='bar' :options="chartOptions" :data="chartData" />
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, reactive } from 'vue';
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
import Table from "../../components/SMAA2/TableComponents.vue"

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
const barEditing = reactive({ value: false })


const tableData = reactive({
    data: []
})

const fields = reactive({
    data: []
})

const updateChart = (data) => {
    barEditing.value = true
    const dataValue = data.data
    const barInstance = bar.value.chart
    const dataLabels = dataValue.labels
    const dataValues = dataValue.datasets

    barInstance.config.data.labels = dataLabels
    barInstance.config.data.datasets = dataValues
    barInstance.update()

    let labelsTable = ['Category']
    let dataTable = []

    for (let value of dataValues) {
        let dict = {}
        dict['Category'] = value.label
        for (let [inx, label] of dataLabels.entries()) {
            dict[label] = value.data[inx]
        }
        dataTable.push(dict);
    }

    for (let label of dataLabels) {
        labelsTable.push(label)
    }

    tableData.data = dataTable
    fields.data = labelsTable
}


const generateResults = () => {
    const savedCriList = JSON.parse(localStorage.getItem('criListTri'));
    const savedPreferenceOption = JSON.parse(localStorage.getItem('preferenceOptionTri'));
    const savedLambda = JSON.parse(localStorage.getItem('lambda'));
    if (savedPreferenceOption && savedCriList && savedLambda) {
        savedPreferenceOption.isEditing = false;
        const body = {
            "criList": { "data": savedCriList },
            "preference": savedPreferenceOption,
            "lambda_value": savedLambda,
        }
        const results = axios.post(
            "http://localhost:5000/smaatriresults",
            body, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((data) => updateChart(data)).catch((err) => alert(err.response.data.error))
    }
}


</script>

<style lang="scss" scoped>
button {
    padding: 8px 16px;
    border: none;
}

div {
    padding-top: 30px;

}
</style>