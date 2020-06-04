import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ['options'],
  mounted () {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    $.ajax({ 
            url: "http://127.0.0.1:8000/api/users/",
              type: "GET",
              success: (response) => {
                this.chartData = response.results
                console.log(response)  
              }
        });
    this.renderChart(this.chartData, this.options)
  }
}