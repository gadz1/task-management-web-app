import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/login.vue'
import signup from '../views/signup.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: signup
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/create',
    name: 'create',
    component: () => import('../views/create.vue')
  },
  {
    path: '/members',
    name: 'members',
    component: () => import('../views/members.vue')
  },
  {
    path: '/tags',
    name: 'tags',
    component: () => import('../views/tags.vue')
  },
  {
    path: '/createtags',
    name: 'tagsCreate',
    component: () => import('../views/tagsCreate.vue')
  },
  {
    path: '/project',
    name: 'projectTemp',
    component: () => import('../views/projectTemp.vue')
  },
  {
    path: '/addTask',
    name: 'addTask',
    component: () => import('../views/addTask.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
