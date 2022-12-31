<template>
  <td class="align-middle">
    <span>{{ task.title }}</span>
  </td>

  <td class="align-middle">
    <i
      class="material-icons mr-2"
      :class="{ done: task.done }"
      @click="taskStore.doneTask(task.id)"
      >check</i
    >

    <i
      class="material-icons"
      :class="{ favorite: task.fav }"
      @click="taskStore.favTask(task.id)"
      >favorite</i
    >
  </td>
</template>

<script setup>
import { useTaskStore } from "@/stores/TaskStore";
const taskStore = useTaskStore();
const props = defineProps({
  task: Object,
});
</script>

