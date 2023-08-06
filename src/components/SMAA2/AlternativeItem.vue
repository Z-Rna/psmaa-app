<script setup>
import { Icon } from "@iconify/vue";
const props = defineProps({
    alt: {
        type: Object,
        required: true,
    },
    index: {
        type: Number,
        required: true,
    }
});

defineEmits(["edit-alt", "update-alt", "delete-alt"])
</script>

<template>
    <li>
        <div class="alt">
            <input v-if="alt.isEditing" type="text"  
            :value="alt.alt"
            @input="$emit('update-alt', $event.target.value, index)"
            />
            <span v-else>
                {{ alt.alt }}
            </span>
        </div>
        <div class="alt-actions">
            <Icon
                v-if="alt.isEditing"
                icon="ph:check-circle"
                class="icon check-icon"
                color="41b080"
                width="22"
                @click="$emit('edit-alt', index)"
            />
            <Icon
                v-else
                icon="ph:pencil-fill"
                class="icon edit-icon"
                color="41b080"
                width="22"
                @click="$emit('edit-alt', index)"
            />
            <Icon 
                icon="ph:trash" 
                class="icon trash-icon" 
                color="f95e5e" 
                width="22" 
                @click="$emit('delete-alt', alt.id)"
            />
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
    .alt-actions {
      opacity: 1;
    }
  }

  .alt {
    flex: 1;

    input[type="text"] {
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
</style>