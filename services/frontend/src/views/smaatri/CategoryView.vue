<script setup>
import { ref, watch, reactive } from "vue";
import { uid } from 'uid';
import AddAlternative from "../../components/SMAATri/AddAlternative.vue";
import AlternativeItem from "../../components/SMAATri/AlternativeItem.vue";

const altState = reactive({
    alt: "Category 1",
    id: uid(),
    isEditing: null,
});

const altState2 = reactive({
    alt: "Category 2",
    id: uid(),
    isEditing: null,
});

const altList = ref([altState, altState2]);

watch(altList, () => {
    setAltListLocalStorage();
}, {
    deep: true,
});

const setAltListLocalStorage = () => {
    localStorage.setItem('catList', JSON.stringify(altList.value));
};

const fetchAltList = () => {
    const savedAltList = JSON.parse(localStorage.getItem('catList'));
    if (savedAltList) {
        altList.value = savedAltList;
        return;
    }
    setAltListLocalStorage();// add default alternative item to the list of alternatives
};

fetchAltList();

const createAlt = (alt) => {
    altList.value.push({
        id: uid(),
        alt,
        isEditing: null,
    });
};

const toggleEditAlt = (pos) => {
    altList.value[pos].isEditing = !altList.value[pos].isEditing;
};

const updateAlt = (value, pos) => {
    altList.value[pos].alt = value
};

const deleteAlt = (id) => {
    if (altList.value.length == 2) {
        alert("You can't remove the last two categories");
        return;
    }
    altList.value = altList.value.filter((alt) => alt.id !== id);
};


</script>

<template>
    <main>
        <AddAlternative @add-alt="createAlt" />
        <ul class="alt-list">
            <AlternativeItem v-for="(alt, index) in altList" :alt="alt" :index="index" @edit-alt="toggleEditAlt"
                @update-alt="updateAlt" @delete-alt="deleteAlt" />
        </ul>
    </main>
</template>

<style lang="scss" scoped>
.alt-list {
    display: flex;
    flex-direction: column;
    list-style: none;
    margin-top: 24px;
    gap: 20px;
}
</style>