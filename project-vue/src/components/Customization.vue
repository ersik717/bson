<template>

	<div id="Third" class="bg-2">
	<div id="customform">
	<div class="container-fluid text-left" style="padding-left:0px; padding-top:56px; padding-bottom:140px;">
	<div class="row">
  <div class="col-sm-4" style="padding-left: 56px;">
  <img v-bind:src="result" id="result" style="height:400px; border-radius: 14px; position: absolute; z-index: 0;">
  <img v-bind:src="bunform" id="bunform" style="height:400px; border-radius: 14px; position: absolute; z-index: 1;">
  <img v-bind:src="stuff" id="stuff" style="height:400px; border-radius: 14px; position: absolute; z-index: 2;">
  <img v-bind:src="topping" id="topping" style="height:400px; border-radius: 14px; position: absolute; z-index: 3;">
  </div>

  <div class="col-sm-8" style="color:#222222; padding-left: 90px; padding-right: 42px;"><h3 style="font-weight: bold; margin-bottom:42px;">Собери свою булочку! </h3>
	<div class="row" style="margin-bottom: 14px;">
	<span style="font-size:21px; margin-left: 39px;">Форма </span>
	</div>
	<select name="bakeform" ref="formpick" id="bundown" v-on:change="bake()">
		<option value="empty">Пусто</option>
		<option value="bread">Хлебная</option>
		<option value="classic">Классическая</option>
		<option value="roll">Рулет</option>
	</select>
	<div class="row" style="margin-bottom: 14px;">
	<span style="font-size:21px; margin-left: 39px;">Начинка</span>
	</div>
	<select name="bakestuff" ref="stuffpick" id="bundown" v-on:change="bake()">
		<option value="empty">Пусто</option>
		<option value="choco">Шоколадная</option>
		<option value="jam">Джем</option>
		<option value="vanilla">Ванильная</option>
	</select>
	<div class="row" style="margin-bottom: 14px;">
	<span style="font-size:21px; margin-left: 39px;">Посыпка</span>
	</div>
	<select name="baketopping" ref="toppick" id="bundown" v-on:change="bake()">
		<option value="empty">Пусто</option>
		<option value="pop">Мак</option>
		<option value="fruit">Фруктовая</option>
		<option value="heart">Сердечки</option>
	</select>
  </div>

 </div> 
 						<div v-model="text" class="form-group" style="color: #222222;">
							<label for="addressinput" style="font-size:21px; margin-left: 28px;">Надпись:</label>
							<input type="text" class="form-control" id="addressinput" placeholder="Напишите текст">
						</div>
			<div v-for="(order, asd) in orders">
            <div v-if="u_id == order.user_id && order.order_confirm == false">
              <button v-if="asd !== 0" @click="createProduct(order.id)">Добавить в корзину</button>
            </div>
            <div v-else>
              <div v-for="(orde, key) in orders" v-if="u_id !== order.user_id">
                <h4 style="visibility: hidden;">{{ cd = key }}</h4>
                  
              </div>
              <button v-if="cd == 0" @click="createOrder()">Создать заказ</button>
              <!-- <div v-for="(ord, index) in orders">
                <div v-if="user_id == ord.user_id && ord.order_confirm && cd <= 2 "> {{ goProduct(ord.id) }} {{ cd + 1 }} </div>
              </div> -->
                 
            </div>
          </div>
 </div> 



</div>

  
</div>

</template>

<script>

	export default({
		data() {
			return {
				result: require("@/assets/Elements/Buns/back.png"),
				bunform: require("@/assets/Elements/Buns/empty.png"),
				stuff: require("@/assets/Elements/Buns/empty.png"),
				topping: require("@/assets/Elements/Buns/empty.png"),
				text: '',
				u_id: sessionStorage.getItem('us_id'),
				users: '',
				orders: '',
			}
			
		},
		beforeCreate() {
			 $.ajax({ 
            url: "http://89.219.32.10/api/users/",
              type: "GET",
              success: (response) => {
                this.users = response

              }
	        });
	        $.ajax({ 
	            url: "http://89.219.32.10/api/orders",
	              type: "GET",
	              success: (response) => {
	                this.orders = response

	              }
	        });
		},
		methods: {
			bake: function bake() {
				this.bunform = require("@/assets/Elements/Buns/" + this.$refs.formpick.value + ".png");
				this.stuff = require("@/assets/Elements/Buns/" + this.$refs.formpick.value + this.$refs.stuffpick.value + ".png");
				this.topping = require("@/assets/Elements/Buns/" + this.$refs.formpick.value + this.$refs.toppick.value + ".png");
			},
			createProduct(someOrderID) {
				var fp = this.$refs.formpick.value
				var sp = this.$refs.stuffpick.value
				var tp = this.$refs.toppick.value
				if (fp == "bread") {
					var fID = 3
					var fCost = 100
				}
				else if (fp == "classic") {
					var fID = 4
					var fCost = 80
				}
				else if (fp == "roll") {
					var fID = 5
					var fCost = 100
				}
				else {
					return false
				}

				if (sp == "choco") {
					var sID = 2
					var sCost = 150
				}
				else if (sp == "jam") {
					var sID = 3
					var sCost = 180
				}
				else if (sp == "vanilla") {
					var sID = 4
					var sCost = 130
				}
				else {
					return false
				}

				if (tp == "pop") {
					var tID = 2
					var tCost = 50
				}
				else if (tp == "fruit") {
					var tID = 3
					var tCost = 100
				}
				else if (tp == "heart") {
					var tID = 4
					var tCost = 70
				}
				else {
					return false
				}
				$.ajax({
			        url: "http://127.0.0.1:8000/api/products/create",
			        type: "POST",
			        data: {
			            product_name: fp + ' ' + sp + ' ' + tp,
			            manufacture_date: "2020-05-10",
			            expire_date: "2020-05-10",
			            product_type: "Булочка",
			            customized: true,
			            product_detailtext: "asd",
			            product_calory: 356,
			            product_cost: fCost + sCost + tCost,
			            productform: fID,
			            productstuff: sID,
			            producttopping: tID,
			            order_id: someOrderID,
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
			createOrder() {
		        $.ajax({
		        url: "http://127.0.0.1:8000/api/orders/create",
		        type: "POST",
		        data: {
		            order_total: 0,
		            order_address: 'asd',
		            order_date: '2020-05-10',
		            order_confirm: false,
		            order_detail_text: "qweasd",
		            user_id: this.u_id
		        },
		        success: (response) => {
		          console.log('success')
		          // this.$router.go(0)
		          alert("Ваш заказ создан, теперь добавьте в корзину")
		        },
		        error: (response) => {
		          console.log('Comments is not working')
		        }
		      })
	        
      	},
	}
	});
  </script>

  <style>

  </style>