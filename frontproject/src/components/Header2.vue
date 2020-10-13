<template>
<!-- <keep-alive> -->
<!-- <html><body> -->
    <!-- <html> -->
    <div id="add-blog">
        <h2>Create a New Post</h2>
        <form >
            <label>Stock Topic:</label>
            <input class="inputclass" type="text" v-model.lazy="blog.title" required />
            <label>Stock Description:</label>
            <textarea class="inputclass" v-model.lazy.trim="blog.content"></textarea>
            <div id="checkboxes">
                <label>Stock Company Field :</label>
                <br>
                <label>pharmaceutical</label>
                <input type="checkbox" value="pharmaceutical" v-model="blog.categories" />
                <label>agricultural</label>
                <input type="checkbox" value="agriculturalr" v-model="blog.categories" />
                <br>
                <label>Building Materials</label>
                <input type="checkbox" value="Building Materials" v-model="blog.categories" />
                <label>Oil and Gas</label>
                <input type="checkbox" value="Oil and Gas" v-model="blog.categories" />
            </div>
            <button class="myButton" v-on:click="toggleData">Enter Data to Create Charts </button>
            <div class="secondDiv"  v-if="this.enterChart" >
                <label for="">Month </label>
                <label for="">Average </label>
                <label for="">Standard Deviation</label>
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[0]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[0]">
                <input type="text" class="input-class" v-model="stds[0]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[1]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[1]">
                <input type="text" class="input-class" v-model="stds[1]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[2]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[2]">
                <input type="text" class="input-class" v-model="stds[2]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[3]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[3]">
                <input type="text" class="input-class" v-model="stds[3]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[4]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[4]">
                <input type="text" class="input-class" v-model="stds[4]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[5]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[5]">
                <input type="text" class="input-class" v-model="stds[5]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[6]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[6]">
                <input type="text" class="input-class" v-model="stds[6]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[7]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[7]">
                <input type="text" class="input-class" v-model="stds[7]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[8]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[8]">
                <input type="text" class="input-class" v-model="stds[8]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[9]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[9]">
                <input type="text" class="input-class" v-model="stds[9]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[10]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[10]">
                <input type="text" class="input-class" v-model="stds[10]">
            </div>
            <div class="secondDiv" v-if="this.enterChart" >
                <select v-model="months[11]" class="select-css">
                <option value="Jan">Jan</option>
                <option value="Feb">Feb</option>
                <option value="Mar">Mar</option>
                <option value="Apr">Apr</option>
                <option value="May">May</option>
                <option value="Jun">Jun</option>
                <option value="Jul">Jul</option>
                <option value="Aug">Aug</option>
                <option value="Sep">Sep</option>
                <option value="Oct">Oct</option>
                <option value="Nov">Nov</option>
                <option value="Dec">Dec</option>
                </select>
                <input type="text" class="input-class" v-model="avgs[11]">
                <input type="text" class="input-class" v-model="stds[11]">
            </div>
            <hr>
            <!-- <button v-if="this.enterChart" v-on:click="ToggleData2" class="myButton">See The Chrts</button> -->
            <div v-if="this.submitted">
                <div class="chart-wrapper">
                    <chart :options="chartOptionsLine"></chart>
                </div>
                <div class="chart-wrapper">
                    <chart :options="chartOptionsLine2"></chart>
                </div>
            </div>
            <!-- <input type="date" id="start" name="trip-start" value="2020-07-22" min="2020-01-01" max="2020-12-31" v-model="blog.date"> -->
            <hr>
            <button v-on:click.prevent="post" class="myButton">Add Post</button>
        </form>
        <div v-if="submitted">
            <h3>Thanks for adding your post</h3>
        </div>
        <div id="preview">
            <h3>Preview Post Info</h3>
            <p>Post title: {{ blog.title }}</p>
            <p>Post content:</p>
            <p style="white-space: pre">{{ blog.content }}</p>
            <p>Post Category:</p>
            <ul>
                <li v-for="category in blog.categories">{{ category }}</li>
            </ul>
            <!-- <p>Post date and time: {{ blog.date }} , {{ blog.time }} </p> -->
        </div>
        
    </div>
    <!-- </body></html> -->
    <!-- </html> -->
    <!-- </keep-alive> -->
</template>

<script>

import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
  data () {
    return {
     blog: {
        title: '',
        content: '',
        categories: [],
        author: '',
        date:'',
        time:'',
    },
    enterChart:false,
            submitted:false,
            months:[],
            avgs:[],
            stds:[],
            chartOptionsLine: {
                xAxis: {
                data: this.months
                },
                yAxis: {
                type: "value"
                },
                series: [
                {
                    type: "line",
                    data:this.avgs
                }
                ],
                title: {
                text: "Monthly Avg Prices",
                x: "center",
                textStyle: {
                    fontSize: 24
                }
                },
                color: ["#127ac2"]
            },
            chartOptionsLine2: {
                xAxis: {
                data: this.months
                },
                yAxis: {
                type: "value"
                },
                series: [
                {
                    type: "line",
                    data:this.stds
                }
                ],
                title: {
                text: "Monthly Standard Deviation Prices",
                x: "center",
                textStyle: {
                    fontSize: 24
                }
                },
                color: ["#127ac2"]
            },
    }
  },
  methods:{
      toggleData:function(){
          this.enterChart=true;
      },
      ToggleData2:function(){
        this.submitted=true;
        this.chartOptionsLine= {
                xAxis: {
                data: this.months
                },
                yAxis: {
                type: "value"
                },
                series: [
                {
                    type: "line",
                    data:this.avgs
                }
                ],
                title: {
                text: "Monthly Avg Prices",
                x: "center",
                textStyle: {
                    fontSize: 24
                }
                },
                color: ["#127ac2"]
        };
        this.chartOptionsLine2= {
                xAxis: {
                data: this.months
                },
                yAxis: {
                type: "value"
                },
                series: [
                {
                    type: "line",
                    data:this.stds
                }
                ],
                title: {
                text: "Monthly Standard Deviation Prices",
                x: "center",
                textStyle: {
                    fontSize: 24
                }
                },
                color: ["#127ac2"]
            };  
      },
      post: function(){
        var postData = {
                postId:1,
                name : this.blog.title,
                description : this.blog.content,
                companyField : this.blog.categories[0],
                postingDate : '2017-11-26',
                postingTime : '12',
                extraField: '',
                avg1:this.avgs[0],
                avg2:this.avgs[1],
                avg3:this.avgs[2],
                avg4:this.avgs[3],
                avg5:this.avgs[4],
                avg6:this.avgs[5],
                avg7:this.avgs[6],
                avg8:this.avgs[7],
                avg9:this.avgs[8],
                avg10:this.avgs[9],
                avg11:this.avgs[10],
                avg12:this.avgs[11],
                std1:this.stds[0],
                std2:this.stds[1],
                std3:this.stds[2],
                std4:this.stds[3],
                std5:this.stds[4],
                std6:this.stds[5],
                std7:this.stds[6],
                std8:this.stds[7],
                std9:this.stds[8],
                std10:this.stds[9],
                std11:this.stds[10],
                std12:this.stds[11],
            };
            let axiosConfig = {
                headers: {
                'Authorization': 'Token ' + this.token
                }
            };
            axios.post(`http://127.0.0.1:8000/api/post/${postData.id}/create_post/`, postData,axiosConfig)
            .then(res => console.log('doroste'))
            .catch(err => console.log('ghalate'))
        }

  },
  created() {
        let token;
        this.token = TokenService.getToken();
  }
}
</script>

<style scoped>
.inputclass{
    border: 10px solid #cec5c500;
}
.chart-wrapper {
  width: 100%;
  height: 700px;
}
.echarts {
  width: 100%;
  height: 100%;
}
.secondDiv{
    margin-top: 5px;
    width: 100%; 
    justify-content: space-between;
    display: flex;
    border: 1px solid #cec5c500;
}
header{
    background-color: greenyellow;
    padding: 10px;
}
.input-class{
    width: 20%;
    border: 4px solid #8842d5;
    border-radius: 5px; 
    margin-left: 10px;
    /* display: inline-block; */
}
.select-css {
    /* display: inline-block; */
    width: 20%;
    font-size: 16px;
    font-family: sans-serif;
    font-weight: 700;
    color: #444;
    line-height: 1.3;
    padding: .6em 1.4em .5em .8em;
    /* width: 20%; */
    max-width: 20%; /* useful when width is set to anything other than 100% */
    box-sizing: border-box;
    margin: 0;
    border: 1px solid #aaa;
    box-shadow: 0 1px 0 1px rgba(0,0,0,.04);
    border-radius: .5em;
    -moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
    background-color: #fff;
    /* note: bg image below uses 2 urls. The first is an svg data uri for the arrow icon, and the second is the gradient. 
        for the icon, if you want to change the color, be sure to use `%23` instead of `#`, since it's a url. You can also swap in a different svg icon or an external image reference
        
    */
    background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007CB2%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'),
      linear-gradient(to bottom, #ffffff 0%,#e5e5e5 100%);
    background-repeat: no-repeat, repeat;
    /* arrow icon position (1em from the right, 50% vertical) , then gradient position*/
    background-position: right .7em top 50%, 0 0;
    /* icon size, then gradient */
    background-size: .65em auto, 100%;
}
/* Hide arrow icon in IE browsers */
.select-css::-ms-expand {
    display: none;
}
/* Hover style */
.select-css:hover {
    border-color: #888;
}
/* Focus style */
.select-css:focus {
    border-color: #aaa;
    /* It'd be nice to use -webkit-focus-ring-color here but it doesn't work on box-shadow */
    box-shadow: 0 0 1px 3px rgba(59, 153, 252, .7);
    box-shadow: 0 0 0 3px -moz-mac-focusring;
    color: #222; 
    outline: none;
}

/* Set options to normal weight */
.select-css option {
    font-weight:normal;
}

/* Support for rtl text, explicit support for Arabic and Hebrew */
*[dir="rtl"] .select-css, :root:lang(ar) .select-css, :root:lang(iw) .select-css {
    background-position: left .7em top 50%, 0 0;
    padding: .6em .8em .5em 1.4em;
}

/* Disabled styles */
.select-css:disabled, .select-css[aria-disabled=true] {
    color: graytext;
    background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22graytext%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E'),
      linear-gradient(to bottom, #ffffff 0%,#e5e5e5 100%);
}

.select-css:disabled:hover, .select-css[aria-disabled=true] {
    border-color: #aaa;
}

h1{
    color: indigo;
    text-align: center;
}
#add-blog *{
    /* overflow-y: scroll;  */
    box-sizing: border-box;
}
#add-blog{
    /* overflow: scroll;  */
    /* position: absolute; */
    margin: 20px auto;
    max-width: 500px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type="text"], textarea{
    display: block;
    width: 100%;
    padding: 8px;
}
#preview{
    padding: 10px 20px;
    border: 1px dotted #ccc;
    margin: 30px 0;
}
h3{
    margin-top: 10px;
}
#checkboxes input{
    display: inline-block;
    margin-right: 10px;
}
#checkboxes label{
    display: inline-block;
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
</style>
