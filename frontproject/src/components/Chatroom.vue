<template>
  <div>
        <div class="container">
          <div class="row">
            <div class="col-sm-6 offset-3">
              <div  id="chat-container" class="card">
                <div class="card-header text-white text-center font-weight-bold subtle-blue-gradient">
                  Share the page URL to invite new friends
                </div>
                <div class="card-body">
                  <div class="container chat-body">
                    <div v-for="message in result"  class="row chat-section">
                      <div class="col-sm-7">
                        <span class="card-text speech-bubble speech-bubble-peer">
                          <label>{{message.person}}</label>
                          : {{message.textBody}}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="card-footer text-muted">
                            <form>
                              <div class="row">
                                <div class="col-sm-10">
                                  <input type="text" placeholder="Type a message" v-model="messageText" />
                                </div>
                                <div class="col-sm-2">
                                  <button class="btn btn-primary" style="background-color: #6d086d" v-on:click="addToMessages">Send</button>
                                </div>
                              </div>
                            </form>
                        </div>
                </div>
                </div>
                </div>
                </div>      

  </div>
</template>

<script>
import axios from 'axios';
import { TokenService } from '../storage/service';

export default {
  data () {
    return {
      result:[],
      messages:[],
      messageText:'',
    }
  },
  methods:{
    addToMessages:function(){
      var postData = {
                textBody: this.messageText,
                dateOfSending: '2020-18-25',
                timeOfSending: '12',
                extraField: '',
      };
      let axiosConfig = {
          headers: {
          'Authorization': 'Token ' + this.token
          }
      };
      axios.post(`http://127.0.0.1:8000/api/joinchat/${postData.id}/create_joinToChat/`, postData,axiosConfig)
      .then(res => console.log('all right , data added'))
      .catch(err => console.log('error!! '))

    }
  },
  created(){
    let token;
    this.token = TokenService.getToken();
    this.$http.get('http://127.0.0.1:8000/api/joinchat/').then(function(data){
      this.result = data.body;
      for (let index = 0; index < this.result.length; index++) {
        this.messages[index]=this.result[index].textBody;
        console.log(this.messages);
      }
      console.log('hiii2');
      });
  }
}
</script>

<style scoped>
.chat-body {
  margin-top: -15px;
  margin-bottom: -5px;
  height: 380px;
  overflow-y: auto;
}
.card-header a {
  text-decoration: underline;
}

.card-body {
  background-color: #ddd;
}
.card-footer input[type="text"] {
  background-color: #ffffff;
  color: #444444;
  padding: 7px;
  font-size: 13px;
  border: 2px solid #cccccc;
  width: 100%;
  height: 38px;
}
.speech-bubble {
  display: inline-block;
  position: relative;
  border-radius: 0.4em;
  padding: 10px;
  background-color: #fff;
  font-size: 14px;
}
.speech-bubble-peer:after {
  content: "";
  position: absolute;
  left: 3px;
  top: 10px;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  border-right-color: #ffffff;
  border-top: 0;
  border-left: 0;
  margin-top: -10px;
  margin-left: -20px;
}
.subtle-blue-gradient {
  background: linear-gradient(45deg,#6d086d, #94749c);
}
.chat-section:first-child {
  margin-top: 10px;
}

.chat-section {
  margin-top: 15px;
}

.send-section {
  margin-bottom: -20px;
  padding-bottom: 10px;
}
</style>
