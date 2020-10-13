import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import Routes from './routes'
import "./plugins/echarts";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'


Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(BootstrapVue);
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const router=new VueRouter({
  routes: Routes,
  mode:'history'
});

new Vue({
  el: '#app',
  render: h => h(App),
  router: router
})
