<template>
    <div >
        <body class="back" style="opacity: 0.8">
           <div class="centered" style="opacity: 1">
             <h1 class="h1class"> Stock Exchange Introduction is Now Digital </h1>
             <button class="myButton">Get Started</button>
           </div>
        </body>
    </div>
</template>

<script>

export default {
  data () {
      return{
          
      }
    
  },
  methods:{
      
  }
}
</script>

<style scoped>
.h1class{
  color: black;
  font-weight: bold;
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
  margin-left: 320px;
  margin-top: 20px;
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
.centered {
  position: absolute;
  top: 30%;
  left: 45%;
  transform: translate(-50%, -50%);
   /* filter: blur(-4px);
  -webkit-filter: blur(-4px);  */
}
.back{
    background-image: url(../assets/a.png);
    /* filter: blur(4px);
      -webkit-filter: blur(4px); */
    /* background-repeat: space; */
    /* background-size: 100%;
    background-color: violet; */
    background-repeat: no-repeat;
    margin: auto 10px;
    width: auto;
    /* margin-left: 20px; */
    margin-left: 300px;
    /* border: 2px solid red; */
    /* border-radius: 25px; */
    height: 2000px;
    /* background-color: yellow; */
}
.sag{
    border-radius:4px;
    box-shadow:inset 0px 39px 0px -24px #dbc4c1;
    /* color: rgb(14, 13, 11); */
	background:linear-gradient(to bottom, #ca918c 5%, #cfa5a2 100%);
	background-color:#dbc4c1;
	border:1px solid #ffffff;
    width: 20%;
}
</style>

