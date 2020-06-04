<template>
	<div>
		<div>
			<navbar></navbar>
		</div>
		<div>
			<customization></customization>
		</div>
		 <div>
    		<Footer></Footer>
  		</div>
	</div>

</template>
<script>
	import Navbar from '@/components/Navbar'
	import Customization from '@/components/Customization'
	import Footer from '@/components/Footer'
	export default {
		name: "Bakery",
		components: {
			Navbar,
			Customization,
			Footer,
		},
	}

	
</script>
