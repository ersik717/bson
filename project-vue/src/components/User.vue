<!-- <template>
    <div class="card text-center m-3">
        <h3 class="card-header">Vue.js Pagination Tutorial & Example</h3>
        <div class="card-body">
            <div v-for="item in pageOfItems" :key="item.id">{{item.comment}}</div>
        </div>
        <div class="card-footer pb-0 pt-3">
            <jw-pagination v-if="computedItems.length" :items="exampleItems" @changePage="onChangePage"></jw-pagination>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            exampleItems: [''],
            pageOfItems: []
        };
    },
    computed: {
        computedItems () {
            return this.exampleItems;
        }
    },
    mounted () {
        // an example array of items to be paged
        // this.exampleItems = [...Array(150).keys()].map(i => ({ id: (i+1), name: 'Item ' + (i+1) }));
        $.ajax({ 
              url: "http://127.0.0.1:8000/api/review",
              type: "GET",
              success: (response) => {
                this.exampleItems = response.results
                console.log(response)

                
              }
        });
    },
    methods: {
        onChangePage(pageOfItems) {
            // update page of items
            this.pageOfItems = pageOfItems;
        }
    }
};
</script> -->


<template>
		<div id="app">
	  <div>
	    Comment:
	    <input type="text" ref="comment" :value="user.comment" :disabled="!isEditing"
	           :class="{view: !isEditing}">
	  </div>
	  <button @click="isEditing = !isEditing" v-if="!isEditing">
	    Edit
	  </button>
	  <button @click="save" v-else-if="isEditing">
	  Save
	  </button>
	  
	  <button v-if="isEditing" @click="isEditing = false">Cancel</button>
	</div>
</template>

<script>
	export default{
  data() {
  	return {
  		isEditing: false,
    	user: {
	      comment: 'John',
    		}
  	}
    
  },
  methods: {
    save() {
      this.user.comment = this.$refs['comment'].value;
      this.isEditing = !this.isEditing;
    }
  }
}
</script>