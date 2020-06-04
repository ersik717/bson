<template>

	<div>
		<div>
			<form enctype=multipart/form-data role="form" method="post">
				<input type="file" @change="onFileSelected()">
	  			<button @click.prevent="onUpload">Upload!</button> 
  			</form>
			
		</div>
		<div>
			<input v-model="result.name"/>
		</div>
		<div>
			<input v-model="result.surname"/>
		</div>
	</div>	
</template>

<script>
	import axios from 'axios'

	export default{
		data() {
			return{
				result: '',
				// surname: '',
				selectedFile: '',
				datas: ''
			}
			
		},
		// beforeCreate() {
		// 	$.ajax({ 
	 //            url: "http://127.0.0.1:8000/api/imagepassport/",
	 //              type: "GET",
	 //              success: (response) => {
	 //                this.name = response.names
	 //                this.surname = response.surname
	 //                console.log(this.name)             
	 //              }
  //      		 });
		// },
		methods: {
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
				
			}
		}
	}
</script>