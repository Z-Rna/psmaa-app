<script setup>
import { Icon } from "@iconify/vue";
const props = defineProps({
    cri: {
        type: Object,
        required: true,
    },
    index: {
        type: Number,
        required: true,
    }
});

defineEmits(["edit-cri", 
            "update-cri", 
            "update-ascending",
            "update-type",
            "update-alt-list",
            "update-alt-list-ordinal",
            "delete-cri",
            ]);
</script>

<template>
    <li>
        <div class="cri">
            <div>
                <label>Name: </label>
                <input v-if="cri.isEditing" type="text"
                :value="cri.cri"
                @input="$emit('update-cri', $event.target.value, index)">
                <span v-else>
                    {{ cri.cri }}
                </span>
            </div>
            <div>
                <label>Type: </label>
                <select v-if="cri.isEditing"
                :value="cri.type"
                @change="$emit('update-type', $event.target.value, index)">
                    <option>cardinal</option>
                    <option>ordinal</option>
                </select>
                <span v-else>
                    {{ cri.type }}
                </span>
            </div>
            <div>
                <label>Ascending: </label>
                <input v-if="cri.isEditing" type="checkbox"
                :checked="cri.ascending"
                @input="$emit('update-ascending', $event.target.checked, index)">
                <span v-else>
                    {{ cri.ascending }}
                </span>
            </div>
            <div v-if="cri.type === 'ordinal'">
                <li v-for="(alt, alt_index) in cri.altList" class="alt-list">
                    <label> {{alt.alt}}: </label>
                    <select class="select-mes" v-if="cri.isEditing" :value="alt.value"
                    @change="$emit('update-alt-list-ordinal', $event.target.value, index, alt_index)">
                            <option v-for="val in cri.altList.length" :value="val">{{ val }}</option>
                    </select>
                    <span v-else>
                        {{ alt.value }}
                    </span>
                </li>
            </div>
            <div v-else>
                <li v-for="(alt, alt_index) in cri.altList" class="alt-list">
                    <label> {{alt.alt}}: </label>
                    <input v-if="cri.isEditing" type="number" step="any" placeholder="0.0" 
                    :value="alt.value"
                    @input="$emit('update-alt-list', $event.target.value, index, alt_index)">
                    <span v-else>
                        {{ alt.value }}
                    </span>
                </li>
            </div>
            
            
        </div>
        <div class="alt-actions">
            <Icon
                v-if="cri.isEditing"
                icon="ph:check-circle"
                class="icon check-icon"
                color="41b080"
                width="22"
                @click="$emit('edit-cri', index)"
            />
            <Icon
                v-else
                icon="ph:pencil-fill"
                class="icon edit-icon"
                color="41b080"
                width="22"
                @click="$emit('edit-cri', index)"
            />
            <Icon 
                icon="ph:trash" 
                class="icon trash-icon" 
                color="f95e5e" 
                width="22" 
                @click="$emit('delete-cri', cri.id)"
            />
        </div>
    </li>
</template>


<style lang="scss" scoped>
.alt-list {
        list-style: none;
        background: none;
        box-shadow: none;
        gap: 5px;
        padding: 2px 0px;
        input[type="number"] {
            border: 2px solid #41b080;
            width: 40px;
        }
    }

li {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 10px;
  background-color: #f1f1f1;
  box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1),
    0 8px 10px -6px rgb(0 0 0 / 0.1);

  &:hover {
    .alt-actions {
      opacity: 1;
    }
  }

  .cri {
    flex: 1;

    input[type="text"] {
      width: 100%;
      padding: 2px 6px;
      border: 2px solid #41b080;
    }
    .select-mes {
        width: 6%;
    }
    select {
        width: 100%;
        padding: 2px 6px;
        border: 2px solid #41b080;
    }
    
  }

  .alt-actions {
    display: flex;
    gap: 6px;
    opacity: 0;
    transition: 150ms ease-in-out;
    .icon {
      cursor: pointer;
    }
  }
  
}
input[type="number"]::-webkit-outer-spin-button,
    input[type="number"]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0; 
    }
</style>