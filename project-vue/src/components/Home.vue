<template>
<div>
	<div>
	<navbar></navbar>
	</div>
	<div>
	<Aboutus></Aboutus>
	</div>
  <div>
    <Footer></Footer>
  </div>
</div>
</template>

<script>
	import Aboutus from '@/components/Aboutus'
	import Navbar from '@/components/Navbar'
  import Footer from '@/components/Footer'
	export default {
		name: "Home",
		components: {
			Aboutus,
			Navbar,
      Footer,
		},

	}
</script>

<style>
	
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