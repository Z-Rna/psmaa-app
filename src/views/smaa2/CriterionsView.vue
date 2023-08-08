<script setup>
import { ref, watch, reactive } from "vue";
import { uid } from 'uid';
import AddCriterion from "../../components/SMAA2/AddCriterion.vue"
import CriterionItem from "../../components/SMAA2/CriterionItem.vue";

const altList = ref([]);

const fetchAltList = () => {
    const savedAltList = JSON.parse(localStorage.getItem('altList'));
    if (savedAltList) {
        altList.value = savedAltList;
    }
};

fetchAltList();

const criState = reactive({
    cri: "Criterion 1",
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

const criList = ref([criState]);

watch(criList, () => {
    setCriListLocalStorage();
}, {
    deep: true,
})

const setCriListLocalStorage = () => {
    localStorage.setItem("criList",JSON.stringify(criList.value));
}

const fetchCriList = () => {
    const savedCriList = JSON.parse(localStorage.getItem("criList"))
    if (savedCriList) {
        criList.value= savedCriList;
        const altListNames = altList.value.map((alt) => alt.alt)
        for (let cri of criList.value) {
            const altNames = cri.altList.map((alt) => alt.alt)
            for (let alt of altListNames) {
                if (!altNames.includes(alt)) {
                    if (cri.type == 'cardinal') {
                            cri.altList.push({
                            alt: alt,
                            value: 0.0,
                        })
                    }
                    else {
                        cri.altList.push({
                            alt: alt,
                            value: cri.altList.length + 1,
                        })
                    }
                    
                }
            }
            for (let alt of altNames) {
                if(!altListNames.includes(alt)){
                    if (cri.type == 'cardinal') {
                        cri.altList = cri.altList.filter((a) => a.alt !== alt)
                    }
                    else {
                        let newAltList = []
                        let altVal = cri.altList.filter((a) => a.alt == alt)[0].value
                        cri.altList = cri.altList.filter((a) => a.alt !== alt)
                        for (let a of cri.altList) {
                            if (a.value > altVal){
                                a.value += -1
                            }
                        }
                    }
                }
            }
        }
        
        return;
    }
    setCriListLocalStorage();
}

fetchCriList();

const addCri = (cri, ascending, type, altList) => {
    altList = altList.slice();
    criList.value.push({
        id: uid(),
        cri,
        ascending,
        type,
        altList,
        isEditing: null,
    })
}

const toggleEditCri = (pos) => {
    criList.value[pos].isEditing = !criList.value[pos].isEditing
}

const updateCri = (value, pos) => {
    criList.value[pos].cri = value;
};

const updateAscending = (value, pos) => {
    criList.value[pos].ascending = value;
};

const updateType = (value, pos) => {
    criList.value[pos].type = value;
}

const updateAltList = (value, pos, altPos) => {
    criList.value[pos].altList[altPos].value = value;

}

const updateAltListOrdinal = (value, pos, altPos) => {
    const altList = criList.value[pos].altList
    for ( let alt of altList) {
        if (alt.value == value) {
            alt.value = altList[altPos].value
            break
        }
    }
    altList[altPos].value = value
}

const deleteCri = (id) => {
    if (criList.value.length == 1) {
        alert("You can't remove the last criterion");
        return;
    }
    criList.value = criList.value.filter((cri) => cri.id !== id)
}
</script>

<template>
    <main>
        <AddCriterion @add-cri="addCri"/>
        <ul class="cri-list">
            <CriterionItem 
            v-for="(cri, index) in criList"
            :cri="cri"
            :index="index"
            @edit-cri="toggleEditCri"
            @update-cri="updateCri"
            @update-ascending="updateAscending"
            @update-type="updateType"
            @update-alt-list="updateAltList"
            @update-alt-list-ordinal="updateAltListOrdinal"
            @delete-cri="deleteCri"
            />
        </ul>
    </main>
</template>

<style lang="scss" scoped>

.cri-list {
    display: flex;
    flex-direction: column;
    list-style: none;
    margin-top: 24px;
    gap: 20px;
  }
</style>