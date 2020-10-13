<template>
  <div id="show-blogs">
        <h1>All Posts</h1>
        <div v-for="blog in blogs" class="single-blog">
            <h4>Title : {{ blog.name }}</h4>
            <h5>Writer  : {{ blog.Writer }}</h5>
            <h6>Stock Category : {{ blog.companyField }}</h6>
            <br>
            <h5>Short Description : {{ blog.description }}</h5>
            <button v-on:click="getInfo(blog)" class="myButton">See The Charts</button>
            <div v-show="seeChartBool">
                <div class="chart-wrapper" >
                    <chart :options="chartOptionsLine"></chart>
                </div>
                <div class="chart-wrapper">
                    <chart :options="chartOptionsLine2"></chart>
                </div>
                <br>
                <label for=""> Give Rating  </label>
                <input class="checkbox-round" type="checkbox" v-on:click="addStar" >
                <input class="checkbox-round" type="checkbox" v-on:click="addStar">
                <input class="checkbox-round" type="checkbox" v-on:click="addStar">
                <input class="checkbox-round" type="checkbox" v-on:click="addStar">
                <input class="checkbox-round" type="checkbox" v-on:click="addStar">
                <br>
                <textarea rows="2" cols="80" placeholder="Enter your comment here... "></textarea>
                <br>
                <button class="myButton" v-on:click="sendData(blog)" v-model.lazy="comments">Send Comment and Rating</button>
           </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
  props: {
    blog: {}
  },
  data () {
    return {
      seeChartBool:false,
      numOfStars:0,
      comments:'',
      blogs: [],
      months:['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
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
            data:[]
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
            data:[]
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
    getInfo:function(blog){
      this.seeChartBool=true;
      var avgs=[];
      var stds=[];
      avgs[0]=blog.avg1;
      avgs[1]=blog.avg2;
      avgs[2]=blog.avg3;
      avgs[3]=blog.avg4;
      avgs[4]=blog.avg5;
      avgs[5]=blog.avg6;
      avgs[6]=blog.avg7;
      avgs[7]=blog.avg8;
      avgs[8]=blog.avg9;
      avgs[9]=blog.avg10;
      avgs[10]=blog.avg11;
      avgs[11]=blog.avg12;
      stds[0]=blog.std1;
      stds[1]=blog.std2;
      stds[2]=blog.std3;
      stds[3]=blog.std4;
      stds[4]=blog.std5;
      stds[5]=blog.std6;
      stds[6]=blog.std7;
      stds[7]=blog.std8;
      stds[8]=blog.std9;
      stds[9]=blog.std10;
      stds[10]=blog.std11;
      stds[11]=blog.std12;
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
            data:avgs
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
            data:stds
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
    addStar:function(){
      this.numOfStars=this.numOfStars+1;
      console.log(this.numOfStars);
    },
    sendData:function(blog){
      var postData = {
        ratingId: 1,
        postId: blog,
        stars: this.numOfStars,
        ratingDate : '2017-11-26',
        ratingTime : '12',
        comment: this.comments,
        extraField: '',
      };
      let axiosConfig = {
        headers: {
        'Authorization': 'Token ' + this.token
        }
      };
      axios.post(`http://127.0.0.1:8000/api/rating/${blog.id}/create_rating/`, postData,axiosConfig)
      .then(res => console.log('doroste'))
      .catch(err => console.log('ghalate'))
    }
  },
  created() {
    this.$http.get('http://127.0.0.1:8000/api/post/').then(function(data){
      this.blogs = data.body;
      console.log('hiii');
            // console.log(data);
      });
    let token;
    this.token = TokenService.getToken();
  }
}
</script>

<style scoped>
.checkbox-round {
    width: 1.3em;
    height: 1.3em;
    background-color: white;
    border-radius: 50%;
    vertical-align: middle;
    border: 1px solid rgb(34, 32, 32);
    -webkit-appearance: none;
    outline: none;
    cursor: pointer;
}

.checkbox-round:checked {
    background-color: rgb(241, 238, 44);
}
#show-blogs{
    max-width: 800px;
    margin: 0px auto;
}
.single-blog{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: rgb(238, 212, 212);
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
