<template>
  <div>
    <div class="header-dark">
      <Head />
      <div class="container hero">
        <Form />
        <div v-if="taskStore.loading" class="loading">
          Loading...
          <span></span>
        </div>
        <section class="vh-100 gradient-custom-2">
          <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center">
              <div class="col-md-12 col-xl-10">
                <div class="card mask-custom">
                  <div class="card-body p-4 text-white">
                    <div class="text-center pt-3 pb-2">
                      <h2 class="my-4">Task List</h2>
                      <button
                        type="button"
                        class="btn btn-dark me-1"
                        data-mdb-ripple-color="light"
                        @click="status = 'undone'"
                        :class="{ stressed: status === 'undone' }"
                      >
                        UnDone ({{ taskStore.undoneCount }})
                      </button>
                      <button
                        type="button"
                        class="btn btn-dark me-1"
                        data-mdb-ripple-color="light"
                        @click="status = 'fav'"
                        :class="{ stressed: status === 'fav' }"
                      >
                        Favorite ({{ taskStore.favCount }})
                      </button>
                      <button
                        type="button"
                        class="btn btn-dark me-1"
                        data-mdb-ripple-color="light"
                        @click="status = 'done'"
                        :class="{ stressed: status === 'done' }"
                      >
                        Done ({{ taskStore.doneCount }})
                      </button>
                    </div>

                    <table class="table text-white mt-2 mb-0">
                      <thead>
                        <tr>
                          <th scope="col" width="90%">Task</th>
                          <th scope="col" width="10%">Actions</th>
                        </tr>
                      </thead>
                      <!-- undone list -->
                      <tbody v-if="status === 'undone'">
                        <tr
                          class="fw-normal"
                          v-for="(tasks, index) in taskStore.undones"
                          :key="index"
                        >
                          <Todo :task="tasks" />
                        </tr>
                      </tbody>
                      <!-- favorite list -->
                      <tbody v-if="status === 'fav'">
                        <tr
                          class="fw-normal"
                          v-for="(tasks, index) in taskStore.favs"
                          :key="index"
                        >
                          <Todo :task="tasks" />
                        </tr>
                      </tbody>
                      <!-- done list -->
                      <tbody v-if="status === 'done'">
                        <tr
                          class="fw-normal done-task"
                          v-for="(tasks, index) in taskStore.dones"
                          :key="index"
                        >
                          <Todo :task="tasks" />
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Head from "@/components/Head.vue";
import Todo from "@/components/Todo.vue";
import Form from "@/components/TaskForm.vue";
import { useTaskStore } from "@/stores/TaskStore";
const taskStore = useTaskStore();
// fetch data
taskStore.getTasks();
const status = ref("undone");
components: {
  Head;
  Todo;
  Form;
}
</script>
