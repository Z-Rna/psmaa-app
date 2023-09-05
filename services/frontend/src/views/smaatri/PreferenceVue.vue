<script setup>
import { ref, watch, reactive } from "vue";
import ChoosePreference from "../../components/SMAA2/ChoosePreference.vue";
import PreferenceItem from "../../components/SMAA2/PreferenceItem.vue";

// Criterions list reading part ------
let criListNames = [];

const fetchCriList = () => {
    const savedCriList = JSON.parse(localStorage.getItem('criListTri'));
    if (savedCriList) {
        criListNames = savedCriList.map((cri) => cri.cri);
    }
};

fetchCriList();
// -----------------------------------


const preferenceOption = reactive({
    name: "missing",
    preferenceArray: [],
    isEditing: null
})


const setPreferenceOptionLocalStorage = () => {
    localStorage.setItem('preferenceOptionTri', JSON.stringify(preferenceOption))
}

const fetchPreferenceOption = () => {
    const savedPreferenceOption = JSON.parse(localStorage.getItem('preferenceOptionTri'));
    if (savedPreferenceOption) {
        preferenceOption.name = savedPreferenceOption.name
        preferenceOption.preferenceArray = savedPreferenceOption.preferenceArray
        if (preferenceOption.name !== 'missing') {
            const criNames = preferenceOption.preferenceArray.map((i) => i.cri)
            for (let cri of criListNames) {
                if (!criNames.includes(cri)) {
                    preferenceOption.preferenceArray.push(
                        {
                            cri: cri,
                            value: 0,
                            isEditing: false
                        });
                }
            }
        }

        return;
    }
    setPreferenceOptionLocalStorage();
}

fetchPreferenceOption();

watch(preferenceOption, () => {
    setPreferenceOptionLocalStorage();
}, {
    deep: true,
})

const choosedPref = (name, preferenceArray) => {
    preferenceOption.name = name;
    preferenceOption.preferenceArray = preferenceArray;
}

const toggleEditPref = (pos) => {
    preferenceOption.preferenceArray[pos].isEditing = !preferenceOption.preferenceArray[pos].isEditing;
}

const updatePref = (value, pos) => {

    if (preferenceOption.name === "cardinal") {
        if (value.split(".").slice(-1)[0] == '') {
            return
        }
        var values = value.split(",");
        var newValues = []
        for (let i = 0; i < values.length; i++) {
            let v = values[i]
            console.log("v", v)
            v = parseFloat(v)
            if (!isNaN(v)) {
                newValues.push(v)
            }
            else {
                return
            }

        }
        console.log(newValues)
        preferenceOption.preferenceArray[pos].value = newValues;
    }
    if (preferenceOption.name === "ordinal") {
        value = parseInt(value)
        let posOld = 0;
        for (let i = 0; i < preferenceOption.preferenceArray.length; i++) {
            if (preferenceOption.preferenceArray[i].value === value) {
                posOld = i;
                break;
            }
        }
        const tmp = preferenceOption.preferenceArray[pos].value;
        preferenceOption.preferenceArray[pos].value = value;
        preferenceOption.preferenceArray[posOld].value = tmp;
    }
}
</script>
<template>
    <main>
        <ChoosePreference :pref="preferenceOption" @choose-pref="choosedPref" />
        <ul class="pref-array">
            <PreferenceItem v-for="(pref, index) in preferenceOption.preferenceArray" :pref="pref"
                :prefs_lenght="preferenceOption.preferenceArray.length" :index="index" :name="preferenceOption.name"
                @edit-pref="toggleEditPref" @update-pref="updatePref" />

        </ul>
    </main>
</template>

<style lang="scss" scoped>
.pref-array {
    display: flex;
    flex-direction: column;
    list-style: none;
    margin-top: 24px;
    gap: 20px;
}
</style>