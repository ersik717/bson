<template>
<div>
	<div>
			<navbar></navbar>
	</div>
	<div>
			<!-- <br><br><br><br>		 -->
		<form @submit.prevent="setRegistration">
  <div id="Third" class="bg-2" style="display: flex; justify-content: center; align-items: center;">
    <div id="customform" style="height: 1650px; width: 500px; margin: 140px; ">
      <div class="container-fluid text-left" style="padding: 42px;">
        <h3 style="font-weight: bold; color:#222222; text-align: center;">Регистрация</h3>
      </div>
      <input type="file" @change="onFileSelected()">
        <button @click.prevent="onUpload">Upload!</button>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Имя:</label>
        <input v-model="result.name" type="text" class="form-control" id="addressinput" placeholder="Введите Имя">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Фамилия:</label>
        <input v-model="result.surname" type="text" class="form-control" id="addressinput" placeholder="Введите Фамилию">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">ИИН:</label>
        <input v-model="result.iin" type="text" class="form-control" id="addressinput" placeholder="Введите ИИН">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Пол:</label>
        <input v-model="result.birthday" type="text" class="form-control" id="addressinput" placeholder="Введите Пол">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Пол:</label>
        <input v-model="result.gender" type="text" class="form-control" id="addressinput" placeholder="Введите Пол">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Никнейм:</label>
        <input v-model="username" type="text" class="form-control" id="addressinput" placeholder="Введите никнейм">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Почта:</label>
        <input v-model="email" type="text" class="form-control" id="addressinput" placeholder="Введите Почту">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Номер телефона:</label>
        <input v-model="user_phone" type="text" class="form-control" id="addressinput" placeholder="Введите Номер телефона">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Адрес:</label>
        <input v-model="user_address" type="text" class="form-control" id="addressinput" placeholder="Введите Адрес">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px;">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Пароль:</label>
        <input v-model="password" type="password" class="form-control" id="addressinput" placeholder="Введите пароль">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px;">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Подтверждение Пароля:</label>
        <input v-model="repeatedPassword" type="password" class="form-control" id="addressinput" placeholder="Подтверждение пароля" required ref="repeatedPasswordEl">
      </div>
      <div class="form-group" style="color: #222222; margin-left: 21px; ">
        <label for="addressinput" style="font-size:21px; margin-left: 28px; float: left;">Введите карту</label>
        <input v-model="customer_cardnumber" type="text" class="form-control" id="addressinput" placeholder="Введите Номер карты">
      </div>
      <div class="row" style="display: flex; justify-content: center; align-items: center;">
        <button type="submit" class="btn btn-warning" style="height:48px; width:240px; border-radius: 14px; font-size: 24px; font-weight: bold;">Регистрация</button>
      </div>
    </div>
    
</div>

		</form>

	</div>

 </div>
</template>

<script>
import $ from 'jquery'
import Navbar from '@/components/Navbar'
import axios from 'axios'
export default {
  components: {
        Navbar,
     	},

  data() {
    return {
      result: '',
      username: null,
      email: null,
      first_name: null,
      last_name: null,
      user_phone: null,
      user_address: null,
      password: null,
      repeatedPassword: null,
      customer_cardnumber: null,
      uploadImage: null,
    };
  },

  watch: {
    repeatedPassword: 'checkPasswordsEquality',
    password: 'checkPasswordsEquality',
  },

  methods: {
    checkPasswordsEquality() {
      const { password, repeatedPassword } = this;
      const { repeatedPasswordEl } = this.$refs;

      if (password !== repeatedPassword) {
        repeatedPasswordEl.setCustomValidity(
          'Пароли должны совпадать',
        );
      } else {
        repeatedPasswordEl.setCustomValidity('');
      }
    },

    onFileSelected() {
        this.selectedFile = event.target.files[0]
        console.log(event.target.files[0])
      },
      onUpload() {
        let fd = new FormData();
        fd.append('imageUpload', this.selectedFile)
        console.log(fd)
        console.log(this.selectedFile)
        axios.post('http://127.0.0.1:8000/api/imagepassport/create', fd, {
            headers: {
                'Content-Type': 'multipart/form-data'
              }
          })
          .then(res => {
            console.log(res.data)
            this.result = res.data
          })
        
      },

    setRegistration() {
    	$.ajax({
	    	url: "http://127.0.0.1:8000/api/users/create/",
	    	type: "POST",
	    	data: {
		    	username: this.username,
		    	email: this.email,
          first_name: this.result.name,
          last_name: this.result.surname,
          user_phone: this.user_phone,
          iin: this.result.iin,
          gender: this.result.gender,
          birthday: this.result.birthday,
          user_address: this.user_address,
		    	password: this.password,
	    	},
        success: (response) => {
          alert("Вы зарегистрированы, теперь войдите в систему")
          console.log('success')
          window.location = '/#/login'
        },
        error: (response) => {
          console.log('setRegistration is not working')
        }
    	})

    },
  },

};
</script>


<style>
  .loader {
  border: 8px solid #f3f3f3; /* Light grey */
  border-top: 8px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 45px;
  height: 45px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
  
  .slideanim {
    visibility:hidden;
    }
  .slide {
      animation-name: slide;
      -webkit-animation-name: slide;
      animation-duration: 1s;
      -webkit-animation-duration: 1s;
      visibility: visible;
  }
  @keyframes slide {
    0% {
      opacity: 0;
      transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      transform: translateY(0%);
    }
  }
  @-webkit-keyframes slide {
    0% {
      opacity: 0;
      -webkit-transform: translateY(70%);
    } 
    100% {
      opacity: 1;
      -webkit-transform: translateY(0%);
    }
  }
 
body{
color: #222222;
background-color: #F0F0F0;
font-family: Century Gothic, Serif;
font-size: 21px;

}
.navbar {
  font-family: Century Gothic, sans-serif;
  font-weight: regular;
    margin-bottom: 0;
    background-color: #222222;
    border: 0;
    font-size: 18px !important;
    letter-spacing: 2px;
    opacity: 1;
  height:77px;
  padding-top: 10px;
  padding-left: 5px;
  padding-right: 20px;
}

.carousel-inner img {
    width: 500px;
  height: 300px;
    margin: auto;
}
.carousel-caption h3 {
    color: #fff !important;
}
.bg-2 {
      background: #F0F0F0;
      color: white;
  }      
.bg-1 {
      background: #222222;
      color: black;
  }
  footer {
    background-color: Black;
    color: White;
    padding: 32px;
}
      .glyphicon {
          color: red;
      }
a{
color: white;
 }
 
 #customform{
  background-color: #FFFFFF;
  height: 750px;
  margin-left: 70px;
  margin-right: 70px;
  margin-top: 100px;
  border-radius: 28px;
  box-shadow: 0px 14px 35px #000000;
  }
  #bundown{
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background-color: #363636;
    border-color: #FBBA12;
    border-width: 2px;
    border-radius: 14px;
    width: 490px;
    height: 49px;
    color: white;
    font-size: 21px;
    padding-left: 21px;
    margin-bottom: 28px;
  }
#addressinput{
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background-color: #EDEDED;
    border-color: #FABE7C;
    border-width: 2px;
    border-radius: 14px;
    width: 450px;
    height: 49px;
    color: #222222;
    font-size: 21px;
    padding-left: 21px;
    margin-bottom: 28px;
  }
 a:before {
  content: "";
  position: absolute;
  width: 100%;
  height: 3px;
  bottom: 0;
  left: 0;
  background-color: #FEC27F;
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out 0s;
}
a:hover:before {
  visibility: visible;
  transform: scaleX(1);
}
a:hover{
color: #FEC27F !important;
}

      
  .image {
   overflow:hidden;
   width: 452px;
   height:300px;
   }
  .image img {
   -moz-transition: all 1s ease-out;
   -o-transition: all 1s ease-out;
   -webkit-transition: all 1s ease-out;
   }

  .image img:hover{
   -webkit-transform: scale(1.1);
   -moz-transform: scale(1.1);
   -o-transform: scale(1.1);
   }
  </style>
