<template>
  <section class="gradient-custom-2">
    <div class="container p-5">
      <div class="row d-flex justify-content-center align-items-center">
        <div class="col-md-12 col-xl-10">
          <div class="card mask-custom">
            <div class="card-body text-white"></div>
            <form
              @click.prevent="formSubmit"
              class="d-flex mb-4 justify-content-center form-inline"
            >
              <div class="form-group">
                <input
                  type="text"
                  class="form-control-plaintext mr-3"
                  placeholder="i wanna do ............"
                  v-model="newTask"
                />
              </div>
              <div class="form-group">
                <button
                  type="submit"
                  class="btn btn-dark"
                  data-mdb-ripple-color="light"
                >
                  Add
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTaskStore } from "@/stores/TaskStore";
import { ref } from "vue";
const taskStore = useTaskStore();
const newTask = ref("");
const formSubmit = () => {
  if (newTask.value.length > 0) {
    taskStore.addTask({
      title: newTask.value,
      fav: false,
      done: false,
      // id: Math.floor(Math.random() * 100),
    });
    newTask.value = "";
  }
};
</script>