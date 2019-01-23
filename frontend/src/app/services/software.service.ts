import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Token } from '@angular/compiler';

// const httpOptions = {
//   headers: new HttpHeaders({
//     'Content-Type': 'application/json',
//     'Authorization': 'JWT token',
//     'Accept': 'application/json'
//   })
// };


@Injectable({
  providedIn: 'root'
})
export class SoftwareService {
  _Token = localStorage.getItem('token')

  private _listUrl = "http://127.0.0.1:8000/api/v1/software/"
  private _createUrl = "http://127.0.0.1:8000/api/v1/software/create"

  createAuthorizationHeader(headers: HttpHeaders) {
    headers.append('Authorization', 'JWT ' +
      this._Token);
  }


constructor(public http: HttpClient) { }

getAll() {
  return this.http.get<any>(this._listUrl)
}

create(softwareData) {
  console.log(softwareData,this._Token)
  return this.http.post<any>(this._createUrl, softwareData, { headers: new HttpHeaders })
    .pipe(
      //catchError(this.handleError)
    )
}

}
