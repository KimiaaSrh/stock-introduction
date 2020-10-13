<template>
  <div class="login">
    <body class="bodyxx">
      <h2>Login Page</h2><br>   
        <b-nav-form @submit.prevent="login" v-if="token==null">
          <label><b>User Name     
        </b>  
        </label>
        <hr>   
        <b-form-input id="Uname" size="sm" class="mr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
        <br>  
        <label style="margin-top: 10px;"><b>Password     
        </b>    
        </label> 
        <hr>   
        <b-form-input id="Pass" size="sm" class="mr-sm-2" placeholder="password" type="password" v-model="password" name="password"></b-form-input>
        <!-- <hr><hr> -->
        <!-- <br> -->
        <b-button size="sm" type="submit" id="log">Login</b-button>
        </b-nav-form>
        <b-nav-form @submit.prevent="logout" v-if="token !== null">
          <b-button type="submit" size="sm" id="log"> Logout</b-button>
        </b-nav-form>
        <br><br>    
        <input style="margin-left:30px;" type="checkbox" id="check" v-if="token == null">    
        <span v-if="token == null">Remember me</span>    
        <br><br>    
        <!-- Forgot <a href="#">Password</a>   -->
    </body>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      username: '',
      password: '',
      token: localStorage.getItem('user-token') || null,
    }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/auth/', {
        username: this.username,
        password: this.password,
      })
      .then(resp => {

      this.token = resp.data.token;
      console.log(this.token)
    //   console.log("kar kard");
      localStorage.setItem('user-token', resp.data.token)
      })
      .catch(err => {
        localStorage.removeItem('user-token')
      })
    },
    logout() {
      localStorage.removeItem('user-token');
      this.token = null;
    },
    }
}
</script>

<style  scoped>
span{  
    color: white;  
    font-size: 17px;  
}  
a{  
    float: right;  
    background-color: rgb(199, 158, 158);  
} 
#log{  
    width: 100px;  
    height: 40px;  
    border: none; 
    /* margin-top: 47px;  */
    margin-left: 140px;
    margin-top: 40px;
    border-radius: 17px;  
    padding-left: 7px;  
    background-color: rgb(209, 162, 207);
    color: rgb(54, 4, 39);  
  
  
} 
h2{  
    text-align: center;  
    color: #277582;  
    padding: 20px;  
} 
.bodyxx  
{  
    margin: 0;  
    padding: 0;  
    background-color:rgb(189, 147, 147);  
    font-family: 'Arial';  
}
#Uname{  
    width: 300px;  
    height: 50px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Pass{  
    width: 300px;  
    height: 50px;  
    border: none;  
    margin-top: 20px;
    border-radius: 3px;  
    padding-left: 8px;  
      
} 
.login{  
        width: 482px;  
        height: 500px;
        overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 40px;  
        background: rgb(189, 147, 147);  
        border-radius: 15px ;  
          
} 
label{  
    color: #42135e;  
    font-size: 17px;  
}  
</style>