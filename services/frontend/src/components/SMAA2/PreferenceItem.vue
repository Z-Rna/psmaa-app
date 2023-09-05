<script setup>
import { Icon } from "@iconify/vue";
const props = defineProps({
    pref: {
        type: Object,
        required: true,
    },
    prefs_lenght: {
        type: Number,
        required: true,
    },
    index: {
        type: Number,
        required: true,
    },
    name: {
        type: String,
        required: true,
    },
})
defineEmits(["update-pref", "edit-pref"])
</script>

<template>
    <li>
        <div class="pref">
            <label>{{ pref.cri }}</label>
            <div v-if="name === 'ordinal'">
                <select v-if="pref.isEditing" :value="pref.value"
                    @change="$emit('update-pref', $event.target.value, index)">
                    <option v-for="val in prefs_lenght" :value="val">{{ val }}</option>
                </select>
                <span v-else>
                    value: {{ pref.value }}
                </span>
            </div>
            <div v-else>
                <input v-if="pref.isEditing" type="text" :value="pref.value"
                    @input="$emit('update-pref', $event.target.value, index)">
                <span v-else>
                    value: {{ pref.value }}
                </span>
            </div>
        </div>
        <div class="pref-actions">
            <Icon v-if="pref.isEditing" icon="ph:check-circle" class="icon check-icon" color="41b080" width="22"
                @click="$emit('edit-pref', index)" />
            <Icon v-else icon="ph:pencil-fill" class="icon edit-icon" color="41b080" width="22"
                @click="$emit('edit-pref', index)" />
        </div>
    </li>
</template>

<style lang="scss" scoped>
li {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 16px 10px;
    background-color: #f1f1f1;
    box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
        0 8px 10px -6px rgb(0 0 0 / 0.1);

    &:hover {
        .pref-actions {
            opacity: 1;
        }
    }

    .pref {
        flex: 1;

        select {
            width: 100%;
            padding: 2px 6px;
            border: 2px solid #41b080;
        }
    }

    input[type="number"]::-webkit-outer-spin-button,
    input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }

    input {
        width: 100%;
        padding: 2px 6px;
        border: 2px solid #41b080;
    }

    .pref-actions {
        display: flex;
        opacity: 0;
        transition: 150ms ease-in-out;

        .icon {
            cursor: pointer;
        }
    }
}
</style>