function makeapostcall() {

  $('body').append('<div class="loading">Loading&#8230;</div>');

  const API_URL = "/gettopthreedomainnames/";
  const requestOptions = {
  method: "POST",
  headers: {
      "Content-Type" : "application/json",
  },
  body: JSON.stringify({
      'blankpost': 'blank'
  })
  }
  fetch(API_URL, requestOptions)
  .then(response => {
  console.log('Response status code:', response.status);
  window.location.href = '/gettopthreedomainnames/'
  $('.loading').remove();
  })
  .catch(error => {
  console.error('Error:', error);
  });
  }



function generate_short_url() {
  var postdata = document.getElementById('exampleInput');
  console.log(postdata.value);
  $('body').append('<div class="loading">Loading&#8230;</div>');
  const posted_value = postdata.value;
  const API_URL = "/posturl/";
  const requestOptions = {
  method: "POST",
  headers: {
      "Content-Type" : "application/json",
  },
  body: JSON.stringify({
      postedurl: posted_value
  })
  }
  fetch(API_URL, requestOptions)
  .then(response => {
  console.log('Response status code:', response.status);
  window.location.href = '/posturl/'
  $('.loading').remove();
  if (response.ok) {
    response.json().then(data => {
        console.log('Short URL:', data.url);
    });
} else {
    console.error('Error:', response.statusText);
}
  })
  .catch(error => {
  console.error('Error:', error);
  });
  }


