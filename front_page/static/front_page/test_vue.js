var test = new Vue({
	delimiters:['[[', ']]'],
	el: '#test',
	data: {
		'test': true,
		'itisnull': null,
		'itisstring': 'string----',
		'filters_data':[]
	},
	mounted () {
    axios
      .get('filters/api/filters/')
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