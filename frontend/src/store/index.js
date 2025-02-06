import { defineStore } from 'pinia';

export const useGameStore = defineStore('game', {
  state: () => ({
    score: 0,
  }),
  actions: {
    incrementScore() {
      this.score++;
    },
  },
});