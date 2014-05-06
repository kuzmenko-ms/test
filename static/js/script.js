/* Author:
km
*/

$(function () {
  tax_data = [
       {"u": "23.34",  "sorned": 467},
       {"u": "24.37 ",  "sorned": 646},
       {"u": "25.39",  "sorned":323},
       {"u": "26.56",  "sorned": 245},
       {"u": "27.89",  "sorned": 654}
  ];
  new Morris.Line({
    element: 'hero-graph',
    data: tax_data,
    xkey: 'u',
    ykeys: ['sorned'],
    labels: ['P']
  });
  $('.code-example').each(function (index, el) {
    eval($(el).text());
  });
});
