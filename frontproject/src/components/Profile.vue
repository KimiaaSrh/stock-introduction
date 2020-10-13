<template>
  <div>
      <body>

          <h2 style="text-align:center">User Profile Card</h2>

          <div class="card">
            <img alt="_" class="imgclass" style="width:100%">
            <!-- <h1>John Doe</h1>
            <p class="title">CEO & Founder, Example</p>
            <p>Harvard University</p>
            <div style="margin: 24px 0;">
              <a href="#"><i class="fa fa-dribbble"></i></a> 
              <a href="#"><i class="fa fa-twitter"></i></a>  
              <a href="#"><i class="fa fa-linkedin"></i></a>  
              <a href="#"><i class="fa fa-facebook"></i></a> 
            </div> -->
            <!-- <label for="">Num of Posts : {{counter}} </label> -->
            <p><button>Num of Posts : {{counter}} </button></p>
            <button class="myButton">
              <router-link to="/addpost" exact>Add Post</router-link>
            </button>
          </div>
      </body>
  </div>
</template>

<script>
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
  data () {
    return {
      result:[],
      counter:0,
      ratingNum:0,
    }
  },
  created(){
    let token;
    this.token = TokenService.getToken();
    this.$http.get('http://127.0.0.1:8000/api/post/').then(function(data){
      this.result = data.body;
      // let pers=this.token.username;
      let pers='acer';
      for (let index = 0; index < this.result.length; index++) {
        if(this.result[index].Writer==pers){
          this.counter=this.counter+1;
        }
      }
      });
  }
}
</script>

<style scoped>

.imgclass{
  width: 100%;
  height:600px;
  background-image: url(../assets/profile2.png);
  background-repeat: no-repeat;
  margin-left: 100px;
}
.myButton {
	box-shadow:inset 0px 39px 0px -24px #d18d8a;
	background:linear-gradient(to bottom, #e4685d 5%, #eb675e 100%);
	background-color:#e4685d;
	border-radius:4px;
	border:1px solid #ffffff;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	padding:6px 15px;
	text-decoration:none;
	text-shadow:0px 1px 0px #b23e35;
}
.myButton:hover {
	background:linear-gradient(to bottom, #eb675e 5%, #e4685d 100%);
	background-color:#eb675e;
}
.myButton:active {
	position:relative;
	top:1px;
}
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 700px;
  height: 700px;
  margin: auto;
  text-align: center;
  font-family: arial;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
