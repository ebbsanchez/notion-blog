var app = new Vue({
	delimiters:['[[', ']]'],
	el: '#filters',
	data: {
		'message':'hello',
		'filters_data': []
	},
	mounted () {
    axios
      .get('https://ebbfilters.herokuapp.com/filters/api/filters/')
      .then(response => {
      	console.log(response);
      	let data = response.data
      	for (var i = data.length - 1; i >= 0; i--) {
      		this.filters_data.push(data[i]);
      	}
      	
      })
      .catch(function (error) { // 请求失败处理
        console.log(error);
      });
  }

});
const data = app.filters_data
