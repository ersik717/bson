import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Registration from '@/components/Registration'
import Bakery from '@/components/Bakery'
import Catalog from '@/components/Catalog'
import Basket from '@/components/Basket'
import Detail from '@/components/Detail'
import Chart from '@/components/Chart'
import ChartContainer from '@/components/ChartContainer'
import Pagination from '@/components/Pagination'
import User from '@/components/User'
import JwPagination from 'jw-vue-pagination';
Vue.component('jw-pagination', JwPagination);

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/registration',
      name: 'registration',
      component: Registration
    },
    {
      path: '/bakery',
      name: 'bakery',
      component: Bakery
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: Catalog
    },
    {
      path: '/basket',
      name: 'basket',
      component: Basket
    },
    {
      path: '/detail/:Pid',
      name: 'detail',
      component: Detail
    },
    {
      path: '/chart',
      name: 'chart',
      component: Chart
    },
    {
      path: '/chartcontainer',
      name: 'chartcontainer',
      component: ChartContainer
    },
    {
      path: '/pagination',
      name: 'pagination',
      component: Pagination
    },
    {
      path: '/user',
      name: 'user',
      component: User
    },
  ]
})

