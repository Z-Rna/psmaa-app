<script setup>
const props = defineProps({
    labels: {
        type: Object,
        required: true,
    },
    fields: {
        type: Object,
        required: true,
    }
});

</script>

<template>
    <table id="tableComponent" class="table table-bordered table-striped">
        <thead>
            <tr>
                <th v-for="field in fields.data" :key='field'>
                    {{ field }}
                </th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in labels.data" :key='item'>
                <td v-for="field in fields.data" :key='field'>{{ item[field] }}</td>
            </tr>
        </tbody>
        <caption>Rank acceptability indices</caption>
    </table>
</template>

<style lang="scss" scoped>
table {
    border-collapse: collapse;
    width: 100%;
    color: #767676;
}

th,
td {
    border: 1px solid #41b080;
    padding: 8px;
    text-align: center;
}
</style>
