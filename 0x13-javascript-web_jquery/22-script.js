$.get('http://swapi.co/api/films/?format=json', function(data) {
  let count = data.count;
  let i = 0;
  while (i < count) {
    $('UL#list_movies').append('<LI>' + data.results[i].title + '</LI>');
    i++;
  }
});
