import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'


let _Token = localStorage.getItem('token')
console.log(_Token)
const httpOptions = {
  headers: new HttpHeaders({
    //'Content-Type': 'application/json',
    'Authorization': `JWT ${_Token}`,
    //'Accept': 'application/json'
  })
};


@Injectable({
  providedIn: 'root'
})
export class SoftwareService {
<<<<<<< HEAD
    token = localStorage.getItem('token');

=======
   // token = localStorage.getItem('token'); 
  
>>>>>>> 4e3630cc1dd66a04cc9f25a3762bf1ac4a4216d9
  private _listUrl = "http://127.0.0.1:8000/api/v1/software/"
  private _createUrl = "http://127.0.0.1:8000/api/v1/software/create"

  // createAuthorizationHeader(headers: HttpHeaders) {
  //   headers.append('Authorization', 'JWT ' +
  //     token);
  // }


constructor(public http: HttpClient) { }

getAll() {
  return this.http.get<any>(this._listUrl)
}

create(softwareData) {
<<<<<<< HEAD
  console.log(softwareData,this.token)

  console.log(_Token)
=======
  console.log(softwareData,httpOptions,_Token)
>>>>>>> 4e3630cc1dd66a04cc9f25a3762bf1ac4a4216d9
  return this.http.post<any>(this._createUrl, softwareData, httpOptions)
    .pipe(
      //catchError(this.handleError)
    )
}

}
