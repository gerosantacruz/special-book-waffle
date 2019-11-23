<template>
    <!-- eslint-disable max-len -->
    <div>
        <b-alert variant="success" show dismissible>{{ message }}</b-alert>
        <br>
    </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
