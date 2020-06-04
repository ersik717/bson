<template>
 <div>
 	<div>
 		<navbar></navbar>
 	</div>
 	<div>
 		<BodyCatalog></BodyCatalog>
 	</div>
 	<div>
 		<Footer></Footer>
 	</div>
 </div>
</template>

<script>
	import Navbar from '@/components/Navbar'
	import Footer from '@/components/Footer'
	import BodyCatalog from '@/components/BodyCatalog'
	export default {
		name: "Catalog",
		components: {
        Navbar,
        Footer,
        BodyCatalog,
     	},
     }
</script>