<template>
  <div class="ComputerPage">
    <div class='container Warranties'>
      <div class='row'>
        <div class='col-6'>
          <button @click='prev()'>Prev</button>
        </div>
        <div class='col-6'>
          <button @click='next()'>Next</button>
        </div>
      </div>
      <div class='row'>
        <div class='col-4'>
          ID
        </div>
        <div class='col-4'>
          Start date
        </div>
        <div class='col-4'>
          End date
        </div>
      </div>
      <div class='row'>
        <div class='col-4'>
          {{ warrantyId }}
        </div>
        <div class='col-4'>
          {{ warrantyStart }}
        </div>
        <div class='col-4'>
          {{ warrantyEnd }}
        </div>
      </div>
    </div>
    <div class='container Components'>
      <div class='row'>
        <div class='col-4'>
          Type
        </div>
        <div class='col-4'>
          Serial Number
        </div>
        <div class='col-4'>
          Manufacturer
        </div>
      </div>
      <div class='row' v-for='component in components'>
        <div class='col-4'>
          {{ component.type }}
        </div>
        <div class='col-4'>
          {{ component.serialNumber }}
        </div>
        <div class='col-4'>
          {{ component.manufacturer }}
        </div>
      </div>
      <div class='row'>
        <div class='col-12'>
          <textarea v-model='rawSql'> 
          </textarea>
          <button @click='process()'>Process</button>
        </div>
        <div class='row'>
          <div class='col-12'>
            {{ retrievedData }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
const ComputerComponentsByWarrantyPage = {
  mounted () {
    this.setCurrentWarranty(1)
  },
  data () {
    return {
      currentWarranty: 1,
      rawSql: '',
      retrievedData: ''
    }
  },
  computed: {
    ...mapState('warrantyStore', {
      warrantyId: state => state.warranty.id,
      warrantyStart: state => state.warranty.startDate,
      warrantyEnd: state => state.warranty.endDate,
      components: state => state.components
    })
  },
  methods: {
    ...mapActions('warrantyStore', [
      'setCurrentWarranty'
    ]),
    process () {
      fetch('/data_center/api/raw_sql/', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          sql: this.$data.rawSql
        })
      })
        .then(response => response.json())
        .then(response => {
          this.$data.retrievedData = response
        })
    },
    next () {
      this.$data.currentWarranty++
      this.setCurrentWarranty(this.$data.currentWarranty)
    },
    prev () {
      this.$data.currentWarranty--
      this.setCurrentWarranty(this.$data.currentWarranty)
    }
  }
}
export default ComputerComponentsByWarrantyPage
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #35495E;
}
</style>
