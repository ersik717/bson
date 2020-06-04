
<template>
  <div>
<div>
    <navbar></navbar>
  </div>
<div class="container">

  <div id="Third" class="bg-2">
  <div id="customform" style="margin-bottom: 70px;">
  <div class="container-fluid text-left" style="padding-left:0px; padding-top:56px; padding-bottom:140px; margin-bottom: 56px;">
  <div v-for="catalog in catalogs" v-if="catalog.id == c_id" :key="catalog.id" class="row">
  <div class="col-sm-4" style="padding-left: 56px;">
  <img :src="catalog.catalog_image" style="height:400px; width: 400px; border-radius: 14px; position: absolute;">
  </div>
  <div class="col-sm-8" style="color:#222222; padding-left: 150px; padding-right: 42px;"><h3 style="font-weight: bold; margin-bottom:42px;">{{catalog.catalog_name}}</h3>
  <div style="color:#222222; margin-right:30px;">
    {{ catalog.catalog_description }}
  </div>
  </div>  
 </div>
 </div>
 <div v-for="catalog in catalogs" v-if="catalog.id == c_id" :key="catalog.id" class="row" style="margin-top: 42px; float: right; margin-right: 90px;">
  <div style="color: #222222; ">
    <span style="font-size:35px; ">Цена:</span>
    <span style="font-size:49px; margin-left: 7px; margin-top: 14px;">{{ catalog.catalog_price }} тг.</span>
  </div>
  </div>
  <div class="row" style="float: right;">

      <!-- <div v-for="(order, asd) in orders">
            <div v-if="user_id == order.user_id && order.order_confirm == false">
              <button v-if="asd !== 0" @click="goProduct(order.id)" type="button" class="btn btn-success" style="height:48px; width:190px; margin-top:140px; border-radius: 14px; font-size: 24px; font-weight: bold;">Добавить в корзину</button>
            </div>
            <div v-else>
              <div v-for="(orde, key) in orders" v-if="user_id !== order.user_id">
                <h4 style="visibility: hidden;">{{ cd = key }}</h4>
                  
              </div>
              <h1 style="color:black;"> {{ cd }} </h1>
               <button v-if="cd == 0" @click="goOrder()" type="button" class="btn btn-success" style="height:48px; width:190px; margin-top:140px; border-radius: 14px; font-size: 24px; font-weight: bold;">Создать заказ</button>
            </div>
          </div>
 -->
   
  </div>
</div>

  
  
  
</div>   



<br>


  <div class="card">
      <div class="card-body">
        <h3 class=text-center>Комментарии</h3>
          <div class="card" style="background-color:lemonchiffon;">
            <div v-for="catalog in catalogs" class="card-body">
              <div v-for="item in pageOfItems" :key="item.id" v-if="catalog.id == c_id && catalog.id == item.catalog" class="row">
                <div v-for="user in users" v-if="item.user == user.id" class="col-md-3">
                  <h5 class="text-left">User: {{ user.username }}</h5>
                  <h5>Given rate: {{ item.rating }}</h5>

                </div>
                <div class="col-md-9">

                  <p> {{ item.comment }} </p>
                    <!-- <input style="border: 0; background-color: white;" type="text" ref="comment" :value="item.comment" :disabled="!isEditing"
                     :class="{view: !isEditing}">
                     <button @click="isEditing = !isEditing" v-if="!isEditing">
                      Edit
                    </button>
                    <button @click="save()" v-else-if="isEditing">
                        Save
                    </button>
              
                    <button v-if="isEditing" @click="isEditing = false">Cancel</button>                    
                    <button class="btn btn-danger" @click="deleteComment(item.id)">Удалить</button> -->
                  </div>
                </div>
              </div>
                  <div class="card-footer pb-0 pt-3">
                      <jw-pagination :items="reviews" @changePage="onChangePage"></jw-pagination>
                  </div>

            </div>
            
      </div>

    </div>
  <br>
  <!-- add review  -->
    <div class="card">
      <div class="card-body">
        <h3 class="text-center">Добавить Комментарий</h3>
        <form @submit.prevent="setReview">
          <label for="comment" >Комментарий</label>
          <textarea v-model="comment" name="comment" id="comment" rows="5" cols="30" class="form-control"></textarea>

          <label for="rating">Rate</label>
          <input v-model="rating" type="range" id="rangeInput"
              name="rating" min="0" max="10" value="0" step="0.5"
              oninput="amount.value=rangeInput.value">
          <output name="amount" id="amount" for="rangeInput">0</output>

          
          <button type="submit">Отправить</button>
        </form>
      </div>
    </div>
  <br>
  <div class="main" style = "display:flex;">
    <div v-for="catalog in catalogs" class="" style = "margin:0px 10px; 0px 10px; position: relative; -webkit-box-direction: normal; flex-direction: column;
    -width: 0;word-wrap: break-word;background-color: #fff;background-clip: border-box; border: 1px solid rgba(0,0,0,.125);border-radius: .25rem;">
      <div v-for="item in catalogs" v-if="(item.id == c_id && item.id !== catalog.id) && (catalog.catalog_stuff == item.catalog_stuff || catalog.catalog_topping == item.catalog_topping)" style="padding: 1.25rem;">
      <div style = "display:flex; flrx-wrap:wrap; flex-direction:column; align-items: center;">
          <div>
            <div >
          <img ::src="item.catalog_image" style = "height:135px; width:215px;">
          </div>

            <h5>Baker: {{ catalog.catalog_name }}</h5>
            <h5 v-for="stuff in stuffs" v-if="catalog.catalog_stuff == stuff.id">Начинка: {{ stuff.stuff_name }}</h5>
            <h5 v-for="topping in toppings" v-if="catalog.catalog_topping == topping.id">Посыпка: {{ topping.topping_name }}</h5>

          </div>
        </div>
      </div>

    </div>
</div>


</div>
<div>
    <Footer></Footer>
  </div>
</div>
</template>

<script>
import $ from 'jquery'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
var moment = require('moment')
export default {
    components: {
        Navbar,
        Footer,
      },
    data() {
        return {
            isEditing: false,
            catalogs: '',
            reviews: [''],
            users: '',
            c_id: sessionStorage.getItem('cat_id'),
            comment: '',
            rating: '',
            catalog: sessionStorage.getItem('cat_id'),
            user_id: sessionStorage.getItem('u_id'), 
            stuffs: '',
            toppings: '',  
            pageOfItems: [],
            orders: '', 
            cd: 0, 

            cat_name: sessionStorage.getItem('cat_PN'),
            cat_date: sessionStorage.getItem('cat_MD'), 
            cat_exDate: sessionStorage.getItem('cat_ED'), 
            cat_type: sessionStorage.getItem('cat_PT'), 
            cat_desc: sessionStorage.getItem('cat_DT'), 
            cat_calory: sessionStorage.getItem('cat_PC'), 
            cat_price: sessionStorage.getItem('cat_PCost'), 
            cat_form: sessionStorage.getItem('cat_PF'), 
            cat_stuff: sessionStorage.getItem('cat_PS'), 
            cat_top: sessionStorage.getItem('cat_PT'),        
        };
    },

    beforeCreate() {
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/catalog",
              type: "GET",
              success: (response) => {
                this.catalogs = response
                console.log(response)

                
              }
        });
        $.ajax({ 
              url: "http://127.0.0.1:8000/api/review",
              type: "GET",
              success: (response) => {
                this.reviews = response
                console.log(response)

                
              }
        });
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/product/stuff/",
              type: "GET",
              success: (response) => {
                this.stuffs = response
                console.log(response)
                
              }
        });
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/product/topping/",
              type: "GET",
              success: (response) => {
                this.toppings = response
                console.log(response)
                
              }
        });
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/users/",
              type: "GET",
              success: (response) => {
                this.users = response

              }
        });
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/orders",
              type: "GET",
              success: (response) => {
                this.orders = response

              }
        });

    },
    methods: {
      deleteComment(e) {
          $.ajax({ 
                url: "http://127.0.0.1:8000/api/review/" + e,
                type: "DELETE",
                success: (response) => {
                  // this.orders = response.results
                  console.log("success")
                  this.$router.go(0)
                }
          });
      },
      save(e) {
          this.user.comment = this.$refs['comment'].value;
          this.isEditing = !this.isEditing;
          console.log(e)

        },
      onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
      setReview() {
        $.ajax({
        url: "http://127.0.0.1:8000/api/review/create",
        type: "POST",
        data: {
            comment: this.comment,
            rating: this.rating,
            catalog: this.catalog,
            user: this.user_id
        },
        success: (response) => {
          console.log('success')
          this.$router.go(0)
        },
        error: (response) => {
          console.log('Comments is not working')
        }
      })
      },
      goProduct(someOrderID) {
        $.ajax({
        url: "http://127.0.0.1:8000/api/products/create",
        type: "POST",
        data: {
            product_name: this.cat_name,
            manufacture_date: this.cat_date,
            expire_date: this.cat_exDate,
            product_type: this.cat_type,
            customized: false,
            product_detailtext: this.cat_desc,
            product_calory: this.cat_calory,
            product_cost: this.cat_price,
            productform: this.cat_form,
            productstuff: this.cat_stuff,
            producttopping: this.cat_top,
            order_id: someOrderID,
            product_catalog_id: this.catalog,
        },
        success: (response) => {
          console.log('success')
          alert("Продукт добавлен в корзину")
        },
        error: (response) => {
          console.log('Comments is not working')
        }
      })
        
      },
      getDate () {
        const toTwoDigits = num => num < 10 ? '0' + num : num;
        let today = new Date();
        let year = today.getFullYear();
        let month = toTwoDigits(today.getMonth() + 1);
        let day = toTwoDigits(today.getDate());
        return `${year}-${month}-${day}`;
      },
      goOrder() {
        $.ajax({
        url: "http://89.219.32.10/api/orders/create",
        type: "POST",
        data: {
            order_total: 0,
            order_address: 'asd',
            order_date: '2020-05-10',
            order_confirm: false,
            order_detail_text: "qweasd",
            user_id: this.user_id
        },
        success: (response) => {
          console.log('success')
          this.$router.go(0)
          alert("Ваш заказ создан, теперь добавьте в корзину")
        },
        error: (response) => {
          console.log('Comments is not working')
        }
      })
        
      },
      onChange(e) {
        this.cd = e.target.value;
      }
      
    }
};

</script>