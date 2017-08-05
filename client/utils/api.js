import axios from 'axios';

// function helperFunctions (sdfdsf) {
//   return 'hi'
// }

export function getAllMenus () {
    var encodedURI = window.encodeURI('http://localhost:8000/api/get/menu/all');

    return axios.get(encodedURI)
      .then(response => response.data.allMenus);
}