<script setup>
import { ref, reactive } from "vue";

const emit = defineEmits(["choose-pref"]);

// Criterions list reading part ------
const criList = ref([]);

const fetchCriList = () => {
    const savedCriList = JSON.parse(localStorage.getItem('criList'));
    if (savedCriList) {
        criList.value = savedCriList;
    }
};

fetchCriList();
// -----------------------------------

const props = defineProps({
    pref: {
        type: Object,
        required: true,
    },
});


const preferenceOption = reactive({
    name: props.pref.name,
    preferenceArray: props.pref.preferenceArray,
});


const changePrefArray = () => {
    preferenceOption.preferenceArray = []

    if (preferenceOption.name === 'cardinal'){
        for (let i = 0; i < criList.value.length; i++) {
            preferenceOption.preferenceArray.push({
                cri: criList.value[i].cri,
                value: 0.0,
                isEditing: null,
            })
        }
    }
    if (preferenceOption.name === 'ordinal') {
        for (let i = 0; i < criList.value.length; i++) {
            preferenceOption.preferenceArray.push({
                cri: criList.value[i].cri,
                value: i+1,
                isEditing: null,
            })
        }
    }
    emit("choose-pref", preferenceOption.name, preferenceOption.preferenceArray.slice())

}
</script>

<template>
    <form class="input-pref">
        <div>
            <label>Choose preference type</label>
            <select @change="changePrefArray" v-model="preferenceOption.name" class="select-option">
                <option>missing</option>
                <option>cardinal</option>
                <option>ordinal</option>
            </select>
        </div>
    </form>
</template>

<style lang="scss" scoped>
main {
    .select-option {
    width: 100%;
    padding: 8px 6px;
    border: 2px solid #41b080;
    }
}
</style>