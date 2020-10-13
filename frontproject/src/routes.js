import Register from './components/Register.vue';
import Login from './components/Login.vue';
import AllPosts from './components/AllPosts.vue';
import MainPage from './components/MainPage.vue';
import Header2 from './components/Header2.vue';
import Profile from './components/Profile.vue';
import Chatroom from './components/Chatroom.vue';

export default [
    { path: '/', component: MainPage},
    { path: '/addpost', component: Header2},
    { path: '/profile', component: Profile},
    { path: '/chat', component: Chatroom},
    { path: '/reg', component: Register},
    { path: '/login', component: Login},
    { path: '/all', component: AllPosts},
]