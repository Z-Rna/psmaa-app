<script setup>
import { ref, reactive } from "vue";

// Alternative list reading part -----
const altList = ref([]);
const catList = ref([]);

const fetchAltList = () => {
    const savedAltList = JSON.parse(localStorage.getItem('altListTri'));
    if (savedAltList) {
        altList.value = savedAltList;
    }
};

const fetchCatList = () => {
    const savedCatList = JSON.parse(localStorage.getItem('catList'));
    if (savedCatList) {
        catList.value = savedCatList;
    }
};


fetchAltList();
fetchCatList();
// -----------------------------------

const criState = reactive({
    cri: "",
    ascending: true,
    indifrence: 0.0,
    preference: 0.0,
    veto: 0.0,
    invalid: null,
    errMsg: "",
    altList: [], // alternative list
    profileList: [],
});

const addAltList = () => {
    for (let i = 0; i < altList.value.length; i++) {
        criState.altList.push({
            alt: altList.value[i].alt,
            value: 0.0,
        });
    }
}

const addProfileList = () => {
    for (let i = 1; i < catList.value.length; i++) {
        criState.profileList.push({
            pro: {
                pro_low: catList.value[i - 1].alt,
                pro_high: catList.value[i].alt,
            },
            value: 0.0,
        });
    }
}

addAltList();
addProfileList();

const emit = defineEmits(["add-cri"])

const addCri = () => {
    criState.invalid = null;
    criState.altList = criState.altList.slice();
    if (criState.cri !== "") {
        emit("add-cri",
            criState.cri,
            criState.indifrence,
            criState.preference,
            criState.veto,
            criState.ascending,
            criState.altList,
            criState.profileList,
        );
        criState.cri = "";
        criState.indifrence = 0.0,
            criState.preference = 0.0,
            criState.veto = 0.0,
            criState.ascending = true;
        criState.altList = [];
        criState.profileList = [];
        addAltList();
        addProfileList();
        return;
    }
    criState.invalid = true;
    criState.errMsg = "Please enter an criterion name.";
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
                <label>Ascending</label>
                <input type="checkbox" id="ascending" v-model="criState.ascending" checked="true" class="checkbox">
            </div>
        </fieldset>
        <fieldset>
            <legend>Tresholds</legend>

            <div>
                <label>Indiffrence</label>
                <input type="number" step="any" placeholder="0.0" v-model="criState.indifrence" class="treshold">
            </div>
            <div>
                <label>Preference</label>
                <input type="number" step="any" placeholder="0.0" v-model="criState.preference" class="treshold">
            </div>
            <div>
                <label>Veto</label>
                <input type="number" step="any" placeholder="0.0" v-model="criState.veto" class="treshold">
            </div>
        </fieldset>
        <fieldset>
            <legend>Measurements</legend>
            <div>
                <li v-for="(alt) in criState.altList">
                    <fieldset>
                        <legend>{{ alt.alt }}</legend>
                        <input type="number" step="any" placeholder="0.0" v-model="alt.value" class="input-fieldset">
                    </fieldset>
                </li>
            </div>
        </fieldset>
        <fieldset>
            <legend>Profiles</legend>
            <div>
                <li v-for="(pro) in criState.profileList">
                    <fieldset>
                        <legend>{{ pro.pro.pro_low }}-{{ pro.pro.pro_high }}</legend>
                        <input type="number" step="any" placeholder="0.0" v-model="pro.value" class="input-fieldset">
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

    .treshold {
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


}
</style>