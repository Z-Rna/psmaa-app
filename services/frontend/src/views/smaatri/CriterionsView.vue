<script setup>
import { ref, watch, reactive } from "vue";
import { uid } from 'uid';
import AddCriterion from "../../components/SMAATri/AddCriterion.vue"
import CriterionItem from "../../components/SMAATri/CriterionItem.vue";

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

const criList = ref([criState]);

watch(criList, () => {
    setCriListLocalStorage();
}, {
    deep: true,
})

const setCriListLocalStorage = () => {
    localStorage.setItem("criListTri", JSON.stringify(criList.value));
}

const fetchCriList = () => {
    const savedCriList = JSON.parse(localStorage.getItem("criListTri"))
    if (savedCriList) {
        criList.value = savedCriList;
        const altListNames = altList.value.map((alt) => alt.alt)
        const catListNames = catList.value.map((cat) => cat.alt)

        for (let cri of criList.value) {
            const altNames = cri.altList.map((alt) => alt.alt)
            const profileNames = cri.profileList
            for (let alt of altListNames) {
                if (!altNames.includes(alt)) {
                    cri.altList.push({
                        alt: alt,
                        value: 0.0,
                    })
                }
            }
            for (let alt of altNames) {
                if (!altListNames.includes(alt)) {
                    cri.altList = cri.altList.filter((a) => a.alt !== alt)
                }
            }
            let l1 = catListNames.length
            let l2 = profileNames.length

            if (l1 - 1 == l2) {
                for (let i = 1; i < l1; i++) {
                    cri.profileList[i - 1].pro.pro_low = catListNames[i - 1]
                    cri.profileList[i - 1].pro.pro_high = catListNames[i]
                }
            }
            else if (l1 > l2) {
                for (let i = 1; i < l1; i++) {
                    if (i < l2) {
                        cri.profileList[i - 1].pro.pro_low = catListNames[i - 1]
                        cri.profileList[i - 1].pro.pro_high = catListNames[i]
                    }
                    else {
                        cri.profileList.push({
                            pro: {
                                pro_low: catListNames[i - 1],
                                pro_high: catListNames[i]
                            },
                            value: 0.0,
                        })
                    }

                }
            }
            else {
                for (let i = 0; i < l2; i++) {
                    if (i < l1 - 1) {
                        cri.profileList[i].pro.pro_low = catListNames[i]
                        cri.profileList[i].pro.pro_high = catListNames[i + 1]
                    }
                    else {
                        cri.profileList = cri.profileList.slice(0, l1 - 1)
                        break
                    }

                }
            }

        }

        return;
    }
    setCriListLocalStorage();
}

fetchCriList();

const addCri = (cri, indifrence, preference, veto, ascending, altList, profileList) => {
    altList = altList.slice();
    criList.value.push({
        id: uid(),
        cri,
        indifrence,
        preference,
        veto,
        ascending,
        altList,
        profileList,
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

const updateAltList = (value, pos, altPos) => {
    criList.value[pos].altList[altPos].value = value;

}

const updateProfileList = (value, pos, proPos) => {
    const profileList = criList.value[pos].profileList
    profileList[proPos].value = value
}

const deleteCri = (id) => {
    if (criList.value.length == 1) {
        alert("You can't remove the last criterion");
        return;
    }
    criList.value = criList.value.filter((cri) => cri.id !== id)
}

const updateQ = (value, pos) => {
    criList.value[pos].indifrence = value;
}

const updateP = (value, pos) => {
    criList.value[pos].preference = value;
}

const updateV = (value, pos) => {
    criList.value[pos].veto = value;
}
</script>

<template>
    <main>
        <AddCriterion @add-cri="addCri" />
        <ul class="cri-list">
            <CriterionItem v-for="(cri, index) in criList" :cri="cri" :index="index" @edit-cri="toggleEditCri"
                @update-cri="updateCri" @update-ascending="updateAscending" @update-alt-list="updateAltList"
                @update-profile-list="updateProfileList" @delete-cri="deleteCri" @update-q="updateQ" @update-p="updateP"
                @update-v="updateV" />
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