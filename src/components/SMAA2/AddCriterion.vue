<script setup>
import { ref, reactive } from "vue";

// Alternative list reading part -----
const altList = ref([]);

const fetchAltList = () => {
    const savedAltList = JSON.parse(localStorage.getItem('altList'));
    if (savedAltList) {
        altList.value = savedAltList;
    }
};

fetchAltList();
// -----------------------------------

const criState = reactive({
    cri: "",
    ascending: true,
    type: "cardinal",
    invalid: null,
    errMsg: "",
    altList: [], // alternative list
});

const addAltList = () => {
    for (let i = 0; i < altList.value.length; i++) {
        criState.altList.push({
            alt: altList.value[i].alt,
            value: 0.0,
        });
    }
}

addAltList();

const emit = defineEmits(["add-cri"])

const addCri = () => {
    criState.invalid = null;
    criState.altList = criState.altList.slice();
    if (criState.cri !== "") {
        emit("add-cri",
            criState.cri,
            criState.ascending,
            criState.type,
            criState.altList
        );
        criState.cri = "";
        criState.ascending = true;
        criState.type = "cardinal";
        criState.altList = [];
        addAltList();
        return;
    }
    criState.invalid = true;
    criState.errMsg = "Please enter an criterion name.";
}

const changeAltValues = (type) => {
    if (type === 'cardinal') {
        for (let alt of criState.altList) {
            alt.value = 0.0
        }
    }
    else {
        for (let [index, alt] of criState.altList.entries()) {
            alt.value = index + 1
        }
    }
}

const swapOrdinalValues = (value, alt_value, idx) => {
    for (let [index, alt] of criState.altList.entries()) {
            if (alt.value == value) {
                alt.value = alt_value
                break;
            }
        }
    criState.altList[idx].value = value
}

</script>

<template>
    <form class="input-cri">
        <fieldset>
            <legend>General information</legend>
            <div>
                <label>Name</label>
                <input type="text" placeholder="name" v-model="criState.cri" class="name">
            </div>
            <div>
                <label>Type</label>
                <select id="type" v-model="criState.type" 
                @change="changeAltValues($event.target.value)">
                    <option>cardinal</option>
                    <option>ordinal</option>
                </select>
            </div>
            <div>
                <label>Ascending</label>
                <input type="checkbox" id="ascending" v-model="criState.ascending" checked="true" class="checkbox">
            </div>
        </fieldset>
        <fieldset>
            <legend>Measurements</legend>
            <div v-if="criState.type === 'ordinal'">
                <li v-for="(alt, index) in criState.altList">
                    <fieldset>
                        <legend>{{ alt.alt }}</legend>
                        <select :value="alt.value" class="select-mes"
                        @change="swapOrdinalValues($event.target.value, alt.value, index)">
                            <option v-for="val in criState.altList.length" :value="val">{{ val }}</option>
                        </select>
                    </fieldset>
                </li>
            </div>
            <div v-else>
                <li v-for="(alt) in criState.altList">
                    <fieldset>
                        <legend>{{ alt.alt }}</legend>
                        <input type="number" step="any" placeholder="0.0" v-model="alt.value" class="input-fieldset">
                    </fieldset>
                </li>
            </div>
        </fieldset>
        <button @click="addCri" type="button">add</button>
    </form>
    <p v-show="criState.invalid" class="err-msg">{{ criState.errMsg }}</p>
</template>

<style lang="scss" scoped>
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

.input-cri {
    display: grid;
    transition: 250ms ease;
    border: 2px solid #41b080;
    padding: 20px;
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
        0 8px 10px -6px rgb(0 0 0 / 0.1);

    input[type=text] {
        width: 100%;
        padding: 8px 6px;
        box-sizing: border-box;
        border: 1px solid #41b080;
    }

    div {
        padding: 6px 6px;
    }

    .checkbox {
        margin-left: 10px;

    }

    .select-mes {
        border: none;
    }

    select {
        width: 100%;
        padding: 8px 6px;
        border-color: #41b080;
        // border: none;
    }

    li {
        list-style: none;
    }

    legend {
        margin-left: 15px;
    }

    fieldset {
        border: 1px #41b080;
        border-style: solid;
    }

    .input-fieldset {
        border: none;
        padding: 8px 6px;
        vertical-align: middle;

        &:focus {
            outline: none;
        }
    }

    button {
        margin-top: 10px;
        height: 30px;
        border: none;
    }


}</style>