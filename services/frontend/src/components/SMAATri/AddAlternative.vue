<script setup>
import { reactive } from "vue";

const emit = defineEmits(["add-alt"]);

const altState = reactive({
  alt: "",
  invalid: null,
  errMsg: "",
});

const addAlt = () => {
  altState.invalid = null;
  if (altState.alt !== "") {
    emit("add-alt", altState.alt);
    altState.alt = "";
    return;
  }
  altState.invalid = true;
  altState.errMsg = "Please enter an category name.";

};
</script>

<template>
  <div class="input-alt" :class="{ 'input-err': altState.invalid }">
    <input type="text" v-model="altState.alt">
    <button @click="addAlt">add</button>
  </div>
  <p v-show="altState.invalid" class="err-msg">{{ altState.errMsg }}</p>
</template>

<style lang="scss" scoped>
.input-alt {
  display: flex;
  transition: 250ms ease;
  border: 2px solid #41b080;

  &.input-err {
    border-color: #930000;
  }

  &:focus-within {
    box-shadow: 0 -4px 6px -1px rgb(0 0 0 / 0.1),
      0 -2px 4px -2px rgb(0 0 0 / 0.1);
  }

  input {
    width: 100%;
    padding: 8px 6px;
    border: none;

    &:focus {
      outline: none;
    }
  }

  button {
    padding: 8px 16px;
    border: none;
  }

}

.err-msg {
  margin-top: 6px;
  font-size: 12px;
  text-align: center;
  color: #930000;
}
</style>