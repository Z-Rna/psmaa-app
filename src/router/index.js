import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
      children: [
        {
          path:'smaa2',
          name:'about_smaa2',
          component: () => import('../views/about/AboutSMAA2View.vue'),
        },
        {
          path: "smaatri",
          name: "about_smaatri",
          component: () => import('../views/about/AboutSMAATriView.vue'),
        },
        {
          path: "project",
          name: "about_project",
          component: () => import('../views/about/AboutProjectView.vue'),
        }
      ]
    },
    {
      path: "/smaa2",
      name: "smaa2",
      component: () => import('../views/SMAA2View.vue'),
      children: [
        {
          path: "alternatives",
          name: "alt_smaa2",
          component: () => import('../views/smaa2/AlternativesView.vue'),
        },
        {
          path: "criterions",
          name: "cri_smaa2",
          component: () => import('../views/smaa2/CriterionsView.vue'),
        },
        {
          path: "preference",
          name: "pref_smaa2",
          component: () => import('../views/smaa2/PreferenceVue.vue'),
        },
        {
          path: 'results',
          name: 'results_smaa2',
          component: () => import('../views/smaa2/ResultVue.vue'),
        }
      ]
    },
    {
      path: "/smaatri",
      name: "smaatri",
      component: () => import('../views/SMAATriView.vue'),
    },
  ]
})

export default router
