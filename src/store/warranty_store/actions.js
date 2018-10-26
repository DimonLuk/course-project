const actions = {
  setCurrentWarranty ({ commit }, pk) {
    fetch(`/data_center/api/components_by_warranty/${pk}`)
      .then(response => response.json())
      .then(responseData => {
        const warranty = {
          id: responseData.warranty.id,
          startDate: responseData.warranty.start_date,
          endDate: responseData.warranty.end_date
        }
        const mapComponent = comp => ({
          type: comp.component_type,
          serialNumber: comp.serial_number,
          manufacturer: comp.manufacturer
        })
        let components = responseData.components.map(mapComponent)
        const mappedData = {
          warranty,
          components
        }
        commit('SET_CURRENT_WARRANTY', mappedData)
      })
  }
}

export default actions
