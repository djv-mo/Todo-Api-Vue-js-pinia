import { defineStore } from "pinia";
import http from "@/http-common";

export const useTaskStore = defineStore("taskStore", {
  state: () => ({
    tasks: [],
    loading: false,
  }),
  getters: {
    // doubleCount: (state) => state.count * 2,
    favs() {
      return this.tasks.filter((task) => task.fav);
    },
    dones() {
      return this.tasks.filter((task) => task.done);
    },
    undones() {
      return this.tasks.filter((task) => !task.done);
    },
    favCount() {
      return this.tasks.reduce((p, c) => {
        return c.fav ? p + 1 : p;
      }, 0);
    },
    doneCount() {
      return this.tasks.reduce((p, c) => {
        return c.done ? p + 1 : p;
      }, 0);
    },
    undoneCount() {
      return this.tasks.reduce((p, c) => {
        return !c.done ? p + 1 : p;
      }, 0);
    },
  },
  actions: {
    async getTasks() {
      this.loading = true;
      const res = await http.get("task/");
      const data = await res.data;
      this.tasks = data;
      this.loading = false;
    },
    async addTask(task) {
      const res = await http.post("task/", task);
      this.tasks.unshift(res.data);

      console.log(res);
    },
    async doneTask(id) {
      const task = this.tasks.find((t) => t.id === id);
      task.done = !task.done;
      const res = await http.patch(`task/${id}/`, { done: task.done });
      console.log(res);
    },
    async favTask(id) {
      const task = this.tasks.find((t) => t.id === id);
      task.fav = !task.fav;
      const res = await http.patch(`task/${id}/`, { fav: task.fav });
      console.log(res);
    },
  },
});
