<template>
  <div>
        <nav class="main-nav">
            <!-- <div class="logo"></div> -->
            <Burger></Burger>
            <!-- <app-header></app-header> -->
            <!-- <router-view></router-view> -->
        </nav>
        <div class="sagg">
          <router-view></router-view>
        </div>
        <Sidebar>
            <ul class="sidebar-panel-nav">
            <li><router-link to="/" exact>Intro Page</router-link></li>
            <br>
            <li><router-link to="/profile" exact>Profile</router-link></li>
            <br>
            <li><router-link to="/all" exact>View Posts</router-link></li>
            <br>
            <li><router-link to="/chat" exact>Chatroom</router-link></li>
            <br>
            <li><router-link to="/login" exact>Login</router-link></li>
            <br>
            <li><router-link to="/reg" exact>Register</router-link></li>
            </ul>
        </Sidebar>
  </div>
</template>

<script>
import Header from './components/Header2.vue';
import MainPage from './components/MainPage.vue';
import Burger from './components/Burger.vue';
import Sidebar from './components/Sidebar.vue';

export default {
  components:{
    'app-header':Header,
    'mainpage':MainPage,
    'Burger':Burger,
    'Sidebar':Sidebar,
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
/* .sagg{
  overflow-y: scroll; overflow-x:hidden;
} */
html {
   /* height: 100%; */
   overflow:auto;
 }

 body {
   border: 0; margin: 0; padding: 0;
   font-family: 'Lato';
   height: 100%;
   background: rgb(101,31,87);
   background: linear-gradient(45deg, rgba(101,31,87,1) 0%, rgba(225,113,87,1) 48%, rgba(249,248,113,1) 100%);
 }

 .logo {
   align-self: center;
   color: #fff;
   font-weight: bold;
   font-family: 'Lato'
 }

 .main-nav {
   display: flex;
   /* height: auto; */
   justify-content: space-between;
   padding: 0.5rem 0.8rem;
 }

 ul.sidebar-panel-nav {
   list-style-type: none;
 }

 ul.sidebar-panel-nav > li > a {
   color: #fff;
   text-decoration: none;
   font-size: 1.5rem;
   display: block;
   padding-bottom: 0.5em;
 }
</style>
