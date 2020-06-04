<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      />
  </div>
</template>

<script>
import LineChart from '@/components/Chart.vue'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: null
  }),
  async mounted () {
    this.loaded = false
    try {
      const { userlist } = await fetch('http://89.219.32.10/api/products/')
      this.chartdata = userlist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>