// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import App from './App'
import router from './router'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.config.productionTip = false
Vue.prototype.appName = 'Мое приложение'
/* eslint-disable no-new */

Vue.mixin({
  data: function() {
    return {
      globalVar:'global variable'
    }
  }
})

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',

})

