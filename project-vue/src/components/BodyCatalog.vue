<template>
    <div>

        <div id="Third" class="bg-2">
  <div class="container-fluid text-left" style="padding-left:0px; padding-top:56px; padding-bottom:140px;">
    <div class="row" style="margin-top: 42px; margin-bottom: 14px; margin-right:100px; float:right;">
      <span style="font-size:21px; margin-top:7px;margin-right:21px; color: #222222;">Сортировать по:</span>
    <select name="bakeform" id="bundown" style="width: 350px;" @change="Sort($event)">
      <option value="pricehigh">Цене(сначала дорогие)</option>
      <option value="pricelow">Цене(сначала дешевые)</option>
      <option value="popular">Популярности</option>
    </select>
    </div>
    <!-- <button @click="sorting *= -1">Toggle order</button> -->
    <div class="catal">
    <ul> 
    <div v-for="item in catalog" :key="item.id" style="color:#222222; margin-top: 42px; margin-bottom: 14px; margin-left:14px; ">
      <li>
      <div id="customcatalog">
        <img :src="item.catalog_image" style="margin: 21px; width: 329px; height: 230px; border-radius:21px; object-fit: cover;">
        <div class="row" style="display: flex; justify-content: center; align-items: center;">
          <span style="font-size:24px; color: #222222;">{{item.catalog_name}}</span>  
        </div>
        <div class="row">
          <img src="@/assets/Elements/star.png" style="margin-left:55px; margin-top:5px; width: 35px; height: 35px;">
          <span style="font-size:32px; color: #222222; margin-left: 7px;">{{item.catalog_rating}}</span>
          <span style="font-size:32px; font-weight:bold; color: #222222; margin-left:120px">{{item.catalog_price}} тг.</span>
        </div>
        <div class="row" style="display: flex; justify-content: center; align-items: center;">
          <div v-for="user in users" v-if="user.username == usern">
          <button @click="goTodetail(item.id); goID(user.id); goPN(item.catalog_name); goMD(item.catalog_date); goED(item.catalog_expiredate); goPT(item.catalog_type); goDT(item.catalog_description); goPC(item.catalog_calory); goPCost(item.catalog_price); goPF(item.catalog_form); goPS(item.catalog_stuff); goPTop(item.catalog_topping)" type="button" class="btn btn-success" style="height:48px; width:190px; margin-top:10px; border-radius: 14px; font-size: 24px; font-weight: bold;">Перейти</button>
        </div>
        </div>
      </div>
      </li>
    </div>
    
    </ul>
  </div>

     <div class="card-footer pb-0 pt-3">
            <jw-pagination :items="catalog" @changePage="onChangePage"></jw-pagination>
        </div>
  </div>
</div>




       
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    data() {
        return {
            pageOfItems: [],
            catalog: [''],
            users: '',
            usern: sessionStorage.getItem('login'), 
            sortByPrice: true
        };
    },
    beforeCreate() {
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/catalog",
              type: "GET",
              success: (response) => {
                this.catalog = response

              }

        });
        $.ajax({ 
            url: "http://127.0.0.1:8000/api/users/",
              type: "GET",
              success: (response) => {
                this.users = response
                // console.log(response)

                
              }
        });
    },
    methods: {
        Sort(event) {
          console.log(event.target.value)
          if (event.target.value == "pricelow") {
            this.catalog.sort((a,b) => {
              if ( this.sortByPrice ) {
                return a.catalog_price - b.catalog_price
              } 
            });
          }
          if (event.target.value == "pricehigh") {
            this.catalog.sort((a,b) => {
              if ( this.sortByPrice ) {
                return b.catalog_price - a.catalog_price
              } 
            });
          }
          if (event.target.value == "popular") {
            this.catalog.sort((a,b) => {
              if ( this.sortByPrice ) {
                return b.catalog_rating - a.catalog_rating
              } 
            });
          }         
          
        },

        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        },
        goDetail() {
            // sessionStorage.setItem("catalog_id", this.catalog.id)
            //this.$router.push({name: "detail"})
            //window.location = '/#/detail/<int:this.catalog.id>'
        },
        goTodetail(prodId) {
            this.$router.push({name:'detail',params:{Pid:prodId}})
            sessionStorage.setItem("cat_id", prodId)
        },
        goID(someID) {
             sessionStorage.setItem("u_id", someID)   
        },
        goPN(somePN) {
             sessionStorage.setItem("cat_PN", somePN)   
        },
        goMD(someMD) {
             sessionStorage.setItem("cat_MD", someMD)   
        },
        goED(someED) {
             sessionStorage.setItem("cat_ED", someED)   
        },
        goPT(somePT) {
             sessionStorage.setItem("cat_PT", somePT)   
        },
        goDT(someDT) {
             sessionStorage.setItem("cat_DT", someDT)   
        },
        goPC(somePC) {
             sessionStorage.setItem("cat_PC", somePC)   
        },
        goPCost(somePCost) {
             sessionStorage.setItem("cat_PCost", somePCost)   
        },
        goPF(somePF) {
             sessionStorage.setItem("cat_PF", somePF)   
        },
        goPS(somePS) {
             sessionStorage.setItem("cat_PS", somePS)   
        },
        goPTop(somePTop) {
             sessionStorage.setItem("cat_PT", somePTop)   
        },
    }
};

</script>


<style>
  .catal ul {
  display: flex !important;
  flex-wrap: wrap !important;
  padding-left: 0 !important;
}

.catal ul li {
  list-style: none !important;
  flex: 0 0 33.333333% !important;
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
#customcatalog{
  background-color: #FFFFFF;
  width: 370px; 
  height:420px;
  margin-left: 70px;
  margin-right: 70px;
  margin-top: 100px;
  border-radius: 28px;
  box-shadow: 0px 14px 35px #000000;
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