<template>
    <button @click="generateResults">Generate Results</button>
</template>

<script setup>
import axios from 'axios';

const generateResults = () => {
    const savedAltList = JSON.parse(localStorage.getItem('altList'));
    const savedCriList = JSON.parse(localStorage.getItem('criList'));
    const savedPreferenceOption = JSON.parse(localStorage.getItem('preferenceOption'));
    if (savedPreferenceOption && savedCriList) {
        savedPreferenceOption.isEditing = false;
        console.log(savedPreferenceOption)
        const body = {
            "criList": { "data": savedCriList },
            "preference": savedPreferenceOption
        }
        const results = axios.post(
            "/smaa2results", 
            body,{
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(()=> console.log("data send from SMAA2"))
    }
}

</script>

<style lang="scss" scoped>
</style>